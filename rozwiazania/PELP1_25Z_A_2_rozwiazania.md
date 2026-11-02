# PELP1 — Test 1 poprawka, wariant A_2 (17.12.2025) — rozwiązania

**Plik źródłowy:** [`PELP1_25Z_A_2_klucz.pdf`](../PELP1_25Z_A_2_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 1, 2 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( R - r \)**

Dwójnik AB: szeregowe połączenie rezystora \( R \) i źródła napięciowego sterowanego prądem (CCVS) o wartości \( r i \) (romb, grot w dół), gdzie \( i \) to prąd portu wpływający do A.

Grot źródła skierowany w dół — biegun **+ od strony B**: idąc wzdłuż prądu (od A przez \( R \), w dół przez źródło do B), spadek na \( R \) to \( iR \), a źródło podnosi potencjał o \( r i \):

\[
u = iR - ri = i(R - r)
\quad\Rightarrow\quad
R_{AB} = R - r
\]

**Kontrola:** gdyby grot był przeciwnie, wyszłoby \( R + r \) (odpowiedź 2). Dla \( r = 0 \) zostaje samo \( R \) ✓. Odpowiedź \( rR/(r+R) \) to błąd „równoległości" — źródło jest w szereg.

---

## B. Układ z oporem nieliniowym RN (1 p.)

**Odpowiedzi: 1 i 2**

Topologia: źródło \( J \) (grot w górę) równolegle z \( R \), następnie źródło \( E \) (grot w prawo) szeregowo do zacisku A; na prawo od A: poziomy rezystor \( R \) (prąd \( I \)) i \( R_N \) (gałąź pionowa); \( U \) — napięcie A-B.

- **1. PRAWDA** — dwójnik na lewo od AB (\( E \) szeregowo z \( J \parallel R \)) jest **liniowy** — można go zastąpić źródłem Thévenina (\( U_{oc} = E + JR \), \( R_T = R \)).
- **2. PRAWDA** — dwójnik na prawo od AB (\( R \) szeregowo z \( R_N \)) ma dobrze określoną charakterystykę \( i(u) \) (napięcia się sumują przy danym prądzie), więc przy obliczaniu \( I \) można go traktować jako **jeden element równoważny** — nieliniowy, ale równoważny.
- 3. FAŁSZ — zasada Tellegena obowiązuje w **całym** obwodzie (jest konsekwencją praw Kirchhoffa), nie tylko po lewej stronie.
- 4. FAŁSZ — \( U = (R + R_N) I \) wymaga prawa Ohma na \( R_N \) — a \( R_N \) jest nieliniowe; naprawdę \( U = E + RJ - IR \).
- 5. FAŁSZ — superpozycja wymaga liniowości całego układu.
- 6. FAŁSZ — dwójnik na lewo zawiera źródła \( E \) i \( J \) — nie jest opisywany prawem Ohma.

---

## C. Napięcie U na źródle prądowym (1 p.)

**Odpowiedzi: 1 i 2**

Topologia: \( E_1 \) (lewa gałąź pionowa, grot w górę) — źródło prądowe \( J \) (poziomo w górnym przewodzie, grot w prawo) — \( R \) (środkowa gałąź pionowa); szczyt \( R \) połączony gołym przewodem ze szczytem \( E_2 \) (prawa gałąź pionowa, grot w górę); \( U \) — napięcie na \( J \) (grot zwrócony ku \( E_1 \)).

Krok 1 — oba końce źródła prądowego mają potencjały **sztywno ustalone** przez źródła napięciowe:

\[
\varphi(\text{lewy węzeł}) = E_1, \qquad \varphi(\text{prawy węzeł}) = E_2
\]

Krok 2 — napięcie na \( J \):

\[
U = E_1 - E_2
\]

(źródło prądowe jest „bramką" — jego prąd nie zmienia napięcia między węzłami przybitymi źródłami napięciowymi; przez \( R \) płynie wtedy \( J \)).

Wnioski:
- \( U \) **zależy tylko od E1 i E2** — odpowiedź 1 ✓;
- \( U \) **nie zależy od J** — odpowiedź 2 ✓;
- \( U \neq 0 \) (3 fałszywa), nie zależy od \( R \) ani \( J \) (4, 5, 6 fałszywe).

---

## D. Napięcie U na wyjściu wzmacniacza (1 p.)

**Odpowiedź: 1 — układ jest nieprawidłowy**

Układ: wejście (+) przez \( R_2 \) do masy ⇒ \( u_+ = 0 \); sprzężenie zwrotne \( R_3 \) z wyjścia do wejścia (−) ⇒ w liniowej pracy wzmacniacza:

\[
u_- = u_+ = 0
\]

Ale do węzła wejścia (−) źródło \( E \) przyłączone jest **bezpośrednio** (gołym przewodem, bez rezystora) między tym węzłem a masą — a idealne źródło napięciowe **wymusza**:

\[
u_- = E \neq 0
\]

Sprzeczność: węzeł nie może być jednocześnie w \( 0 \) (masa urojona) i w \( E \). Układ nie ma poprawnego rozwiązania w modelu liniowym — **układ jest nieprawidłowy**.

**Kontrola:** dystraktory \( E(1 + R_3/R_{1,2}) \) i \( -E R_3/R_{1,2} \) to wzory wzmacniaczy, które wyszłyby, gdyby źródło \( E \) było przyłączone **przez rezystor** (odwracający/nieodwracający). Samo \( E \) (odpowiedź 2) to „powtarzacz" — też nie, bo warunek masy urojonej jest złamany.

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — \( 3\ \text{A} \)**

Figura: dwa obszary (lewy i prawy) połączone mostkiem „H": górny przewód z prądem \( 1\ \text{A} \) (strzałka w prawo — wpływa do górnego węzła środkowego), dolny przewód z prądem \( 2\ \text{A} \) (strzałka w prawo — wpływa do prawego obszaru), pionowa poprzeczka z prądem \( I \) (strzałka w dół).

Krok 1 — KCL w prawym obszarze (ma tylko dwa przyłącza): prąd wpływający dolnym przewodem \( 2\ \text{A} \) musi wypływać górnym — więc górnym przewodem płynie \( 2\ \text{A} \) **w lewo**, do węzła środkowego.

Krok 2 — KCL w górnym węźle środkowym: wpływają \( 1\ \text{A} \) (z lewego) i \( 2\ \text{A} \) (z prawego), a wypływa \( I \):

\[
I = 1 + 2 = 3\ \text{A}
\]

**Kontrola:** KCL w lewym obszarze: wypływa \( 1\ \text{A} \) górą, dolnym przewodem musi wpływać \( 1\ \text{A} \) — bilans domyka się ✓. Odpowiedź \( -3\ \text{A} \) to ta sama suma z odwróconą strzałką \( I \).

---

## F. Superpozycja — składowa od J1 (1 p.)

**Odpowiedź: 1 — \( J_1 \dfrac{R_2}{R_1+R_2} \)**

Topologia: \( J_1 \) (skrajna lewa gałąź pionowa, grot w dół) przyłączona do węzła N; z N: \( R_1 \) w dół do dolnej szyny (prąd \( I \) — strzałka w górę) oraz \( R_2 \) poziomo do gałęzi źródła \( E \); dalej \( E \) i \( J_2 \) (prawe gałęzie pionowe).

Superpozycja — tylko \( J_1 \):
- \( E \to \) zwarcie,
- \( J_2 \to \) rozwarcie.

Zwarcie \( E \) przyłącza prawy koniec \( R_2 \) do dolnej szyny, więc z węzła N zaczynają się **dwie równoległe gałęzie do masy**: \( R_1 \) i \( R_2 \). Źródło \( J_1 \) (grot w dół) **pobiera** prąd \( J_1 \) z węzła N, więc z masy przez \( R_1 \) i \( R_2 \) płyną prądy do N:

\[
\varphi_N = -J_1 \cdot (R_1 \parallel R_2)
\]

Prąd \( I \) (w górę przez \( R_1 \), od masy do N):

\[
I = \frac{0 - \varphi_N}{R_1} = J_1 \frac{R_1 R_2}{R_1 + R_2} \cdot \frac{1}{R_1} = J_1\frac{R_2}{R_1+R_2}
\]

**Kontrola:** to klasyczny **dzielnik prądowy**: \( J_1 \) rozdziela się na \( R_1 \) i \( R_2 \) odwrotnie proporcjonalnie do oporów — prąd przez \( R_1 \) jest tym mniejszy, im większe \( R_1 \) ✓. Dystraktor \( J_1 R_1/(R_1+R_2) \) to pomyłka gałęzi; 0 — błąd „źródło prądowe nie widzi oporów".

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( 1\ \text{mW} \)**

Topologia: źródło prądowe \( 2\ \text{mA} \) (grot w górę) równolegle z \( 2\ \text{k}\Omega \); z ich wspólnego węzła górnego opór \( 2\ \text{k}\Omega \) w górnym przewodzie do zacisku A; dolna szyna (goły przewód) do zacisku B; obciążenie \( R \) między A i B.

Krok 1 — napięcie rozwarcia (\( R \) odłączone): przez górny \( 2\ \text{k}\Omega \) nie płynie prąd, więc całe \( 2\ \text{mA} \) płynie przez równoległy \( 2\ \text{k}\Omega \):

\[
U_{oc} = 2\ \text{mA} \cdot 2\ \text{k}\Omega = 4\ \text{V}
\]

Krok 2 — opór Thévenina (źródło prądowe rozwieramy): z portu A-B widak szereg dwóch \( 2\ \text{k}\Omega \):

\[
R_T = 2\ \text{k}\Omega + 2\ \text{k}\Omega = 4\ \text{k}\Omega
\]

Krok 3 — moc maksymalna:

\[
P_{max} = \frac{U_{oc}^2}{4 R_T} = \frac{16}{16\,000} = 1\ \text{mW}
\]

**Kontrola:** dystraktor 4 mW to \( U_{oc}^2/R_T \) (moc przy zwarciu); 2 mW — pominięcie jednego \( 2\ \text{k}\Omega \) w \( R_T \); 0,5 mW i 0,25 mW — źle odczytane \( U_{oc} \).

---

## H. Dwójnik bezźródłowy (1 p.)

**Odpowiedzi: 1 i 2 — dwójniki z rysunków 1 i 2**

Zestaw pięciu dwójników:
1. \( R \) ze źródłem sterowanym \( ku \),
2. dioda \( D \) ze źródłem \( E > 0 \),
3. \( R \) ze źródłem \( E > 0 \),
4. dioda \( D \) ze źródłem \( E > 0 \) (druga konfiguracja),
5. źródło \( E > 0 \) ze źródłem sterowanym \( ri \).

Kryterium „zera na charakterystyce" (najczęściej używane): dwójnik jest bezźródłowy, gdy jego charakterystyka \( i(u) \) **przechodzi przez początek układu współrzędnych** — czyli przy \( u = 0 \) prąd \( i = 0 \) (brak niezależnego źródła energii):

- **dwójnik 1**: \( u = 0 \Rightarrow ku = 0 \Rightarrow i = 0 \) — charakterystyka przechodzi przez (0,0) ✓,
- **dwójnik 2** (dioda + \( E \)): dioda zaporuje dla \( u < E \), więc w otoczeniu zera (i w samym \( u = 0 \)) prąd \( i = 0 \) — pozioma część charakterystyki zawiera początek układu ✓,
- dwójniki 3, 4 (w drugiej konfiguracji) i 5: źródło \( E \) przesuwa charakterystykę tak, że przy \( u = 0 \) płynie niezerowy prąd (lub występuje niezerowe napięcie przy \( i = 0 \)) — nie są bezźródłowe.

**Uwaga (kompendium §7.6):** według drugiego kryterium — „w środku nie ma żadnego źródła" — bezźródłowy nie byłby żaden z dwójników 1–5 (odpowiedź 6). Klucz zaznacza **1 i 2** (tak samo jak w identycznym zestawie 20L_A_1 · G) — to znana niespójność kluczy, którą trzeba znać, a nie „naprawiać".

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( R - r \) | \( u = iR - ri \); grot CCVS w dół |
| B | 1, 2 | lewy liniowy ⇒ Thévenin; prawy \( R + R_N \) ⇒ element równoważny |
| C | 1, 2 | \( U = E_1 - E_2 \); oba końce przybite źródłami napięciowymi |
| D | nieprawidłowy | \( E \) przybija \( u_- \), a sprzężenie wymusza \( u_- = 0 \) |
| E | 3 A | \( I = 1 + 2 \) (oba prądy dopływają do węzła górnego) |
| F | \( J_1 R_2/(R_1+R_2) \) | dzielnik prądowy: \( E \) zwarte, \( J_2 \) rozwarte |
| G | 1 mW | \( U_{oc} = 4\ \text{V} \), \( R_T = 4\ \text{k}\Omega \); \( 16/16\,000 \) |
| H | 1, 2 | charakterystyka przez (0,0): dwójniki 1 i 2 (niespójność klucza — §7.6) |
