"""Retry HTTP-403'd URLs using stronger browser-like fetches: full Chrome
header set, session cookies, Referer, random jitter, multiple UA rotation."""
from __future__ import annotations
import hashlib
import json
import os
import random
import time
import threading
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from bs4 import BeautifulSoup

ROOT = r"d:/VSCODE PROJECTS/DreamMachine Book/Research"
MANIFEST = os.path.join(ROOT, "manifest.json")
SCRAPED = os.path.join(ROOT, "scraped")

USER_AGENTS = [
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) Version/17.6 Safari/605.1.15"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
     "Chrome/132.0.0.0 Safari/537.36"),
]

# Slow it right down: anti-bot systems flag burst patterns.
HOST_DELAY_S = 2.5
_host_last: dict[str, float] = {}
_host_lock = threading.Lock()


def url_hash(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def host_of(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def wait_for_host(host: str) -> None:
    with _host_lock:
        last = _host_last.get(host, 0.0)
        wait = HOST_DELAY_S - (time.time() - last)
        if wait > 0:
            time.sleep(wait + random.uniform(0.2, 1.5))
        _host_last[host] = time.time()


def build_headers(host: str, ua: str) -> dict[str, str]:
    return {
        "User-Agent": ua,
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,image/apng,*/*;q=0.8"
        ),
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Sec-Ch-Ua": '"Chromium";v="132", "Google Chrome";v="132", "Not?A_Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        # Pretend we came from Google search.
        "Referer": f"https://www.google.com/",
        "DNT": "1",
    }


def extract_text(html: str, content_type: str) -> tuple[str, str]:
    if "html" not in (content_type or "").lower():
        return "", html[:60000]
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "iframe", "svg",
                     "nav", "footer", "aside", "form"]):
        tag.decompose()
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    elif soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)
    main = soup.find("article") or soup.find("main") or soup.body or soup
    import re
    text = main.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title[:300], text[:60000]


def fetch_one(url: str) -> dict:
    out_path = os.path.join(SCRAPED, f"{url_hash(url)}.json")
    host = host_of(url)
    wait_for_host(host)

    ua = random.choice(USER_AGENTS)
    record = {
        "url": url,
        "host": host,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "status": None,
        "http_status": None,
        "title": "",
        "final_url": "",
        "content_type": "",
        "text": "",
        "error": "",
        "retried": True,
    }
    try:
        sess = requests.Session()
        sess.headers.update(build_headers(host, ua))
        # Hit the homepage first to pick up cookies.
        try:
            home = f"https://{host}/"
            sess.get(home, timeout=10)
            time.sleep(random.uniform(0.5, 1.5))
        except Exception:
            pass
        r = sess.get(url, timeout=20, allow_redirects=True)
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
    except Exception as e:
        record["status"] = "error"
        record["error"] = f"{type(e).__name__}: {e}"[:200]

    # Preserve any earlier metadata.
    issue = bucket = None
    try:
        with open(out_path, encoding="utf-8") as f:
            old = json.load(f)
        issue = old.get("issue")
        bucket = old.get("bucket")
    except Exception:
        pass
    record["issue"] = issue
    record["bucket"] = bucket

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False)
    return record


def main():
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    targets = [m["url"] for m in manifest if m["status"] == "http_403"]
    print(f"Retrying {len(targets)} 403'd URLs")

    start = time.time()
    counts: dict[str, int] = {}
    done = 0
    # Lower parallelism to avoid burst detection.
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(fetch_one, u): u for u in targets}
        for fut in as_completed(futures):
            rec = fut.result()
            counts[rec["status"]] = counts.get(rec["status"], 0) + 1
            done += 1
            if done % 10 == 0 or done == len(targets):
                el = time.time() - start
                rate = done / el if el else 0
                print(f"  [{done:>3}/{len(targets)}]  {rate:.2f}/s  {counts}")
    print(f"\nFinal: {counts}")


if __name__ == "__main__":
    main()
