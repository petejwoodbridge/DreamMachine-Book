"""Extract every URL cited in the book manuscript and figure out which ones the
scraper hasn't already fetched. Write a top-up scrape list."""
import os
import re
import json
import hashlib

BOOK_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Book"
SCRAPED = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/scraped"
TOPUP = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/topup_urls.json"

URL_RE = re.compile(r"https?://[^\s<>)\]]+")

def url_hash(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]

urls = set()
for f in sorted(os.listdir(BOOK_DIR)):
    if not f.endswith(".md") or f.startswith("Welcome") or f.startswith("Citation"):
        continue
    text = open(os.path.join(BOOK_DIR, f), encoding="utf-8").read()
    for u in URL_RE.findall(text):
        urls.add(u.rstrip(".,);]>"))

book_urls = sorted(urls)
print(f"Unique URLs cited in book: {len(book_urls)}")

missing = []
for u in book_urls:
    path = os.path.join(SCRAPED, f"{url_hash(u)}.json")
    if not os.path.exists(path):
        missing.append(u)

print(f"Missing from scraped cache: {len(missing)}")

with open(TOPUP, "w", encoding="utf-8") as f:
    json.dump([{"url": u, "issue": None, "bucket": "book_cited"} for u in missing],
              f, indent=1)
print(f"Wrote top-up list: {TOPUP}")
