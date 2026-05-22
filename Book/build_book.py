"""Build the Dream Machine manuscript and render it to PDF.

Pipeline:
    1. Read chapter files in CHAPTER_ORDER (and APPENDIX_ORDER).
    2. Normalise chapter headings: "# Chapter N" + "## Title" -> "# Chapter N — Title".
    3. Assemble front matter (cover, title page, copyright, back-cover blurb,
       table of contents placeholder) and back matter (citation index).
    4. Write the combined manuscript to build/manuscript.md.
    5. Run pandoc to produce build/manuscript.html with an embedded book.css.
    6. Run headless Microsoft Edge to render the HTML to PDF.

Run:
    python Book/build_book.py
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # Book/
BUILD = ROOT / "build"
ASSETS = ROOT / "assets"
BUILD.mkdir(exist_ok=True)

OUT_MD = BUILD / "manuscript.md"
OUT_HTML = BUILD / "manuscript.html"
COVER_HTML = BUILD / "_cover.html"
BACK_COVER_HTML = BUILD / "_back_cover.html"
COVER_PDF = BUILD / "_cover.pdf"
BACK_COVER_PDF = BUILD / "_back_cover.pdf"
CONTENT_PDF = BUILD / "_content.pdf"
CITATION_INDEX = ROOT / "Citation_Index.md"

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

# --- Source order ----------------------------------------------------------

FRONT_FILES = [
    "00_Foreword.md",
    "00a_Reader_Paths.md",
]

CHAPTER_FILES = [
    "01_The_Day_Sora_Landed.md",
    "02_A_History_of_Resistance.md",
    "03_The_Human_AI_Agency_Continuum.md",
    "04_Dead_Internet_Living_Web.md",
    "05_The_Slop_Ceiling.md",
    "06_The_88_Percent.md",
    "07_The_Studios_Decide.md",
    "08_Worlds_Not_Pictures.md",
    "09_AI_In_Everything.md",
    "10_What_Is_Newly_Possible.md",
    "11_The_Orchestrator.md",
    "12_Authenticity_New_Scarcity.md",
    "13_Coordination_Collapse.md",
    "14_The_New_Jobs.md",
    "15_Choosing_the_Future.md",
    "16_The_Tools.md",
    "17_Five_Years_Inside_the_Dream_Machine.md",
    "18_Epilogue.md",
]

APPENDIX_FILES = [
    "A1_Appendix_Quantitative_Anatomy.md",
    "A2_Glossary.md",
    "A3_Bibliography_by_Topic.md",
    "A4_Deep_Dive_Shadow_AI.md",
    "A5_Deep_Dive_Adoption_Dynamics.md",
    "A6_Deep_Dive_AI_Stigma.md",
    "A7_Deep_Dive_AI_Intent.md",
    "A8_Source_Index.md",
]

TITLE = "Dream Machine"
SUBTITLE = "The New Creative Economy"
AUTHOR = "Pete Woodbridge"
PLACE = "DreamLab, the North West, UK"
DATE = "21 May 2026"
# Used both in the colophon and in the output PDF filename. Each new edition
# of the book gets a fresh dated PDF so prior versions are retained alongside.
EDITION_SLUG = "2026-05-21"
OUT_PDF = BUILD / f"Dream_Machine_{EDITION_SLUG}.pdf"

# --- Header normaliser ----------------------------------------------------

CHAPTER_HEADER_RE = re.compile(
    r"\A#\s+(?P<kind>Chapter\s+\d+|Epilogue|Foreword|Appendix\s+[A-Z][^\n]*)\s*\n+##\s+(?P<title>[^\n]+)\s*\n+",
    re.DOTALL,
)

H1_ONLY_RE = re.compile(r"\A#\s+(?P<title>[^\n]+)\s*\n+")


def normalise_chapter(text: str, fallback_label: str | None = None) -> tuple[str, str]:
    """Collapse the chapter's two top headings into one and return (normalised text, display title)."""
    m = CHAPTER_HEADER_RE.match(text)
    if m:
        kind = re.sub(r"\s+", " ", m.group("kind").strip())
        title = m.group("title").strip()
        display = f"{kind} — {title}" if "Appendix" not in kind else kind
        body = text[m.end():]
        # Demote any remaining H2s to H3 etc. to avoid duplicate top-level headings
        body = demote_headings(body)
        return f"# {display}\n\n{body}", display
    m = H1_ONLY_RE.match(text)
    if m:
        title = m.group("title").strip()
        body = text[m.end():]
        body = demote_headings(body)
        display = title if not fallback_label else f"{fallback_label}: {title}"
        return f"# {display}\n\n{body}", display
    # Fall back: leave content as-is, prepend the label
    if fallback_label:
        return f"# {fallback_label}\n\n{text}", fallback_label
    return text, "Untitled"


