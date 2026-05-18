"""Analyse the scraped corpus and produce a per-chapter research dossier.

For each chapter footnote that points to a URL we successfully fetched, surface:
- the actual headline
- the published date if findable
- the load-bearing claim or quote
- relevance signal (does this confirm, contradict or extend what the chapter says?)

Output: Research/dossier/chapter_NN.md, one file per chapter.
"""
from __future__ import annotations
import hashlib
import json
import os
import re
from collections import defaultdict

ROOT = r"d:/VSCODE PROJECTS/DreamMachine Book"
BOOK_DIR = os.path.join(ROOT, "Book")
SCRAPED_DIR = os.path.join(ROOT, "Research", "scraped")
DOSSIER_DIR = os.path.join(ROOT, "Research", "dossier")
MANIFEST_PATH = os.path.join(ROOT, "Research", "manifest.json")

os.makedirs(DOSSIER_DIR, exist_ok=True)

_URL_ANGLE_RE = re.compile(r"<(https?://[^>]+)>")
_URL_BARE_RE = re.compile(r"https?://[^\s<>)\]]+")


class _UrlExtractor:
    """Extract URLs from a footnote body, preferring `<...>`-wrapped ones but
    catching bare URLs too. Trim trailing punctuation."""

    def findall(self, body: str) -> list[str]:
        wrapped = _URL_ANGLE_RE.findall(body)
        residual = _URL_ANGLE_RE.sub(" ", body)
        bare = _URL_BARE_RE.findall(residual)
        urls = wrapped + [u.rstrip(".,);]") for u in bare]
        seen = set()
        out = []
        for u in urls:
            if u not in seen:
                seen.add(u)
                out.append(u)
        return out

    def sub(self, repl: str, body: str) -> str:
        body = _URL_ANGLE_RE.sub(repl, body)
        body = _URL_BARE_RE.sub(repl, body)
        return body


URL_RE = _UrlExtractor()
FN_BODY_RE = re.compile(r"^\[\^(\d+)\]:\s*(.+?)(?=^\[\^|\Z)", re.M | re.S)

CHAPTER_FILES = [
    "00_Prologue.md",
    "01_The_Day_Sora_Landed.md",
    "02_The_Human_AI_Agency_Continuum.md",
    "03_Dead_Internet_Living_Web.md",
    "04_The_Slop_Ceiling.md",
    "05_The_88_Percent.md",
    "06_The_Studios_Decide.md",
    "07_Worlds_Not_Pictures.md",
    "08_AI_In_Everything.md",
    "09_The_Orchestrator.md",
    "10_Authenticity_New_Scarcity.md",
    "11_Coordination_Collapse.md",
    "12_Choosing_the_Future.md",
    "13_Epilogue.md",
]


