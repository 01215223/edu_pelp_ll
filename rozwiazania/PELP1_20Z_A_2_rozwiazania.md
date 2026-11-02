# Test 1 PELP1 (16.12.2020, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_20Z_A_2_klucz.pdf`](../PELP1_20Z_A_2_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | Σ |
|---|---|---|---|---|---|---|---|---|
| Odp. | 1, 2 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 9 pkt |

## A. Właściwości elementu skupionego (1 p.)

Element skupiony to obszar, w którym oddziaływania elektromagnetyczne
przenoszone są **natychmiast w całym obszarze elementu** (wymiary pomijalnie
małe względem długości fali). Prawdziwe są **dwie** opcje:

1. **ładunek elektryczny wewnątrz obszaru elementu jest stały** ✔ —
   element może gromadzić ładunek tylko na zaciskach (kondensator), ale
   wewnątrz obszaru bilans ładunku jest zerowy;
2. **zmiany pola elektromagnetycznego zachodzą wewnątrz całego obszaru
   elementu równocześnie** ✔ — to istota założenia skupionego: brak opóźnień
   propagacji wewnątrz elementu.

Pozostałe opcje błędne:

- 3 — pole magnetyczne wokół elementu **nie musi** być pomijalnie małe
  (cewka!);
- 4 — pole elektryczne nie jest zerowe (byłby to element bez napięcia);
- 5 — równania elementu mogą zawierać czas (\(u = L\,di/dt\));
- 6 — zmiany pola nie są pomijalnie małe — są **równocześnie**, ale wcale
  nie znikome.

**Odpowiedź: 1, 2.**

## B. Charakterystyka oporu nieliniowego (1 p.)

Opór nieliniowy to element rezystancyjny bezwładny bez własnej SEM — jego
charakterystyka \(i(u)\) musi być **jednoznaczna**, **ciągła** i **przechodzić
przez początek układu** (przy \(u = 0\) płynie \(i = 0\)). Te warunki spełniają
wykresy **1** (krzywa „z garbem”) i **2** (schodkowa, monotoniczna).

Pozostałe:

- 3 — pozioma prosta \(i = \mathrm{const}\): idealne źródło prądowe;
- 4 — nie przechodzi przez zero → element czynny (ma SEM);
- 5 — pionowy skok w zerze → niejednoznaczność przy \(u = 0\);
- 6 — krzywa „zawinięta” → kilka wartości \(i\) dla jednego \(u\)
  (histereza, element z pamięcią).

**Odpowiedź: 1, 2.**

## C. Gwiazda i trójkąt w układzie pięciu oporów (1 p.)

Schemat: dwa zaciski wejściowe po lewej; **węzeł górny-środkowy** łączy \(R_1\),
\(R_2\) i górny koniec \(R_3\); **węzeł dolny-środkowy** łączy \(R_4\), \(R_5\)
i dolny koniec \(R_3\); **węzeł prawy** łączy \(R_2\), \(R_5\) i zacisk
wyjściowy.

- **Opcja 1 ✔** — \(R_4\), \(R_5\), \(R_3\) schodzą się w jednym węźle
  (dolnym-środkowym), a ich trzy pozostałe końce są „na zewnątrz” — to
  **gwiazda**.
- **Opcja 2 ✔** — \(R_2\) (górny-środkowy ↔ prawy), \(R_5\)
  (prawy ↔ dolny-środkowy) i \(R_3\) (górny-środkowy ↔ dolny-środkowy) łączą
  trzy węzły parami — **trójkąt**.

Pozostałe opcje błędne jak w teście z 04.11.2020 (wspólny tylko jeden koniec
oporu z odgałęzieniem trzeciego elementu wyklucza zarówno szereg, jak i
równoległość).

**Odpowiedź: 1, 2.**

## D. Opór statyczny i dynamiczny nieliniowego oporu (2 p.)

Charakterystyka elementu: prosta \(i = u \cdot 1\,\mathrm{mA/V}\) od
\((-1\,\mathrm{V}, -1\,\mathrm{mA})\) do \((1\,\mathrm{V}, 1\,\mathrm{mA})\),
a następnie **odcinek pionowy** przy \(u = 1\,\mathrm{V}\) (prąd rośnie bez
wzrostu napięcia).

