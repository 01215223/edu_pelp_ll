# PELP1 — materiały i kompendium

Repozytorium zawiera klucze odpowiedzi do kolokwium wykładowego z przedmiotu
**PELP1 (podstawy elektroniki i teoria obwodów)** — 35 plików PDF z lat 2019–2026
(252 pytania) — oraz opracowane na ich podstawie **kompendium wiedzy**.

## Kompendium

➡️ **`kompendium/index.html`** — otwórz w przeglądarce (działa offline).
Do druku: **`kompendium/kompendium.pdf`** (43 strony A4).

* 12 rozdziałów: od konwencji i praw Kirchhoffa, przez elementy nieliniowe,
  aż po metrologię, mostek Wheatstone'a i oscyloskop,
* 13 wektorowych rysunków schematów i wykresów,
* 18 rozwiązanych zadań + 30 zdań-pułapek + formułownik,
* aneks z **wszystkimi 252 pytaniami** z kluczy (z filtrowaniem po temacie
  i odsyłaczami do rozdziałów),
* wersja do druku: `Ctrl/⌘+P` → PDF (arkusz A4, bez panelu bocznego).

Szczegóły, struktura katalogów i sposób ponownego zbudowania dokumentu:
[`kompendium/README.md`](kompendium/README.md).

## Szybkie rozwiązywanie obwodów (omówienie zadań)

➡️ **`szybkie/szybkie.pdf`** — 14 stron A4: jak policzyć Test 1 w 35 minut.
Wersja do przeglądania: **`szybkie/index.html`**.

* 11 archetypów zadań (opór zastępczy ze źródłem sterowanym, Thévenin/Norton,
  moc maksymalna, PPK, superpozycja, wzmacniacz operacyjny, punkt pracy z wykresu…),
* każde zadanie: wycinek z oryginalnego klucza + rachunek krok po kroku + pułapki,
* budżet czasu, kolejność rozwiązywania, lista najczęstszych dystraktorów,
* indeks wszystkich pytań z omówionych archetypów.

Szczegóły: [`szybkie/README.md`](szybkie/README.md).

## Teoria obwodów z omówionymi zadaniami (wersja 2 kompendium)

➡️ **`teoria/teoria.pdf`** — 27 stron A4: **cała teoria obwodów Testu 1** oparta na
prawdziwych pytaniach z kluczy. Wersja do przeglądania: **`teoria/index.html`**.

* 8 rozdziałów teorii: element skupiony, prawa Kirchhoffa i łączenie źródeł,
  superpozycja, dwójniki i źródła sterowane, Thévenin/Norton/dopasowanie,
  elementy nieliniowe, dioda, moc,
* **51 wycinków oryginalnych pytań** z kluczy (rysunek + pełna treść + wszystkie
  odpowiedzi z pogrubioną prawidłową),
* do każdego pytania **omówienie odpowiedzi**: dlaczego zaznaczona jest prawidłowa,
  skąd biorą się poszczególne dystraktory i jak sprawdzić wynik w kilka sekund,
* omówione także warianty z terminów poprawkowych (`A_2`), których nie ma
  w wersji podstawowej,
* opisy **niespójności w kluczach** (kilka odpowiedzi prawidłowych, sporne
  pytanie o dwójnik bezźródłowy) — bez „naprawiania” kluczy,
* aneks: **wszystkie 132 pytania Testu 1** z 17 kluczy (pytanie → numer odpowiedzi).

Szczegóły: [`teoria/README.md`](teoria/README.md).

## Pliki źródłowe

`PELP1_*.pdf` — klucze odpowiedzi (dane wejściowe). Nazwa pliku koduje test:

| Fragment nazwy | Znaczenie |
|---|---|
| `19Z`, `20L`, `21Z`, … | rok i semestr (Z — zimowy, L — letni) |
| `A` / `B` | wariant testu |
| `_1` / `_2` | Test 1 (teoria obwodów) / Test 2 (miernictwo) |
| `_popr` / `- poprawa` | termin poprawkowy |
| `klucz` / `key` | wersja z zaznaczonymi odpowiedziami prawidłowymi |

## Odtworzenie kompendium

```bash
pip install markdown pymupdf matplotlib    # + node: npm install katex @resvg/resvg-js
cd build
python3 make_crops.py      # wycinki zadań -> szybkie/zadania/
python3 build_szybkie.py   # szybkie/index.html + źródło PDF
python3 mkpdf.py ../szybkie/_pdf_source.html ../szybkie/szybkie.pdf ../szybkie
python3 build_teoria.py --pdf   # teoria/index.html + teoria/teoria.pdf
python3 figures.py
python3 build.py --pdf-src
python3 mkpdf.py
python3 check.py
```
