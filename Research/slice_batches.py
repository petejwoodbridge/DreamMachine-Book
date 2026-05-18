"""Slice the URL index into agent-sized batches and write each batch as a text
file the research agents can read.
"""
import json
import os

IDX = json.load(open(r"d:/VSCODE PROJECTS/DreamMachine Book/Research/url_index.json", encoding="utf-8"))
OUT = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/batches"
os.makedirs(OUT, exist_ok=True)

# Priority order. Each tuple: (bucket, max_urls, batch_size)
PLAN = [
    ("research_policy", 20, 20),    # 1 batch
    ("primary_press", 80, 27),      # 3 batches
    ("industry_trade", 120, 30),    # 4 batches
    ("company_blog", 60, 30),       # 2 batches
    ("music_industry", 120, 30),    # 4 batches
    ("games_industry", 100, 25),    # 4 batches
    ("tech_press", 120, 30),        # 4 batches
    ("blog_essay", 13, 13),         # 1 batch
]

batch_files = []
for bucket, cap, size in PLAN:
    items = IDX["by_bucket"].get(bucket, [])
    items = items[:cap]
    for i in range(0, len(items), size):
        chunk = items[i:i + size]
        idx = i // size + 1
        path = os.path.join(OUT, f"{bucket}_{idx:02d}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Research batch: {bucket} #{idx}\n")
            f.write(f"# URLs: {len(chunk)}\n\n")
            for it in chunk:
                f.write(f"[Issue {it['issue']}] {it['url']}\n")
        batch_files.append((path, len(chunk)))

print(f"Wrote {len(batch_files)} batch files:")
for path, n in batch_files:
    print(f"  {os.path.basename(path):<32} {n:>3} URLs")
print(f"\nTotal URLs to research: {sum(n for _, n in batch_files)}")
