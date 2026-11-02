# Test 1 PELP2 popr. (19.05.2021, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_21L_A_2_klucz.pdf`](../PELP1_21L_A_2_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H | Σ |
|---|---|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 | 1, 2, 3 | 1 | 1 | 1 | 1 | 1 | 9 pkt |

## A. Opór zastępczy dwójnika z szeregowym źródłem sterowanym (1 p.)

Dwójnik AB: opór \(R\) i źródło napięciowe sterowane \(ku\) połączone
**szeregowo** między zaciskami \(A\) i \(B\); \(u\) to napięcie na \(R\),
a źródło sterowane jest zwrócone **zgodnie** z napięciem na \(R\).

Prąd \(i\) płynie przez oba elementy szeregowo; spadek na oporze: \(u = iR\),
czyli \(i = u/R\). Napięcie na zaciskach:

\[
u_{AB} = u + ku = u(1+k)
\]

Stąd:

\[
R_{AB} = \frac{u_{AB}}{i} = \frac{u(1+k)}{u/R} = R(1+k) = R(k+1)
\]

**Odpowiedź: 1 (\(R(k+1)\)).**

Kontrola: \(k = 0\) daje \(R\) ✔; \(k = 1\) daje \(2R\) — dwa opory w
szeregu ✔. Dystraktor \(R(k-1)\) (opcja 7) to wariant, w którym źródło
sterowane **przeciwdziała** napięciu \(u\) (wtedy napięcia się odejmują — to
układ z pytania A testu z 24.03.2021). Opcja 11 („zależy od \(u\)”) jest
fałszywa, bo \(u\) skraca się w stosunku — opór jest **stały**, mimo że w
środku dwójnika jest źródło sterowane napięciem.

## B. Opór statyczny i dynamiczny elementu nieliniowego (1 p.)

Charakterystyka elementu: łamana od \((0,0)\) o małym nachyleniu do
\((3\,\mathrm{V}, 1\,\mathrm{mA})\), dalej odcinek stromy (nachylenie
\(2\,\mathrm{mA/V}\)) przez \((4\,\mathrm{V}, 3\,\mathrm{mA})\).

Element podłączono do **idealnego źródła prądowego 3 mA** — punkt pracy leży
na poziomie \(i = 3\,\mathrm{mA}\), czyli na stromym odcinku:

\[
i = 3\,\mathrm{mA} \quad\Rightarrow\quad u = 4\,\mathrm{V}
\]

- **Opór statyczny**: \(R_s = \dfrac{u}{i} = \dfrac{4\,\mathrm{V}}{3\,\mathrm{mA}} \approx 1{,}33\,\mathrm{k\Omega}\),
- **Opór dynamiczny**: nachylenie stromego odcinka
  \(\dfrac{\Delta i}{\Delta u} = \dfrac{3-1}{4-3} = 2\,\mathrm{mA/V}\), więc
  \(R_d = \dfrac{1}{2\,\mathrm{mA/V}} = 0{,}5\,\mathrm{k\Omega}\).

**Odpowiedź: 1 (\(R_s = 1{,}33\,\mathrm{k\Omega}\), \(R_d = 0{,}5\,\mathrm{k\Omega}\)).**

Dystraktor \(R_d = 2\,\mathrm{k\Omega}\) (opcja 3) to odwrócenie nachylenia
(\(1/\mathrm{mS}\) zamiast \(1/(2\,\mathrm{mS})\)) — uwaga na jednostki.

## C. Od czego zależy napięcie U na źródle prądowym J1 (1 p.)

Układ: \(J_1\) (z napięciem \(U\)) w gałęzi lewej; \(R_1\) poziomo; \(J_2\)
pionowo do węzła środkowego; \(E\)–\(R_2\) szeregowo od węzła środkowego do
szyny.

KCL w węźle górnym-lewym: całe \(J_1\) musi płynąć przez \(R_1\) (innej drogi
nie ma):

\[
V(N_1) - V(N_C) = J_1 R_1
\]

KCL w węźle środkowym: prąd przez gałąź \(E\)–\(R_2\) to \(J_1 + J_2\):

\[
V(N_C) = E + (J_1 + J_2) R_2
\]

Zatem:

\[
U = V(N_1) = E + (J_1 + J_2) R_2 + J_1 R_1
\]

We wzorze występują **wszystkie** elementy układu. Prawdziwe są więc opcje:
\(U\) zależy od \(J_1\) (1 ✔), od \(R_1\) (2 ✔), od wszystkich elementów
(3 ✔).

