# Komentarz do wykładów PELP1 (W1–W5)

➡️ **`index.html`** — otwórz w przeglądarce (działa offline).
Do druku: **`wyklady.pdf`** — 37 stron A4.

Dokument odpowiada na inne pytanie niż pozostałe opracowania w repozytorium.
Kompendium mówi *co* obowiązuje, `teoria/` pokazuje *jak pytają*, `szybkie/`
uczy *tempa*. Tutaj jest **dlaczego dana metoda działa i jak jej użyć** —
na tle pięciu wykładów (`PELP1_W1.pdf` … `PELP1_W5.pdf`).

## Co jest w środku

| Rozdział | Temat | Powiązanie z wykładami |
|---|---|---|
| 0 | Jak czytać + mapa wykładów | — |
| 1 | Elementy, źródła, strzałkowanie | W1 (6.10.2021, 17 slajdów) |
| 2 | Prawa Kirchhoffa, superpozycja, Tellegen | W2 (3.03.2021, 16 slajdów) |
| 3 | Dwójniki, źródła sterowane, ruchliwość, kompensacja | W3 (10.03.2021, 18 slajdów) |
| 4 | Thévenin, Norton, dopasowanie, mostek | W4 (17.03.2021, 17 slajdów) |
| 5 | Elementy nieliniowe, dioda, sygnały, RMS | W5 (24.03.2021, 17 slajdów) |
| 6 | Jak korzystam z twierdzeń i zasad (7 pełnych przykładów + 3 zadania) | wszystkie |
| 7 | Ściąga: formułownik, 20 zdań-pułapek, indeks 69 tematów | — |

Każde twierdzenie jest użyte na **liczbowym przykładzie**, nie tylko
streczone. Wspólny obwód odniesienia ($E_1=12$ V, $R_1=2\ \Omega$,
$R_2=3\ \Omega$, $E_2=4$ V, $R_3=2\ \Omega$ → $V_A=6$ V) wraca w kilku
rozdziałach, więc widać, jak ta sama odpowiedź powstaje z różnych metod.

Odsyłacze `[W3/s.14]` prowadzą do slajdu konkretnego wykładu. Na końcu
rozdziału 7 jest indeks: temat → slajd → sekcja tego dokumentu.

## Struktura katalogów

```
wyklady/
├── wyklady.md        # źródło (Markdown + ramki ::: + wzory KaTeX)
├── index.html        # wersja do przeglądania (generowana)
├── wyklady.pdf       # wersja do druku (generowana)
├── figury/*.svg      # 11 rysunków wektorowych (źródło)
├── figury/png/*.png  # te same rysunki jako PNG (dla PDF)
└── _pdf_source.html  # produkt pośredni budowy PDF (w .gitignore)
```

Rysunki generuje `build/figures_wyklady.py` (rysowane „ręcznie” w SVG,
w konwencji IEC: prostokąt = rezystor, okrąg = źródło) — nie ma tu żadnych
bitmap z wykładów.

## Ponowne zbudowanie

```bash
cd build
python3 figures_wyklady.py        # 11 x SVG + PNG do wyklady/figury/
python3 build_wyklady.py --pdf    # index.html + _pdf_source.html + wyklady.pdf
python3 check_wyklady.py          # kontrola: rysunki, wzory, odsyłacze, rachunki
```

`build_wyklady.py` korzysta ze wspólnego `mkpdf.make()` (MuPDF Story + KaTeX
z `kompendium/katex/`), więc KaTeX musi być wcześniej wyrenderowany przez
`build/build.py`.

`check_wyklady.py` przelicza 17 liczb z przykładów (obwód odniesienia,
superpozycja, Thévenin, mostek, dzielnik obciążony, dioda, sygnały, moc
dopasowania) i porównuje je z wartościami podanymi w tekście — dzięki temu
poprawka jednego rezystora nie zostawia w dokumencie nieaktualnych wyników.

## Znane ograniczenia

* MuPDF Story (renderer PDF) gubi wiersze tabeli łamanej między stronami —
  dlatego indeks w §7.3 jest podzielony na 5 tabel (po jednej na wykład),
  a w CSS jest `table { break-inside: avoid }`.
* W `$$…$$` nie używamy polskiego tekstu ani `\begin{cases}` — ten renderer
  ich nie składnia poprawnie. Wzory „z opisem” są pisane jako tekst + osobny
  wzór.
* Na ostatniej stronie PDF mogą zostać blade szare paski po tabeli uciętej
  przy dnie strony — to artefakt renderera (występuje też w `kompendium.pdf`),
  nie treść dokumentu; wersja HTML jest czysta.
