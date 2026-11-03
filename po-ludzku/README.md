# Obwody po ludzku — komentarz do „Wykład - slajdy.pdf” (W1–W4)

➡️ **`index.html`** — otwórz w przeglądarce (działa offline).
Do druku: **`po-ludzku.pdf`**.

Dokument komentuje połączony zestaw slajdów **„Wykład - slajdy.pdf”**
(68 stron: W1 s. 1–17, W2 s. 18–33, W3 s. 34–51, W4 s. 52–68)
w możliwie prosty i sugestywny sposób: **najpierw intuicja
i obraz, potem wzór, na końcu przykład na liczbach**. Jest to
warstwa wejściowa do reszty materiałów w repozytorium — formalny
komentarz do tych samych wykładów (plus W5) mieszka w `../wyklady/`,
a teoria z oryginalnymi pytaniami w `../teoria/`.

Oryginalny plik slajdów **nie jest załączony** do repozytorium
(to materiał wykładowcy); odsyłacze mają postać
`[plik s. 29 = W2/s. 12]` — strona połączonego PDF-u i numer
ze stopki slajdu.

## Co jest w środku

| Rozdział | Temat | Strony pliku |
|---|---|---:|
| 0 | Analogia wodna, potencjał, obwód z dwiema bateriami | — |
| 1 | W1 — elementy: źródła, opór, *C*/*L*, źródła sterowane | 1–17 |
| 2 | W2 — Kirchhoff, dzielniki, kompensacja, superpozycja | 18–33 |
| 3 | W3 — czarne skrzynki, *R*z, Y–Δ, Thévenin, Norton | 34–51 |
| 4 | W4 — wzmacniacz operacyjny, nieliniowe, moc, dopasowanie | 52–68 |
| 5 | Warsztat: wybór metody + 6 zadań z odpowiedziami | — |
| 6 | Ściąga: formułownik, 15 zdań-pułapek, indeks 68 slajdów | — |

Jeden obwód przewodzi całości: dwie baterie 9 V i 6 V z oporami
po 2 Ω karmią wspólny węzeł A (wynik $U_A = 5$ V). Ten sam wynik
pojawia się z równania węzłowego, superpozycji, Thévenina
i kompensacji — żeby było widać, że metody różnią się drogą,
a nie odpowiedzią.

## Struktura katalogów

```
po-ludzku/
├── po-ludzku.md      # źródło (Markdown + ramki ::: + wzory KaTeX)
├── index.html        # wersja do przeglądarki (generowana)
├── po-ludzku.pdf     # wersja do druku (generowana)
├── figury/*.svg      # 11 rysunków wektorowych (źródło)
├── figury/png/*.png  # te same rysunki jako PNG (dla PDF)
└── _pdf_source.html  # produkt pośredni budowy PDF (w .gitignore)
```

## Ponowne zbudowanie

```bash
cd build
python3 figures_po_ludzku.py     # 11 x SVG + PNG do po-ludzku/figury/
python3 build_po_ludzku.py --pdf # index.html + po-ludzku.pdf
python3 check_po_ludzku.py       # kontrola liczb, rysunków i indeksu slajdów
```

`check_po_ludzku.py` przelicza ponad 30 wartości z przykładów
(obwód z dwiema bateriami, dzielniki, mostek, Thévenin, punkt pracy,
dopasowanie, zadania treningowe) i pilnuje, by indeks w §6.3
pokrywał strony 1–68 połączonego pliku slajdów dokładnie po jednej.
