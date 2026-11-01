#!/usr/bin/env python3
"""Wycinki zadań z kluczy PDF -> szybkie/zadania/*.png (dla dokumentu o szybkim liczeniu).

Każdy wycinek to całe zadanie: rysunek, treść, odpowiedzi (z pogrubioną prawidłową).
Uruchomienie: python3 make_crops.py
"""
from __future__ import annotations

import os
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inspect_task import find_question  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "szybkie", "zadania")

# (plik, litera) -> nazwa pliku wycinka
TASKS = [
    ("PELP1_25Z_A_1_klucz", "A", "25Z_A_1_A"),
    ("PELP1_24Z_A_1_klucz", "A", "24Z_A_1_A"),
    ("PELP1_23Z_A_1_klucz", "A", "23Z_A_1_A"),
    ("PELP1_19Z_A_1_klucz", "A", "19Z_A_1_A"),
    ("PELP1_19Z_A_1_klucz", "C", "19Z_A_1_C"),
    ("PELP1_24Z_A_1_klucz", "H", "24Z_A_1_H"),
    ("PELP1_25Z_A_1_klucz", "H", "25Z_A_1_H"),
    ("PELP1_21L_A_1_klucz", "F", "21L_A_1_F"),
    ("PELP1_25Z_A_1_klucz", "G", "25Z_A_1_G"),
    ("PELP1_21L_A_1_klucz", "H", "21L_A_1_H"),
    ("PELP1_24Z_A_1_klucz", "G", "24Z_A_1_G"),
    ("PELP1_24Z_A_1_klucz", "E", "24Z_A_1_E"),
    ("PELP1_23Z_A_1_klucz", "E", "23Z_A_1_E"),
    ("PELP1_23Z_A_1_klucz", "F", "23Z_A_1_F"),
    ("PELP1_25Z_A_1_klucz", "D", "25Z_A_1_D"),
    ("PELP1_25Z_A_1_klucz", "B", "25Z_A_1_B"),
    ("PELP1_25Z_A_1_klucz", "F", "25Z_A_1_F"),
]

DPI = 180


def main():
    os.makedirs(OUT, exist_ok=True)
    for fname, letter, out in TASKS:
        path = os.path.join(ROOT, fname + ".pdf")
        doc, pno, start, end, _ = find_question(path, letter)
        page = doc[pno]
        clip = pymupdf.Rect(38, start - 3, page.rect.x1 - 38, min(end, page.rect.y1 - 26))
        pix = page.get_pixmap(dpi=DPI, clip=clip, colorspace=pymupdf.csGRAY)
        dst = os.path.join(OUT, out + ".png")
        pix.save(dst)
        print(f"{out:14s} {pix.width}x{pix.height}  {os.path.getsize(dst)/1024:.0f} kB")


if __name__ == "__main__":
    main()
