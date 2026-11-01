# Teoria obwodów — kompendium z omówionymi zadaniami

Druga wersja kompendium: **teoria obwodów Testu 1** oparta na prawdziwych pytaniach z kluczy PELP1 (2019–2026), z **omówieniem każdej odpowiedzi** — nie tylko tej prawidłowej.

| Plik | Co to jest |
|---|---|
| `teoria.pdf` | **produkt główny** — 27 stron A4, gotowe do druku |
| `index.html` | ta sama treść w przeglądarce (offline, KaTeX, spis treści) |
| `teoria.md` | źródło treści |
| `zadania/*.png` | 51 wycinków oryginalnych pytań z kluczy (rysunek + treść + odpowiedzi, z pogrubioną prawidłową) |

## Co jest w środku

1. **Model obwodu** — element skupiony (pięć warunków), wielkości i konwencje, katalog elementów; pytanie o „co jest prawdą dla każdego elementu skupionego” i o połączenia szeregowe/równoległe.
2. **Prawa Kirchhoffa i łączenie źródeł** — PPK/NPK, zasada Tellegena, tablica „co wolno łączyć”, równanie oczka i węzła; sprzeczność dwóch idealnych źródeł napięciowych równolegle.
3. **Metody analizy** — pięć wariantów PPK z kluczy (w tym odpowiedź „układ jest sprzeczny”), superpozycja (trzy warianty + lista kontrolna), najbardziej chytra rodzina pytań: „od czego zależy napięcie na źródle prądowym” (litera C).
4. **Dwójniki** — opór zastępczy ze źródłem sterowanym (sześć wariantów), dwójnik bezźródłowy, punkt pracy elementu nieliniowego (`R_s`, `R_d`), parametry źródła Nortona.
5. **Twierdzenia** — `E_T` z rozwarcia, `J_N` ze zwarcia, moc maksymalna i dysponowana, wzmacniacz operacyjny w dwóch krokach.
6. **Elementy nieliniowe i moc** — prawo Ohma a nieliniowość, moc w obwodzie prądu stałego (`C` → rozwarcie, `L` → zwarcie), mostek Wheatstone'a.
7. **Poprawy (`A_2`)** — sześć pytań, których nie ma w wersji podstawowej.
8. **Zestawienie archetypów** (litera → co tam jest → metoda) + aneks z **wszystkimi 132 pytaniami Testu 1**.

Każde omówione pytanie ma trzy warstwy: **wycinek z klucza**, **pełną treść z opcjami** i **omówienie odpowiedzi** — dlaczego zaznaczona jest prawidłowa, skąd biorą się dystraktory (jaki błąd je produkuje) i jak sprawdzić wynik w kilka sekund. Liczby są przeliczone od zera i zgadzają się z kluczami; miejsca, w których klucze są niespójne (kilka odpowiedzi prawidłowych, sporne pytanie o dwójnik bezźródłowy), są opisane wprost.

## Przebudowa

```bash
pip install markdown pymupdf matplotlib      # node: npm install katex @resvg/resvg-js
cd build
python3 build_teoria.py --pdf   # teoria/index.html + teoria/_pdf_source.html + teoria/teoria.pdf
python3 check.py                # kontrola jakości wszystkich trzech dokumentów
```

Wycinki pytań generuje `build/dump_q.py` (podgląd treści klucza z zaznaczonymi
odpowiedziami) oraz funkcja `find_question()` z `build/inspect_task.py`
(współrzędne pytania w PDF → przycięcie stroną MuPDF):

```bash
cd build
python3 dump_q.py PELP1_25Z_A_1_klucz E      # treść pytania + pogrubione odpowiedzi
```
