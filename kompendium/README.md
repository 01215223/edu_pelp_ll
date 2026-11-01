# Kompendium PELP1 — podstawy elektroniki i teoria obwodów

Kompendium wiedzy do kolokwium wykładowego z przedmiotu **PELP1**, opracowane na
podstawie **35 kluczy odpowiedzi** (252 pytania, lata 2019–2026) znajdujących się
w katalogu głównym repozytorium.

## Co jest w środku

```
kompendium/
├── index.html        ← GŁÓWNY PLIK: całe kompendium (otwórz w przeglądarce)
├── kompendium.md     ← źródło treści w Markdown
├── figury/           ← 13 rysunków SVG (schematy obwodów, wykresy, mostek…)
└── katex/            ← CSS + fonty do wzorów (wzory są renderowane statycznie)
build/
├── build.py          ← generator: Markdown → HTML (+ aneks z bankiem pytań)
├── figures.py        ← generator rysunków SVG
├── svgkit.py         ← mini-biblioteka symboli schematów (IEC)
├── katex_render.js   ← statyczne renderowanie wzorów (KaTeX)
└── bank.json         ← 252 pytania z kluczy + klasyfikacja tematyczna
```

## Jak korzystać

* **Czytanie:** otwórz `kompendium/index.html` w przeglądarce (działa offline, bez internetu).
* **PDF:** w przeglądarce `Ctrl/⌘+P` → „Zapisz jako PDF”. Arkusz stylów ma osobną
  wersję do druku (bez panelu bocznego, A4, z zachowaniem ramek i rysunków).
* **Szukanie:** `Ctrl/⌘+F` w przeglądarce albo wyszukiwarka w §12 (bank pytań),
  z filtrem po temacie.

## Struktura treści

| Rozdział | Zakres | Odpowiada pytaniom |
|---|---|---|
| 0 | format kolokwium, mapa tematów, plan powtórki na 3 dni | — |
| 1 | wielkości i konwencje, element skupiony, prawo Ohma, łączenie rezystorów, C i L w prądzie stałym, rezystancja zastępcza, źródła sterowane | typ A, F |
| 2 | prawa Kirchhoffa, metody analizy (Millman, oczkowa), źródła rzeczywiste i łączenie źródeł | typ C, D, E |
| 3 | superpozycja, zasada Tellegena, Thévenin/Norton, dopasowanie i moc dysponowana | typ F, G, H |
| 4 | elementy nieliniowe: $R_s$ i $R_d$, punkt pracy, dioda idealna, analiza dwustanowa | typ B, G, H |
| 5 | klasyfikacja dwójników, czwórniki | typ B, D, H |
| 6 | błąd i niepewność, metody pomiarowe, niepewność złożona, zaokrąglanie, statystyka | typ A, C, F, G |
| 7 | przyrządy analogowe i cyfrowe, charakterystyki niepewności, dobór zakresu | typ B, D, E, F |
| 8 | metoda techniczna i błąd pobrania, mostek Wheatstone'a, metoda czteroprzewodowa | typ A, B, E, F |
| 9 | oscyloskop: tor sygnału, sprzężenie, wyzwalanie, rodzaje, ADC | typ C, D |
| 10 | 18 rozwiązanych zadań (rachunek + metrologia) | wszystkie |
| 11 | formułownik i 30 zdań-pułapek | powtórka |
| 12 | bank 252 pytań z kluczy z filtrowaniem i odsyłaczami do rozdziałów | aneks |

## Odtworzenie/build

```bash
# wymagania: python3 + pip install markdown pymupdf ; node + npm install katex
cd build
python3 figures.py     # regeneruje rysunki SVG
python3 build.py       # buduje ../kompendium/index.html
```

`build.py` wstawia do treści dwa automatyczne aneksy: mapę tematów (`<!--TOPICMAP-->`)
i bank pytań (`<!--BANK-->`), a wzory renderuje do HTML KaTeX-a na etapie budowania —
dzięki temu plik wynikowy jest samowystarczalny i nie wymaga JavaScriptu.

## Uwagi o źródłach

* W repozytorium były tylko **klucze** (bez slajdów i bez arkuszy dla studentów),
  więc teoria została odtworzona pod kątem kompetencji sprawdzanych pytaniami.
* Klucze dopuszczają **kilka odpowiedzi prawidłowych** w jednym pytaniu (do testu
  wybierana jest jedna) — w aneksie widać wszystkie, zgodnie z kluczem.
* W kilku miejscach klucze są wewnętrznie niespójne (np. liczenie niepewności
  złożonej dwiema metodami daje 0,12 V albo 0,2 V; jednostka mV zamiast V
  w jednym arkuszu). Takie przypadki są opisane w treści, a nie „wygładzone”.
