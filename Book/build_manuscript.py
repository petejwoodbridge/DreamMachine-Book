"""Build the final manuscript: combine chapter files into a single book.md and
a citation index extracted from all footnotes.
"""
import os
import re

BOOK_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Book"
OUT_MANUSCRIPT = os.path.join(BOOK_DIR, "Welcome_to_the_Dream_Machine.md")
OUT_INDEX = os.path.join(BOOK_DIR, "Citation_Index.md")

CHAPTER_ORDER = [
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

TITLE = "Welcome to the Dream Machine"
SUBTITLE = "The Next Creative Economy"
AUTHOR = "Pete Woodbridge"
PLACE = "DreamLab, the North West, UK"
DATE = "May 2026"

URL_RE = re.compile(r"<(https?://[^>]+)>")

def main():
    # === Build the manuscript ===
    out = []

    # Title page
    out.append(f"# {TITLE}\n")
    out.append(f"## *{SUBTITLE}*\n")
    out.append(f"**{AUTHOR}**\n")
    out.append(f"*{PLACE}*  ")
    out.append(f"*{DATE}*\n")
    out.append("\n---\n")

    # Table of contents
    out.append("## Contents\n")
    toc_items = [
        ("Prologue", "Welcome to the Dream Machine"),
        ("Chapter 1", "The Day Sora Landed"),
        ("Chapter 2", "The Human–AI Agency Continuum"),
        ("Chapter 3", "Dead Internet, Living Web"),
        ("Chapter 4", "The Slop Ceiling"),
        ("Chapter 5", "The 88%"),
        ("Chapter 6", "The Studios Decide"),
        ("Chapter 7", "Worlds, Not Pictures"),
        ("Chapter 8", "AI in Everything, Everywhere, All at Once"),
        ("Chapter 9", "The Orchestrator"),
        ("Chapter 10", "Authenticity as the New Scarcity"),
        ("Chapter 11", "Coordination Collapse"),
        ("Chapter 12", "Choosing the Future"),
        ("Epilogue", "A Letter from the Dream Machine"),
    ]
    for kind, title in toc_items:
        out.append(f"- **{kind}** — {title}")
    out.append("\n---\n")

    # Concatenate each chapter
    for f in CHAPTER_ORDER:
        path = os.path.join(BOOK_DIR, f)
        text = open(path, encoding="utf-8").read()
        out.append(text)
        out.append("\n\\newpage\n")

    # Save
    manuscript = "\n".join(out)
    with open(OUT_MANUSCRIPT, "w", encoding="utf-8") as fh:
        fh.write(manuscript)

    # === Build the citation index ===
    # Extract every footnote definition from each chapter
    fn_pattern = re.compile(r"^\[\^(\d+[a-z]?)\]:\s*(.+)$", re.M)
    by_chapter = []

    for f in CHAPTER_ORDER:
        if f == "00_Prologue.md":
            chapter_label = "Prologue"
        elif f == "13_Epilogue.md":
            chapter_label = "Epilogue"
        else:
            num = int(f.split("_")[0])
            chapter_label = f"Chapter {num}"

        text = open(os.path.join(BOOK_DIR, f), encoding="utf-8").read()
        notes = fn_pattern.findall(text)
        if notes:
            by_chapter.append((chapter_label, notes))

    # Write the citation index
    idx_lines = []
    idx_lines.append(f"# Citation Index\n")
    idx_lines.append(f"*{TITLE}: {SUBTITLE}*\n")
    idx_lines.append(f"All footnoted sources, by chapter. Every claim of substance "
                     f"in the manuscript is anchored to one of these references.\n")
    idx_lines.append("\n---\n")

    total = 0
    unique_urls = set()

    for chapter_label, notes in by_chapter:
        idx_lines.append(f"## {chapter_label}\n")
        for num, body in notes:
            idx_lines.append(f"**{num}.** {body}\n")
            for url in URL_RE.findall(body):
                unique_urls.add(url)
        total += len(notes)
        idx_lines.append("")

    idx_lines.append("\n---\n")
    idx_lines.append(f"## Summary\n")
    idx_lines.append(f"- **Total footnotes**: {total}")
    idx_lines.append(f"- **Unique primary-source URLs cited**: {len(unique_urls)}")
    idx_lines.append(f"- **Source corpus**: 29 editions of *Dream Machine | Creative AI* (October 2025 – May 2026)\n")

    with open(OUT_INDEX, "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx_lines))

    # Word count
    word_count = len(manuscript.split())

    print(f"Manuscript: {OUT_MANUSCRIPT}")
    print(f"  Words: {word_count:,}")
    print(f"Citation index: {OUT_INDEX}")
    print(f"  Footnotes: {total}")
    print(f"  Unique URLs: {len(unique_urls)}")


if __name__ == "__main__":
    main()
