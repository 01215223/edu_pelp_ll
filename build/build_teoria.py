#!/usr/bin/env python3
"""Buduje dokument „Teoria obwodów — kompendium z omówionymi zadaniami”.

Wejście:  teoria/teoria.md  (+ wycinki pytań w teoria/zadania/*.png)
Wyjście: teoria/index.html        — wersja do przeglądarki (KaTeX)
         teoria/_pdf_source.html  — wersja dla PDF (wzory jako PNG)
         teoria/teoria.pdf        — produkt końcowy (przez mkpdf)

Użycie:
    python3 build_teoria.py          # HTML + źródło PDF
    python3 build_teoria.py --pdf    # dodatkowo PDF
"""
from __future__ import annotations

import json
import os
import re
import sys

import markdown

import build as K

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "teoria")
SRC = os.path.join(DOC, "teoria.md")
OUT_HTML = os.path.join(DOC, "index.html")
OUT_PDFSRC = os.path.join(DOC, "_pdf_source.html")
OUT_PDF = os.path.join(DOC, "teoria.pdf")


def krotka(nazwa: str) -> str:
    """PELP1_25Z_A_1_klucz -> 25Z_A_1"""
    return nazwa.replace("PELP1_", "").replace("_klucz", "").replace("_key", "")


def annex() -> str:
    """Indeks: wszystkie pytania Testu 1 z kluczy + numery odpowiedzi."""
    rows = [r for r in json.load(open(os.path.join(HERE, "bank.json")))
            if r["hdr"].startswith("Test 1")]

    def key(name: str):
        m = re.search(r"(\d{2})([LZ])_A_(\d)", name)
        if not m:
            return (99, 0, 0, name)
        return (int(m.group(1)), 0 if m.group(2) == "L" else 1, int(m.group(3)), name)

    files: dict[str, list] = {}
    for r in rows:
        files.setdefault(r["file"], []).append(r)

    parts = [
        '<p class="tiny">Każde pytanie Testu 1 z 17 kluczy w repozytorium '
        "(plik · litera → numery odpowiedzi prawidłowych w kluczu; dwa lub trzy "
        "numery oznaczają, że klucz dopuszcza więcej niż jedną odpowiedź).</p>",
    ]
    for f in sorted(files, key=key):
        items = ", ".join(
            f'<b>{r["l"]}</b>→{",".join(str(x) for x in r["a"])}'
            for r in sorted(files[f], key=lambda r: r["l"])
        )
        parts.append(f'<p class="annexlist"><b>{krotka(f)}</b> · {items}</p>')
    parts.append(
        f'<p class="tiny">Razem: {len(rows)} pytań z {len(files)} plików kluczy.</p>'
    )
    return "\n".join(parts)


TEMPLATE = K.TEMPLATE.replace(
    "<title>Kompendium PELP1 — Podstawy elektroniki i teoria obwodów</title>",
    "<title>Teoria obwodów z omówionymi zadaniami — PELP1</title>",
).replace(
    "<h1>Kompendium PELP1</h1>",
    "<h1>Teoria obwodów</h1>",
).replace(
    "Podstawy elektroniki i teoria obwodów<br>\n  na podstawie 35 kluczy kolokwiów (2019–2026)",
    "Kompendium z omówionymi zadaniami<br>\n  Test 1 · 132 pytania z 17 kluczy + demo (2019–2026)",
).replace(
    '<div class="kicker">PELP1 · kompendium</div>',
    '<div class="kicker">PELP1 · teoria obwodów</div>',
)


# wzory w tekście muszą mieć wysokość tekstu (matplotlib renderuje je w 11 pt,
# a tekst w PDF ma 9 pt); wzory blokowe zostają w naturalnej wielkości
EXTRA_CSS = """
.mathimg { height: 9.4pt; width: auto; }
.mathblock .mathimg { height: auto; width: auto; max-width: 100%; }
figure img { max-height: 12cm; width: auto; }
"""


MATHBLOCK = re.compile(r'<div class="mathblock">.*?</div>', re.S)
IMG_SIZE = re.compile(r'(<img class="mathimg"[^>]*?)width="([\d.]+)" height="([\d.]+)"')


def _scale(m, factor: float, max_h: float) -> str:
    w, h = float(m.group(2)) * factor, float(m.group(3)) * factor
    if h > max_h:                      # wzór „wysoki” (np. z Σ) — doskaluj do wysokości linii
        w, h = w * max_h / h, max_h
    return f'{m.group(1)}width="{w:.1f}" height="{h:.1f}"'


def scale_inline_math(html: str, factor: float = 0.80, max_h: float = 14.2) -> str:
    """Pomniejsza wzory w tekście (matplotlib renderuje je w 11 pt, tekst ma 9 pt).

    Wzory blokowe (div.mathblock) zostają w naturalnej wielkości — MuPDF Story
    nie respektuje nadpisywania height/width w CSS, więc skalujemy atrybuty.
    """
    out, pos = [], 0
    for m in MATHBLOCK.finditer(html):
        out.append(IMG_SIZE.sub(
            lambda x: _scale(x, factor, max_h), html[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(IMG_SIZE.sub(
        lambda x: _scale(x, factor, max_h), html[pos:]))
    return "".join(out)


def build_doc(mode: str, out_path: str) -> str:
    text = open(SRC, encoding="utf-8").read()
    text = text.replace("<!--ANNEX-->", annex())

    text = K.boxes_and_figures(text)
    text, store = K.protect_math(text)

    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc", "md_in_html", "footnotes", "admonition"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "2-3", "slugify": K.slugify}},
    )
    html = md.convert(text)
    html = K.restore_math(html, K.render_math(store, mode))
    if mode == "img":
        html = scale_inline_math(html)

    m = re.search(r"<h1[^>]*>(.*?)</h1>(.*?)(?=<h2)", html, re.S)
    if m:
        hero = (
            f'<div class="hero"><div class="kicker">PELP1 · teoria obwodów</div>'
            f"<h1>{m.group(1)}</h1>{m.group(2)}</div>"
        )
        html = html[: m.start()] + hero + html[m.end():]

    toc = K._toc_from_tokens(md.toc_tokens)
    page = TEMPLATE.replace("__TOC__", toc).replace("__BODY__", html)

    # KaTeX jest wspólny z kompendium (jeden katalog, zero duplikatów)
    page = page.replace('href="katex/katex.min.css"', 'href="../kompendium/katex/katex.min.css"')

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"OK -> {out_path}  ({len(page)/1024:.0f} kB)")

    if mode == "img":
        # MuPDF Story nie rysuje SVG przez <img> — tu rysunki są PNG, więc nic nie podmieniamy
        pass
    return page


def main() -> int:
    build_doc("katex", OUT_HTML)
    build_doc("img", OUT_PDFSRC)
    if "--pdf" in sys.argv:
        import mkpdf
        mkpdf.make(OUT_PDFSRC, OUT_PDF, DOC, css=mkpdf.CSS + EXTRA_CSS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
