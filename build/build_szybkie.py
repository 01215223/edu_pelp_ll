#!/usr/bin/env python3
"""Buduje dokument „Szybkie rozwiązywanie obwodów”.

Wejście:  szybkie/szybkie.md  (+ wycinki w szybkie/zadania/*.png)
Wyjście: szybkie/index.html          — wersja do przeglądarki (KaTeX)
         szybkie/_pdf_source.html    — wersja dla PDF (wzory jako PNG)
         szybkie/szybkie.pdf         — produkt końcowy (przez mkpdf)

Użycie:
    python3 build_szybkie.py            # HTML + źródło PDF
    python3 build_szybkie.py --pdf      # dodatkowo PDF
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict

import markdown

import build as K

RE_PAREN = re.compile(r"\s*\([^)]*\)\s*$")  # funkcje wspólne z kompendium

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "szybkie")
SRC = os.path.join(DOC, "szybkie.md")
OUT_HTML = os.path.join(DOC, "index.html")
OUT_PDFSRC = os.path.join(DOC, "_pdf_source.html")
OUT_PDF = os.path.join(DOC, "szybkie.pdf")
KATEX_SRC = "/home/user/buildtools/node_modules/katex/dist"

# temat (etykieta z ekstrakcji) -> metoda rozwiązywania w jednym zdaniu
METODA = {
    "Opór zastępczy dwójnika (ze źródłami sterowanymi)": "wpisz prąd gałęzi, dodaj, podziel u/i",
    "Punkt pracy elementu nieliniowego (Rs, Rd)": "odczyt z wykresu: R<sub>s</sub> = u/i, R<sub>d</sub> = Δu/Δi",
    "Napięcie/prąd źródła – wpływ parametrów": "rozstrzygnij, co wymusza stan (bez rachunku)",
    "Napięcie w obwodzie (obliczenia)": "dzielnik, wtórnik, metoda węzłowa",
    "Prądowe prawo Kirchhoffa": "jedno równanie w węźle",
    "Zasada superpozycji": "zeruj pozostałe źródła, licz jedną składową",
    "Moc maksymalna wydzielana w R (dopasowanie)": "R = R<sub>T</sub>, potem E<sub>T</sub>²/(4R<sub>T</sub>)",
    "Moc dysponowana dwójnika": "to samo co moc maksymalna",
    "Równoważnik Thévenina / Nortona": "E<sub>T</sub> z rozwarcia, J<sub>N</sub> ze zwarcia",
    "Charakterystyka dwójnika z diodą idealną": "dwa przypadki: dioda zwarta / rozwarta",
    "Rozpoznawanie połączeń (szeregowo/równolegle, gwiazda/trójkąt)": "te same dwa węzły = równolegle",
    "Równania Kirchhoffa (węzeł / oczko)": "zaznacz zwroty, napisz sumę",
    "Moc w połączeniach szereg./równol.": "P = I²R (szeregowo) / P = U²/R (równolegle)",
    "Dwójnik bezźródłowy / źródłowy": "sprawdź, czy źródło jest w środku",
    "Elementy skupione – założenia": "warunki modelu",
    "Oscyloskop – budowa, tryby, ADC": "wiedza opisowa",
    "Dobór przyrządu i zakresu": "policz Δ<sub>g</sub> dla każdej opcji",
    "Metoda techniczna i błąd metody": "porównaj R<sub>x</sub> z √(R<sub>a</sub>R<sub>v</sub>)",
    "Pojęcia: niepewność i błąd": "definicja",
    "Zaokrąglanie wyniku pomiaru": "niepewność 1–2 cyfry, wynik do tego miejsca",
    "Niepewność złożona – rachunek": "różniczka zupełna / suma geometryczna",
    "Wykresy niepewności przyrządu cyfrowego": "hiperbola vs prosta",
    "Statystyka serii pomiarów": "s, potem s/√n",
    "Własności niepewności przyrządów cyfrowych": "zależy od zakresu i wskazania",
    "Mostek Wheatstone’a": "równowaga: R<sub>x</sub>/R<sub>0</sub> = R<sub>1</sub>/R<sub>2</sub>",
    "Rodzaje i metody pomiaru": "definicja",
    "Czwórnik": "parametry ABCD",
    "Łączenie źródeł idealnych": "co wolno łączyć",
    "Zasada Tellegena": "bilans mocy",
}

# archetypy omówione w dokumencie (kolejność i podpisy)
ARCHETYPY = [
    ("Opór zastępczy dwójnika (ze źródłami sterowanymi)", "§3.1 Opór zastępczy ze źródłem sterowanym"),
    ("Równoważnik Thévenina / Nortona", "§3.3–3.4 Thévenin i Norton"),
    ("Moc maksymalna wydzielana w R (dopasowanie)", "§3.5 Moc maksymalna"),
    ("Moc dysponowana dwójnika", "§3.6 Moc dysponowana"),
    ("Prądowe prawo Kirchhoffa", "§3.7 Prądowe prawo Kirchhoffa"),
    ("Zasada superpozycji", "§3.8 Superpozycja"),
    ("Napięcie w obwodzie (obliczenia)", "§3.9 Wzmacniacz operacyjny / dzielnik"),
    ("Punkt pracy elementu nieliniowego (Rs, Rd)", "§3.10 Punkt pracy z wykresu"),
]

ARCH_SKROT = {
    "Opór zastępczy dwójnika (ze źródłami sterowanymi)": "opór zastępczy",
    "Równoważnik Thévenina / Nortona": "Thévenin / Norton",
    "Moc maksymalna wydzielana w R (dopasowanie)": "moc maksymalna",
    "Moc dysponowana dwójnika": "moc dysponowana",
    "Prądowe prawo Kirchhoffa": "PPK / węzeł",
    "Zasada superpozycji": "superpozycja",
}


def krotka(nazwa: str) -> str:
    """PELP1_25Z_A_1_klucz -> 25Z_A_1"""
    return nazwa.replace("PELP1_", "").replace("_klucz", "").replace("_key", "")


def letter_map() -> str:
    rows = [r for r in json.load(open(os.path.join(HERE, "bank.json")))
            if r["hdr"].startswith("Test 1")]
    n_files = len({r["file"] for r in rows})
    per = defaultdict(Counter)
    pkt = defaultdict(list)
    for r in rows:
        per[r["l"]][r["lab"]] += 1
        pkt[r["l"]].append(2 if r["stem"].startswith("2p") else 1)

    out = [
        f'<p class="tiny">Statystyka z {n_files} kluczy Testu 1 '
        f"({sum(len(v) for v in pkt.values())} pytań): dwa najczęstsze tematy pod daną literą.</p>",
        '<table class="map"><thead><tr><th class="c">Pyt.</th><th class="c">Pkt</th>'
        "<th>Co tam prawie zawsze jest</th><th>Metoda</th></tr></thead><tbody>",
    ]
    for lit in "ABCDEFGH":
        c = per.get(lit, Counter())
        if not c:
            continue
        top = c.most_common(2)
        opis = " · ".join(
            f"{RE_PAREN.sub('', lab)} <b>({n}×)</b>" for lab, n in top
        )
        met = METODA.get(top[0][0], "—")
        p = pkt[lit]
        lo, hi = min(p), max(p)
        pkt_txt = str(lo) if lo == hi else f"{lo}–{hi}"
        out.append(
            f'<tr><td class="c"><b>{lit}</b></td><td class="c">{pkt_txt}</td>'
            f"<td>{opis}</td><td>{met}</td></tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def annex() -> str:
    rows = json.load(open(os.path.join(HERE, "bank.json")))
    parts = [
        '<p class="tiny">Wszystkie pytania z kluczy, które należą do omówionych archetypów '
        "(klucz · pytanie → numer odpowiedzi prawidłowej w kluczu; brak przy dwóch numerach "
        "oznacza, że klucz dopuszcza obie).</p>"
    ]
    for lab, tytul in ARCHETYPY:
        sel = sorted((r for r in rows if r["lab"] == lab), key=lambda r: r["file"])
        if not sel:
            continue
        items = ", ".join(
            f'{krotka(r["file"])}·{r["l"]}→{",".join(str(x) for x in r["a"])}' for r in sel
        )
        parts.append(
            f"<h4>{tytul} <span class=\"tiny\">({len(sel)} pytań w kluczach)</span></h4>"
            f'<p class="annexlist">{items}</p>'
        )
    return "\n".join(parts)


TEMPLATE = K.TEMPLATE.replace(
    "<title>Kompendium PELP1 — Podstawy elektroniki i teoria obwodów</title>",
    "<title>Szybkie rozwiązywanie obwodów — omówienie zadań z kluczy PELP1</title>",
).replace(
    "<h1>Kompendium PELP1</h1>",
    "<h1>Szybkie liczenie</h1>",
).replace(
    "Podstawy elektroniki i teoria obwodów<br>\n  na podstawie 35 kluczy kolokwiów (2019–2026)",
    "Omówienie zadań z kluczy<br>Test 1 · obwody · 2019–2026",
).replace(
    '<div class="kicker">PELP1 · kompendium</div>',
    '<div class="kicker">PELP1 · szybkie rozwiązywanie obwodów</div>',
)


def build_doc(mode: str, out_path: str) -> str:
    text = open(SRC, encoding="utf-8").read()
    text = text.replace("<!--LETTERMAP-->", letter_map())
    text = text.replace("<!--ANNEX-->", annex())

    text = K.boxes_and_figures(text)
    text, store = K.protect_math(text)

    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc", "md_in_html", "footnotes", "admonition"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "2-3", "slugify": K.slugify}},
    )
    html = md.convert(text)
    html = K.restore_math(html, K.render_math(store, mode))

    m = re.search(r"<h1[^>]*>(.*?)</h1>(.*?)(?=<h2)", html, re.S)
    if m:
        hero = (
            f'<div class="hero"><div class="kicker">PELP1 · szybkie rozwiązywanie obwodów</div>'
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
    return page


def main() -> int:
    build_doc("katex", OUT_HTML)
    build_doc("img", OUT_PDFSRC)
    if "--pdf" in sys.argv:
        import mkpdf
        mkpdf.make(OUT_PDFSRC, OUT_PDF, DOC)
    return 0


if __name__ == "__main__":
    sys.exit(main())
