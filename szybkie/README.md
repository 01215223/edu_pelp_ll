# Szybkie rozwiązywanie obwodów — omówienie zadań z kluczy

Praktyczny dodatek do kompendium: **jak liczyć zadania z Testu 1 w 35 minut**, na prawdziwych zadaniach z 35 kluczy PELP1 (2019–2026).

| Plik | Co to jest |
|---|---|
| `szybkie.pdf` | **produkt główny** — 14 stron A4, gotowe do druku |
| `index.html` | ta sama treść w przeglądarce (offline, KaTeX, spis treści) |
| `szybkie.md` | źródło treści |
| `zadania/*.png` | wycinki oryginalnych zadań z kluczy (rysunek + treść + odpowiedzi z pogrubioną prawidłową) |

## Co jest w środku

1. **Anatomia Testu 1** — tabela „litera pytania → typ zadania → metoda”, z częstościami policzonymi z bazy 252 pytań; budżet czasu na 35 minut i kolejność rozwiązywania.
2. **Siedem nawyków** — reguły skracające rachunek: policz tylko to, o co pytają; zwarcie/rozwarcie jako dźwignia; idealne źródło „zżera” opór; co zeruje się w superpozycji; kontrola granic i miana; „ładny wynik”; eliminacja po znaku i rzędzie.
3. **Archetypy z rozwiązanymi zadaniami** (§3.1–3.11):
   * opór zastępczy dwójnika ze źródłem sterowanym (`gu`, `βi`, `ri`),
   * idealne źródło wymuszające stan gałęzi,
   * Thévenin (`E_T` z rozwarcia) i Norton (`J_N` ze zwarcia),
   * moc maksymalna i moc dysponowana (`E_T²/(4R_T)` + wzór skrócony),
   * prądowe prawo Kirchhoffa (w tym odpowiedź „układ jest sprzeczny”),
   * superpozycja i dzielnik prądu,
   * wzmacniacz operacyjny (cała litera D w dwóch krokach),
   * punkt pracy elementu nieliniowego: `R_s = u/i`, `R_d = Δu/Δi`,
   * pytania jakościowe (litera C) bez rachunku.
4. **Kontrola wyniku w pięć sekund** + lista sześciu najczęstszych dystraktorów w kluczach.
5. **Ściąga** „widzę w treści → robię → wynik”.
6. **Indeks wszystkich pytań** należących do omówionych archetypów (klucz · pytanie → numer odpowiedzi prawidłowej).

Każde zadanie ma wycinek z oryginalnego klucza (z pogrubioną odpowiedzią), rachunek krok po kroku i kontrolę. Liczby są przeliczone od zera — zgadzają się z odpowiedziami zaznaczonymi w kluczach.

## Przebudowa

```bash
pip install markdown pymupdf matplotlib      # node: npm install katex @resvg/resvg-js
cd build
python3 make_crops.py        # wycinki zadań z PDF-ów kluczy -> szybkie/zadania/*.png
python3 build_szybkie.py     # szybkie/index.html + szybkie/_pdf_source.html
python3 mkpdf.py ../szybkie/_pdf_source.html ../szybkie/szybkie.pdf ../szybkie
python3 check.py             # kontrola jakości obu dokumentów
```

Podgląd pojedynczego zadania z klucza (do pisania nowych rozdziałów):

```bash
cd build
python3 inspect_task.py PELP1_25Z_A_1_klucz A --dpi 200   # wypisze linie + zapisze PNG
```

## Uwagi

* Wycinki zawierają znak wodny „PJATK” z oryginalnych kluczy — nie był usuwany.
* `_pdf_source.html` to produkt pośredni (wzory jako PNG) i jest w `.gitignore`.
* Arkusz KaTeX-a (`kompendium/katex/`) jest wspólny z kompendium — `index.html` linkuje go względnie, więc katalog `szybkie/` działa offline bez duplikowania 328 kB fontów.
* Klucze miejscami dopuszczają dwie odpowiedzi prawidłowe (np. `−1 mA` i `1 mA`); wtedy dokument tak to opisuje, zamiast wybierać jedną.
