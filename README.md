# PELP1 — materiały i kompendium

Repozytorium zawiera klucze odpowiedzi do kolokwium wykładowego z przedmiotu
**PELP1 (podstawy elektroniki i teoria obwodów)** — 35 plików PDF z lat 2019–2026
(252 pytania) — oraz pięć opracowanych dokumentów do nauki:
**kompendium**, **teorię z omówionymi pytaniami**, **szybkie rozwiązywanie
zadań**, **komentarz do wykładów** oraz jego przystępną wersję wstępną
**„Obwody po ludzku”**.

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

## Komentarz do wykładów (W1–W5) — jak używać twierdzeń

➡️ **`wyklady/wyklady.pdf`** — 37 stron A4: objaśnienia i przykłady do pięciu
wykładów PELP1 (`PELP1_W1.pdf` … `PELP1_W5.pdf`). Wersja do przeglądania:
**`wyklady/index.html`**.

* przechodzi przez materiał wykład po wykładzie (elementy i strzałkowanie,
  prawa Kirchhoffa, superpozycja i Tellegen, dwójniki i źródła sterowane,
  ruchliwość źródeł i kompensacja, Thévenin/Norton/dopasowanie, elementy
  nieliniowe i sygnały),
* **każde twierdzenie jest użyte na liczbowym przykładzie** — nie tylko
  streszczone: ten sam obwód odniesienia ($E_1=12$ V, $V_A=6$ V) rozwiązany
  superpozycją, Théveninem i kompensacją, żeby było widać, że wynik musi
  wyjść ten sam,
* 7 pełnych przykładów „jak wybrać metodę” + 3 zadania do samodzielnego
  policzenia (z odpowiedziami), 11 rysunków wektorowych,
* ściąga: formułownik, **20 zdań-pułapek**, indeks 69 tematów (temat → slajd
  wykładu → sekcja dokumentu).

Szczegóły, struktura i sposób zbudowania: [`wyklady/README.md`](wyklady/README.md).

## Obwody po ludzku — wykłady W1–W4 intuicyjnie (68 slajdów)

➡️ **`po-ludzku/po-ludzku.pdf`** — 25 stron A4: sugestywne objaśnienia
połączonego zestawu slajdów **`Wykład - slajdy.pdf`** (68 stron: W1 modele
elementów, W2 prawa i zasady, W3 elementy zastępcze, W4 elementy
nieliniowe/wzmacniacz operacyjny/moc). Wersja do przeglądania:
**`po-ludzku/index.html`**.

* kolejność odwrotna niż na slajdach: **najpierw obraz i intuicja**
  (analogia wodna, potencjał jako wysokość, źródła jako „uparciuchy”),
  potem wzór, na końcu zawsze przykład policzony do końca,
* jeden obwód-przewodnik (baterie 9 V i 6 V, trzy opory po 2 Ω,
  $U_A = 5$ V) rozwiązany równaniem węzłowym, superpozycją,
  Théveninem i zweryfikowany kompensacją oraz bilansem mocy,
* 11 własnych rysunków, „sprawdź się” po każdym wykładzie, 6 zadań
  treningowych z odpowiedziami, 15 zdań-pułapek,
* **indeks wszystkich 68 slajdów**: strona połączonego PDF-u → sekcja,
* to warstwa wejściowa: po niej formalny `wyklady/` czyta się dużo łatwiej.
  Sam plik slajdów nie jest załączony do repozytorium.

Szczegóły: [`po-ludzku/README.md`](po-ludzku/README.md).

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
python3 figures_wyklady.py      # rysunki do wyklady/
python3 build_wyklady.py --pdf  # wyklady/index.html + wyklady/wyklady.pdf
python3 check_wyklady.py        # kontrola liczb i odsyłaczy w wyklady/
python3 figures_po_ludzku.py    # rysunki do po-ludzku/
python3 build_po_ludzku.py --pdf # po-ludzku/index.html + po-ludzku/po-ludzku.pdf
python3 check_po_ludzku.py       # kontrola liczb, rysunków i indeksu 68 slajdów
python3 figures.py
python3 build.py --pdf-src
python3 mkpdf.py
python3 check.py
```