def demote_headings(text: str) -> str:
    """Demote every H2 in `text` to H3, etc., so the chapter's top heading is the only H1/H2.

    Because the chapter's own "## Title" is already stripped by normalise_chapter, anything
    starting with "## " in `text` is a section, and should become H3 in the final document.
    """
    lines = text.split("\n")
    out = []
    in_code = False
    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        if re.match(r"^#{2,5}\s", line):
            out.append("#" + line)  # add one level of depth
        else:
            out.append(line)
    return "\n".join(out)


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


# --- Footnote prefixing ---------------------------------------------------

_FOOTNOTE_REF_RE = re.compile(r"\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]")


def prefix_footnotes(text: str, prefix: str) -> str:
    """Make footnote IDs unique by prefixing them with a per-chapter slug.

    Catches both definitions (``[^x]: ...``) and references (``[^x]``).
    Skips inline notes ``^[...]`` since those have no IDs.
    """
    def repl(m: re.Match[str]) -> str:
        ident = m.group(1)
        if ident.startswith(prefix + "-"):
            return m.group(0)
        return f"[^{prefix}-{ident}]"
    return _FOOTNOTE_REF_RE.sub(repl, text)


def slugify_for_footnote(name: str) -> str:
    base = Path(name).stem.lower()
    return re.sub(r"[^a-z0-9]+", "", base)[:12] or "ch"


# --- Pandoc-compatible heading slug ---------------------------------------

def pandoc_slug(text: str) -> str:
    """Replicate Pandoc's heading-id algorithm closely enough for our use."""
    import unicodedata
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    # Lowercase
    text = text.lower()
    # Replace anything not [a-z0-9_-] with a space, then collapse runs to single dash
    text = re.sub(r"[^a-z0-9_\-]+", " ", text)
    text = re.sub(r"\s+", "-", text.strip())
    # Strip leading non-letter (Pandoc requires id starts with a letter)
    text = re.sub(r"^[^a-z]+", "", text)
    return text or "section"


# --- Front matter (HTML, no Pandoc parsing) -------------------------------

