# Test 1 PELP1 (04.11.2020, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_20Z_A_1_klucz.pdf`](../PELP1_20Z_A_1_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | Σ |
|---|---|---|---|---|---|---|---|---|
| Odp. | 1, 2, 3 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 9 pkt |

## A. Właściwości elementu skupionego (1 p.)

Element skupiony to wydzielony obszar, w którym oddziaływania
elektromagnetyczne opisujemy bez zmiennych przestrzennych. Prawdziwe są
**trzy** warunki definicyjne:

1. **pole magnetyczne wokół elementu jest w przybliżeniu stałe** ✔ — wymiary
   elementu są pomijalnie małe względem długości fali, więc opóźnienia
   rozchodzenia się oddziaływań w obrębie elementu pomijamy;
2. **pole elektryczne wokół elementu jest w przybliżeniu potencjalne** ✔ —
   napięcie między zaciskami jest jednoznacznie określone (niezależne od drogi);
3. **równania elementu nie zawierają zmiennych przestrzennych (x, y, z)** ✔ —
   wielkościami stanu są tylko prądy, napięcia, ładunki i strumienie.

Pozostałe opcje są błędne:

- 4 — pole magnetyczne nie musi być pomijalnie małe (cewka ma duże pole i jest
  elementem skupionym);
- 5 — ładunek może się gromadzić wewnątrz elementu (kondensator!); warunkiem
  jest tylko, by nie gromadził się w węzłach obwodu;
- 6 — pole elektryczne nie jest zerowe (element bez napięcia?); ma być
  **potencjalne**, a nie zerowe;
- 7 — równania elementu mogą zawierać czas (\(u = L\,di/dt\), \(i = C\,du/dt\));
  chodzi o brak zależności **przestrzennej**.

**Odpowiedź: 1, 2, 3.**

## B. Charakterystyka oporu nieliniowego (1 p.)

Opór nieliniowy to **rezystancyjny element bezwładny (bezinercyjny) bez
własnej SEM**. Jego charakterystyka i(u) musi być:

- **jednoznaczna** — jednej wartości \(u\) odpowiada jedna wartość \(i\),
- **ciągła**,
- **przechodzi przez początek układu** — przy \(u = 0\) płynie \(i = 0\)
  (element pasywny, bez własnego źródła energii).

Te warunki spełniają wykresy **1** (łamana „N-kształtna” przez zero) i
**2** (schodkowa, monotoniczna, przez zero).

Dlaczego pozostałe nie:

- 3 — pozioma prosta \(i = \mathrm{const}\): idealne **źródło prądowe**;
- 4 — nie przechodzi przez zero: przy \(u = 0\) płynie prąd ≠ 0, czyli element
  **czynny** (ma w sobie SEM);
- 5 — pionowy skok w zerze: charakterystyka **niejednoznaczna** przy \(u = 0\);
- 6 — krzywa „zawinięta”: jednej wartości \(u\) odpowiada kilka wartości \(i\)
  (histereza / rezystancja ujemna) — element z pamięcią.

**Odpowiedź: 1, 2.** (Słowa-klucze: jednoznaczna, ciągła, przez zero.)

## C. Gwiazda i trójkąt w układzie pięciu oporów (1 p.)

Schemat: dwa zaciski wejściowe po lewej; **węzeł górny-środkowy** łączy \(R_1\),
\(R_2\) i górny koniec \(R_3\); **węzeł dolny-środkowy** łączy \(R_4\), \(R_5\)
i dolny koniec \(R_3\); **węzeł prawy** łączy \(R_2\), \(R_5\) i zacisk
wyjściowy.

- **Opcja 1 ✔** — \(R_1\), \(R_2\), \(R_3\) schodzą się w jednym węźle
  (górnym-środkowym), a ich trzy pozostałe końce są „na zewnątrz” — to
  definicja **gwiazdy**.
- **Opcja 2 ✔** — \(R_2\) (górny-środkowy ↔ prawy), \(R_5\)
  (prawy ↔ dolny-środkowy) i \(R_3\) (górny-środkowy ↔ dolny-środkowy) łączą
  **trzy węzły parami**: każda para oporów ma wspólny węzeł, ale żadnego
  węzła wspólnego dla wszystkich trzech — to **trójkąt**.

