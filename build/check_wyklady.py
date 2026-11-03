#!/usr/bin/env python3
"""Kontrola jakości dokumentu „Komentarz do wykładów 1–5”.

Sprawdza:
  * czy każdy rysunek z `::: figura ...` istnieje (SVG i PNG),
  * czy w gotowym HTML nie ma resztek znaczników ramek (`:::`) ani
    nieprzetworzonych wzorów (\\x00MATH...),
  * czy nie ma błędów KaTeX-a,
  * czy wszystkie odsyłacze w spisie treści mają odpowiedniki w treści,
  * czy w źródle Markdown nie ma sekwencji `\\n` (literał) i cyrylicy,
  * czy liczby „okrągłe” z przykładów są zgodne z przeliczeniem (wybrane
    przykłady — patrz CHECKS niżej).

Użycie:
    python3 check_wyklady.py
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "wyklady")
MD = os.path.join(DOC, "wyklady.md")
HTML = os.path.join(DOC, "index.html")

errors: list[str] = []
warnings: list[str] = []


# --------------------------------------------------------------- 1. rysunki
def check_figures() -> None:
    src = open(MD, encoding="utf-8").read()
    figs = re.findall(r"^::: figura (\S+)", src, re.M)
    print(f"· rysunki w treści: {len(figs)}")
    for f in figs:
        svg = os.path.join(DOC, f)
        png = os.path.join(DOC, f.replace("figury/", "figury/png/").replace(".svg", ".png"))
        if not os.path.exists(svg):
            errors.append(f"brak rysunku SVG: {f}")
        if not os.path.exists(png):
            errors.append(f"brak rysunku PNG: {os.path.relpath(png, DOC)}")


# --------------------------------------------------------------- 2. HTML
def check_html() -> None:
    if not os.path.exists(HTML):
        errors.append("brak wyklady/index.html — uruchom build_wyklady.py")
        return
    html = open(HTML, encoding="utf-8").read()
    print(f"· HTML: {len(html)/1024:.0f} kB")

    if ":::" in html:
        errors.append("w HTML zostały znaczniki ramek ':::'")
    if "\x00MATH" in html:
        errors.append("w HTML zostały nieprzetworzone wzory (\\x00MATH)")
    n_err = html.count("math-error")
    if n_err:
        errors.append(f"KaTeX zgłosił {n_err} błędów wzorów")

    # spis treści vs treść
    ids = set(re.findall(r'id="([^"]+)"', html))
    hrefs = re.findall(r'<a href="#([^"]+)"', html)
    missing = [h for h in hrefs if h not in ids]
    print(f"· odsyłacze w spisie treści: {len(hrefs)}")
    for h in sorted(set(missing)):
        errors.append(f"spis treści wskazuje nieistniejący cel: #{h}")

    # puste ramki
    for m in re.finditer(r'<div class="box (\w+)"[^>]*>(.*?)</div>', html, re.S):
        body = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if len(body) < 25:
            warnings.append(f"bardzo krótka ramka '{m.group(1)}': {body[:40]!r}")


# --------------------------------------------------------------- 3. Markdown
def check_markdown() -> None:
    src = open(MD, encoding="utf-8").read()
    if re.search(r"\\n(?![a-zA-Z])", src):
        errors.append("w Markdown jest literał '\\\\n' (powinien być koniec linii)")
    cyr = [c for c in set(src) if 0x0400 <= ord(c) <= 0x04FF]
    if cyr:
        errors.append(f"w Markdown są znaki cyrylicy: {cyr}")
    if "\u00ad" in src:                     # miękki dywiz
        errors.append("w Markdown jest miękki dywiz (U+00AD)")
    # niezamknięte ramki
    opened = closed = 0
    for line in src.split("\n"):
        t = line.strip()
        if t == ":::":
            closed += 1
        elif t.startswith(":::"):
            opened += 1
    print(f"· ramki: otwarte {opened}, zamknięte {closed}")


# ------------------------------------------------- 4. rachunki z przykładów
def check_math() -> None:
    """Przelicza najważniejsze przykłady i porównuje z liczbami w tekście."""
    def close(a, b, tol=5e-3):
        return abs(a - b) <= tol * max(1.0, abs(b))

    tests = []

    # obwód odniesienia §2.4: V = 6 V, I1 = 3 A, I2 = 2 A, I3 = 1 A
    E1, R1, R2, E2, R3 = 12.0, 2.0, 3.0, 4.0, 2.0
    V = (E1 * R2 * R3 + E2 * R1 * R2) / (R1 * R2 + R2 * R3 + R1 * R3)
    tests.append(("obwód odniesienia: V", V, 6.0))
    tests.append(("I1", (E1 - V) / R1, 3.0))
    tests.append(("I2", V / R2, 2.0))
    tests.append(("I3", (V - E2) / R3, 1.0))

    # superpozycja
    Gsum = 1 / R1 + 1 / R2 + 1 / R3
    tests.append(("superpozycja U'", (E1 / R1) / Gsum, 4.5))
    tests.append(("superpozycja U''", (E2 / R3) / Gsum, 1.5))

    # Thévenin
    tests.append(("E_T", E1 - R1 * (E1 - E2) / (R1 + R3), 8.0))
    tests.append(("J_N", E1 / R1 + E2 / R3, 8.0))
    tests.append(("R_W", R1 * R3 / (R1 + R3), 1.0))
    tests.append(("P w R2", ((8.0 / (1.0 + 3.0)) ** 2) * 3.0, 12.0))
    tests.append(("P_dysp", 8.0 ** 2 / (4 * 1.0), 16.0))

    # mostek: Rz = 23,94 Ω
    import numpy as np
    a, b, c, d, e = 10.0, 20.0, 30.0, 40.0, 50.0
    G = np.zeros((3, 3))
    I = np.array([1.0, 0.0, 0.0])
    def add(i, j, r):
        g = 1 / r
        G[i, i] += g; G[j, j] += g; G[i, j] -= g; G[j, i] -= g
    add(0, 1, a); add(0, 2, b)
    G[1, 1] += 1 / c; G[2, 2] += 1 / d
    add(1, 2, e)
    Rz = np.linalg.solve(G, I)[0]
    tests.append(("Rz mostka", float(Rz), 23.94))

    # dzielnik obciążony: 4 V
    tests.append(("dzielnik obciążony", 12 * 5000 / (10000 + 5000), 4.0))

    # dioda odcinkowo-liniowa: 11,8 mA
    tests.append(("dioda i [mA]", (2 - 0.7) / 110 * 1000, 11.8))

    # sygnały: prostokąt 25 %
    d_, X0, Xm = 0.25, 2.0, 3.0
    sr = (X0 + Xm) * d_ + (X0 - Xm) * (1 - d_)
    rms = ((X0 + Xm) ** 2 * d_ + (X0 - Xm) ** 2 * (1 - d_)) ** 0.5
    tests.append(("średnia prostokąta", sr, 0.5))
    tests.append(("RMS prostokąta", rms, 2.646))

    # dopasowanie: 12 V, 4 Ω → 9 W
    tests.append(("P_dysp 12 V / 4 Ω", 12 ** 2 / (4 * 4), 9.0))

    bad = 0
    for name, got, want in tests:
        if not close(got, want):
            errors.append(f"rachunek: {name} = {got:.4g}, w tekście {want:g}")
            bad += 1
    print(f"· sprawdzone rachunki: {len(tests)} (niezgodnych: {bad})")


def main() -> int:
    print("Kontrola: wyklady/")
    check_figures()
    check_markdown()
    check_math()
    check_html()

    print()
    for w in warnings:
        print(f"OSTRZEŻENIE: {w}")
    if errors:
        for e in errors:
            print(f"BŁĄD: {e}")
        print(f"\n{len(errors)} błędów")
        return 1
    print("Wszystko OK ✔")
    return 0


if __name__ == "__main__":
    sys.exit(main())