def build_static_front_matter() -> str:
    """Title page, half-title, blurb, epigraph — pure HTML, no markdown."""
    parts = []

    # Half-title page
    parts.append(
        f'<div class="half-title-page">'
        f'<h1 class="half-title">{TITLE}</h1>'
        f'<p class="half-title-url">'
        f'<a href="https://dreamlab.org.uk">dreamlab.org.uk</a>'
        f'</p>'
        f'</div>'
    )

    # Title page
    parts.append(
        f'<div class="title-page">'
        f'<h1 class="book-title">{TITLE}</h1>'
        f'<h2 class="book-subtitle">{SUBTITLE}</h2>'
        f'<p class="book-author">{AUTHOR}</p>'
        f'<p class="book-edition-date">{DATE}</p>'
        f'<p class="book-imprint">DreamLab AI Collective</p>'
        f'</div>'
    )

    # Copyright / colophon page
    parts.append(
        f'<div class="colophon-page">'
        f'<p class="colophon">'
        f'<em>{TITLE}: {SUBTITLE}</em><br/>'
        f'© 2026 {AUTHOR}. All rights reserved.<br/>'
        f'Edition of {DATE}.<br/><br/>'
        f'Written and edited at DreamLab in the North West of England, '
        f'between October 2025 and May 2026, in parallel with thirty weekly '
        f'editions of the <em>Dream Machine</em> newsletter.<br/><br/>'
        f'All footnoted claims are sourced. Every footnote links either to a '
        f'primary source or to the issue of <em>Dream Machine</em> in which the '
        f'item was first discussed.'
        f'</p>'
        f'</div>'
    )

    # Back-cover blurb / praise page (drawn from MARKETING.md)
    parts.append(
        f'<div class="blurb-page">'
        f'<h2 class="blurb-heading">About this book</h2>'
        f'<p class="blurb">'
        f'In September 2025, a synthetic actress walked onto a Zurich film '
        f'festival stage, OpenAI shipped Sora 2, and Pete Woodbridge sat down '
        f'to write a newsletter about it. Thirty weekly issues later, what '
        f'began as a one-month experiment had become <em>Dream Machine</em> — '
        f'the most-read working-creative record of the AI transition.'
        f'</p>'
        f'<p class="blurb">'
        f'This is the book that record produced. From the slop ceiling that the '
        f'audience is already enforcing, to the 88% of UK creators demanding '
        f'licensing in all cases, to the chess-grandmaster strategy of '
        f'deliberately playing the move the machine wouldn’t make — Woodbridge '
        f'holds the whole picture together in a way no journalist, academic or '
        f'platform-company keynote has managed.'
        f'</p>'
        f'<p class="blurb">'
        f'Equal parts history, manifesto and operating manual, <em>Dream '
        f'Machine</em> is the field guide to the most consequential year in '
        f'creative work since cinema learned to talk.'
        f'</p>'
        f'<p class="blurb-tagline">'
        f'<em>The age of the </em>How<em> is ending. Welcome the </em>Why<em>.</em>'
        f'</p>'
        f'</div>'
    )

    return "\n".join(parts)


def build_toc(entries: list[tuple[str, str, str]],
              page_numbers: dict[str, int] | None = None) -> str:
    """Build a clickable TOC from a list of (kind, label, id) tuples.

    ``kind`` is one of: 'front', 'chapter', 'appendix', 'index'.
    If ``page_numbers`` is provided, render the page number next to each entry.
    """
    rows: list[str] = []
    rows.append('<div class="toc-page">')
    rows.append('<h1 class="toc-heading">Contents</h1>')
    rows.append('<ul class="toc-list">')
    last_kind = None
    for kind, label, ident in entries:
        if kind != last_kind and kind in {"appendix", "index"}:
            rows.append('</ul>')
            rows.append(f'<h2 class="toc-section-heading">'
                        f'{"Appendices" if kind == "appendix" else "Reference"}</h2>')
            rows.append('<ul class="toc-list">')
        css = f"toc-entry toc-{kind}"
        page_num_html = ""
        if page_numbers and ident in page_numbers:
            page_num_html = f'<span class="toc-page-num">{page_numbers[ident]}</span>'
        rows.append(
            f'<li class="{css}">'
            f'<a href="#{ident}">'
            f'<span class="toc-label">{label}</span>'
            f'<span class="toc-leader"></span>'
            f'{page_num_html}'
            f'</a>'
            f'</li>'
        )
        last_kind = kind
    rows.append('</ul>')
    rows.append('</div>')
    return "\n".join(rows)


def find_chapter_pages(content_pdf: Path,
                       toc_entries: list[tuple[str, str, str]]) -> dict[str, int]:
    """Return a dict mapping chapter id to its 1-indexed page in content_pdf.

    Strategy: each chapter starts with a single-letter drop cap rendered at
    ~23pt (from the CSS rule ``section.level1 > h1 + p::first-letter``). These
    drop caps are unique 1-letter glyphs at large font size, appearing exactly
    once per chapter at the chapter's opening paragraph. Find them in document
    order and zip with TOC entries.
    """
    import fitz
    pdf = fitz.open(content_pdf)

    drop_cap_pages: list[int] = []
    for pg_idx in range(pdf.page_count):
        page = pdf[pg_idx]
        for block in page.get_text("dict").get("blocks", []):
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    size = span.get("size", 0)
                    # Drop cap: single letter, >=22pt
                    if size >= 22 and len(text) == 1 and text.isalpha():
                        drop_cap_pages.append(pg_idx + 1)
                        break
                else:
                    continue
                break

    result: dict[str, int] = {}
    for entry, page in zip(toc_entries, drop_cap_pages):
        kind, label, ident = entry
        result[ident] = page

    pdf.close()
    return result