Pozostałe opcje błędne: \(R_1\) i \(R_2\) (oraz \(R_4\) i \(R_5\)) mają wspólny
tylko jeden koniec, a w tym węźle odgałęzia się jeszcze trzeci element — więc
nie są ani szeregowo (ten sam prąd), ani równolegle (ta sama para węzłów).
\(R_2\) i \(R_5\) mają wspólny węzeł prawy, ale różne drugie końce — nie są
równoległe.

**Odpowiedź: 1, 2.** (Szybki test: zamaluj węzły — trzy opory w jednym punkcie
= gwiazda; trzy węzły połączone parami = trójkąt.)

## D. Opór statyczny i dynamiczny nieliniowego oporu (2 p.)

Charakterystyka elementu: prosta przez początek układu o nachyleniu
1 mA/V, **nasycająca się** na poziomie \(i = \pm 1\,\mathrm{mA}\)
(od \(|u| = 1\,\mathrm{V}\)).

Źródło rzeczywiste prądowe: \(J = 3\,\mathrm{mA}\) równolegle z
\(G_w = 1\,\mathrm{mS}\). Prosta obciążenia źródła:

\[
i = J - G_w u = 3\,\mathrm{mA} - u\cdot 1\,\mathrm{mS}
\]

Punkt pracy leży na **nasyceniu** (\(u > 1\,\mathrm{V}\), \(i = 1\,\mathrm{mA}\)):

\[
1 = 3 - u \quad\Rightarrow\quad u = 2\,\mathrm{V}
\]

Punkt pracy: \((u, i) = (2\,\mathrm{V},\ 1\,\mathrm{mA})\).

- **Opór statyczny**: \(R_s = \dfrac{u}{i} = \dfrac{2\,\mathrm{V}}{1\,\mathrm{mA}} = 2\,\mathrm{k\Omega}\).
- **Opór dynamiczny**: na poziomym odcinku nasycenia \(di/du = 0\), więc
  \(R_d = \dfrac{du}{di} = \infty\).

**Odpowiedź: 1 (2 kΩ i ∞).**

Kontrola dystraktorów: \(1/2\,\mathrm{k\Omega}\) to odwrócenie ułamka (\(i/u\));
\(0\) zamiast \(\infty\) to pomylenie odcinka poziomego z pionowym; \(\infty\)
jako \(R_s\) dotyczyłoby tylko pionowego odcinka charakterystyki.

## E. SEM źródła Thévenina dwójnika ze źródłem sterowanym (1 p.)

Dwójnik: źródło \(E\) (gałąź lewa), \(R_1\) (od górnego zacisku \(E\) do węzła
\(N_1\)), źródło sterowane \(gu\) między \(N_1\) a dolną szyną, \(R_2\) od
\(N_1\) do zacisku \(A\); \(u\) to napięcie na \(R_2\); zaciski \(A\)–\(B\)
stanowią port wyjściowy.

Port **otwarty** → przez \(R_2\) nie płynie prąd → \(u = 0\).

\[
gu = 0 \quad\Rightarrow\quad \text{źródło sterowane gaśnie (przerwa)}
\]

Zostaje oczko \(E\)–\(R_1\) bez prądu — brak spadku na \(R_1\), więc:

\[
E_T = u_{AB} = E
\]

**Odpowiedź: 1 (E).**

To najważniejsza własność źródeł sterowanych: **gdy wielkość sterująca wyzeruje
się w danych warunkach zadania, źródło sterowane „gaśnie” samo z siebie**.
Dystraktory \(E(1 \pm gR_{1,2})\), \(E/(1 \pm gR_{1,2})\) to wynik
„policzenia” źródła, które w tych warunkach w ogóle nie działa.

## F. Wkład źródła e2 w napięcie u — superpozycja (1 p.)

Dane: \(e_1 = 1\,\mathrm{V}\), \(e_2 = 2\,\mathrm{V}\), \(j_1 = 1\,\mathrm{A}\),
\(j_2 = 2\,\mathrm{A}\), \(R_1 = 1\,\mathrm{k\Omega}\), \(R_2 = 2\,\mathrm{k\Omega}\).

