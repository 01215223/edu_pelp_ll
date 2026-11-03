#!/usr/bin/env python3
"""Buduje „Obwody po ludzku” (katalog po-ludzku/).

Wejście:  po-ludzku/po-ludzku.md  + rysunki po-ludzku/figury/*.svg
Wyjście:  po-ludzku/index.html        — wersja do przeglądarki (KaTeX)
          po-ludzku/_pdf_source.html  — wersja dla PDF (wzory jako PNG)
          po-ludzku/po-ludzku.pdf     — produkt końcowy (przez mkpdf)

Dokument komentuje plik „Wykład - slajdy.pdf” (68 slajdów = W1–W4)
w możliwie prosty, intuicyjny sposób; formalny, szczegółowy komentarz
do tych samych wykładów jest w katalogu wyklady/.

Użycie:
    python3 build_po_ludzku.py           # HTML + źródło PDF
    python3 build_po_ludzku.py --pdf     # dodatkowo PDF
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

import markdown

import build as K

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "po-ludzku")
SRC = os.path.join(DOC, "po-ludzku.md")
OUT_HTML = os.path.join(DOC, "index.html")
OUT_PDFSRC = os.path.join(DOC, "_pdf_source.html")
OUT_PDF = os.path.join(DOC, "po-ludzku.pdf")

TEMPLATE = (
    K.TEMPLATE.replace(
        "<title>Kompendium PELP1 — Podstawy elektroniki i teoria obwodów</title>",
        "<title>Obwody po ludzku — wykłady 1–4 PELP1 (68 slajdów)</title>",
    )
    .replace("<h1>Kompendium PELP1</h1>", "<h1>Obwody po ludzku</h1>")
    .replace(
        "Podstawy elektroniki i teoria obwodów<br>\n  na podstawie 35 kluczy kolokwiów (2019–2026)",
        "Wykłady 1–4 po ludzku: intuicja najpierw, wzór potem,<br>\n"
        "  przykład na liczbach zawsze",
    )
    .replace(
        '<div class="kicker">PELP1 · kompendium</div>',
        '<div class="kicker">PELP1 · wykłady 1–4 · po ludzku</div>',
    )
)

EXTRA_CSS = """
.mathimg { height: 9.4pt; width: auto; }
.mathblock .mathimg { height: auto; width: auto; max-width: 100%; }
figure img { max-height: 12cm; width: auto; }
/* MuPDF Story gubi treść tabeli łamanej między stronami — nie pozwalamy dzielić */
table, figure { break-inside: avoid; }
"""

MATHBLOCK = re.compile(r'<div class="mathblock">.*?</div>', re.S)
IMG_SIZE = re.compile(r'(<img class="mathimg"[^>]*?)width="([\d.]+)" height="([\d.]+)"')


def _scale(m, factor: float, max_h: float) -> str:
    w, h = float(m.group(2)) * factor, float(m.group(3)) * factor
    if h > max_h:
        w, h = w * max_h / h, max_h
    return f'{m.group(1)}width="{w:.1f}" height="{h:.1f}"'


def scale_inline_math(html: str, factor: float = 0.80, max_h: float = 14.2) -> str:
    out, pos = [], 0
    for m in MATHBLOCK.finditer(html):
        out.append(IMG_SIZE.sub(lambda x: _scale(x, factor, max_h), html[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(IMG_SIZE.sub(lambda x: _scale(x, factor, max_h), html[pos:]))
    return "".join(out)


def build_doc(mode: str, out_path: str) -> str:
    text = open(SRC, encoding="utf-8").read()
    text = K.boxes_and_figures(text)
    text, store = K.protect_math(text)

    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc", "md_in_html", "footnotes", "admonition"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "2-3",
                                   "slugify": K.slugify}},
    )
    html = md.convert(text)
    rendered = K.render_math(store, mode)
    html = K.restore_math(html, rendered)
    if mode == "img":
        html = scale_inline_math(html)

    m = re.search(r"<h1[^>]*>(.*?)</h1>(.*?)(?=<h2)", html, re.S)
    if m:
        hero = (
            '<div class="hero"><div class="kicker">PELP1 · wykłady 1–4 · po ludzku</div>'
            f"<h1>{m.group(1)}</h1>{m.group(2)}</div>"
        )
        html = html[: m.start()] + hero + html[m.end():]

    toc = K.restore_math(K._toc_from_tokens(md.toc_tokens), rendered)
    page = TEMPLATE.replace("__TOC__", toc).replace("__BODY__", html)

    # KaTeX jest wspólny z kompendium (jeden katalog, zero duplikatów)
    page = page.replace('href="katex/katex.min.css"',
                        'href="../kompendium/katex/katex.min.css"')

    if mode == "img":
        # MuPDF Story nie rysuje SVG przez <img> — podmieniamy na PNG 2×
        page = page.replace('src="figury/', 'src="figury/png/')
        page = page.replace('.svg"', '.png"')

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"OK -> {out_path}  ({len(page)/1024:.0f} kB)")
    return page


def main() -> int:
    if not os.path.exists(os.path.join(DOC, "figury", "hero.svg")):
        subprocess.run([sys.executable, os.path.join(HERE, "figures_po_ludzku.py")],
                       check=True)
    build_doc("katex", OUT_HTML)
    build_doc("img", OUT_PDFSRC)
    if "--pdf" in sys.argv:
        import mkpdf
        mkpdf.make(OUT_PDFSRC, OUT_PDF, DOC, css=mkpdf.CSS + EXTRA_CSS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
