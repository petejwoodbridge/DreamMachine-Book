"""Scrape the top-up URL list (book citations missing from the original corpus)."""
import importlib.util
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = r"d:/VSCODE PROJECTS/DreamMachine Book/Research"
spec = importlib.util.spec_from_file_location("scrape", os.path.join(ROOT, "scrape.py"))
scrape = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scrape)

topup = json.load(open(os.path.join(ROOT, "topup_urls.json"), encoding="utf-8"))
print(f"Top-up scraping {len(topup)} URLs")

start = time.time()
done = 0
status = {}
with ThreadPoolExecutor(max_workers=6) as pool:
    futures = {pool.submit(scrape.fetch_one, it): it for it in topup}
    for fut in as_completed(futures):
        rec = fut.result()
        done += 1
        status[rec["status"]] = status.get(rec["status"], 0) + 1
        if done % 10 == 0 or done == len(topup):
            elapsed = time.time() - start
            print(f"  [{done:>3}/{len(topup)}] {done/elapsed:.1f}/s — {status}")

print(f"\nFinal: {status}")
