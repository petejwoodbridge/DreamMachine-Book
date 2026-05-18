"""Fetch every substantive URL referenced across the 29 newsletter issues.

Reads the URL index built by `build_url_index.py`, fetches each URL with a real
browser User-Agent, extracts cleaned text, and writes one JSON file per URL plus
a roll-up manifest. Idempotent: re-runs only fetch URLs that don't yet have a
saved record.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

IDX_PATH = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/url_index.json"
OUT_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/scraped"
MANIFEST = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/manifest.json"

os.makedirs(OUT_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
}

MAX_WORKERS = 8
TIMEOUT = 15
HOST_DELAY_S = 0.6  # be polite — at most ~1.6 requests/s per host
MAX_TEXT_CHARS = 60_000  # cap stored text per page

# Per-host last-request timestamp for polite throttling.
_host_last = {}
_host_lock = threading.Lock()


def url_hash(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def host_of(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def wait_for_host(host: str) -> None:
    with _host_lock:
        last = _host_last.get(host, 0.0)
        now = time.time()
        wait = HOST_DELAY_S - (now - last)
        if wait > 0:
            time.sleep(wait)
        _host_last[host] = time.time()


def extract_text(html: str, content_type: str) -> tuple[str, str]:
    """Return (title, cleaned_text)."""
    if "html" not in (content_type or "").lower():
        return "", html[:MAX_TEXT_CHARS]

    soup = BeautifulSoup(html, "html.parser")

    # drop chrome
    for tag in soup(["script", "style", "noscript", "iframe", "svg",
                     "nav", "footer", "aside", "form"]):
        tag.decompose()

    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    elif soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)

    # Prefer the article/main content if present
    main = soup.find("article") or soup.find("main") or soup.body or soup
    text = main.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title[:300], text[:MAX_TEXT_CHARS]


def fetch_one(item: dict) -> dict:
    url = item["url"]
    issue = item.get("issue")
    bucket = item.get("bucket")
    out_path = os.path.join(OUT_DIR, f"{url_hash(url)}.json")

    if os.path.exists(out_path):
        # Already done; return cached metadata for the manifest
        try:
            with open(out_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass  # corrupted; refetch

    wait_for_host(host_of(url))

    record = {
        "url": url,
        "issue": issue,
        "bucket": bucket,
        "host": host_of(url),
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "status": None,
        "http_status": None,
        "title": "",
        "final_url": "",
        "content_type": "",
        "text": "",
        "error": "",
    }

    try:
        r = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            allow_redirects=True,
        )
        record["http_status"] = r.status_code
        record["final_url"] = r.url
        record["content_type"] = r.headers.get("Content-Type", "")
        if r.status_code == 200:
            title, text = extract_text(r.text, record["content_type"])
            record["title"] = title
            record["text"] = text
            record["status"] = "ok"
        else:
            record["status"] = f"http_{r.status_code}"
    except requests.exceptions.Timeout:
        record["status"] = "timeout"
        record["error"] = "timeout"
    except requests.exceptions.SSLError as e:
        record["status"] = "ssl_error"
        record["error"] = str(e)[:200]
    except requests.exceptions.ConnectionError as e:
        record["status"] = "connection_error"
        record["error"] = str(e)[:200]
    except Exception as e:
        record["status"] = "error"
        record["error"] = f"{type(e).__name__}: {e}"[:200]

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False)

    return record


def main():
    idx = json.load(open(IDX_PATH, encoding="utf-8"))
    items = []
    for bucket, lst in idx["by_bucket"].items():
        for it in lst:
            items.append(it)

    # Deduplicate by URL
    seen = set()
    uniq = []
    for it in items:
        if it["url"] not in seen:
            seen.add(it["url"])
            uniq.append(it)

    print(f"Total URLs to attempt: {len(uniq):,}")

    # Skip ones we already have
    todo = []
    cached = 0
    for it in uniq:
        path = os.path.join(OUT_DIR, f"{url_hash(it['url'])}.json")
        if os.path.exists(path):
            cached += 1
        else:
            todo.append(it)
    print(f"Already cached: {cached}")
    print(f"To fetch: {len(todo)}")

    start = time.time()
    completed = 0
    status_counts = {}
    results = []

    if todo:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = {pool.submit(fetch_one, it): it for it in todo}
            for fut in as_completed(futures):
                rec = fut.result()
                results.append(rec)
                completed += 1
                status_counts[rec["status"]] = status_counts.get(rec["status"], 0) + 1
                if completed % 25 == 0 or completed == len(todo):
                    elapsed = time.time() - start
                    rate = completed / elapsed if elapsed else 0
                    print(f"  [{completed:>4}/{len(todo)}] "
                          f"{rate:.1f}/s — {status_counts}")

    # Build the manifest from all cached records
    manifest = []
    for it in uniq:
        path = os.path.join(OUT_DIR, f"{url_hash(it['url'])}.json")
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    r = json.load(f)
                manifest.append({
                    "url": r["url"],
                    "issue": r.get("issue"),
                    "bucket": r.get("bucket"),
                    "host": r.get("host"),
                    "status": r.get("status"),
                    "http_status": r.get("http_status"),
                    "title": r.get("title", ""),
                    "text_chars": len(r.get("text", "")),
                    "hash": url_hash(r["url"]),
                })
            except Exception:
                pass

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)

    # Final summary
    total = len(manifest)
    ok = sum(1 for m in manifest if m["status"] == "ok")
    print()
    print(f"=== Manifest written to {MANIFEST} ===")
    print(f"Total records: {total}")
    print(f"OK (text captured): {ok} ({100*ok/total:.1f}%)")
    final_counts = {}
    for m in manifest:
        final_counts[m["status"]] = final_counts.get(m["status"], 0) + 1
    for s in sorted(final_counts, key=lambda k: -final_counts[k]):
        print(f"  {s:>20}: {final_counts[s]}")


if __name__ == "__main__":
    main()
