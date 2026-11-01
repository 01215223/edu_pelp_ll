#!/usr/bin/env python3
"""Wypisuje pełną treść pytania z klucza: linie (x, y, pogrubienie) + opcje z odpowiedziami.

Użycie: python3 dump_q.py PELP1_20Z_A_1_klucz A PELP1_demo_A C ...
"""
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))
from inspect_task import find_question  # noqa: E402


def dump(fname, letter):
    path = os.path.join(ROOT, fname + ".pdf")
    doc, pno, start, end, block = find_question(path, letter)
    print(f"\n===== {fname} · {letter}   (strona {pno + 1}) =====")
    rows = {}
    for r in block:
        key = round(r["y"] / 6)
        rows.setdefault(key, []).append(r)
    for key in sorted(rows):
        line = " | ".join(
            ("**" + r["t"] + "**") if r["b"] else r["t"] for r in sorted(rows[key], key=lambda r: r["x"])
        )
        if line.strip() and not line.startswith(("Koniec testu", "To jeszcze nie koniec")):
            print("   ", line)


if __name__ == "__main__":
    args = sys.argv[1:]
    for i in range(0, len(args), 2):
        dump(args[i], args[i + 1])