Fałszywe: \(U = 0\) (4), „nie zależy od \(E\)” (5 — występuje we wzorze),
„nie zależy od \(J_2\)” (6), „nie zależy od \(R_2\)” (7).

**Odpowiedź: 1, 2, 3.**

## D. Wzmacniacz operacyjny — od czego zależy U (1 p.)

Układ: źródło \(E\) przez \(R_1\) do wejścia \(+\); wejście \(-\) połączone
\(R_3\) (sprzężenie zwrotne) z węzłem wyjściowym; w węźle wyjściowym
\(R_2\) do masy i \(R_4\) szeregowo do zacisku \(U\); \(U\) mierzone na
otwartym wyjściu.

Zasady wzmacniacza idealnego: \(u_+ = u_-\) oraz \(i_+ = i_- = 0\).

- Przez \(R_1\) nie płynie prąd (wejście \(+\) nie pobiera prądu) →
  \(u_+ = E\), więc też \(u_- = E\).
- Do wejścia \(-\) przyłączone jest **tylko** \(R_3\): skoro \(i_- = 0\),
  przez \(R_3\) nie płynie prąd → brak spadku na \(R_3\).
- Przez \(R_4\) (szeregowo z otwartym wyjściem) nie płynie prąd → brak
  spadku na \(R_4\).
- Węzeł wyjściowy ma napięcie \(u_- = E\); \(R_2\) do masy odbiera prąd
  dostarczany przez wyjście wzmacniacza — nie zmienia napięcia węzła.

\[
U = E
\]

**Odpowiedź: 1 — wartość żadnego z oporów nie wpływa na U.**

To ten sam wzmacniacz „powielacz napięcia” w przebraniu: napięcie wyjścia
daje samo źródło \(E\); opory są albo w gałęziach bez prądów, albo obciążają
idealne wyjście, które i tak wymusza \(E\).

## E. Połączenia równoległe w sieci pięciu elementów (1 p.)

Węzły sieci: **górny-lewy** łączy elementy 3 (od dołu), 1 (od prawej) i 5
(od prawej); **górny-prawy** łączy elementy 5 (od lewej), 2 (od prawej) i 4
(od góry); **szyna dolna** łączy dolne końce elementów 3 i 4 oraz środek
(elementy 1 i 2 spotykają się na szynie).

Czyli:

- element 1: górny-lewy ↔ szyna; element 3: górny-lewy ↔ szyna →
  **równoległe**,
- element 2: górny-prawy ↔ szyna; element 4: górny-prawy ↔ szyna →
  **równoległe**,
- element 5: górny-lewy ↔ górny-prawy — łączy dwa różne węzły, nic mu nie
  odpowiada.

**Odpowiedź: 1 — (1 i 3) oraz (2 i 4).**

## F. SEM Thévenina dwójnika z szeregowym źródłem sterowanym 3u (1 p.)

Dwójnik AB: jedna gałąź szeregowo między zaciskami: źródło \(2\,\mathrm{V}\),
źródło sterowane \(3u\) i opór \(2\,\mathrm{k\Omega}\); \(u\) to napięcie na
zaciskach \(A\)–\(B\) (\(+\) przy \(A\)).

Port **otwarty** → w oczku nie płynie prąd (\(i = 0\)) → spadek na
\(2\,\mathrm{k\Omega}\) jest zerowy, całe napięcie portowe tworzą źródła:

\[
u = 3u - 2\,\mathrm{V}
\quad\Rightarrow\quad
-2u = -2\,\mathrm{V}
\quad\Rightarrow\quad
u = 1\,\mathrm{V}
\]

A ponieważ \(E_T\) to napięcie stanu jałowego:

\[
E_T = u = 1\,\mathrm{V}
\]

**Odpowiedź: 1 (1 V).**

To zadanie „na 10 sekund”: w stanie jałowym nie trzeba znać \(R_T\) — nie ma
prądu, więc żaden opór nie wnosi napięcia, a źródło sterowane daje
równanie \(u = 3u - 2\) rozwiązane w jednej linijce.

## G. Superpozycja: składowa prądu I od źródła J1 (1 p.)

Układ: \(J_1\) w gałęzi lewej (strzałka **w dół** — „wysysa” prąd z węzła
górnego-lewego), \(R_1\) pionowo z prądem \(I\) (w dół), \(R_2\) poziomo do
węzła gałęzi \(E\), \(E\) pionowo, \(J_2\) w gałęzi prawej.