def url_hash(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def load_scraped(url: str) -> dict | None:
    path = os.path.join(SCRAPED_DIR, f"{url_hash(url)}.json")
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def first_paragraphs(text: str, max_chars: int = 1200) -> str:
    """Return the leading paragraphs of an article, capped."""
    if not text:
        return ""
    # Skip navigation noise at the top: many articles repeat their headline,
    # publish date, and social-share gunk in the first 200 chars.
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    # Pull lines that look like real sentences (longer than 60 chars).
    para = []
    n = 0
    for ln in lines:
        if len(ln) < 50:
            continue
        para.append(ln)
        n += len(ln) + 1
        if n >= max_chars:
            break
    return "\n\n".join(para)[:max_chars]


def extract_quote(text: str) -> str:
    """Best-effort: pull the most striking quoted sentence from the body."""
    if not text:
        return ""
    # Prefer "smart" quotes commonly used in journalism.
    candidates = re.findall(r"[“\"]([^“”\"]{20,260})[”\"]", text)
    if not candidates:
        return ""
    # Heuristic: prefer the longest quote that contains a verb-like word and
    # isn't obviously chrome (cookies / subscribe / share).
    bad = ("cookie", "subscribe", "newsletter", "sign in", "log in", "share")
    candidates = [c for c in candidates if not any(b in c.lower() for b in bad)]
    if not candidates:
        return ""
    return max(candidates, key=len).strip()


def parse_chapter_footnotes(chapter_path: str) -> list[tuple[int, str, list[str]]]:
    """Return [(footnote_number, body_text, [urls])] for one chapter."""
    text = open(chapter_path, encoding="utf-8").read()
    out = []
    for m in FN_BODY_RE.finditer(text):
        num = int(m.group(1))
        body = m.group(2).strip()
        urls = URL_RE.findall(body)
        out.append((num, body, urls))
    return sorted(out, key=lambda t: t[0])


def chapter_label(filename: str) -> str:
    if filename.startswith("00"):
        return "Prologue"
    if filename.startswith("13"):
        return "Epilogue"
    n = int(filename.split("_")[0])
    return f"Chapter {n}"


def write_dossier(filename: str) -> dict:
    chapter_path = os.path.join(BOOK_DIR, filename)
    label = chapter_label(filename)
    notes = parse_chapter_footnotes(chapter_path)

    lines = []
    lines.append(f"# Research dossier — {label}\n")
    lines.append(f"Source file: `{filename}`\n")
    lines.append(f"Footnotes parsed: {len(notes)}\n")
    lines.append("\n---\n")

    captured = 0
    failed = 0

    for num, body, urls in notes:
        lines.append(f"## Footnote [{num}]\n")
        # Strip URLs from the body for the heading line.
        body_clean = URL_RE.sub("", body)
        body_clean = re.sub(r"\s{2,}", " ", body_clean).strip()
        lines.append(f"*Citation as written:* {body_clean[:240]}{'…' if len(body_clean) > 240 else ''}\n")

        if not urls:
            lines.append("_No URL in footnote (newsletter cross-reference only)._\n")
            continue

        for url in urls:
            rec = load_scraped(url)
            lines.append(f"### {url}")
            if rec is None:
                lines.append("- *Not yet scraped.*")
                failed += 1
                continue
            if rec.get("status") != "ok":
                lines.append(f"- *Fetch status:* `{rec.get('status')}` "
                             f"(HTTP {rec.get('http_status')})")
                failed += 1
                continue
            captured += 1
            title = (rec.get("title") or "").replace("\n", " ").strip()
            text = rec.get("text") or ""
            lines.append(f"- **Title:** {title or '(no title found)'}")
            lines.append(f"- **Host:** `{rec.get('host')}`")
            lines.append(f"- **Final URL:** {rec.get('final_url') or url}")
            lines.append(f"- **Captured text:** {len(text):,} chars")
            quote = extract_quote(text)
            if quote:
                lines.append(f"- **Notable quote:**\n  > \"{quote}\"")
            lede = first_paragraphs(text, 1000)
            if lede:
                lines.append(f"- **Lede:**\n\n```\n{lede}\n```")
        lines.append("")

    summary = {
        "chapter": label,
        "file": filename,
        "footnotes": len(notes),
        "captured": captured,
        "failed": failed,
    }
    lines.append("\n---\n")
    lines.append(f"## Summary\n")
    lines.append(f"- Footnotes: {len(notes)}")
    lines.append(f"- Successfully scraped sources: {captured}")
    lines.append(f"- Failed / not-yet-scraped: {failed}")

    out_path = os.path.join(DOSSIER_DIR, filename.replace(".md", "_dossier.md"))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return summary


def main():
    if not os.path.exists(MANIFEST_PATH):
        print("No manifest yet — scrape still running. Re-run after scrape completes.")
    else:
        manifest = json.load(open(MANIFEST_PATH, encoding="utf-8"))
        total = len(manifest)
        ok = sum(1 for m in manifest if m["status"] == "ok")
        print(f"Manifest: {total} records, {ok} successful ({100*ok/total:.1f}%)")

    summaries = []
    for f in CHAPTER_FILES:
        if not os.path.exists(os.path.join(BOOK_DIR, f)):
            continue
        s = write_dossier(f)
        summaries.append(s)
        print(f"  {s['chapter']:<13} {s['footnotes']:>3} notes  "
              f"{s['captured']:>3} captured  {s['failed']:>3} missing")

    total_notes = sum(s["footnotes"] for s in summaries)
    total_cap = sum(s["captured"] for s in summaries)
    print(f"\nTotal: {total_notes} footnotes, {total_cap} with captured content "
          f"({100*total_cap/total_notes:.1f}%)")
    print(f"Dossiers written to: {DOSSIER_DIR}")


if __name__ == "__main__":
    main()
