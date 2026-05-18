"""Convert each Deep Dive PDF into a .md file in a 'Deep Dive MD' folder,
preserving embedded hyperlinks as inline [text](url) markdown.
"""
import os
import warnings
import logging

logging.getLogger("pdfminer").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

import pdfplumber

SRC_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Deep Dive PDFs"
OUT_DIR = r"d:/VSCODE PROJECTS/DreamMachine Book/Deep Dive MD"

os.makedirs(OUT_DIR, exist_ok=True)


def rect_overlap(word, link):
    cx = (word["x0"] + word["x1"]) / 2
    cy = (word["top"] + word["bottom"]) / 2
    return link["x0"] <= cx <= link["x1"] and link["top"] <= cy <= link["bottom"]


def page_to_markdown(page):
    links = page.hyperlinks or []
    words = page.extract_words(
        x_tolerance=2,
        y_tolerance=3,
        keep_blank_chars=False,
        use_text_flow=True,
        extra_attrs=["fontname", "size"],
    )

    for w in words:
        w["uri"] = None
        for link in links:
            if rect_overlap(w, link):
                w["uri"] = link.get("uri")
                break

    lines = {}
    for w in words:
        key = round(w["top"] / 3) * 3
        lines.setdefault(key, []).append(w)

    out_lines = []
    for key in sorted(lines.keys()):
        line_words = sorted(lines[key], key=lambda w: w["x0"])
        parts = []
        i = 0
        while i < len(line_words):
            w = line_words[i]
            if w["uri"]:
                uri = w["uri"]
                group = [w["text"]]
                j = i + 1
                while j < len(line_words) and line_words[j]["uri"] == uri:
                    group.append(line_words[j]["text"])
                    j += 1
                text = " ".join(group)
                text = text.replace("[", "\\[").replace("]", "\\]")
                parts.append(f"[{text}]({uri})")
                i = j
            else:
                parts.append(w["text"])
                i += 1
        out_lines.append(" ".join(parts))

    return out_lines


def convert(pdf_path, md_path):
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    with pdfplumber.open(pdf_path) as pdf:
        chunks = [f"# {title}\n"]
        for i, page in enumerate(pdf.pages, start=1):
            chunks.append(f"\n## Page {i}\n")
            lines = page_to_markdown(page)
            chunks.append("\n".join(lines))

        all_uris = []
        seen = set()
        for page in pdf.pages:
            for link in page.hyperlinks or []:
                u = link.get("uri")
                if u and u not in seen:
                    seen.add(u)
                    all_uris.append(u)

        if all_uris:
            chunks.append("\n\n---\n\n## All embedded URLs (in document order)\n")
            for u in all_uris:
                chunks.append(f"- {u}")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(chunks) + "\n")


def main():
    files = [f for f in os.listdir(SRC_DIR) if f.lower().endswith(".pdf")]
    files.sort()
    for f in files:
        pdf_path = os.path.join(SRC_DIR, f)
        md_path = os.path.join(OUT_DIR, os.path.splitext(f)[0] + ".md")
        print(f"Converting {f} -> {os.path.basename(md_path)}")
        convert(pdf_path, md_path)
    print(f"\nDone. {len(files)} files written to {OUT_DIR}")


if __name__ == "__main__":
    main()
