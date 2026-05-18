"""Cross-cut the dossiers: produce a tight per-chapter list of the captured
quotes and headline claims, so the author can scan and pick what to promote
into the manuscript.

For each chapter:
- For each scraped source: the host, the headline, the most quotable line.
- Skip sources where no notable quote was extracted (still listed by title).

Output: Research/digest.md — one compact file.
"""
import os
import re
from glob import glob

DOSSIER_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/dossier"
OUT = r"d:/VSCODE PROJECTS/DreamMachine Book/Research/digest.md"

HEAD_RE = re.compile(r"^### (https?://[^\n]+)$", re.M)
TITLE_RE = re.compile(r"^- \*\*Title:\*\* (.+)$", re.M)
HOST_RE = re.compile(r"^- \*\*Host:\*\* `([^`]+)`", re.M)
QUOTE_RE = re.compile(r"^- \*\*Notable quote:\*\*\n\s*> \"(.+)\"$", re.M)

CHAPTERS = sorted(glob(os.path.join(DOSSIER_DIR, "*.md")))

lines = []
lines.append("# Captured-Quote Digest\n")
lines.append("Every notable quote pulled from a successfully-scraped source, "
             "grouped by chapter. Use this to pick what to promote into the "
             "manuscript text rather than only the footnotes.\n")

total_quotes = 0
for path in CHAPTERS:
    fname = os.path.basename(path)
    if fname.startswith("12_") or fname.startswith("13_"):
        continue  # they have no/few captured sources
    title = fname.replace("_dossier.md", "")
    lines.append(f"\n---\n\n## {title}\n")

    text = open(path, encoding="utf-8").read()
    # Split on ### headings (one per URL)
    blocks = re.split(r"^### (https?://[^\n]+)$", text, flags=re.M)
    # blocks[0] is the dossier header before any URL; pairs follow
    chapter_quotes = 0
    for i in range(1, len(blocks), 2):
        url = blocks[i]
        body = blocks[i+1] if i+1 < len(blocks) else ""
        title_m = TITLE_RE.search(body)
        host_m = HOST_RE.search(body)
        quote_m = QUOTE_RE.search(body)
        if not title_m:
            continue  # not a captured one
        title_str = title_m.group(1)
        host = host_m.group(1) if host_m else ""
        line = f"- **{host}** — [{title_str[:120]}]({url})"
        if quote_m:
            line += f"  \n  > \"{quote_m.group(1)[:240]}\""
            chapter_quotes += 1
        lines.append(line)
    if chapter_quotes:
        total_quotes += chapter_quotes
        lines.append(f"\n*{chapter_quotes} quotes captured for this chapter.*")

lines.append(f"\n\n---\n\n**Total: {total_quotes} captured quotes across all chapters.**\n")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Wrote digest with {total_quotes} quotes -> {OUT}")
