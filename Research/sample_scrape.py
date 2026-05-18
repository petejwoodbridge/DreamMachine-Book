"""Run the scraper against a 20-URL sample drawn from across the bucket mix."""
import json
import os
import sys
import importlib.util

ROOT = r"d:/VSCODE PROJECTS/DreamMachine Book/Research"

spec = importlib.util.spec_from_file_location("scrape", os.path.join(ROOT, "scrape.py"))
scrape = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scrape)

idx = json.load(open(os.path.join(ROOT, "url_index.json"), encoding="utf-8"))

# Pull a handful from each priority bucket.
sample = []
quota = {
    "primary_press": 4,
    "industry_trade": 4,
    "music_industry": 3,
    "games_industry": 3,
    "company_blog": 3,
    "research_policy": 2,
    "tech_press": 1,
}
for bucket, n in quota.items():
    items = idx["by_bucket"].get(bucket, [])[:n]
    sample.extend(items)

print(f"Sampling {len(sample)} URLs across buckets")
for it in sample:
    rec = scrape.fetch_one(it)
    status = rec["status"]
    title = (rec.get("title") or "")[:80]
    chars = len(rec.get("text", ""))
    print(f"  [{status:>14}] {chars:>6} chars  {title}")
    print(f"                  {it['url']}")
