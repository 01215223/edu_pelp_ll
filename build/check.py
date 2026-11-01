#!/usr/bin/env python3
"""Kontrola jakości kompendium: spójność odsyłaczy, wzorów, rysunków i aneksu.

Uruchom po `python3 build.py`:

    python3 check.py

Kod wyjścia 1 oznacza wykryte problemy.
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
KOMP = os.path.join(ROOT, "kompendium")
MD = os.path.join(KOMP, "kompendium.md")
HTML = os.path.join(KOMP, "index.html")
SZYB = os.path.join(ROOT, "szybkie")
SZYB_MD = os.path.join(SZYB, "szybkie.md")
SZYB_HTML = os.path.join(SZYB, "index.html")
TEOR = os.path.join(ROOT, "teoria")
TEOR_MD = os.path.join(TEOR, "teoria.md")
TEOR_HTML = os.path.join(TEOR, "index.html")

problems: list[str] = []


def main() -> int:
    md = open(MD, encoding="utf-8").read()
    html = open(HTML, encoding="utf-8").read()
    rows = json.load(open(os.path.join(HERE, "bank.json"), encoding="utf-8"))

    # ---------------------------------------------------------- 1. struktura MD
    if md.count(":::") % 2:
        problems.append("niedomknięte ramki ::: w kompendium.md")
    heads = {m.group(1) for m in re.finditer(r"^#{2,3}\s+(\d+(?:\.\d+)?)", md, re.M)}
    for ref in sorted(set(re.findall(r"§(\d+(?:\.\d+)?)", md))):
        if ref not in heads:
            problems.append(f"odsyłacz §{ref} nie ma odpowiadającego nagłówka")

    # ------------------------------------------------------- 2. wzory i markdown
    body = html[html.find("<main>"): html.find("</main>")]
    if "\x00" in html:
        problems.append("niepodmienione placeholdery wzorów")
    if 'class="katex-error"' in html or 'class="math-error"' in html:
        problems.append("wzór, którego KaTeX nie potrafi zrenderować")
    if "**" in re.sub(r"<[^>]+>", " ", body):
        problems.append("nieprzetworzone pogrubienia (**) w treści")
    if ":::" in body:
        problems.append("literalne ::: w treści")

    # ------------------------------------------------------------- 3. rysunki
    for src in set(re.findall(r'<img src="([^"]+)"', html)):
        if not os.path.exists(os.path.join(KOMP, src)):
            problems.append(f"brak pliku rysunku: {src}")
    figs_md = len(re.findall(r"^::: figura", md, re.M))
    figs_html = body.count("<figure>")
    if figs_md != figs_html:
        problems.append(f"rysunków w MD: {figs_md}, w HTML: {figs_html}")

    # --------------------------------------------------------------- 4. aneks
    n_boxes = body.count('class="box')
    if n_boxes // 2 != body.count("box-title"):
        problems.append("ramka bez tytułu")
    tests = len(set(r["hdr"] for r in rows))
    if f"{len(rows)} pytań" not in html:
        problems.append("niezgodna liczba pytań w nagłówku aneksu")
    for r in rows:
        for a in r["a"]:
            if not 1 <= a <= 20:
                problems.append(f"podejrzany numer odpowiedzi {a} ({r['file']} {r['l']})")
    if not all(r["lab"] != "INNE" for r in rows):
        problems.append("część pytań bez klasyfikacji tematycznej")

    # --------------------------------------------------------- 5. spis treści
    ids = set(re.findall(r'<h[1-3] id="([^"]+)"', html))
    for href in set(re.findall(r'<a href="#([^"]+)" class="lvl', html)):
        if href not in ids:
            problems.append(f"spis treści wskazuje nieistniejący nagłówek: {href}")

    # ----------------------------------------- 6. dokument „szybkie rozwiązywanie”
    check_szybkie()

    # ------------------------------- 7. dokument „teoria + omówione zadania”
    check_teoria()

    # ----------------------------------------------------------------- raport
    n_boxes = body.count('class="box')
    print("testów: %d, pytań: %d, rysunków: %d, ramek: %d, wzorów: %d"
          % (tests, len(rows), figs_html, n_boxes // 2, html.count('class="katex"')))
    if problems:
        print("\nPROBLEMY:")
        for p in problems:
            print(" -", p)
        return 1
    print("OK — brak problemów.")
    return 0


def check_teoria() -> None:
    """Sprawdza teoria/teoria.md + HTML: wycinki, przypisy do kluczy, aneks."""
    if not os.path.exists(TEOR_MD):
        problems.append("brak teoria/teoria.md")
        return
    md = open(TEOR_MD, encoding="utf-8").read()
    html = open(TEOR_HTML, encoding="utf-8").read()
    body = html[html.find("<main>"): html.find("</main>")]
    rows = json.load(open(os.path.join(HERE, "bank.json"), encoding="utf-8"))
    known = {(r["file"], r["l"]): r["a"] for r in rows}

    if md.count(":::") % 2:
        problems.append("teoria: niedomknięte ramki :::")
    if ":::" in body:
        problems.append("teoria: literalne ::: w treści")
    if "\x00" in body:
        problems.append("teoria: niepodmienione placeholdery wzorów")
    if 'class="katex-error"' in html or 'class="math-error"' in html:
        problems.append("teoria: wzór, którego KaTeX nie potrafi zrenderować")
    txt = re.sub(r"<[^>]+>", " ", body)
    if "**" in txt:
        problems.append("teoria: nieprzetworzone pogrubienia (**)")
    if "$" in txt:
        problems.append("teoria: surowy $ w treści (wzór poza KaTeX-em)")
    if "pytania na następnej stronie" in txt:
        problems.append("teoria: w wycinku został stopka „Ciąg dalszy pytania…”")

    # wycinki: plik istnieje + pytanie istnieje w kluczu + numer odpowiedzi się zgadza
    used = set()
    for m in re.finditer(r"^::: figura zadania/(\S+?)_([A-H])\.png \| (.*)$", md, re.M):
        f, lit, cap = m.group(1), m.group(2), m.group(3)
        used.add(f"{f}_{lit}.png")
        if not os.path.exists(os.path.join(TEOR, "zadania", f"{f}_{lit}.png")):
            problems.append(f"teoria: brak pliku wycinka zadania/{f}_{lit}.png")
        key = (f"PELP1_{f}_klucz", lit) if f.startswith("20") or f.startswith("19") else (f"PELP1_{f}", lit)
        key = (f"PELP1_{f}", lit) if f.startswith("demo") else (f"PELP1_{f}_klucz", lit)
        if key not in known:
            problems.append(f"teoria: nie ma pytania {lit} w kluczu {key[0]}")
            continue
        cm = re.search(r"Klucz (\S+), pytanie ([A-H])", cap)
        if cm:
            if cm.group(1) != f:
                problems.append(f"teoria: podpis {f}_{lit} mówi o kluczu {cm.group(1)}")
            if cm.group(2) != lit:
                problems.append(f"teoria: podpis {f}_{lit} mówi o pytaniu {cm.group(2)}")
        bm = re.search(r"\*\*(\d)\*\*", cap)
        if bm and int(bm.group(1)) not in known[key]:
            problems.append(
                f"teoria: podpis {f}·{lit} podaje odpowiedź {bm.group(1)}, "
                f"a klucz ma {known[key]}"
            )

    figs_md = len(re.findall(r"^::: figura ", md, re.M))
    figs_html = body.count("<figure>")
    if figs_md != figs_html:
        problems.append(f"teoria: rysunków w MD: {figs_md}, w HTML: {figs_html}")

    # każdy klucz Testu 1 musi być przynajmniej raz zacytowany
    cited = {m.group(1) for m in re.finditer(r"Klucz (\S+), pytanie", md)}
    for f in sorted({r["file"] for r in rows if r["hdr"].startswith("Test 1")}):
        short = f.replace("PELP1_", "").replace("_klucz", "")
        if short not in cited:
            problems.append(f"teoria: klucz {short} nie ma żadnego omówionego pytania")

    n_boxes = len(re.findall(r'<div class="box ', body))
    if n_boxes != body.count("box-title"):
        problems.append("teoria: ramka bez tytułu")
    if f"{len(rows)} pytań" in body or "Razem: 132 pytań" not in body:
        problems.append("teoria: aneks nie zawiera pełnej listy pytań Testu 1")

    n_katex = html.count('class="katex"')
    print(f"teoria: ramek {n_boxes}, rysunków {figs_html}, wzorów {n_katex}")


def check_szybkie() -> None:
    """Sprawdza szybkie/szybkie.md + HTML (odsyłacze do plików, ramki, wzory)."""
    if not os.path.exists(SZYB_MD):
        problems.append("brak szybkie/szybkie.md")
        return
    md = open(SZYB_MD, encoding="utf-8").read()
    html = open(SZYB_HTML, encoding="utf-8").read()
    body = html[html.find("<main>"): html.find("</main>")]

    if md.count(":::") % 2:
        problems.append("szybkie: niedomknięte ramki :::")
    if ":::" in body:
        problems.append("szybkie: literalne ::: w treści")
    if "\x00" in body:
        problems.append("szybkie: niepodmienione placeholdery wzorów")
    if 'class="katex-error"' in html or 'class="math-error"' in html:
        problems.append("szybkie: wzór, którego KaTeX nie potrafi zrenderować")
    txt = re.sub(r"<[^>]+>", " ", body)
    if "**" in txt:
        problems.append("szybkie: nieprzetworzone pogrubienia (**)")
    if "`" in txt:
        problems.append("szybkie: nieprzetworzone `code` w treści")
    if "$" in txt:
        problems.append("szybkie: surowy $ w treści (wzór poza KaTeX-em)")

    # odsyłacze do wycinków zadań + istnienie plików
    for m in re.finditer(r"^::: figura (\S+)", md, re.M):
        src = m.group(1)
        for sub in (SZYB, KOMP):
            if os.path.exists(os.path.join(sub, src)):
                break
        else:
            problems.append(f"szybkie: brak pliku wycinka: {src}")
    figs_md = len(re.findall(r"^::: figura", md, re.M))
    figs_html = body.count("<figure>")
    if figs_md != figs_html:
        problems.append(f"szybkie: rysunków w MD: {figs_md}, w HTML: {figs_html}")
    used = set(re.findall(r"zadania/([\w-]+\.png)", md))
    on_disk = set(os.listdir(os.path.join(SZYB, "zadania")))
    for extra in sorted(on_disk - used):
        problems.append(f"szybkie: nieużywany wycinek zadania/{extra}")
    for missing in sorted(used - on_disk):
        problems.append(f"szybkie: użyty, ale nieistniejący wycinek zadania/{missing}")

    n_boxes = len(re.findall(r'<div class="box ', body))
    if n_boxes != body.count("box-title"):
        problems.append("szybkie: ramka bez tytułu")
    if body.count('class="mathblock"') > 0 and "mathimg" not in body:
        problems.append("szybkie: blok wzoru bez obrazka")

    n_katex = html.count('class="katex"')
    print(f"szybkie: ramek {n_boxes}, rysunków {figs_html}, wzórów {n_katex}")


if __name__ == "__main__":
    sys.exit(main())