Zasada superpozycji — liczymy wkład **samego \(J_1\)**:

- \(J_2 \to\) **przerwa**, \(E \to\) **zwarcie** (gałąź \(E\) staje się
  częścią szyny).

Zostaje: \(J_1\) (w dół, czyli pobiera prąd z węzła \(N_1\)) zasilające
\(R_1 \parallel R_2\) (przez zwarcie \(E\) opór \(R_2\) jest między \(N_1\)
a szyną). KCL w węźle \(N_1\):

\[
J_1 + \frac{V(N_1)}{R_1} + \frac{V(N_1)}{R_2} = 0
\quad\Rightarrow\quad
V(N_1) = -J_1 \cdot \frac{R_1 R_2}{R_1 + R_2}
\]

Prąd \(I\) (w dół przez \(R_1\)):

\[
I = \frac{V(N_1)}{R_1} = -J_1 \cdot \frac{R_2}{R_1 + R_2}
\]

**Odpowiedź: 1 (\(-J_1 \dfrac{R_2}{R_1+R_2}\)).**

Uwaga na znak: ujemna wartość bierze się stąd, że \(J_1\) z **grotami w dół**
wyciąga prąd z węzła — potencjał węzła staje się ujemny, więc prąd \(I\)
płynący „w dół” (umownie dodatni) ma wartość ujemną. Dystraktor z \(R_1\)
w liczniku (opcja 2) to wynik pomylenia gałęzi.

## H. Moc maksymalna w oporze R (2 p.)

Dwójnik zasilający: źródło prądowe \(8\,\mathrm{mA}\) równolegle z
\(1\,\mathrm{k\Omega}\); \(3\,\mathrm{k\Omega}\) szeregowo do zacisku \(A\);
\(R\) (odbiornik) między \(A\) i \(B\); szyna dolna wspólna.

**Krok 1 — SEM Thévenina** (port otwarty): prąd źródła płynie przez
\(1\,\mathrm{k\Omega}\):

\[
E_T = 8\,\mathrm{mA} \cdot 1\,\mathrm{k\Omega} = 8\,\mathrm{V}
\]

(przez \(3\,\mathrm{k\Omega}\) przy otwartym porcie nie płynie prąd — brak
spadku).

**Krok 2 — prąd zwarciowy** (zwarcie A–B): źródło \(8\,\mathrm{mA}\)
rozdziela się między \(1\,\mathrm{k\Omega}\) i gałąź
\(3\,\mathrm{k\Omega}\)–zwarcie:

\[
I_{sc} = 8\,\mathrm{mA} \cdot \frac{1}{1+3} = 2\,\mathrm{mA}
\]

**Krok 3 — moc maksymalna:**

\[
R_T = \frac{E_T}{I_{sc}} = \frac{8\,\mathrm{V}}{2\,\mathrm{mA}} = 4\,\mathrm{k\Omega}
\quad (= 3\,\mathrm{k\Omega} + 1\,\mathrm{k\Omega} \text{ po wyzerowaniu źródła})
\]

\[
P_{\max} = \frac{E_T^2}{4 R_T} = \frac{8^2}{4 \cdot 4000} = 4\,\mathrm{mW}
\]

**Odpowiedź: 1 (4 mW).**

Kontrola: \(P_{\max} = E_T \cdot I_{sc}/4 = 8 \cdot 2\,\mathrm{mA}/4 = 4\,\mathrm{mW}\)
✔. Dystraktor 16 mW to moc przy zwarciu \(E_T^2/R_T\) — zawsze 4 razy
większa od mocy dysponowanej.

## Kontrola wyników

| Pyt. | Wynik | Klucz |
|---|---|---|
| A | \(R(k+1)\) | ✔ |
| B | 1,33 kΩ i 0,5 kΩ | ✔ |
| C | 1, 2, 3 | ✔ |
| D | żaden z oporów | ✔ |
| E | (1 i 3) oraz (2 i 4) | ✔ |
| F | 1 V | ✔ |
| G | \(-J_1 R_2/(R_1+R_2)\) | ✔ |
| H | 4 mW | ✔ |

Wszystkie wyniki zgadzają się z kluczem (pogrubione odpowiedzi w pliku
`PELP1_21L_A_2_klucz.pdf`).
