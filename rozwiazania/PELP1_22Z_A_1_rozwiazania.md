# PELP1 — Test 1, wariant A_1 (16.11.2022) — rozwiązania

**Plik źródłowy:** [`PELP1_22Z_A_1_klucz.pdf`](../PELP1_22Z_A_1_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 1, 2 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( r \)**

Dwójnik AB składa się z rezystora \( R \) połączonego **równolegle** ze źródłem napięciowym sterowanym prądem (CCVS) o wartości \( r\cdot i \), przy czym prąd sterujący \( i \) to prąd wpływający do zacisku A.

Rozwiązanie: źródło sterowane \( r i \) jest źródłem **napięciowym** włączonym równolegle z \( R \), więc narzuca napięcie na zaciskach:

\[
u = r\, i
\]

Stąd opór zastępczy:

\[
R_{AB} = \frac{u}{i} = \frac{r\, i}{i} = r
\]

Rezystor \( R \) nie ma żadnego wpływu — równolegle do idealnego źródła napięciowego „nie widzi" on napięcia dwójnika (prąd źródła sterowanego dopasowuje się tak, by KCL było spełnione).

**Kontrola:** jednostki się zgadzają (\( r \) w omach), wynik nie zależy od \( i \), więc odpowiedź 6 („zależy od wartości prądu") odpada.

---

## B. Układ z oporem nieliniowym RN (1 p.)

**Odpowiedzi: 1 i 2**

Układ: po lewej stronie zacisków AB źródło prądowe \( J \) równolegle z oporem nieliniowym \( R_N \), w szeregu z \( E \); po prawej stronie dwa jednakowe opory \( R \) połączone równolegle; prąd \( I \) płynie przez prawy opór \( R \).

- **1. PRAWDA** — prąd wpływający do węzła A rozdziela się na dwa **jednakowe** równoległe opory \( R \), więc obowiązuje dzielnik prądowy: \( I = \frac{i_A}{2} \). Podział prądu między równoległe gałęzie to czysta KCL — nie wymaga liniowości elementów.
- **2. PRAWDA** — zasada superpozycji obowiązuje **wyłącznie w obwodach liniowych**; opór nieliniowy \( R_N \) ją unieważnia.
- 3. FAŁSZ — zasada Tellegena (bilans mocy) wynika z praw Kirchhoffa i obowiązuje w każdym obwodzie, także nieliniowym.
- 4. FAŁSZ — prądowe prawo Kirchhoffa to aksjomat topologii obwodu, zawsze prawdziwe.
- 5. FAŁSZ — dwójnik po lewej stronie zawiera element nieliniowy \( R_N \), więc nie da się go zastąpić źródłem Thevenina (liniowy dwójnik zastępczy wymaga liniowości).
- 6. FAŁSZ — \( R_N \) z definicji nie spełnia prawa Ohma.

---

## C. Napięcie U na źródle prądowym J2 (1 p.)

**Odpowiedzi: 1 i 2**

Topologia: gałęzie \( E \), \( R_1 \) i \( J_1 \) połączone **równolegle** między węzłem N1 a dolną szyną; z N1 przez \( R_2 \) do węzła N2, a z N2 przez \( J_2 \) do dolnej szyny. Napięcie \( U \) jest na \( J_2 \).

Krok 1 — potencjał N1: idealne źródło napięciowe \( E \) jest włączone równolegle do \( R_1 \) i \( J_1 \), więc **narzuca** potencjał węzła:

\[
\varphi_{N1} = E
\]

Opór \( R_1 \) i źródło \( J_1 \) nie mają na to wpływu (źródło napięciowe „wygrywa" z równoległymi elementami).

Krok 2 — KCL w węźle N2: przez \( J_2 \) płynie cały prąd z \( R_2 \):

\[
i_{R2} = J_2 \quad\Rightarrow\quad U = \varphi_{N2} = \varphi_{N1} - J_2 R_2 = E - J_2 R_2
\]

Wnioski:
- \( U \) **zależy od E** — odpowiedź 1 prawdziwa;
- \( U \) **nie zależy od J1** — odpowiedź 2 prawdziwa;
- nie zależy też od \( R_1 \) (odpowiedź 4 fałszywa), ale **zależy od R2** (odpowiedź 5 fałszywa); \( U \neq 0 \) (odpowiedź 3 fałszywa).

**Kontrola:** napięcie na źródle prądowym w ogóle nie zależy od samego źródła \( J_2 \)... uwaga: zależy tu od \( J_2 \) przez spadek na \( R_2 \) — ale pytanie dotyczyło \( J_1 \), więc rozumowanie się broni.

---

## D. Napięcie U — wzmacniacz operacyjny (1 p.)

**Odpowiedź: 1 — \( \dfrac{E}{2} \)**

Układ: dzielnik z dwóch jednakowych oporów \( R \) zasila wejście nieodwracające (+) wzmacniacza; sprzężenie zwrotne — jeden opór \( R \) od wyjścia do wejścia odwracającego (−), które nie ma innych połączeń; na wyjściu opór szeregowy \( R \) do rozwartych zacisków, na których mierzone jest \( U \).

Krok 1 — wejście (+): dzielnik napięcia z jednakowych oporów:

\[
u_+ = E \cdot \frac{R}{R+R} = \frac{E}{2}
\]

Krok 2 — wzmacniacz idealny ze sprzężeniem zwrotnym ujemnym:

\[
u_- = u_+ = \frac{E}{2}
\]

Krok 3 — prąd wejściowy idealnego wzmacniacza \( i_- = 0 \), więc na oporze sprzężenia zwrotnego nie ma spadku napięcia:

\[
u_{wyj} = u_- = \frac{E}{2}
\]

Krok 4 — zaciski wyjściowe są rozwarte (brak obciążenia), prąd przez szeregowy opór \( R \) nie płynie, więc:

\[
U = u_{wyj} = \frac{E}{2}
\]

Założenie \( R > 0 \) i skończone gwarantuje poprawną pracę dzielnika na wejściu.

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — \( -5\ \text{A} \)**

Figura przedstawia węzeł, do którego dopływają prądy \( 2\ \text{A} \) i \( 3\ \text{A} \), a prąd \( I \) jest zdefiniowany jako **dopływający** do węzła. Prawo Kirchhoffa:

\[
2 + 3 + I = 0 \quad\Rightarrow\quad I = -5\ \text{A}
\]

Ujemny znak oznacza, że faktycznie \( 5\ \text{A} \) **opuszcza** węzeł gałęzią \( I \).

**Uwaga (niespójność w kluczu):** na rysunku widnieje jeszcze gałąź z etykietą \( 1\ \text{A} \) bez grotu; przy wzięciu jej do bilansu suma \( 1+2+3 = 6\ \text{A} \) nie daje się pogodzić z odpowiedzią \( 5\ \text{A} \) (różnica zawsze parzysta). Kompendium ([`teoria/index.html`](../teoria/index.html), hasło „22Z_A_1, pytanie E") flaguje to jako niespójność klucza: w oryginalnym teście jeden z grotów był odwrócony albo etykieta inna. Samokontrola z kompendium: „jeśli suma różni się od odpowiedzi o wartość jednego z prądów — odwróć ten prąd, a nie całe równanie". Odpowiedź klucza: **−5 A**.

---

## F. Superpozycja — składowa prądu I od źródła J1 (1 p.)

**Odpowiedź: 1 — \( -J_1\dfrac{R_1}{R_1+R_2} \)**

(Uwaga: w kluczu jest odręczna poprawka — pytanie dotyczy składowej **prądu I**, nie napięcia U.)

Topologia: \( J_1 \) i \( R_1 \) równolegle w węźle N1, z N1 przez \( R_2 \) do węzła N2, w którym \( E \) i \( J_2 \) łączą się z dolną szyną. Prąd \( I \) płynie odcinkiem od \( R_1 \) do \( R_2 \) (grot w prawo). Grot źródła \( J_1 \) skierowany **w dół** — źródło pobiera prąd z węzła N1.

Zasada superpozycji — liczymy tylko składową od \( J_1 \):
- \( E \to \) zwarcie (idealne źródło napięciowe zerujemy zwarciem),
- \( J_2 \to \) rozwarcie (idealne źródło prądowe zerujemy rozwieraniem).

Pozostaje: \( J_1 \) równolegle z \( R_1 \) i \( R_2 \) (przez zwarty \( E \) na masę). KCL w N1:

\[
\frac{u_{N1}}{R_1} + \frac{u_{N1}}{R_2} = -J_1
\quad\Rightarrow\quad
u_{N1} = -J_1 \frac{R_1 R_2}{R_1+R_2}
\]

Prąd \( I \) (przez \( R_2 \), w prawo):

\[
I = \frac{u_{N1}}{R_2} = -J_1\frac{R_1}{R_1+R_2}
\]

**Kontrola:** gdyby grot \( J_1 \) wskazywał w górę, wyszłoby \( +J_1 R_1/(R_1+R_2) \) (odpowiedź 2) — grot w dół daje znak ujemny. Składowa od \( J_1 \) nie może zależeć od \( E \) ani \( J_2 \) — zgadza się, w wyniku ich nie ma.

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( \dfrac{4}{10}\ \text{mW} = 0{,}4\ \text{mW} \)**

Topologia: źródło prądowe \( 1\ \text{mA} \) (grot w dół) równolegle z \( 4\ \text{k}\Omega \), następnie \( 6\ \text{k}\Omega \) szeregowo do zacisku A; obciążenie \( R \) między A i B.

Krok 1 — Thévenin od strony zacisków A-B (bez \( R \)):

**Napięcie rozwarcia** (\( R \to \infty \)): prąd przez \( 6\ \text{k}\Omega \) nie płynie, więc cały prąd źródła (pobierany z górnego węzła) płynie przez \( 4\ \text{k}\Omega \):

\[
|U_{oc}| = 1\ \text{mA} \cdot 4\ \text{k}\Omega = 4\ \text{V}
\]

**Opór wewnętrzny** (źródło prądowe rozwieramy):

\[
R_T = 4\ \text{k}\Omega + 6\ \text{k}\Omega = 10\ \text{k}\Omega
\]

Krok 2 — moc maksymalna przy \( R = R_T \):

\[
P_{max} = \frac{U_{oc}^2}{4 R_T} = \frac{4^2}{4 \cdot 10\,000} = \frac{16}{40\,000}\ \text{W} = 0{,}4\ \text{mW} = \frac{4}{10}\ \text{mW}
\]

**Kontrola:** przy dopasowaniu \( R = 10\ \text{k}\Omega \) prąd obwodu \( 4\text{V}/20\text{k}\Omega = 0{,}2\ \text{mA} \), moc \( I^2 R = 0{,}04 \cdot 10 = 0{,}4\ \text{mW} \) ✓.

---

## H. Dwójnik bezźródłowy (1 p.)

**Odpowiedzi klucza: 1 i 2 — ale patrz uwaga poniżej**

Pięć dwójników:
1. opór \( R \) równolegle ze źródłem sterowanym \( ku \),
2. dioda \( D \) równolegle ze źródłem \( E > 0 \),
3. źródło równolegle z szeregowym \( R + E > 0 \),
4. dioda \( D \) równolegle ze źródłem \( E > 0 \),
5. źródło sterowane \( ri \) równolegle ze źródłem \( E > 0 \),
6. „żaden nie jest bezźródłowy".

**Definicja** (kompendium §4.3): dwójnik bezźródłowy (bierny) nie zawiera **żadnego** źródła — ani niezależnego (\( E \), \( J \)), ani sterowanego (\( ku \), \( gu \), \( ri \), \( \beta i \)). W każdym z pięciu rysunków jest źródło → definicyjnie poprawna byłaby odpowiedź **6**.

**Klucz zaznacza jednak 1 i 2.** To znana niespójność w tej rodzinie zadań (te same rysunki w 20L_A_1·G i 25Z_A_2·H). Kryterium „charakterystyka \( i(u) \) przechodzi przez początek układu" uzasadnia dwójnik 1: przy \( u = 0 \) źródło \( ku \) daje zero, więc \( i = 0 \). Dla dwójnika 2 (dioda ∥ \( E>0 \)) charakterystyka jest przesunięta — klucz prawdopodobnie bierze poprawkę na inną wersję rysunku w oryginalnym teście.

**Praktyczna wskazówka z kompendium:** czytaj obrazki, nie numerację; w tej rodzinie kluczy są niejednoznaczności, które trzeba znać, a nie „naprawiać".

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( r \) | \( u = ri \Rightarrow u/i = r \), niezależne od \( i \) |
| B | 1, 2 | dwa równe \( R \) ⇒ dzielnik; \( R_N \) ⇒ brak superpozycji i Thévenina |
| C | 1, 2 | \( U = E - J_2 R_2 \) — jest E, nie ma \( J_1 \) |
| D | \( E/2 \) | powtarzacz: \( u_+ = E/2 \), brak prądu ⇒ \( U = E/2 \) |
| E | \( -5\ \text{A} \) | KCL: \( 2+3+I=0 \); klucz flagowany w kompendium (1+2+3=6≠5) |
| F | \( -J_1\frac{R_1}{R_1+R_2} \) | grot \( J_1 \) w dół ⇒ znak ujemny; wynik bez \( E \), \( J_2 \) |
| G | \( \frac{4}{10}\ \text{mW} \) | \( U_{oc}=4\ \text{V} \), \( R_T=10\ \text{k}\Omega \), \( P=E_T^2/4R_T \) |
| H | 1, 2 | definicja ⇒ 6; kryterium zera ⇒ 1; znana niespójność klucza |
