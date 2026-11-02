# PELP1 — Test 1, wariant A_1 (8.11.2023) — rozwiązania

**Plik źródłowy:** [`PELP1_23Z_A_1_klucz.pdf`](../PELP1_23Z_A_1_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 1, 2 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( \dfrac{1}{g} \)**

Dwójnik AB: **szeregowe** połączenie rezystora \( R \) i źródła prądowego sterowanego napięciem (VCCS) o wartości \( g u \) (romb, grot w dół), gdzie \( u \) to napięcie na zaciskach AB.

W gałęzi szeregowej płynie wszędzie ten sam prąd — a źródło prądowe **wymusza** wartość tego prądu:

\[
i = g\,u
\]

(niezależnie od tego, jaki jest opór \( R \) — napięcie na \( R \) „dopasuje się"). Stąd:

\[
R_{AB} = \frac{u}{i} = \frac{1}{g}
\]

**Kontrola:** opór \( R \) w ogóle nie występuje w wyniku — szeregowe idealne źródło prądowe narzuca prąd gałęzi, więc reszta gałęzi jest nieistotna. Gdyby grot źródła był przeciwnie, wyszłoby \( -1/g \) (odpowiedź 2).

---

## B. Układ z oporem nieliniowym RN (1 p.)

**Odpowiedzi: 1 i 2**

Układ: po lewej stronie zacisków AB źródło \( E_1 \), z którego wychodzą **dwie równoległe gałęzie** do węzła A: górna z samym \( R \) (płynie nią prąd \( I \)) i środkowa z \( E_2 \) szeregowo z \( R \); po prawej stronie sam opór nieliniowy \( R_N \) między A i B.

- **1. PRAWDA** — prądowe prawo Kirchhoffa to aksjomat topologii obwodu; obowiązuje zawsze, także przy elementach nieliniowych.
- **2. PRAWDA** — dwójnik po lewej stronie (\( E_1 \) z gałęziami \( R \) oraz \( E_2 + R \)) jest **liniowy** — można go zastąpić równoważnym źródłem Nortona.
- 3. FAŁSZ — zasada superpozycji wymaga obwodu liniowego; \( R_N \) ją unieważnia.
- 4. FAŁSZ — \( R_N \) z definicji nie spełnia prawa Ohma.
- 5. FAŁSZ — prąd \( I \) w gałęzi górnej nie wynika z dzielnika prądowego: gałęzie równoległe nie są jednakowe (jedna zawiera \( E_2 \)), a układ zasilany jest źródłem **napięciowym** \( E_1 \), którego prąd wyjściowy nie jest znany z góry (zależy od nieliniowego \( R_N \)). Dzielnik prądowy dotyczy podziału znanego prądu na jednakowe w budowie gałęzie rezystancyjne.
- 6. FAŁSZ — zasada Tellegena (bilans mocy) obowiązuje w każdym obwodzie.

---

## C. Napięcie U (1 p.)

**Odpowiedzi: 1 i 2**

Topologia: \( R_1 \) równolegle z idealnym źródłem \( E \) (lewa część), dalej \( R_2 \) w gałęzi poziomej do węzła nad źródłem prądowym \( J \) (prawa gałąź pionowa); \( U \) to napięcie na źródle prądowym \( J \).

Krok 1 — idealne źródło napięciowe \( E \) narzuca potencjał węzła po lewej stronie \( R_2 \):

\[
\varphi_{N1} = E \quad\Rightarrow\quad R_1 \text{ nie ma wpływu}
\]

Krok 2 — KCL w węźle nad \( J \): przez \( R_2 \) płynie cały prąd \( J \):

\[
U = \varphi_{N2} = \varphi_{N1} - J R_2 = E - J R_2
\]

Wnioski:
- \( U \) **zależy od E** — odpowiedź 1 prawdziwa;
- \( U \) **nie zależy od R1** — odpowiedź 2 prawdziwa;
- \( U \neq 0 \) (3 fałszywa), \( U \) **zależy od R2** (4 fałszywa), nie zależy od „wszystkich elementów", bo pomijamy \( R_1 \) (5 fałszywa), jest określone (6 fałszywa).

---

## D. Napięcie U — wzmacniacz operacyjny (1 p.)

**Odpowiedź: 1 — \( 2E \)**

Układ: wzmacniacz nieodwracający — wejście (+) zasilane ze źródła \( E \); wejście (−) połączone oporem \( R \) do masy i oporem \( R \) do wyjścia (sprzężenie zwrotne); \( U \) to napięcie wyjściowe (na obciążeniu \( R \) do masy).

Wzmacniacz idealny ze sprzężeniem zwrotnym ujemnym:

\[
u_- = u_+ = E
\]

Dzielnik na wejściu odwracającym: napięcie \( u_- \) to część napięcia wyjściowego:

\[
u_- = u_w \frac{R}{R+R} = \frac{u_w}{2}
\]

Stąd:

\[
\frac{u_w}{2} = E \quad\Rightarrow\quad U = u_w = 2E
\]

To klasyczny nieodwracający wzmacniacz o wzmocnieniu \( 1 + R/R = 2 \).

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — układ jest sprzeczny**

Figura: dwa wymuszone prądy \( 1\ \text{A} \) i \( 2\ \text{A} \) (źródła idealne — wydajność wymuszona z zewnątrz) spotykają się w węźle, który **nie ma innego wyjścia** poza przewodem z prądem \( I \).

Bilans węzła:

\[
1\ \text{A} + 2\ \text{A} = 0 \quad\text{— niemożliwe}
\]

Prąd \( I \) nie ma jak „odpłynąć" — oba źródła są idealne, a węzeł nie ma trzeciego przewodu, który mógłby przejąć różnicę. **Taki obwód nie istnieje fizycznie.**

**Jak rozpoznać wariant „sprzeczny" (kompendium, trzy sygnały):**
1. suma prądów wymuszonych w węźle nie może dać zera (tu \( 1+2 = 3 \neq 0 \));
2. dwa idealne źródła napięciowe o różnych SEM połączone równolegle (sprzeczność z NPK);
3. dwa idealne źródła prądowe o różnych prądach połączone szeregowo (sprzeczność z PPK).

Kolejność działania na teście: najpierw bilans (5 sekund), potem rachunek. Jeśli bilans jest sprzeczny, żadna liczba w odpowiedziach nie jest prawidłowa.

---

## F. Superpozycja — składowa prądu I od źródła J1 (1 p.)

**Odpowiedź: 1 — \( -J_1\dfrac{R_1}{R_1+R_2} \)**

Topologia: \( J_1 \) (grot **w dół**) równolegle z \( R_1 \); z tego węzła przez \( R_2 \) do węzła nad źródłem \( E \), a dalej \( J_2 \) (obie gałęzie pionowe); \( I \) to prąd w gałęzi \( E \) ze strzałką **w dół**.

Zasada superpozycji — tylko składowa od \( J_1 \):
- \( E \to \) zwarcie,
- \( J_2 \to \) rozwarcie.

Pozostaje: \( J_1 \) (grot w dół — pobiera prąd z węzła \( N \)) zasila równoległe \( R_1 \) i \( R_2 \) (przez zwarte \( E \) do masy). Napięcie węzła:

\[
u_N = -J_1\frac{R_1 R_2}{R_1+R_2}
\]

Prąd \( I \) płynie od węzła \( N \) przez \( R_2 \) i w dół przez gałąź (zwartego) \( E \):

\[
I = \frac{u_N}{R_2} = -J_1\frac{R_1}{R_1+R_2}
\]

**Kontrolka:** to dzielnik prądowy — prąd \( J_1 \) dzieli się między \( R_1 \) i \( R_2 \); przez \( R_2 \) (a więc i przez gałąź \( E \)) płynie część \( \frac{R_1}{R_1+R_2} \). Grot \( J_1 \) w dół odwraca znak. W wyniku nie ma \( E \) ani \( J_2 \) ✓.

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( \dfrac{3}{10}\ \text{mW} = 0{,}3\ \text{mW} \)**

Topologia: oczko złożone ze źródła \( 3\ \text{V} \) (dolna gałąź), oporu \( 3\ \text{k}\Omega \) (górna gałąź) i oporu \( 2\ \text{k}\Omega \) (gałąź pionowa w środku); zaciski A (góra) i B (dół) po prawej stronie, obciążenie \( R \) między A i B — równolegle do \( 2\ \text{k}\Omega \).

Krok 1 — Thévenin od strony zacisków A-B (bez \( R \)):

**Napięcie rozwarcia:** w oczku płynie prąd (oczeko jest domknięte przez \( 3\,\text{k} \), \( 2\,\text{k} \) i źródło):

\[
i = \frac{3\ \text{V}}{3\ \text{k} + 2\ \text{k}} = 0{,}6\ \text{mA}
\]

Napięcie \( U_{oc} \) to spadek na \( 2\ \text{k}\Omega \) (bo zaciski A-B obejmują właśnie tę gałąź):

\[
U_{oc} = 0{,}6\ \text{mA} \cdot 2\ \text{k}\Omega = 1{,}2\ \text{V}
\]

**Opór wewnętrzny:** źródło \( 3\ \text{V} \) zastępujemy zwarciem; patrząc w port A-B widzimy \( 2\ \text{k}\Omega \) równolegle z \( (3\ \text{k}\Omega + 0) \):

\[
R_T = 2\ \text{k} \parallel 3\ \text{k} = \frac{2 \cdot 3}{2+3} = 1{,}2\ \text{k}\Omega
\]

Krok 2 — moc maksymalna przy \( R = R_T \):

\[
P_{max} = \frac{U_{oc}^2}{4 R_T} = \frac{1{,}44}{4 \cdot 1{,}2\ \text{k}} = \frac{1{,}44}{4{,}8\ \text{k}} = 0{,}3\ \text{mW} = \frac{3}{10}\ \text{mW}
\]

**Kontrola:** przy dopasowaniu \( R = 1{,}2\ \text{k}\Omega \) prąd \( 1{,}2/2{,}4 = 0{,}5\ \text{mA} \), moc \( 0{,}5^2 \cdot 1{,}2\ \text{k} = 0{,}3\ \text{mW} \) ✓.

---

## H. Dwójnik bezźródłowy (1 p.)

**Odpowiedzi klucza: 1 i 2 — ale patrz uwaga poniżej**

Pięć dwójników (każdy między zaciskami):
1. opór \( R \) równolegle ze źródłem sterowanym \( ku \) (sterowanie napięciem \( u \) na zaciskach),
2. źródło prądowe z diodą \( D \) i elementem \( E > 0 \),
3. źródło \( E > 0 \) z diodą \( D \) w gałęzi równoległej,
4. źródło sterowane \( ri \) ze źródłem \( E > 0 \),
5. źródło \( E > 0 \) równolegle z diodą \( D \),
6. „żaden nie jest bezźródłowy".

**Definicja** (kompendium §4.3): dwójnik bezźródłowy (bierny) nie zawiera **żadnego** źródła — ani niezależnego (\( E \), \( J \)), ani sterowanego (\( ku \), \( gu \), \( ri \), \( \beta i \)). W każdym z pięciu rysunków jest źródło → definicyjnie poprawna byłaby odpowiedź **6**.

**Klucz zaznacza jednak 1 i 2** — to znana niespójność w tej rodzinie zadań (identyczna w 20L_A_1·G, 22Z_A_1·H i 25Z_A_2·H). Kryterium „charakterystyka \( i(u) \) przechodzi przez początek układu" uzasadnia dwójnik 1: przy \( u = 0 \) źródło \( ku \) daje zero, więc \( i = 0 \). Dla dwójnika 2 (źródło prądowe z \( E > 0 \)) charakterystyka jest przesunięta — klucz prawdopodobnie bierze poprawkę na inną wersję rysunku w oryginalnym teście.

**Praktyczna wskazówka z kompendium:** czytaj obrazki, nie numerację; w tej rodzinie kluczy są niejednoznaczności, które trzeba znać, a nie „naprawiać".

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( \frac{1}{g} \) | źródło prądowe szeregowo: \( i = gu \Rightarrow u/i = 1/g \); \( R \) nieistotne |
| B | 1, 2 | KCL i Tellegen zawsze; lewy liniowy ⇒ Norton; brak dzielnika (gałęzie różne, źródło napięciowe) |
| C | 1, 2 | \( U = E - J R_2 \) — jest E, nie ma \( R_1 \) |
| D | \( 2E \) | nieodwracający: \( 1 + R/R = 2 \) |
| E | sprzeczny | bilans \( 1 + 2 = 0 \) niemożliwy; brak trzeciego przewodu |
| F | \( -J_1\frac{R_1}{R_1+R_2} \) | dzielnik; grot \( J_1 \) w dół ⇒ znak ujemny; bez \( E \), \( J_2 \) |
| G | \( \frac{3}{10}\ \text{mW} \) | \( U_{oc} = 1{,}2\ \text{V} \) (dzielnik \( 3\cdot\frac{2}{5} \)), \( R_T = 2\text{k}\parallel3\text{k} = 1{,}2\ \text{k}\Omega \) |
| H | 1, 2 | definicja ⇒ 6; kryterium zera ⇒ 1; znana niespójność klucza |
