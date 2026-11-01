#!/usr/bin/env python3
"""Buduje PDF z pliku HTML przygotowanego dla MuPDF Story.

PDF powstaje przez PyMuPDF Story, więc potrzebna jest wersja HTML, w której wzory
są obrazkami PNG (matplotlib mathtext):
    kompendium:  build.py --pdf-src   -> kompendium/_pdf_source.html
    szybkie:     build_szybkie.py     -> szybkie/_pdf_source.html

Użycie:
    python3 mkpdf.py                       # kompendium -> kompendium/kompendium.pdf
    python3 mkpdf.py SRC.html OUT.pdf KAT  # dowolny dokument (KAT = katalog z obrazkami)
"""
from __future__ import annotations

import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CSS = """
@page { size: A4; }
body { font-size: 9pt; line-height: 1.45; color: #16202c; font-family: sans-serif; }
h1 { font-size: 21pt; color: #16202c; margin: 0 0 6pt 0; }
h2 { font-size: 15pt; color: #16202c; border-bottom: 1px solid #e2e8ee; margin-top: 16pt; }
h3 { font-size: 11.5pt; color: #0b5fa5; margin-top: 12pt; }
h4 { font-size: 10pt; color: #4a5a6a; }
p { margin: 3pt 0; }
li { margin: 1pt 0; }
.box { margin: 5pt 0; padding: 5pt 7pt; background-color: #f6f8fa; border-left: 3px solid #7b8794; }
.box-title { font-size: 7pt; font-weight: bold; color: #4a5a6a; margin: 0 0 2pt 0; }
.box.def { background-color: #f2f8fd; border-left-color: #2979b8; }
.box.wzor { background-color: #f7f5ff; border-left-color: #6d28d9; }
.box.uwaga { background-color: #fffbeb; border-left-color: #c98a06; }
.box.pulapka { background-color: #fdf2f2; border-left-color: #c0392b; }
.box.przyklad { background-color: #f4faf6; border-left-color: #157f4b; }
.box.metoda { background-color: #f2fbfb; border-left-color: #0e7c86; }
.box.zapamietaj { background-color: #f5f7ff; border-left-color: #3b4fbe; }
.box.klucz { background-color: #f0f7f4; border-left-color: #0f766e; }
.box.ciekawostka { background-color: #fafafa; border-left-color: #8b8b8b; }
table { border-collapse: collapse; font-size: 8pt; margin: 4pt 0; width: 100%; }
th, td { border: 1px solid #d7dee5; padding: 2pt 4pt; }
th { background-color: #f2f5f8; font-weight: bold; }
figure { margin: 6pt 0; }
figcaption { font-size: 7.5pt; color: #7b8794; margin-top: 2pt; }
img { max-width: 100%; }
.mathimg { margin: 0 1pt; }
.mathblock { display: block; text-align: center; margin: 4pt 0; }
.math-plain { font-family: monospace; font-size: 8pt; }
.badge { color: #0b5fa5; font-size: 7.5pt; }
.tiny { font-size: 7pt; color: #9aa5b1; }
details { border: 1px solid #e2e8ee; margin: 4pt 0; padding: 3pt; }
summary { font-weight: bold; font-size: 8.5pt; }
"""


def make(src_html: str, out_pdf: str, base_dir: str, css: str = CSS) -> str:
    if not os.path.exists(src_html):
        raise SystemExit(f"BRAK {src_html} — najpierw zbuduj źródło PDF")
    html = open(src_html, encoding="utf-8").read()
    body = html[html.find("<main>") + 6: html.find("</main>")]
    body = re.sub(r"<button[^>]*>.*?</button>", "", body, flags=re.S)

    story = pymupdf.Story(html=f"<body>{body}</body>", user_css=css,
                          archive=pymupdf.Archive(base_dir))
    mediabox = pymupdf.paper_rect("a4")
    where = mediabox + (36, 32, -36, -32)

    raw = out_pdf + ".raw"
    writer = pymupdf.DocumentWriter(raw)
    story.write(writer, lambda n, filled: (mediabox, where, pymupdf.Identity))
    writer.close()

    doc = pymupdf.open(raw)
    doc.save(out_pdf, deflate=True, garbage=4, clean=True)
    n, pages = doc.page_count, doc.page_count
    doc.close()
    os.remove(raw)
    print(f"OK -> {out_pdf} ({pages} stron, {os.path.getsize(out_pdf)/1e6:.1f} MB)")
    return out_pdf


def main() -> int:
    if len(sys.argv) >= 4:
        make(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        komp = os.path.join(ROOT, "kompendium")
        make(os.path.join(komp, "_pdf_source.html"),
             os.path.join(komp, "kompendium.pdf"), komp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