# --- Citation index -------------------------------------------------------

URL_RE = re.compile(r"<(https?://[^>]+)>")
FOOTNOTE_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.+)$", re.M)


def build_citation_index(chapter_data: list[tuple[str, str]]) -> str:
    """Build a markdown citation index keyed by chapter label."""
    lines: list[str] = []
    lines.append("# Citation Index\n")
    lines.append(f"*{TITLE}: {SUBTITLE}*\n")
    lines.append(
        "All footnoted sources, organised by chapter. Every claim of substance "
        "in the manuscript is anchored to one of these references.\n"
    )
    lines.append("\n---\n")

    total = 0
    unique_urls: set[str] = set()

    for label, raw_text in chapter_data:
        notes = FOOTNOTE_RE.findall(raw_text)
        if not notes:
            continue
        lines.append(f"## {label}\n")
        for num, body in notes:
            lines.append(f"**{num}.** {body}\n")
            for url in URL_RE.findall(body):
                unique_urls.add(url)
        total += len(notes)
        lines.append("")

    lines.append("\n---\n")
    lines.append("## Summary\n")
    lines.append(f"- **Total footnotes**: {total}")
    lines.append(f"- **Unique primary-source URLs cited**: {len(unique_urls)}")
    lines.append("- **Source corpus**: 30 editions of *Dream Machine | Creative AI* (October 2025 – May 2026)\n")

    return "\n".join(lines)


# --- Assembly --------------------------------------------------------------

def assemble() -> tuple[str, list[tuple[str, str, str]]]:
    """Read every chapter, build the markdown body, and return (body_md, toc_entries)."""
    pieces: list[str] = []
    chapter_data: list[tuple[str, str]] = []   # (label, raw_text) for the citation index
    toc_entries: list[tuple[str, str, str]] = []  # (kind, label, id)

    def add(file: str, kind: str) -> None:
        raw = read(file)
        normalised, label = normalise_chapter(raw)
        # The slug Pandoc will assign to the chapter's H1
        ident = pandoc_slug(label)
        chapter_data.append((label, raw))
        normalised = prefix_footnotes(normalised, slugify_for_footnote(file))
        pieces.append(normalised)
        toc_entries.append((kind, label, ident))

    for f in FRONT_FILES:
        add(f, "front")
    for f in CHAPTER_FILES:
        add(f, "chapter")
    for f in APPENDIX_FILES:
        add(f, "appendix")

    # Citation index (write to file + include in manuscript)
    citation_md = build_citation_index(chapter_data)
    CITATION_INDEX.write_text(citation_md, encoding="utf-8")
    pieces.append(citation_md)
    toc_entries.append(("index", "Citation Index", pandoc_slug("Citation Index")))

    body_md = "\n\n".join(pieces)
    return body_md, toc_entries


# --- Pandoc + Edge --------------------------------------------------------

def find_edge() -> str:
    for p in EDGE_PATHS:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("Microsoft Edge not found at expected paths.")


CONTENT_SHELL = """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <link rel="stylesheet" href="{css_uri}"/>
</head>
<body>
{static_front}
{toc}
{body}
</body>
</html>
"""

COVER_SHELL = """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <style>
    @page {{ size: 6in 9in; margin: 0; }}
    html, body {{ margin: 0; padding: 0; width: 6in; height: 9in; }}
    .full-cover {{
      width: 6in;
      height: 9in;
      background-image: url("{cover_uri}");
      background-size: cover;
      background-position: center bottom;
      background-repeat: no-repeat;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
  </style>
</head>
<body><div class="full-cover"></div></body>
</html>
"""


