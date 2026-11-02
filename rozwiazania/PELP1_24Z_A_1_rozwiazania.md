# PELP1 — Test 1, wariant A_1 (30.10.2024) — rozwiązania

**Plik źródłowy:** [`PELP1_24Z_A_1_klucz.pdf`](../PELP1_24Z_A_1_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 | 1 | 1, 2 | 1 | 1 | 1 | 1 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( \dfrac{R}{1-\beta} \)**

Dwójnik AB: dwie gałęzie równoległe między zaciskami A (góra) i B (dół):
- rezystor \( R \), przez który płynie prąd \( i \) (strzałka w dół),
- źródło prądowe sterowane prądem (CCCS) o wartości \( \beta i \), ze strzałką w **górę**.

Krok 1 — napięcie dwójnika to napięcie na \( R \) (gałęzie równoległe):

\[
u = i\,R
\]

Krok 2 — KCL w górnym węźle: prąd wpływający z zacisku A plus prąd wtłaczany przez źródło sterowane (\( \beta i \) w górę) równa się prądowi \( i \) płynącemu w dół przez \( R \):

\[
i_{AB} + \beta i = i \quad\Rightarrow\quad i_{AB} = i(1-\beta)
\]

Krok 3 — definicja oporu zastępczego:

\[
R_{AB} = \frac{u}{i_{AB}} = \frac{iR}{i(1-\beta)} = \frac{R}{1-\beta}
\]

**Kontrola:** dla \( \beta = 0 \) źródło znika i zostaje samo \( R \) ✓. Dla \( \beta \to 1 \) opór rośnie do nieskończoności (źródło tłumi prąd portu) ✓.

---

## B. Układ z oporem nieliniowym RN (1 p.)

**Odpowiedź: 1 — dwójnik na lewo od zacisków AB można zastąpić źródłem Thévenina**

Topologia: źródło prądowe \( J \) (grot w górę) równolegle z \( R \) (gałęzie pionowe), a następnie źródło \( E \) (grot w prawo, w stronę A) szeregowo w górnym przewodzie do zacisku A. Na prawo od A: poziomy rezystor \( R \) (prąd \( I \)) i \( R_N \) (gałąź pionowa). \( U \) — napięcie A-B (strzałka w górę).

- **1. PRAWDA** — dwójnik na lewo od AB to \( E \) szeregowo z (\( J \parallel R \)): wszystkie elementy **liniowe**, więc można go zastąpić źródłem Thévenina:
  \[
  U_{oc} = E + JR \quad (\text{stan jałowy: } J \text{ płynie przez } R), \qquad R_T = R
  \]
- 2. FAŁSZ — \( U = E + RJ \) to tylko napięcie **jałowe** (przy \( I = 0 \)). Przy obciążeniu: \( U = E + RJ - IR \) — spadek na \( R_T \) psuje równość.
- 3. FAŁSZ — \( R_N \) nie spełnia prawa Ohma.
- 4. FAŁSZ — dzielnik napięciowy wymaga elementów liniowych i znanej sieci; tu \( R_N \) jest nieliniowe.
- 5. FAŁSZ — zasada Tellegena (bilans mocy) wynika z praw Kirchhoffa i obowiązuje w każdym obwodzie, także nieliniowym.

---

## C. Od czego zależy napięcie U (1 p.)

**Odpowiedź: 1 — zależy od wartości J1**

Topologia: \( E \) (lewa gałąź pionowa, grot w górę) — \( R_1 \) (górny przewód lewy) — węzeł N; z N w dół źródło prądowe \( J_1 \) (grot w górę); z N w prawo źródło \( J_2 \) (grot w **lewo** — wtłacza prąd do N), a za nim \( R_2 \) (prawa gałąź pionowa) do dolnej szyny. \( U \) — napięcie na \( J_1 \) (strzałka w górę, grot przy N).

Krok 1 — \( R_2 \) nie gra żadnej roli: prąd przez gałąź \( J_2 \)–\( R_2 \) jest **wymuszony** przez źródło prądowe (\( \varphi_{N2} = J_2 R_2 \)), a napięcie \( \varphi_N \) nie wpływa na ten prąd (bramka prądowa).

Krok 2 — KCL w węźle N: prądy wpływające \( J_1 \) (grot w górę) i \( J_2 \) (grot w lewo) muszą odpłynąć przez \( R_1 \) do źródła \( E \):

\[
\frac{U - E}{R_1} + J_1 + J_2 = 0
\quad\Rightarrow\quad
U = E + R_1 (J_1 + J_2)
\]

Wnioski:
- \( U \) **zależy od J1** — odpowiedź 1 prawdziwa ✓;
- \( U \) **nie zależy od R2** (odpowiedź 3 fałszywa);
- \( U \neq 0 \) (odpowiedź 2 fałszywa);
- \( U \) **zależy od R1** (i od E oraz J2) — więc odpowiedź 4 „nie zależy od wartości R1" jest fałszywa.

**Wskazówka:** to lustrzany wariant zadania o „bramce" — tu pytanie brzmi „od czego zależy", a pułapką jest sugerowanie, że prąd źródłowy \(`J_1\`) zniknie. Każdy mikroprąd z N musi wrócić do E przez \( R_1 \), tworząc spadek.

---

## D. Czwórnik ze wzmacniaczem operacyjnym (1 p.)

**Odpowiedzi: 1 i 2**

Czwórnik: wzmacniacz operacyjny, wejście (+) z napięciem \( u_1 \) i prądem \( i_1 \); wyjście z napięciem \( u_2 \); sprzężenie zwrotne rezystorem \( R \) z wyjścia do wejścia (−), prąd w tym przewodzie \( i_2 \).

- **1. PRAWDA** — \( i_1 = i_2 \): idealny wzmacniacz **nie pobiera prądu** na żadnym wejściu, więc \( i_1 = 0 \) i \( i_2 = 0 \) — są równe (oba zerowe).
- **2. PRAWDA** — \( u_1 = u_2 \): pętla zamknięta daje \( u_+ = u_- \), czyli \( u_- = u_1 \); a ponieważ \( i_2 = 0 \), na rezystorze sprzężenia nie ma spadku:
  \[
  u_2 = u_- = u_+ = u_1
  \]
- 3. FAŁSZ — \( u_2 = -u_1 \) to wzmacniacz **odwracający** (sprzężenie do wejścia (+)); tu sprzężenie idzie do (−).
- 4. FAŁSZ — \( u_2 = R i_2 \): skoro \( i_2 = 0 \), dawałoby \( u_2 = 0 \) zawsze — sprzeczne z \( u_2 = u_1 \).
- 5. FAŁSZ — \( i_2 > 0 \): prąd wejściowy wynosi dokładnie 0.

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — \( 1\ \text{A} \)**

Figura: trzy obszary (lewy, środkowy, prawy) w rzędzie. Przewody:
- lewy–środkowy (górny): \( 1\ \text{A} \), strzałka w lewo (do lewego),
- lewy–środkowy (środkowy): bez etykiety,
- środkowy–prawy (górny): \( 3\ \text{A} \), strzałka w lewo (do środkowego),
- środkowy–prawy (środkowy): \( I \), strzałka w prawo (do prawego),
- lewy–prawy (dolny obejście): \( 2\ \text{A} \), strzałka w prawo (do prawego).

Krok 1 — KCL w prawym obszarze (najprościej: ma tylko trzy przyłącza):

\[
\underbrace{I}_{\text{wpływa}} + \underbrace{2}_{\text{wpływa}} = \underbrace{3}_{\text{wypływa}}
\quad\Rightarrow\quad
I = 3 - 2 = 1\ \text{A}
\]

Krok 2 — kontrola spójności pozostałych obszarów: KCL w środkowym: wpływają \( 3 + 1 = 4 \), wypływają \( 1 + I = 2 \)... po policzeniu prądu w nieoznaczonym przewodzie lewy–środkowy (\( 4 - 1 - 1 = 2\ \text{A} \) w lewo) bilans lewego: \( 1 + 2 = 3 \)... wszystkie KCL się zgadzają ✓.

**Wskazówka:** przy „kałużach" zawsze znajdź obszar z **najmniejszą liczbą przyłączy** — tu prawy ma tylko trzy, w tym dwa znane.

---

## F. Połączenia równoległe (1 p.)

**Odpowiedź: 1 — tylko (4 i 5)**

Topologia: element 3 — skrajna lewa gałąź pionowa; element 1 — górny przewód lewy; element 4 — środkowa gałąź pionowa; element 2 — górny przewód prawy; element 5 — skrajna prawa gałąź pionowa; dolna szyna łączy doły elementów 3, 4, 5. **Nad rysunkiem przewód łączy górny węzeł środkowy z górnym węzłem prawym** — więc te dwa węzły to elektrycznie **jeden węzeł** (element 2 jest zwarty tym przewodem — wisi między tym samym węzłem).

Węzły: A (góra-lewo: elementy 3 i 1), C (góra-środek = góra-prawo: elementy 1, 2, 4, 5), B (dolna szyna: elementy 3, 4, 5).

\[
\text{element 4: } C \leftrightarrow B, \qquad \text{element 5: } C \leftrightarrow B
\]

Elementy 4 i 5 łączą **tę samą parę węzłów** — są równoległe ✓. Pozostałe pary nie mają obu węzłów wspólnych:
- (2 i 5): element 2 jest zwarty (C–C), nie definiuje gałęzi między różnymi węzłami;
- (3 i 5): różne górne węzły (A vs C);
- (3 i 4): j.w.;
- (1 i 2): 1 jest między A i C, 2 między C i C.

---

## G. Moc dysponowana źródła na lewo od zacisków AB (2 p.)

**Odpowiedź: 1 — \( 9\ \text{mW} \)**

Topologia: źródło prądowe \( 4\ \text{mA} \) (grot w górę) równolegle z \( 3\ \text{k}\Omega \) (gałęzie pionowe po lewej), a z górnego węzła opór \( 1\ \text{k}\Omega \) w przewodzie poziomym do zacisku A; B na dolnej szynie.

Krok 1 — źródło Thévenina dla części na lewo od A-B:

**Napięcie rozwarcia** (stan jałowy: przez \( 1\ \text{k}\Omega \) nie płynie prąd, więc całe \( 4\ \text{mA} \) płynie przez \( 3\ \text{k}\Omega \)):

\[
E_T = 4\ \text{mA} \cdot 3\ \text{k}\Omega = 12\ \text{V}
\]

**Opór wewnętrzny** (źródło prądowe rozwieramy — zostaje \( 3\ \text{k}\Omega \) szeregowo z \( 1\ \text{k}\Omega \) prowadzącym do zacisku):

\[
R_T = 3\ \text{k}\Omega + 1\ \text{k}\Omega = 4\ \text{k}\Omega
\]

Krok 2 — moc dysponowana (maksymalna, jaką odbiornik może pobrać przy \( R = R_T \)):

\[
P_{dysp} = \frac{E_T^2}{4 R_T} = \frac{144}{16\,000} = 9\ \text{mW}
\]

**Kontrola:** dystraktor 12 mW to \( E_T^2/R_T \) (moc przy zwarciu), 36 mW — \( E_T^2/R_T \) z pominięciem czwórki, 4 mW i 16 mW — błędne \( E_T \) (np. 4 V) lub wzięcie \( R_T = 1\ \text{k}\Omega \).

---

## H. Wydajność prądowa JN źródła Nortona (1 p.)

**Odpowiedź: 1 — \( 1\ \text{mA} \)**

Dwójnik AB: trzy gałęzie równoległe: źródło prądowe \( 1\ \text{mA} \) (grot w górę), rezystor \( 2\ \text{k}\Omega \) (z napięciem \( u \)) oraz źródło prądowe sterowane napięciem (VCCS) \( g u \) (grot w dół), przy \( g = 2\ \text{mS} \).

Zasada Nortona: \( J_N \) = prąd zwarcia zacisków A-B.

Zwijamy A z B (zwarcie): napięcie \( u = 0 \), więc źródło sterowane daje

\[
g \cdot u = 2\ \text{mS} \cdot 0 = 0
\]

— **gaśnie niezależnie od wartości g**. Zostaje samo źródło \( 1\ \text{mA} \), którego prąd nie ma innej drogi niż zwarcie:

\[
J_N = 1\ \text{mA}
\]

**Kontrola:** wartość \( g = 2\ \text{mS} \) jest w treści zadania wyłącznie jako pokusa policzenia \( g u \) przy \( u \) z innego stanu obwodu (dystraktory 2 mA / −2 mA). Dystraktory ±... wynikają też z umowy znaku \( J_N \) (od A czy od B).

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( R/(1-\beta) \) | KCL: \( i_{AB} = i - \beta i \); \( u = iR \) |
| B | 1 | lewy dwójnik liniowy (\( E \) + \( J \parallel R \)) ⇒ Thévenin; \( U = E + RJ - IR \neq E + RJ \) |
| C | 1 | \( U = E + R_1(J_1 + J_2) \) — bez \( R_2 \) (bramka), z \( J_1 \) i \( R_1 \) |
| D | 1, 2 | \( i_1 = i_2 = 0 \); \( u_2 = u_- = u_+ = u_1 \) (brak spadku na R) |
| E | 1 A | prawy obszar: \( I + 2 = 3 \) |
| F | tylko (4 i 5) | przewód górny zwiera węzły ⇒ 4 i 5 między tą samą parą węzłów |
| G | 9 mW | \( E_T = 4\,\text{mA} \cdot 3\,\text{k} = 12\ \text{V} \), \( R_T = 4\ \text{k}\Omega \); \( 144/16\,000 \) |
| H | 1 mA | zwarcie: \( u = 0 \Rightarrow gu = 0 \); zostaje 1 mA |
