"""One-off utility: swap front and back cover pages in every Dream Machine PDF.

Run after replacing Book/assets/cover.png and Book/assets/back_cover.png. This
re-renders 6"x9" cover PDFs from those images via headless Edge, then walks
every Dream_Machine*.pdf in Book/build/ and replaces page 1 (front cover) and
the final page (back cover) without touching the interior.

The KDP-interior PDF (no covers) is skipped automatically.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
BUILD = ROOT / "build"

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

COVER_SHELL = """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8"/>
  <title>cover</title>
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


def find_edge() -> str:
    for p in EDGE_PATHS:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("Microsoft Edge not found at expected paths.")


def render_cover_pdf(img: Path, html_out: Path, pdf_out: Path) -> None:
    html_out.write_text(
        COVER_SHELL.format(cover_uri=img.resolve().as_uri()),
        encoding="utf-8",
    )
    edge = find_edge()
    subprocess.run(
        [
            edge,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_out}",
            html_out.resolve().as_uri(),
        ],
        check=True,
        capture_output=True,
    )


def swap_covers(target: Path, front_pdf: Path, back_pdf: Path) -> None:
    """Replace the first and last page of `target` with the given cover PDFs."""
    src = fitz.open(target)
    n = src.page_count
    if n < 3:
        raise RuntimeError(f"{target.name} has only {n} pages — cannot swap covers")

    out = fitz.open()
    with fitz.open(front_pdf) as fp:
        out.insert_pdf(fp)
    # Interior pages: 1 .. n-2 (0-indexed, inclusive)
    out.insert_pdf(src, from_page=1, to_page=n - 2)
    with fitz.open(back_pdf) as bp:
        out.insert_pdf(bp)

    src.close()
    tmp = target.with_suffix(".pdf.tmp")
    out.save(tmp, garbage=4, deflate=True)
    out.close()
    os.replace(tmp, target)


def main() -> int:
    front_img = ASSETS / "cover.png"
    back_img = ASSETS / "back_cover.png"
    if not front_img.exists() or not back_img.exists():
        print("Missing cover images in assets/.", file=sys.stderr)
        return 1

    front_html = BUILD / "_cover.html"
    back_html = BUILD / "_back_cover.html"
    front_pdf = BUILD / "_cover.pdf"
    back_pdf = BUILD / "_back_cover.pdf"

    print(">> Rendering new cover PDFs from assets...")
    render_cover_pdf(front_img, front_html, front_pdf)
    render_cover_pdf(back_img, back_html, back_pdf)

    targets = sorted(
        p for p in BUILD.glob("Dream_Machine*.pdf")
        if "KDP_interior" not in p.name
    )
    if not targets:
        print("No target PDFs found.", file=sys.stderr)
        return 1

    print(f">> Swapping covers in {len(targets)} PDF(s):")
    for t in targets:
        before = t.stat().st_size
        swap_covers(t, front_pdf, back_pdf)
        after = t.stat().st_size
        print(f"   {t.name}  {before/1024/1024:.2f} MB -> {after/1024/1024:.2f} MB")

    for p in (front_html, back_html, front_pdf, back_pdf):
        try:
            p.unlink()
        except FileNotFoundError:
            pass

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
