#!/usr/bin/env python3
"""Kontrola jakości dokumentu „Obwody po ludzku”.

Sprawdza:
  * czy każdy rysunek z `::: figura ...` istnieje (SVG i PNG),
  * czy w gotowym HTML nie ma resztek znaczników ramek (`:::`) ani
    nieprzetworzonych wzorów,
  * czy nie ma błędów KaTeX-a i martwych odsyłaczy spisu treści,
  * czy liczby z przykładów zgadzają się z niezależnym przeliczeniem,
  * czy indeks w §6.3 pokrywa wszystkie 68 stron połączonego PDF-u.

Użycie:
    python3 check_po_ludzku.py
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "po-ludzku")
MD = os.path.join(DOC, "po-ludzku.md")
HTML = os.path.join(DOC, "index.html")

errors: list[str] = []
warnings: list[str] = []


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


def check_html() -> None:
    if not os.path.exists(HTML):
        errors.append("brak po-ludzku/index.html — uruchom build_po_ludzku.py")
        return
    html = open(HTML, encoding="utf-8").read()
    print(f"· HTML: {len(html)/1024:.0f} kB")
    if ":::" in html:
        errors.append("w HTML zostały znaczniki ramek ':::'")
    if "\x00MATH" in html:
        errors.append("w HTML zostały nieprzetworzone wzory")
    n_err = html.count("math-error")
    if n_err:
        errors.append(f"KaTeX zgłosił {n_err} błędów wzorów")
    ids = set(re.findall(r'id="([^"]+)"', html))
    hrefs = re.findall(r'<a href="#([^"]+)"', html)
    print(f"· odsyłacze w spisie treści: {len(hrefs)}")
    for h in sorted({h for h in hrefs if h not in ids}):
        errors.append(f"spis treści wskazuje nieistniejący cel: #{h}")


def check_markdown() -> None:
    src = open(MD, encoding="utf-8").read()
    if re.search(r"\\text\{", src):
        errors.append("wzory zawierają \\text{...} (renderer PDF ich nie składa)")
    if "\\dysp" in src:
        errors.append("wzory zawierają nieistniejącą komendę \\dysp")
    cyr = [c for c in set(src) if 0x0400 <= ord(c) <= 0x04FF]
    if cyr:
        errors.append(f"w Markdown są znaki cyrylicy: {cyr}")
    opened = closed = 0
    kinds = {"def", "wzor", "uwaga", "pulapka", "przyklad",
             "metoda", "zapamietaj", "ciekawostka", "klucz", "figura"}
    for line in src.split("\n"):
        t = line.strip()
        if t == ":::":
            closed += 1
        elif t.startswith(":::"):
            opened += 1
            kind = t[3:].strip().split()[0]
            if kind not in kinds:
                errors.append(f"nieznany rodzaj ramki: {kind!r}")
    print(f"· ramki: otwarte {opened}, zamknięte {closed}")
    if opened != closed:
        errors.append("liczba otwarć i zamknięć ramek się nie zgadza")

    # indeks slajdów: strony 1..68 dokładnie raz
    idx = src[src.find("### 6.3"):]
    pages = [int(x) for x in re.findall(r"^\| (\d+) \|", idx, re.M)]
    if pages != list(range(1, 69)):
        errors.append(f"indeks §6.3 nie pokrywa stron 1–68 po kolei: {pages}")
    else:
        print("· indeks slajdów: strony 1–68 kompletne")


def check_math() -> None:
    def close(a, b, tol=5e-3):
        return abs(a - b) <= tol * max(1.0, abs(b))

    t = []
    # obwód z dwiema bateriami: E1=9, E2=6, R=2,2,2
    E1, E2, R = 9.0, 6.0, 2.0
    UA = (E1 / R + E2 / R) / (3 / R)
    t += [("hero UA", UA, 5.0), ("hero I1", (E1 - UA) / R, 2.0),
          ("hero I2", UA / R, 2.5), ("hero I3", (E2 - UA) / R, 0.5),
          ("hero P bilans", E1 * 2 + E2 * 0.5 - (8 + 12.5 + 0.5), 0.0)]
    # superpozycja
    t += [("U'A", E1 * (R / 2) / (R + R / 2), 3.0),
          ("U''A", E2 * (R / 2) / (R + R / 2), 2.0),
          ("moc R2 prawdziwa", 2.5 ** 2 * 2, 12.5),
          ("moc R2 suma bledna", 1.5 ** 2 * 2 + 1.0 ** 2 * 2, 6.5)]
    # Thévenin / Norton / dopasowanie
    ET = E1 - R * (E1 - E2) / (2 * R)
    t += [("ET", ET, 7.5), ("RW", R / 2, 1.0), ("JN", E1 / R + E2 / R, 7.5),
          ("Pdysp hero", ET ** 2 / 4, 14.0625)]
    for r0, p in ((0.25, 9.0), (2.0, 12.5), (4.0, 9.0)):
        t.append((f"P(R0={r0})", (ET / (1 + r0)) ** 2 * r0, p))
    # przykłady porozrzucane
    t += [
        ("przykl.1.1 u", -5 * 2, -10.0), ("przykl.1.1 p", 5 * 2 ** 2, 20.0),
        ("energia C [mJ]", 0.5 * 100e-6 * 100 * 1000, 5.0),
        ("energia L", 0.5 * 0.05 * 4, 0.1),
        ("bateria I", 9 / 9, 1.0), ("bateria U", 9 * 8 / 9, 8.0),
        ("dzielnik N", 12 * 9 / 12, 9.0),
        ("dzielnik N obciazony", 12 * 4.5 / 7.5, 7.2),
        ("dzielnik P I1", 6 * 4 / 6, 4.0), ("dzielnik P U", 4 * 2, 8.0),
        ("Rz przykl.3.1", 4 * 4 / 8, 2.0),
        ("mostek Rz", 6 * 9 / 15, 3.6),
        ("Rz sterowane", 3 * 3, 9.0),
        ("zamiana zrodel J", 12 / 3, 4.0), ("zamiana zrodel I", 12 / 9, 4 / 3),
        ("WO uwy", -(4 / 1) * 1.5, -6.0),
        ("Q Rs", 4 / 2, 2.0), ("Q Rd", 1 / (4 / 4), 1.0),
        ("dioda I [mA]", 5 / 1000 * 1000, 5.0),
        ("T2 obciazony", 20 * 8 / 12, 40 / 3),
        ("T4 ET", 12 * 6 / 8, 9.0), ("T4 RW", 2 * 6 / 8, 1.5),
        ("T4 P", 1.5 ** 2 * 4.5, 10.125),
        ("T6 Pdysp", 20 ** 2 / (4 * 5), 20.0),
    ]
    bad = 0
    for name, got, want in t:
        if not close(got, want):
            errors.append(f"rachunek: {name} = {got:.6g}, w tekście {want:g}")
            bad += 1
    print(f"· sprawdzone rachunki: {len(t)} (niezgodnych: {bad})")


def main() -> int:
    print("Kontrola: po-ludzku/")
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