Źródło rzeczywiste napięciowe: \(E = 3\,\mathrm{V}\) szeregowo z
\(R_w = 1\,\mathrm{k\Omega}\). Prosta obciążenia źródła:

\[
u = E - R_w i = 3\,\mathrm{V} - i \cdot 1\,\mathrm{k\Omega}
\]

Punkt pracy leży na **odcinku pionowym** (\(u = 1\,\mathrm{V}\)):

\[
i = \frac{3 - 1}{1\,\mathrm{k\Omega}} = 2\,\mathrm{mA}
\]

Punkt pracy: \((u, i) = (1\,\mathrm{V},\ 2\,\mathrm{mA})\).

- **Opór statyczny**: \(R_s = \dfrac{u}{i} = \dfrac{1\,\mathrm{V}}{2\,\mathrm{mA}} = \frac{1}{2}\,\mathrm{k\Omega}\).
- **Opór dynamiczny**: na odcinku pionowym \(du/di = 0\), więc
  \(R_d = 0\).

**Odpowiedź: 1 (1/2 kΩ i 0).**

## E. Wydajność Nortona dwójnika z CCVS (1 p.)

Dwójnik: źródło \(J\) (gałąź lewa, w górę) równolegle z \(R_1\); źródło
sterowane \(ri\) w gałęzi górnej między węzłem \(R_1\) a zaciskiem \(A\);
\(R_2\) między \(A\) i \(B\); prąd sterujący \(i\) płynie w dół przez
\(R_2\); port \(A\)–\(B\).

Przy **zwarciu A–B**:

\[
i = 0 \quad\Rightarrow\quad ri = 0 \quad\Rightarrow\quad \text{CCVS } = 0\ \text{V (zwarcie)}
\]

Wtedy cała górna szyna jest na potencjale szyny dolnej → spadek na \(R_1\) jest
zerowy → przez \(R_1\) nie płynie prąd, a **całe \(J\) przepływa przez
zwarcie**:

\[
J_N = I_{sc} = J
\]

**Odpowiedź: 1 (J).**

Dystraktory \(J(1 \pm r/R_{1,2})\), \(J/(1 \pm r/R_{1,2})\) powstałyby przy
założeniu, że źródło sterowane pracuje w warunkach zwarciowych — a ono
**gaśnie** (\(i = 0\) na zwartym \(R_2\)).

## F. Wkład źródła j2 w prąd i — superpozycja (1 p.)

Dane: \(e_1 = 1\,\mathrm{V}\), \(e_2 = 2\,\mathrm{V}\), \(j_1 = 1\,\mathrm{A}\),
\(j_2 = 2\,\mathrm{A}\), \(R_1 = 1\,\mathrm{k\Omega}\), \(R_2 = 2\,\mathrm{k\Omega}\).

Dwójnik: \([j_1 \parallel e_1]\) — (gałąź górna) — \(R_1\) — \(e_2\) — węzeł —
\([R_2 \parallel j_2]\) — szyna; \(i\) to prąd w górnej szynie (kierunek:
w prawo).

Zasada superpozycji: liczymy wkład **samego \(j_2\)**, pozostałe źródła
wyzerowane:

- \(e_1 \to\) **zwarcie**, \(e_2 \to\) **zwarcie**,
- \(j_1 \to\) **przerwa** (lewa część obwodu nie istnieje).

Zostaje: \(j_2\) (w górę) równolegle z \(R_2\) napędzające węzeł X, z którego
prąd może odpływać tylko przez \(R_1\) (przez zwarcia \(e_2\) i \(e_1\) do
szyny):

\[
V_X = j_2 \cdot (R_1 \parallel R_2) = 2\,\mathrm{A} \cdot \frac{1 \cdot 2}{1 + 2}\,\mathrm{k\Omega} = \frac{4}{3}\,\mathrm{kV}
\]

Prąd przez \(R_1\) płynie **od węzła X w lewo** (do szyny przez zwarcia), a
\(i\) jest zdefiniowane w prawo:

\[
i^{(j_2)} = -\frac{V_X}{R_1} = -\frac{\tfrac{4}{3}\,\mathrm{kV}}{1\,\mathrm{k\Omega}} = -\frac{4}{3}\,\mathrm{A}
\]

**Odpowiedź: 1 (−4/3 A).**

Dystraktory: \(4/3\,\mathrm{A}\) — błędny znak (niezauważona orientacja
strzałki \(i\)); \(2/3\,\mathrm{A}\) — podział \(j_2 \cdot R_1/(R_1+R_2)\) bez
znaku; \(1/2\,\mathrm{A}\), \(1\,\mathrm{A}\) — wyniki z innych źródeł.

## G. Moc dysponowana dwójnika z VCCS — twierdzenie Thévenina (2 p.)

Dane: \(E = 12\,\mathrm{V}\), \(R_1 = 1\,\mathrm{k\Omega}\),
\(R_2 = 2\,\mathrm{k\Omega}\), \(g = \tfrac{1}{2}\,\mathrm{mS}\).

Dwójnik: źródło \(E\) (gałąź lewa), \(R_1\) od górnego zacisku \(E\) do węzła
\(N_1\), źródło sterowane \(gu\) między \(N_1\) a dolną szyną (strzałka w
górę), \(R_2\) od \(N_1\) do zacisku \(A\); \(u\) to napięcie na \(R_2\)
(\(+\) przy \(A\)); port \(A\)–\(B\).

**Krok 1 — SEM Thévenina (port otwarty).** Przez \(R_2\) nie płynie prąd →
\(u = 0\) → VCCS gaśnie. Zostaje oczko \(E\)–\(R_1\) bez prądu — brak spadku
na \(R_1\):

\[
E_T = u_{oc} = E = 12\,\mathrm{V}
\]

**Krok 2 — prąd zwarciowy (zwarcie A–B).** Teraz \(u_A = 0\), więc
\(u = -V_{N_1}\). KCL w węźle \(N_1\) (prąd sterujący \(g u\) wpływa do
węzła z szyny; gdy \(u < 0\), realnie **pobiera** prąd z węzła):

\[
\frac{E - V_{N_1}}{R_1} + g\,u = \frac{V_{N_1}}{R_2},
\qquad u = -V_{N_1}
\]

\[
\frac{12 - V_{N_1}}{1\,\mathrm{k\Omega}} - \frac{1}{2}\,\mathrm{mS}\cdot V_{N_1} = \frac{V_{N_1}}{2\,\mathrm{k\Omega}}
\]

Po pomnożeniu przez \(2\,\mathrm{k\Omega}\):

\[
2(12 - V_{N_1}) - V_{N_1} = V_{N_1}
\quad\Rightarrow\quad V_{N_1} = 6\,\mathrm{V}
\]

\[
I_{sc} = \frac{V_{N_1}}{R_2} = \frac{6\,\mathrm{V}}{2\,\mathrm{k\Omega}} = 3\,\mathrm{mA}
\]

**Krok 3 — moc dysponowana:**

\[
R_T = \frac{E_T}{I_{sc}} = \frac{12\,\mathrm{V}}{3\,\mathrm{mA}} = 4\,\mathrm{k\Omega}
\]

\[
P_{dysp} = \frac{E_T I_{sc}}{4} = \frac{E_T^2}{4 R_T}
= \frac{12\,\mathrm{V} \cdot 3\,\mathrm{mA}}{4} = 9\,\mathrm{mW}
\]

**Odpowiedź: 1 (9 mW).**

## Kontrola wyników

| Pyt. | Wynik | Klucz |
|---|---|---|
| A | 1, 2 | ✔ |
| B | 1, 2 | ✔ |
| C | 1, 2 | ✔ |
| D | 1/2 kΩ i 0 | ✔ |
| E | \(J_N = J\) | ✔ |
| F | −4/3 A | ✔ |
| G | 9 mW | ✔ |

Wszystkie wyniki zgadzają się z kluczem (pogrubione odpowiedzi w pliku
`PELP1_20Z_A_2_klucz.pdf`).
