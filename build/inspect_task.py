#!/usr/bin/env python3
"""Podgląd pojedynczego pytania z klucza: wycinek strony (PNG) + uporządkowane linie.

Użycie:
    python3 inspect_task.py PELP1_25Z_A_1_klucz A [--dpi 200]

Wypisuje linie z zachowaniem układu (kolumny) i znacznikiem B dla pogrubień,
oraz zapisuje /tmp/task_<plik>_<litera>.png do obejrzenia.
"""
from __future__ import annotations

import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LETTER = re.compile(r"^([A-H])\.$")


def lines_with_boxes(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            spans = [s for s in l["spans"] if s["text"].strip()]
            if not spans:
                continue
            out.append(
                {
                    "t": "".join(s["text"] for s in spans).strip(),
                    "b": any("Bold" in s["font"] for s in spans),
                    "x": min(s["bbox"][0] for s in spans),
                    "y": min(s["bbox"][1] for s in spans),
                    "y1": max(s["bbox"][3] for s in spans),
                }
            )
    out.sort(key=lambda r: (round(r["y"] / 3), r["x"]))
    return out


def find_question(path, letter):
    doc = pymupdf.open(path)
    for pno, page in enumerate(doc):
        ls = lines_with_boxes(page)
        idx = [i for i, r in enumerate(ls) if LETTER.match(r["t"]) and r["t"][0] == letter]
        # litera pytania bywa w sąsiedztwie numeru punktacji — wybieramy pierwszą
        if not idx:
            continue
        i = idx[0]
        start = ls[i]["y"] - 8
        end = None
        for r in ls[i + 1:]:
            if LETTER.match(r["t"]) and r["t"][0] > letter:
                end = r["y"] - 6
                break
            if r["t"].startswith("To jeszcze nie koniec") or r["t"].startswith("strona "):
                end = r["y"] - 4
                break
        if end is None:
            end = page.rect.y1 - 40
        block = [r for r in ls if start <= r["y"] < end]
        # dolna krawędź treści = najniższa linia bez stopki strony
        tresc = [r for r in block if not r["t"].startswith(("Koniec testu", "To jeszcze nie koniec"))]
        bottom = max((r["y1"] for r in tresc), default=end)
        return doc, pno, start, min(end, bottom + 3), block
    return None, None, None, None, None


def main():
    name, letter = sys.argv[1], sys.argv[2]
    dpi = 200
    if "--dpi" in sys.argv:
        dpi = int(sys.argv[sys.argv.index("--dpi") + 1])
    path = os.path.join(ROOT, name if name.endswith(".pdf") else name + ".pdf")
    doc, pno, start, end, block = find_question(path, letter)
    if doc is None:
        print("nie znaleziono pytania")
        return 1
    print(f"# {name} {letter}  (strona {pno + 1}, y {start:.0f}–{end:.0f})")
    for r in block:
        print(f"{r['x']:6.0f} {r['y']:6.0f} {'B' if r['b'] else ' '} {r['t']}")
    page = doc[pno]
    clip = pymupdf.Rect(36, start, page.rect.x1 - 36, min(end, page.rect.y1 - 30))
    out = f"/tmp/task_{name.replace('PELP1_', '')}_{letter}.png"
    page.get_pixmap(dpi=dpi, clip=clip).save(out)
    print("PNG:", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