def render_content_html(md_text: str,
                        toc_entries: list[tuple[str, str, str]],
                        page_numbers: dict[str, int] | None = None) -> None:
    OUT_MD.write_text(md_text, encoding="utf-8")
    css = ASSETS / "book.css"

    # Re-run pandoc only on the first pass; on the second pass the body HTML
    # hasn't changed, only the TOC. Skip pandoc when _body.html exists fresh.
    body_html_file = BUILD / "_body.html"
    if page_numbers is None or not body_html_file.exists():
        cmd = [
            "pandoc",
            str(OUT_MD),
            "-o", str(body_html_file),
            "--from=markdown+footnotes+raw_html+smart+inline_notes",
            "--to=html5",
            "--section-divs",
            "--no-highlight",
        ]
        subprocess.run(cmd, check=True)
    body_html = body_html_file.read_text(encoding="utf-8")

    page = CONTENT_SHELL.format(
        title=TITLE,
        css_uri=css.resolve().as_uri(),
        static_front=build_static_front_matter(),
        toc=build_toc(toc_entries, page_numbers),
        body=body_html,
    )
    OUT_HTML.write_text(page, encoding="utf-8")


def render_cover_html(out: Path, img_filename: str) -> None:
    img_uri = (ASSETS / img_filename).resolve().as_uri()
    out.write_text(COVER_SHELL.format(title=TITLE, cover_uri=img_uri), encoding="utf-8")


def edge_print(html: Path, pdf: Path) -> None:
    edge = find_edge()
    cmd = [
        edge,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf}",
        html.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def merge_pdfs(parts: list[Path], out: Path) -> None:
    import fitz  # PyMuPDF
    merged = fitz.open()
    for p in parts:
        with fitz.open(p) as src:
            merged.insert_pdf(src)
    merged.save(out)
    merged.close()


def render_pdf(md: str, toc_entries: list[tuple[str, str, str]]) -> None:
    # 1. Covers (standalone PDFs, zero margins)
    render_cover_html(COVER_HTML, "cover.png")
    edge_print(COVER_HTML, COVER_PDF)
    render_cover_html(BACK_COVER_HTML, "back_cover.png")
    edge_print(BACK_COVER_HTML, BACK_COVER_PDF)

    # 2. First pass: render content with empty page numbers
    print("   pass 1: rendering content for page-number discovery")
    edge_print(OUT_HTML, CONTENT_PDF)

    # 3. Find which page each chapter starts on within content PDF
    page_map = find_chapter_pages(CONTENT_PDF, toc_entries)
    # Offset by 1 to account for the front cover that will precede content
    final_pages = {k: v + 1 for k, v in page_map.items()}
    print(f"   discovered {len(final_pages)}/{len(toc_entries)} chapter pages")

    # 4. Second pass: re-render content with real page numbers in the TOC
    print("   pass 2: re-rendering content with TOC page numbers")
    render_content_html(md, toc_entries, final_pages)
    edge_print(OUT_HTML, CONTENT_PDF)

    # 5. Merge front cover + content + back cover
    merge_pdfs([COVER_PDF, CONTENT_PDF, BACK_COVER_PDF], OUT_PDF)

    # Clean up
    for p in (COVER_PDF, BACK_COVER_PDF, CONTENT_PDF, COVER_HTML, BACK_COVER_HTML):
        try: p.unlink()
        except FileNotFoundError: pass


def rebuild_site() -> None:
    """Refresh the static-site data catalogs (tools/issues/use-cases/etc).

    The site lives under ../site/ and is regenerated from the same markdown
    sources the book is built from, so each new edition picks up the latest
    tool inventory, newsletter issues and chapter titles automatically.
    Silently skipped if site/build_site.py is missing.
    """
    site_builder = ROOT.parent / "site" / "build_site.py"
    if not site_builder.exists():
        return
    print(">> Refreshing site data...")
    try:
        subprocess.run([sys.executable, str(site_builder)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"   site refresh failed ({e}); continuing", file=sys.stderr)


def main() -> int:
    print(">> Assembling manuscript...")
    md, toc_entries = assemble()
    word_count = len(md.split())
    print(f"   Words: {word_count:,}  TOC entries: {len(toc_entries)}")

    print(">> Rendering HTML via pandoc...")
    render_content_html(md, toc_entries)
    print(f"   {OUT_HTML}")

    print(">> Rendering PDF (two-pass for TOC page numbers)...")
    render_pdf(md, toc_entries)
    print(f"   {OUT_PDF}")

    rebuild_site()

    if OUT_PDF.exists():
        size_mb = OUT_PDF.stat().st_size / (1024 * 1024)
        print(f"\nDone. PDF: {OUT_PDF}  ({size_mb:.2f} MB)")
        return 0
    print("PDF was not produced.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
