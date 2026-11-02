# PELP1 — Test 1 poprawkowy, wariant A_2 (21.12.2022) — rozwiązania

**Plik źródłowy:** [`PELP1_22Z_A_2_klucz.pdf`](../PELP1_22Z_A_2_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1, 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( \dfrac{R}{1-k} \)**

Dwójnik AB: **szeregowe** połączenie źródła napięciowego sterowanego napięciem (VCVS) \( k u \) (romb, grot w górę) i rezystora \( R \); napięcie sterujące \( u \) to napięcie na samych zaciskach AB.

Obchodzimy pętlę: napięcie źródła sterowanego (biegun + od strony grotu) dodaje się do spadku na \( R \):

\[
u = k\,u + i\,R
\]

Stąd:

\[
u(1-k) = i\,R \quad\Rightarrow\quad R_{AB} = \frac{u}{i} = \frac{R}{1-k}
\]

**Kontrola:** dla \( k = 0 \) dostajemy \( R \) ✓ (samo R). Dla \( k \to 1 \) opór rośnie do nieskończoności — źródło sterowane „podtrzymuje" całe napięcie. Wynik nie zależy od \( u \) (odpowiedź 7 odpada).

---

## B. Układ z oporem nieliniowym RN (1 p.)

**Odpowiedzi: 1 i 2**

Układ: po lewej stronie zacisków AB źródło prądowe \( J \) równolegle z liniowym \( R \), w szeregu (w przewodzie górnym) źródło \( E \); po prawej stronie \( R \) (z prądem \( I \)) szeregowo z oporem nieliniowym \( R_N \); \( U \) to napięcie na zaciskach A-B.

- **1. PRAWDA** — dwójnik po lewej stronie (\( J \parallel R \), potem \( E \)) jest **liniowy** i zawiera źródła, więc można go zastąpić równoważnym źródłem Nortona (a więc i Thevenina).
- **2. PRAWDA** — dwójnik po prawej stronie to szeregowe połączenie \( R \) i \( R_N \); z punktu widzenia zacisków AB zachowuje się jak **jeden element równoważny** o charakterystyce \( u = R\,i + u_{RN}(i) \). Przy obliczaniu \( U \) (napięcia na zaciskach) liczy się tylko ta charakterystyka — więc zastąpienie elementem równoważnym jest poprawne.
- 3. FAŁSZ — zasada Tellegena (bilans mocy) obowiązuje w **całym** obwodzie, liniowym i nieliniowym; nie da się jej „wyłączyć" dla połowy schematu.
- 4. FAŁSZ — \( R_N \) nie spełnia prawa Ohma, więc \( U \neq (R + R_N) I \); poza tym \( U \) to napięcie na zaciskach, nie na prawym dwójniku.
- 5. FAŁSZ — superpozycja wymaga liniowości, a \( R_N \) jest nieliniowy.
- 6. FAŁSZ — lewy dwójnik zawiera źródła \( J \) i \( E \) — nie jest opisywany samym prawem Ohma.

---

## C. Napięcie U na źródle prądowym (1 p.)

**Odpowiedź: 1 — zależy od wartości wszystkich elementów układu**

Topologia: \( R_1 \) (lewa gałąź pionowa), źródło \( E \) (poziomo, górny lewy odcinek), źródło prądowe \( J_1 \) (środkowa gałąź pionowa), źródło prądowe \( J_2 \) (poziomo, górny prawy odcinek), \( R_2 \) (prawa gałąź pionowa); dolna szyna wspólna. Napięcie \( U \) jest oznaczone na **poziomym** źródle prądowym (strzałka \( U \) pod tą gałęzią — w treści pytania omyłkowo nazwano je \( J_1 \); gdyby \( U \) było na pionowym źródle, nie zależałoby od \( R_2 \) i odpowiedź 5 byłaby prawdziwa, a klucz jej nie zaznacza).

Rachunek (KCL):
- węzeł prawy: przez \( R_2 \) płynie cały prąd \( J_2 \): \( \varphi_{N3} = J_2 R_2 \);
- węzeł środkowy: \( \varphi_{N2} = E + R_1(J_1 + J_2) \) (prąd \( J_1 \) wpływa, \( J_2 \) wypływa w prawo, lewa gałąź \( R_1E \) odbiera).

\[
U = \varphi_{N2} - \varphi_{N3} = E + R_1(J_1 + J_2) - J_2 R_2
\]

Widać **wszystkie** elementy: \( E \), \( R_1 \), \( R_2 \), \( J_1 \), \( J_2 \) → odpowiedź 1 prawdziwa, a odpowiedzi 4 („nie zależy od J2") i 5 („nie zależy od R2") fałszywe. \( U \neq 0 \) i nie zależy „tylko od E".

---

## D. Napięcie U — wzmacniacz operacyjny (1 p.)

**Odpowiedź: 1 — \( E \)**

Układ: wejście nieodwracające (+) zasilane ze źródła \( E \) przez opór \( R \) (brak prądu wejściowego → \( u_+ = E \)); wyjście wzmacniacza przez opór szeregowy \( R \) do węzła X; węzeł X połączony oporem sprzężenia zwrotnego \( R \) z wejściem odwracającym (−) oraz oporem \( R \) do masy; \( U \) to napięcie na tym oporze do masy, czyli \( u_X \).

Krok 1 — idealny wzmacniacz ze sprzężeniem zwrotnym ujemnym:

\[
u_- = u_+ = E
\]

Krok 2 — prąd wejściowy \( i_- = 0 \), więc na oporze sprzężenia zwrotnego nie ma spadku:

\[
u_X = u_- = E
\]

Krok 3 — \( U = u_X = E \).

**Kontrola:** cała konfiguracja to wzmocnienie 1 (powtarzacz): prąd płynący przez opór do masy (\( E/R \)) dostarcza wyjście przez opór szeregowy — napięcie wyjścia wzmacniacza wynosi \( 2E \), ale na zaciskach \( U = E \). Założenie \( R > 0 \) skończone zapewnia poprawną pracę.

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — \( 1\ \text{A} \)**

Figura: dwa obszary (dwójniki wieloterminalowe) połączone przewodami; prądy wymuszone \( 2\ \text{A} \) i \( 3\ \text{A} \) doprowadzone **z przeciwnych stron** (patrz groty — jeden prąd wpływa do rozpatrywanego węzła, drugi z niego wypływa), a \( I \) płynie gałęzią poprzeczną.

Bilans węzła (PPK) daje **różnicę**, nie sumę:

\[
I = 3\ \text{A} - 2\ \text{A} = 1\ \text{A}
\]

**Pułapka (z kompendium §7.3):** sumę \( 2+3 = 5\ \text{A} \) (odpowiedź 2) dostaje się tylko wtedy, gdyby oba prądy wpływały do tego samego węzła. Odpowiedź „różnica czy suma?" zawsze dają kierunki grotów — jeden węzeł, jedno równanie KCL.

---

## F. Superpozycja — składowa prądu I od źródła J1 (1 p.)

**Odpowiedź: 1 — \( J_1\dfrac{R_2}{R_1+R_2} \)**

Topologia: \( J_1 \) (skrajna lewa gałąź, **grot w dół**) i \( R_1 \) połączone u góry przewodem (wspólny węzeł N), z N przez \( R_2 \) do węzła nad \( E \), dalej \( J_2 \) (obie gałązie pionowe przy \( E \)); \( I \) jest zaznaczony na odcinku nad \( R_1 \) ze strzałką **w górę** (prąd płynący do N).

Zasada superpozycji — tylko składowa od \( J_1 \):
- \( E \to \) zwarcie,
- \( J_2 \to \) rozwarcie.

Pozostaje: źródło \( J_1 \) (grot w dół — **pobiera** prąd z węzła N) zasila równoległe \( R_1 \) i \( R_2 \) (przez zwarte \( E \) do masy). Napięcie węzła:

\[
u_N\left(\tfrac{1}{R_1}+\tfrac{1}{R_2}\right) = -J_1
\quad\Rightarrow\quad
u_N = -J_1\frac{R_1 R_2}{R_1+R_2}
\]

Prąd przez \( R_1 \) płynie **od masy do węzła N** (w górę), czyli zgodnie ze strzałką \( I \):

\[
I = \frac{0 - u_N}{R_1} = J_1\frac{R_2}{R_1+R_2}
\]

**Kontrola:** to klasyczny dzielnik prądowy — prąd \( J_1 \) rozdziela się odwrotnie proporcjonalnie do oporów: przez \( R_1 \) płynie część \( \frac{R_2}{R_1+R_2} \), przez \( R_2 \) część \( \frac{R_1}{R_1+R_2} \) (odpowiedź 2). Grot \( J_1 \) w dół odwraca kierunki prądów w obu oporach — dzięki temu \( I > 0 \). W wyniku nie ma śladu \( E \) ani \( J_2 \) ✓.

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( \dfrac{4}{3}\ \text{mW} \)**

Topologia: idealne źródło \( 4\ \text{V} \) równolegle z \( 6\ \text{k}\Omega \), dalej \( 3\ \text{k}\Omega \) szeregowo do zacisku A; obciążenie \( R \) między A i B.

Krok 1 — Thévenin od strony zacisków A-B (bez \( R \)):

**Napięcie rozwarcia:** brak prądu przez \( 3\ \text{k}\Omega \), źródło narzuca węzeł:

\[
U_{oc} = 4\ \text{V}
\]

**Opór wewnętrzny:** źródło \( 4\ \text{V} \) zastępujemy zwarciem — ale zwarcie **zawiera również równoległe \( 6\ \text{k}\Omega \)** (\( 6\ \text{k}\Omega \parallel 0 = 0 \)):

\[
R_T = 3\ \text{k}\Omega
\]

**Pułapka:** błędem jest liczyć \( R_T = 6\ \text{k} + 3\ \text{k} = 9\ \text{k}\Omega \) (wtedy wyszłoby \( \frac{4}{9}\ \text{mW} \), odpowiedź 2). Opór równoległy do idealnego źródła napięciowego nigdy nie wnosi oporu zastępczego.

Krok 2 — moc maksymalna przy \( R = R_T = 3\ \text{k}\Omega \):

\[
P_{max} = \frac{U_{oc}^2}{4 R_T} = \frac{16}{4 \cdot 3\,000} = \frac{4}{3}\ \text{mW}
\]

**Kontrola:** przy dopasowaniu prąd \( 4\text{V}/6\text{k}\Omega = 0{,}667\ \text{mA} \), moc \( I^2 R = 0{,}444 \cdot 3 = 1{,}33\ \text{mW} \) ✓.

---

## H. Charakterystyka dwójnika AB z diodą idealną (1 p.)

**Odpowiedź: 1 — wykres 1**

Dwójnik AB: gałąź górna — dioda idealna \( D \) (kierunek przewodzenia od B do A), źródło \( 1\ \text{V} \) i \( 1\ \text{k}\Omega \) szeregowo; gałąź dolna — źródło prądowe \( 1\ \text{mA} \) (grot od A do B). \( u = V_A - V_B \), \( i \) wpływa do A.

Dwa stany diody (metoda z kompendium §4):

**Stan 1 — dioda zaporowa (u ≥ −1 V):** przez gałąź górną nie płynie prąd, cały prąd daje źródło \( 1\ \text{mA} \):

\[
i = 1\ \text{mA}
\]

**Stan 2 — dioda przewodzi (u ≤ −1 V):** gałąź górna to \( 1\ \text{k}\Omega \) z przesunięciem \( 1\ \text{V} \): \( i_{g} = \frac{u+1}{1\ \text{k}\Omega} \). Prąd węzłowy:

\[
i = \frac{u+1}{1\ \text{k}\Omega} + 1\ \text{mA} = \frac{u}{1\ \text{k}\Omega} + 2\ \text{mA}
\]

(prosta o nachyleniu \( 1\ \text{mA/V} \), przecina oś prądów w \( u = -2\ \text{V} \)).

Charakterystyka: **pozioma \( i = 1\ \text{mA} \) dla \( u \geq -1 \), prosta przez punkty \( (-2,\,0) \) i \( (-1,\,1\ \text{mA}) \) dla \( u \leq -1 \)** — załamanie w punkcie \( (-1\ \text{V},\,1\ \text{mA}) \). To dokładnie **wykres 1**.

**Kontrola (dwa punkty):** dla \( u = 0 \): \( i = 1\ \text{mA} \); dla \( u = -2\ \text{V} \): \( i = 0 \). Żaden inny wykres nie przechodzi przez oba te punkty:
- wykres 3: załamanie w \( (0,\,1\ \text{mA}) \) i rosnąca prosta na prawo — nie przechodzi przez \( (-2,\,0) \);
- wykresy 4 i 5: pionowe odcinki (idealne źródło napięciowe) — nasz dwójnik ma skończone nachylenie \( 1\ \text{mA/V} \);
- wykres 2: malejąca prosta i \( i = 0 \) dla \( u > 1 \) — niezgodne z izotropowym \( 1\ \text{mA} \).

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( \frac{R}{1-k} \) | \( u = ku + iR \Rightarrow u(1-k)=iR \); dla \( k=0 \): \( R \) |
| B | 1, 2 | lewy liniowy ⇒ Norton; prawy = element równoważny; RN ⇒ brak superpozycji |
| C | 1 | \( U = E + R_1(J_1+J_2) - J_2 R_2 \) — wszystkie elementy |
| D | \( E \) | powtarzacz: \( u_+ = E \), brak prądu w sprzężeniu ⇒ \( U = E \) |
| E | \( 1\ \text{A} \) | KCL: \( 3 - 2 \); groty przeciwne ⇒ różnica, nie suma |
| F | \( J_1\frac{R_2}{R_1+R_2} \) | dzielnik prądowy; grot \( J_1 \) w dół ⇒ prądy w górę |
| G | \( \frac{4}{3}\ \text{mW} \) | \( U_{oc}=4\ \text{V} \), \( R_T=3\ \text{k}\Omega \) (zwarcie źródła zwiera \( 6\ \text{k}\Omega \)) |
| H | wykres 1 | punkty \( (0,\,1\ \text{mA}) \) i \( (-2\ \text{V},\,0) \); załamanie w \( (-1,\,1\ \text{mA}) \) |
