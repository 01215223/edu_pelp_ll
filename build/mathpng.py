#!/usr/bin/env python3
"""Renderowanie wzorów do PNG (matplotlib mathtext) — wersja do PDF.

Wersja HTML używa KaTeX-a (HTML+CSS, wygląda najlepiej w przeglądarce),
ale generator PDF (MuPDF Story) nie obsługuje tak złożonego CSS, więc do
PDF-u wzory są rasteryzowane tutaj.
"""
from __future__ import annotations

import base64
import io
import json
import os
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

CACHE_PATH = "/tmp/_mathpng_cache.json"
_cache: dict[str, str] = {}
if os.path.exists(CACHE_PATH):
    _cache = json.load(open(CACHE_PATH))

DPI = 300
SIZE = 11.0
PX_PER_INCH = 96.0


def sanitize(t: str) -> str:
    """Doprowadza TeX do postaci akceptowanej przez matplotlib mathtext."""
    t = t.strip()
    if t.startswith("$$") and t.endswith("$$"):
        t = t[2:-2]
    elif t.startswith("$") and t.endswith("$"):
        t = t[1:-1]
    t = t.strip()

    # tekst w formule
    t = re.sub(r"\\text\{([^{}]*)\}", r"\\mathrm{\1}", t)
    t = re.sub(r"\\mathrm\{\s*\}", "", t)
    # ułamki i pierwiastki
    t = t.replace("\\tfrac", "\\frac").replace("\\dfrac", "\\frac")
    t = re.sub(r"\\sqrt\s*([0-9A-Za-z])", r"\\sqrt{\1}", t)
    t = re.sub(r"\\frac\s*([0-9])([0-9])", r"\\frac{\1}{\2}", t)
    t = re.sub(r"\\frac\s*([0-9])(?![0-9{])", r"\\frac{\1}", t)
    t = re.sub(r"\\frac\s*([A-Za-z])(?![{\w])", r"\\frac{\1}", t)
    # delimitery (\left, \right) — najpierw, żeby nie kolidowało z \le
    t = t.replace("\\left.", "").replace("\\right.", "")
    t = t.replace("\\left", "").replace("\\right", "")
    # relacje
    t = t.replace("\\Longleftrightarrow", "\\Leftrightarrow")
    t = t.replace("\\Longrightarrow", "\\Rightarrow")
    t = re.sub(r"\\ge(?![a-zA-Z])", r"\\geq ", t)
    t = re.sub(r"\\le(?![a-zA-Z])", r"\\leq ", t)
    t = t.replace("\\neqq", "\\neq")
    t = re.sub(r"\\ne(?![a-zA-Z])", r"\\neq ", t)
    t = t.replace("\\|", "\\parallel ").replace("\\Vert", "\\parallel ")
    t = re.sub(r"(\\parallel)(?=[A-Za-z0-9])", r"\1 ", t)
    # macierze -> zapis tekstowy [a b; c d]
    def mat(m):
        rows = m.group(1).replace("\\\\", ";").replace("&", " ")
        return "[" + re.sub(r"\s+", " ", rows).strip() + "]"
    t = re.sub(r"\\begin\{bmatrix\}(.*?)\\end\{bmatrix\}", mat, t, flags=re.S)
    # odstępy
    t = t.replace("\\qquad", "\\quad\\quad").replace("\\-", "-")
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\s+", " ", t).strip()   # mathtext nie znosi znaków nowej linii
    return t


def _plain(t: str) -> str:
    """Awaryjnie: bardzo uproszczony zapis tekstowy."""
    t = sanitize(t)
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    t = re.sub(r"\\sqrt\{([^{}]*)\}", r"√(\1)", t)
    t = re.sub(r"\\(mathrm|mathit|mathbf)\{([^{}]*)\}", r"\2", t)
    t = re.sub(r"[_^]\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"[_^](\w)", r"\1", t)
    t = re.sub(r"\\[a-zA-Z]+", "", t)
    return t.replace("{", "").replace("}", "").strip()


def render(tex: str) -> str:
    """Zwraca gotowy tag <img> z data-URI (albo tekst, gdy się nie uda)."""
    key = tex
    if key in _cache:
        return _cache[key]

    from matplotlib.mathtext import MathTextParser

    def check(s):
        MathTextParser("path").parse(f"${s}$")
        return True

    def try_math(s):
        check(s)
        fig = plt.figure(figsize=(0.01, 0.01))
        fig.text(0, 0, f"${s}$", fontsize=SIZE, color="#16202c")
        buf = io.BytesIO()
        fig.savefig(buf, dpi=DPI, bbox_inches="tight", pad_inches=0.02,
                    transparent=True, format="png")
        plt.close(fig)
        buf.seek(0)
        return buf

    buf = None
    try:
        buf = try_math(sanitize(tex))
    except Exception:
        try:
            buf = try_math(_plain(tex))
        except Exception:
            buf = None
    if buf is None:
        html = f'<span class="math-plain">{_plain(tex)}</span>'
        _cache[key] = html
        return html

    from PIL import Image
    im = Image.open(buf)
    w, h = im.size
    w96, h96 = w / DPI * PX_PER_INCH, h / DPI * PX_PER_INCH
    b64 = base64.b64encode(buf.getvalue()).decode()
    html = (f'<img class="mathimg" src="data:image/png;base64,{b64}" '
            f'width="{w96:.1f}" height="{h96:.1f}" style="vertical-align:middle">')
    _cache[key] = html
    return html


def flush():
    json.dump(_cache, open(CACHE_PATH, "w"))


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    out = []
    for i, t in enumerate(data):
        disp = t.startswith("$$")
        img = render(t)
        out.append(f'<div class="mathblock">{img}</div>' if disp else img)
        if i % 100 == 0:
            print(i, file=sys.stderr)
    flush()
    json.dump(out, open(sys.argv[2], "w"))
    print(f"zrenderowano {len(data)} wzorów", file=sys.stderr)
