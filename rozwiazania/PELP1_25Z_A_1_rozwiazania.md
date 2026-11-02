# PELP1 — Test 1, wariant A_1 (5.11.2025) — rozwiązania

**Plik źródłowy:** [`PELP1_25Z_A_1_klucz.pdf`](../PELP1_25Z_A_1_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 | 1, 2 | 1 | 1 | 1 | 1 | 1 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( \dfrac{1}{G-g} \)**

Dwójnik AB: przewodność \( G \) i źródło prądowe sterowane napięciem (VCCS) \( g u \) (romb, strzałka w górę) połączone **równolegle** między zaciskami A (góra) i B (dół). \( u \) to napięcie portu (strzałka w górę).

Krok 1 — prąd przez przewodność (z A do B): \( G u \).

Krok 2 — źródło sterowane wtłacza prąd \( g u \) **do węzła A** (strzałka w górę), czyli od strony portu jest to prąd ujemny:

\[
i_{AB} = G u - g u = (G - g)\,u
\]

Krok 3:

\[
R_{AB} = \frac{u}{i_{AB}} = \frac{1}{G-g}
\]

**Kontrola:** \( g = 0 \Rightarrow R_{AB} = 1/G \) (sama przewodność) ✓. Dystraktor \( 1/(G+g) \) — błąd kierunku strzałki rombu; \( gG/(g+G) \) — potraktowanie \( g \) jak przewodności (błąd pojęciowy: \( g \) to transkonduktancja, nie element rezystancyjny).

---

## B. Opór statyczny i dynamiczny elementu nieliniowego (1 p.)

**Odpowiedź: 1 — \( R_s = 1{,}33\ \text{k}\Omega,\ R_d = 0{,}5\ \text{k}\Omega \)**

Element nieliniowy o charakterystyce \( i(u) \) (płaski start, potem łamana o rosnącym nachyleniu) zasilony jest z **idealnego źródła prądowego 3 mA** — źródło wymusza prąd, więc:

Krok 1 — **punkt pracy**: szukamy punktu na charakterystyce, w którym \( i = 3\ \text{mA} \). Odczyt z rysunku (stroma część): \( u \approx 4\ \text{V} \).

Krok 2 — **opór statyczny** (stosunek u/i w punkcie pracy):

\[
R_s = \frac{u}{i} = \frac{4\ \text{V}}{3\ \text{mA}} \approx 1{,}33\ \text{k}\Omega
\]

Krok 3 — **opór dynamiczny** (odwrotność nachylenia charakterystyki w punkcie pracy); nachylenie stromej części to ok. \( 2\ \text{mA/V} \):

\[
R_d = \frac{\Delta u}{\Delta i} = \frac{1}{2\ \text{mS}} = 0{,}5\ \text{k}\Omega
\]

**Kontrola:** dla charakterystyki wypukłej (prąd rośnie szybciej niż liniowo) zawsze \( R_d < R_s \) — od razu eliminuje opcje 2, 5 i 6. Wartość \( R_s = 0{,}75\ \text{k}\Omega \) to pomyłka \( 3/4 \) zamiast \( 4/3 \) (odwrotny ułamek).

---

## C. Napięcie U na źródle prądowym J2 (1 p.)

**Odpowiedzi: 1 i 2**

Topologia: \( E \) (lewa gałąź pionowa, grot w górę) z \( R_1 \) i \( J_1 \) przyłączonymi do tego samego górnego węzła; stamtąd \( R_2 \) (poziomo) do węzła \( J_2 \) (prawa gałąź pionowa, grot w górę); \( U \) — napięcie na \( J_2 \) (strzałka w górę).

Krok 1 — źródło \( E \) **przybija** lewy górny węzeł do potencjału \( E \). Elementy \( R_1 \) i \( J_1 \) przyłączone do tego węzła równolegle nie zmieniają tego potencjału (źródło idealne „połyka" ich prądy).

Krok 2 — KCL w węźle \( J_2 \): prąd wpływający przez \( R_2 \) plus \( J_2 \) (grot w górę) równa się zero (bramka — \( J_2 \) wymusza swój prąd), więc przez \( R_2 \) płynie prąd o wartości \( J_2 \) i odkłada spadek \( J_2 R_2 \):

\[
U = E \pm J_2 R_2 \quad(\text{co do znaku})
\]

Wnioski:
- **U zależy od E** — odpowiedź 1 prawdziwa ✓;
- **U nie zależy od J1** — odpowiedź 2 prawdziwa ✓;
- 3 (U = 0) fałszywa; 4 (zależy od R1) fałszywa; 5 (nie zależy od R2) fałszywa — \( R_2 \) stoi w gałęzi, przez którą płynie \( J_2 \); 6 (od wszystkich) fałszywa.

---

## D. Napięcie U na wyjściu wzmacniacza (1 p.)

**Odpowiedź: 1 — \( E \)**

Układ: źródło \( E \) (grot w prawo) między masą a wejściem **(+)**; wejście (−) połączone **wyłącznie** rezystorem \( R_1 \) z wyjściem wzmacniacza (sprzężenie zwrotne); \( R_2 \) między wyjściem a masą (obciążenie); \( U \) — napięcie wyjściowe.

Krok 1 — pętla zamknięta (sprzężenie przez \( R_1 \)) ⇒:

\[
u_- = u_+ = E
\]

Krok 2 — wejście (−) idealnego wzmacniacza nie pobiera prądu, a ma **tylko jedno** przyłącze (przez \( R_1 \)) — więc prąd przez \( R_1 \) wynosi zero i nie ma na nim spadku:

\[
U = u_- = E
\]

Krok 3 — \( R_2 \) (obciążenie) nie ma wpływu: idealne wyjście wzmacniacza utrzymuje \( U = E \) przy dowolnym skończonym obciążeniu.

**Kontrola:** to powtarzacz w przebraniu — wzmocnienie 1. Odpowiedzi 3 i 4 (\( E(1+R_1/R_2) \), \( E(1+R_2/R_1) \)) to nieodwracający wzmacniacz z dzielnikiem w sprzężeniu; 5 i 6 to wzmacniacz odwracający.

---

## E. Natężenia I1 i I2 (1 p.)

**Odpowiedź: 1 — \( -1{,}5\ \text{A} \)**

Figura: węzeł, z którego wychodzą cztery przewody — \( I_1 \) (w lewo), \( I_2 \) (w prawo), \( 1\ \text{A} \) (w lewo-dół), \( 2\ \text{A} \) (w prawo-dół). **Wszystkie cztery groty skierowane są od węzła na zewnątrz.**

Krok 1 — KCL (suma prądów wypływających = 0):

\[
I_1 + I_2 + 1 + 2 = 0
\]

Krok 2 — warunek zadania \( I_1 = I_2 = I \):

\[
2I = -3\ \text{A} \quad\Rightarrow\quad I = -1{,}5\ \text{A}
\]

**Kontrola:** wartość bezwzględna 1,5 A (odpowiedź 2) to ta sama liczba bez znaku — dla kogoś, kto uznał groty za „wpływające". Opcja 3 A to \( 1 + 2 \) bez warunku \( I_1 = I_2 \); 1 A to różnica \( 2 - 1 \); „za mało danych" jest fałszywe — KCL nie potrzebuje oporów.

---

## F. Połączenia równoległe (1 p.)

**Odpowiedź: 1 — (1 i 2) oraz (3 i 5)**

Topologia: elementy 3, 4, 5 pionowe; elementy 1, 2 poziome w środkowym rzędzie (1 między wierzchołkami 3 i 4, 2 między wierzchołkami 4 i 5); **górna szyna łączy wierzchołki 3 i 5** (i węzeł nad 4 jest osobny); dolna szyna łączy podstawy 3, 4, 5.

Węzły:
- **A** = górna szyna (wierzchołki 3 i 5),
- **B** = węzeł nad 4 (między 1 i 2),
- **D** = dolna szyna (podstawy 3, 4, 5).

Przynależność elementów:
- 1: między A i B; 2: między B i A ⇒ **1 ∥ 2** ✓,
- 3: między A i D; 5: między A i D ⇒ **3 ∥ 5** ✓,
- 4: między B i D — szeregowo względem obu par.

**Kontrola:** opcje 2 i 3 to „połowa prawdy" (ktoś sprawdził tylko jedną parę); opcja 4 miesza 4 z parami, których nie łączy wspólna para węzłów.

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( \dfrac{3}{10}\ \text{mW} \)**

Topologia: źródło \( 3\ \text{V} \) — opór szeregowy \( 3\ \text{k}\Omega \) — zacisk A; między A i B opór \( 2\ \text{k}\Omega \); obciążenie \( R \) również między A i B.

Krok 1 — napięcie rozwarcia (dzielnik napięcia \( 3\,\text{k} \)–\( 2\,\text{k} \)):

\[
E_T = 3\ \text{V} \cdot \frac{2}{3+2} = 1{,}2\ \text{V}
\]

Krok 2 — opór Thévenina (źródło zwarte):

\[
R_T = 3\ \text{k}\Omega \parallel 2\ \text{k}\Omega = 1{,}2\ \text{k}\Omega
\]

Krok 3 — moc maksymalna:

\[
P_{max} = \frac{E_T^2}{4 R_T} = \frac{1{,}44}{4 \cdot 1200} = 0{,}3\ \text{mW} = \frac{3}{10}\ \text{mW}
\]

**Wzór skrócony** (źródło + opór szeregowy \( R_s \) + opór równoległy \( R_p \)):
\[
P_{max} = \frac{E^2 R_p}{4 R_s (R_s + R_p)} = \frac{9 \cdot 2000}{4 \cdot 3000 \cdot 5000} = 0{,}3\ \text{mW} \checkmark
\]

**Kontrola:** \( 5/6\ \text{mW} \) to błąd wymiaru (\( E^2/R_T \)); \( 10/3 \) i \( 10/6\ \text{mW} \) — pominięcie dzielnika lub paralleli w \( R_T \).

---

## H. Wydajność prądowa JN źródła Nortona (1 p.)

**Odpowiedź: 1 — \( J \)**

Dwójnik AB: źródło prądowe \( J \) (grot w górę) równolegle z \( R_1 \), potem **źródło napięciowe sterowane prądem** (CCVS) \( r i \) w górnym przewodzie, a na końcu \( R_2 \) (przez który płynie prąd sterujący \( i \)) między zaciskami A i B.

Zasada Nortona: \( J_N \) = prąd zwarcia zacisków A-B.

Zwijamy A z B (zwarcie):
- zwarcie **bocznikuje \( R_2 \)**, więc \( u_{R2} = 0 \Rightarrow i = 0 \);
- źródło sterowane \( r \cdot i = r \cdot 0 = 0\ \text{V} \) — staje się kawałkiem przewodu;
- ten „przewód" zwiera lewy węzeł z A, więc **\( R_1 \) też jest zwarte**;
- cały prąd \( J \) płynie przez zwarcie:

\[
J_N = J
\]

**Kontrola:** dystraktory \( J/(1+r/R_{1,2}) \) powstają z założenia, że przez romb płynie prąd zwarcia — a przecież jest on sterowany prądem \( i \) gałęzi, którą zwarcie zeruje (kompendium §5.3: „zwarcie ⇒ źródła sterowane prądem gałęzi zwieranej gasną").

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( 1/(G-g) \) | \( i_{AB} = (G-g)u \); romb wtłacza prąd do A |
| B | \( R_s = 1{,}33\ \text{k} \), \( R_d = 0{,}5\ \text{k} \) | punkt pracy (4 V, 3 mA); nachylenie 2 mA/V |
| C | 1, 2 | \( U = E \pm J_2 R_2 \); \( R_1 \), \( J_1 \) nie zmieniają potencjału węzła |
| D | \( E \) | \( u_- = u_+ = E \); zero prądu w \( R_1 \) ⇒ zero spadku |
| E | \( -1{,}5\ \text{A} \) | \( 2I + 1 + 2 = 0 \) (groty na zewnątrz) |
| F | (1 i 2) oraz (3 i 5) | węzły: A (góra), B (środek), D (dół) |
| G | \( 3/10\ \text{mW} \) | \( E_T = 1{,}2\ \text{V} \), \( R_T = 1{,}2\ \text{k}\Omega \) |
| H | \( J \) | zwarcie: \( i = 0 \Rightarrow ri = 0 \); \( R_1 \) zwarte, cały \( J \) w zwarcie |