Zasada superpozycji: liczymy wkład **samego \(e_2\)**, pozostałe źródła
wyzerowane:

- \(e_1 \to\) **zwarcie**,
- \(j_1 \to\) **przerwa** (przerywa lewą część obwodu),
- \(j_2 \to\) **przerwa**.

Zostaje jedna pętla: \(e_2\) – \(R_2\) – węzeł środkowy – \(R_1\) – szyna
dolna. Opory są **szeregowo**:

\[
i^{(e_2)} = \frac{e_2}{R_1 + R_2} = \frac{2\,\mathrm{V}}{3\,\mathrm{k\Omega}} = \frac{2}{3}\,\mathrm{mA}
\]

Napięcie \(u\) mierzone jest na \(R_1\):

\[
u^{(e_2)} = i^{(e_2)} \cdot R_1 = \frac{2}{3}\,\mathrm{mA} \cdot 1\,\mathrm{k\Omega} = \frac{2}{3}\,\mathrm{V}
\]

**Odpowiedź: 1 (2/3 V).**

Uwaga: gdyby \(u\) było na \(R_2\), wyszłoby \(4/3\,\mathrm{V}\) (opcja 3) —
dystrybutor napięcia ten sam, rozstrzyga wyłącznie to, na którym oporze
narysowano strzałkę \(u\). Opcja \(1/3\,\mathrm{V}\) to ten sam dystrybutor
policzony od \(e_1 = 1\,\mathrm{V}\) — najczęstszy błąd (złe źródło).

## G. Moc dysponowana dwójnika z CCVS — twierdzenie Nortona (2 p.)

Dane: \(J = 4\,\mathrm{mA}\), \(R_1 = 1\,\mathrm{k\Omega}\),
\(R_2 = 2\,\mathrm{k\Omega}\), \(r = 1\,\mathrm{k\Omega}\).

Dwójnik: źródło \(J\) (gałąź lewa, w górę) równolegle z \(R_1\); źródło
sterowane \(ri\) w gałęzi górnej między węzłem \(R_1\) a zaciskiem \(A\);
\(R_2\) między \(A\) i \(B\); prąd sterujący \(i\) płynie w dół przez \(R_2\);
port \(A\)–\(B\).

**Krok 1 — wydajność Nortona (zwarcie A–B).** Zwarcie równoleguje \(R_2\):

\[
i = 0 \quad\Rightarrow\quad ri = 0 \quad\Rightarrow\quad \text{CCVS } = 0\ \text{V (zachowuje się jak zwarcie)}
\]

Cała górna szyna ma potencjał szyny dolnej, więc przez \(R_1\) nie płynie prąd,
a całe \(J\) przepływa przez zwarcie:

\[
J_N = I_{sc} = J = 4\,\mathrm{mA}
\]

**Krok 2 — SEM Thévenina (port otwarty).** Prąd przez \(R_2\) nie płynie →
\(i = 0\) → \(ri = 0\). Węzeł górny obciążony jest tylko przez \(R_1\):

\[
u_{oc} = J \cdot R_1 = 4\,\mathrm{mA} \cdot 1\,\mathrm{k\Omega} = 4\,\mathrm{V}
\]

**Krok 3 — moc dysponowana:**

\[
R_T = \frac{u_{oc}}{J_N} = \frac{4\,\mathrm{V}}{4\,\mathrm{mA}} = 1\,\mathrm{k\Omega}
\]

\[
P_{dysp} = \frac{J_N^2 R_T}{4} = \frac{u_{oc} J_N}{4}
= \frac{4\,\mathrm{V} \cdot 4\,\mathrm{mA}}{4} = 4\,\mathrm{mW}
\]

**Odpowiedź: 1 (4 mW).**

## Kontrola wyników

| Pyt. | Wynik | Klucz |
|---|---|---|
| A | 1, 2, 3 | ✔ |
| B | 1, 2 | ✔ |
| C | 1, 2 | ✔ |
| D | 2 kΩ i ∞ | ✔ |
| E | \(E_T = E\) | ✔ |
| F | 2/3 V | ✔ |
| G | 4 mW | ✔ |

Wszystkie wyniki zgadzają się z kluczem (pogrubione odpowiedzi w pliku
`PELP1_20Z_A_1_klucz.pdf`).
