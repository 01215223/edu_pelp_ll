# PELP1 — Test 1 poprawkowy, wariant A_2 (20.12.2023) — rozwiązania

**Plik źródłowy:** [`PELP1_23Z_A_2_klucz.pdf`](../PELP1_23Z_A_2_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 1 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( R - r \)**

Dwójnik AB: **szeregowe** połączenie rezystora \( R \) i źródła napięciowego sterowanego prądem (CCVS) o wartości \( r i \) (romb, grot w dół), gdzie \( i \) to prąd portu wpływający do A (płynie przez \( R \), następnie w dół przez źródło do B).

Grot źródła skierowany w dół — biegun **+ od strony B**: idąc wzdłuż prądu (od A przez \( R \) w dół przez źródło do B), spadek na \( R \) to \( i R \), a źródło **podnosi** potencjał o \( r i \):

\[
u = i\,R - r\,i = i\,(R - r)
\]

Stąd:

\[
R_{AB} = \frac{u}{i} = R - r
\]

**Kontrola:** gdyby grot źródła był przeciwnie (+ od strony A), źródło działałoby zgodnie z prądem i wyszłoby \( R + r \) (odpowiedź 2). Gdyby źródło zastąpić zwarciem (\( r = 0 \)), zostaje samo \( R \) ✓.

---

## B. Układ z oporem nieliniowym RN (1 p.)

**Odpowiedzi: 1 i 2**

Układ: po lewej stronie \( E_1 \), z którego wychodzą **dwie równoległe gałęzie** do węzła A: z oporem \( R \) (płynie nią prąd \( I \)) i z oporem nieliniowym \( R_N \); po prawej stronie źródło \( E_2 \) między A a dolną szyną.

- **1. PRAWDA** — zasada Tellegena (bilans mocy) wynika z praw Kirchhoffa i obowiązuje w każdym obwodzie, także nieliniowym.
- **2. PRAWDA** — połączenie równoległe \( R \) i \( R_N \) można z punktu widzenia zacisków zastąpić **jednym oporem zastępczym nieliniowym**: ich charakterystyki się sumują (\( i(u) = u/R + i_{RN}(u) \)) — to poprawne pojęcie, nie mylić z prawem Ohma.
- 3. FAŁSZ — superpozycja wymaga liniowości; \( R_N \) ją unieważnia.
- 4. FAŁSZ — \( R_N \) nie spełnia prawa Ohma (dlatego odpowiedź 2 mówi o „oporze zastępczym nieliniowym", a nie o zwykłym oporze).
- 5. FAŁSZ — dzielnik prądowy dotyczy podziału znanego prądu na **jednakowe, liniowe** gałęzie rezystancyjne; tu jedna gałąź jest nieliniowa, a układ zasilany jest źródłem napięciowym \( E_1 \) (prąd źródła nie jest znany z góry).
- 6. FAŁSZ — napięciowe prawo Kirchhoffa (oczkowe) obowiązuje zawsze — jest sumą spadków napięć po oczku.

---

## C. Prąd I — bramka prądowa (1 p.)

**Odpowiedzi: 1 i 2**

Topologia: \( R_1 \) (lewa gałąź pionowa) równolegle ze źródłem \( E \) (środkowa gałąź, z prądem \( I \) wypływającym z niego do górnego węzła), \( R_2 \) w gałęzi poziomej, źródło prądowe \( J \) (prawa gałąź pionowa, grot w górę).

Krok 1 — źródło \( E \) narzuca potencjał górnego węzła: \( \varphi_{N1} = E \), więc prąd przez \( R_1 \) to zawsze \( E/R_1 \).

Krok 2 — KCL w prawym węźle: źródło \( J \) (grot w górę) wtłacza prąd \( J \) do węzła; ten prąd **musi** popłynąć przez \( R_2 \) do węzła środkowego (bramka prądowa) — niezależnie od wartości \( R_2 \).

Krok 3 — KCL w węźle środkowym:

\[
\underbrace{I}_{\text{z gałęzi } E} + \underbrace{J}_{\text{przez } R_2} = \frac{E}{R_1}
\quad\Rightarrow\quad
I = \frac{E}{R_1} - J
\]

Wnioski:
- \( I \) **nie zależy od R2** — odpowiedź 1 prawdziwa (to esencja bramki prądowej: prąd źródła prądowego jest wymuszony, \( R_2 \) zmienia tylko napięcie);
- \( I \) **zależy od J** — odpowiedź 2 prawdziwa;
- \( I \neq 0 \) (3 fałszywa), nie zależy od wszystkich elementów — nie ma w nim \( R_2 \) (4 fałszywa), zależy od E i \( R_1 \) (5 fałszywa), jest w pełni określone (6 fałszywa).

**Wskazówka z kompendium §7.4:** „bramka prądowa" = źródło prądowe zawsze wygrywa z oporem w swojej gałęzi — żadna wartość \( R_2 \) nie zmieni prądu \( J \), a więc i bilansu węzła.

---

## D. Napięcie U — wzmacniacz operacyjny (1 p.)

**Odpowiedź: 1 — \( E \)**

Układ: wejście (+) zasilane ze źródła \( E \); wejście (−) połączone oporem \( R \) z **zaciskiem wyjściowym** (sprzężenie zwrotne); wyjście wzmacniacza przez opór szeregowy \( R \) do węzła X, a węzeł X dodatkowo oporem \( R \) do masy; \( U \) to napięcie na zacisku X.

Krok 1 — idealny wzmacniacz ze sprzężeniem zwrotnym ujemnym:

\[
u_- = u_+ = E
\]

Krok 2 — prąd wejściowy \( i_- = 0 \), więc na oporze sprzężenia zwrotnego nie ma spadku — napięcie na zacisku X równa się napięciu na wejściu (−):

\[
u_X = u_- = E \quad\Rightarrow\quad U = E
\]

**Kontrola:** to powtarzacz (wzmocnienie 1). Prąd płynący przez opór do masy (\( E/R \)) dostarcza wyjście wzmacniacza przez opór szeregowy — na jego drodze nie ma spadku wpływu na \( U \). Opory w tym układzie nie mają wpływu na wynik — jest ich po prostu „za dużo".

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — \( -2\ \text{A} \)**

Figura: trzy obszary (górny, dolny-lewy, dolny-prawy) połączone przez **węzeł centralny**. Gałęzie:
- dolny-lewy → górny: \( 1\ \text{A} \),
- górny → dolny-prawy: \( 2\ \text{A} \),
- dolny-prawy → węzeł centralny: \( 3\ \text{A} \),
- dolny-lewy → węzeł centralny: \( I \),
- węzeł centralny → górny: bez etykiety,
- dolny-lewy ↔ dolny-prawy (poziomo): bez etykiety.

Krok 1 — KCL w węźle górnym: dopływa \( 1\ \text{A} \) z dolnego-lewego i prąd \( x \) z węzła centralnego, wypływa \( 2\ \text{A} \):

\[
1 + x = 2 \quad\Rightarrow\quad x = 1\ \text{A}
\]

Krok 2 — KCL w węźle centralnym: dopływają \( I \) i \( 3\ \text{A} \), wypływa \( x = 1\ \text{A} \):

\[
I + 3 = 1 \quad\Rightarrow\quad I = -2\ \text{A}
\]

Ujemny znak: prąd \( I \) faktycznie płynie **do** węzła centralnego (wbrew narysowanej strzałce).

**Kontrola (KCL w dolnym-lewym):** wypływa \( 1\ \text{A} \) (góra) \( + I \) (węzeł) \( + 1\ \text{A} \) (poziomo — wynika z bilansu dolnego-prawego: \( 2 + I_{poziom} = 3 \)) — a \( I = -2 \): \( 1 - 2 + 1 = 0 \) ✓.

---

## F. Superpozycja — składowa prądu I od źródła E2 (1 p.)

**Odpowiedź: 1 — \( E_2\dfrac{R_1+R_2}{R_1 R_2} \)**

Topologia: gałąź 1 (skrajna lewa): \( E_1 \); gałąź 2: \( E_2 \) (grot w dół) z prądem \( I \) (strzałka w dół, nad źródłem); gałąź 3: \( R_2 \) pionowo; gałąź 4 (skrajna prawa): \( J \); w górnym przewodzie między gałęziami 1 i 2 — opór \( R_1 \).

Zasada superpozycji — tylko składowa od \( E_2 \):
- \( E_1 \to \) zwarcie,
- \( J \to \) rozwarcie.

Pozostaje: źródło \( E_2 \) z górnym węzłem, do którego \( R_1 \) (przez zwarte \( E_1 \)) i \( R_2 \) łączą się z masą — czyli \( R_1 \parallel R_2 \) jako obciążenie źródła \( E_2 \). Prąd płynący w dół przez źródło \( E_2 \):

\[
I = \frac{E_2}{R_1 \parallel R_2} = E_2\left(\frac{1}{R_1} + \frac{1}{R_2}\right) = E_2\frac{R_1+R_2}{R_1 R_2}
\]

**Kontrola:** zsumowanie konduktancji to znak, że dwa opory są równolegle. W wyniku nie ma śladu \( E_1 \) ani \( J \) ✓. Odpowiedź 4 (\( E_2 \frac{R_1 R_2}{R_1+R_2} \)) to błąd „przecinkowy" — pomnożenie zamiast podzielenia przez opór równoważny.

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( 16\ \text{mW} \)**

Topologia: w górnym przewodzie źródło prądowe \( 4\ \text{mA} \) (grot w prawo); \( 1\ \text{k}\Omega \) — skrajna lewa gałąź pionowa; \( 4\ \text{k}\Omega \) — środkowa gałąź pionowa; zaciski A (góra, po prawej) i B (dół), obciążenie \( R \) między nimi.

Krok 1 — Thévenin od strony zacisków A-B (bez \( R \)):

**Napięcie rozwarcia:** obwód przerowany w A — cały prąd źródła \( 4\ \text{mA} \) płynie przez \( 4\ \text{k}\Omega \) (jedyna droga):

\[
U_{oc} = 4\ \text{mA} \cdot 4\ \text{k}\Omega = 16\ \text{V}
\]

(Opór \( 1\ \text{k}\Omega \) to pułapka-deko­racja: ustawia tylko potencjał węzła po lewej, nie wpływa ani na \( U_{oc} \), ani na \( R_T \).)

**Opór wewnętrzny:** źródło prądowe rozwieramy — górny przewód między \( 1\ \text{k}\Omega \) a \( 4\ \text{k}\Omega \) zostaje przerwany, więc z portu A-B widać wyłącznie \( 4\ \text{k}\Omega \):

\[
R_T = 4\ \text{k}\Omega
\]

Krok 2 — moc maksymalna przy \( R = R_T \):

\[
P_{max} = \frac{U_{oc}^2}{4 R_T} = \frac{16^2}{4 \cdot 4\ \text{k}} = \frac{256}{16\,000} = 16\ \text{mW}
\]

**Kontrola:** przy dopasowaniu \( R = 4\ \text{k}\Omega \) prąd \( 16/8\,000 = 2\ \text{mA} \), moc \( 2^2 \cdot 4 = 16\ \text{mW} \) ✓.

---

## H. Charakterystyka dwójnika AB z diodą idealną (1 p.)

**Odpowiedź: 1 — wykres 1**

Dwójnik AB: od zacisku A — źródło \( 1\ \text{V} \) (grot w prawo, czyli biegun + od strony bloku równoległego), potem **blok równoległy**: dioda idealna \( D \) (anoda od strony A, przewodzi w prawo) ∥ \( 1\ \text{k}\Omega \), do zacisku B. \( u = \varphi_A - \varphi_B \), \( i \) wpływa do A.

Ponieważ \( \varphi_M - \varphi_A = 1\ \text{V} \) (grot źródła od strony węzła M bloku):

\[
u = u_p - 1
\]

gdzie \( u_p \) to napięcie na bloku równoległym.

**Stan 1 — dioda przewodzi (u_p = 0):** cały prąd płynie diodą (na \( 1\ \text{k}\Omega \) zero), a napięcie portu jest **sztywno ustalone**:

\[
u = -1\ \text{V} \quad (\text{pionowa półprosta w górę dla } i \geq 0)
\]

**Stan 2 — dioda zaporowa (u_p < 0, czyli i < 0):** prąd płynie tylko przez \( 1\ \text{k}\Omega \): \( u_p = i \cdot 1\ \text{k}\Omega \), stąd:

\[
u = i \cdot 1\ \text{k}\Omega - 1
\quad\Rightarrow\quad
i = \frac{u + 1}{1\ \text{k}\Omega}
\]

prosta o nachyleniu \( 1\ \text{mA/V} \) przechodząca przez \( (-1\ \text{V},\,0) \), rozciągnięta w dół po lewej.

Charakterystyka: **prosta przez \( (-1,\,0) \) o nachyleniu \( 1\ \text{mA/V} \) dla \( u \leq -1 \) oraz pionowa półprosta w \( u = -1\ \text{V} \) skierowana w górę** — dokładnie **wykres 1**.

**Kontrola (dwa punkty):** \( i = 1\ \text{mA} \Rightarrow u = -1\ \text{V} \); \( i = -1\ \text{mA} \Rightarrow u = -2\ \text{V} \). Wykres 4 (pozioma dla \( u > -1 \)) odpowiadałby dwójnikowi **bez** równoległego \( 1\ \text{k}\Omega \); wykres 2 i 3 mają załamanie w \( u = +1 \) (odwrotna polaryzacja źródła); wykres 5 ma pion w \( u = 0 \) (dwójnik bez źródła).

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( R - r \) | \( u = iR - ri \); grot CCVS w dół ⇒ źródło przeciw prądowi |
| B | 1, 2 | Tellegen zawsze; \( R \parallel R_N \) = opór zastępczy nieliniowy; brak superpozycji/dzielnika/Ohma |
| C | 1, 2 | \( I = E/R_1 - J \) — bramka prądowa: bez \( R_2 \), z \( J \) |
| D | \( E \) | powtarzacz: \( u_+ = E \), brak prądu w sprzężeniu ⇒ \( U = E \) |
| E | \( -2\ \text{A} \) | górny: \( 1 + x = 2 \); centralny: \( I + 3 = 1 \) |
| F | \( E_2\frac{R_1+R_2}{R_1 R_2} \) | \( E_2 \) obciążone \( R_1 \parallel R_2 \) (suma konduktancji) |
| G | \( 16\ \text{mW} \) | \( U_{oc} = 4\,\text{mA} \cdot 4\,\text{k} = 16\ \text{V} \), \( R_T = 4\ \text{k}\Omega \); \( 1\ \text{k} \) to dekoracja |
| H | wykres 1 | pion w \( u = -1 \) (dioda przewodzi), prosta \( i = (u+1)/1\text{k} \) po lewej |
