# PELP1 — materiały i kompendium

Repozytorium zawiera klucze odpowiedzi do kolokwium wykładowego z przedmiotu
**PELP1 (podstawy elektroniki i teoria obwodów)** — 35 plików PDF z lat 2019–2026
(252 pytania) — oraz opracowane na ich podstawie **kompendium wiedzy**.

## Kompendium

➡️ **`kompendium/index.html`** — otwórz w przeglądarce (działa offline).

* 12 rozdziałów: od konwencji i praw Kirchhoffa, przez elementy nieliniowe,
  aż po metrologię, mostek Wheatstone'a i oscyloskop,
* 13 wektorowych rysunków schematów i wykresów,
* 18 rozwiązanych zadań + 30 zdań-pułapek + formułownik,
* aneks z **wszystkimi 252 pytaniami** z kluczy (z filtrowaniem po temacie
  i odsyłaczami do rozdziałów),
* wersja do druku: `Ctrl/⌘+P` → PDF (arkusz A4, bez panelu bocznego).

Szczegóły, struktura katalogów i sposób ponownego zbudowania dokumentu:
[`kompendium/README.md`](kompendium/README.md).

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
pip install markdown pymupdf     # + node: npm install katex
cd build && python3 figures.py && python3 build.py
```
