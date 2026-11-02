# Test 1 PELP1 popr. (22.12.2021, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_21Z_A_2_klucz.pdf`](../PELP1_21Z_A_2_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H | Σ |
|---|---|---|---|---|---|---|---|---|---|
| Odp. | 1, 2 | 1, 2 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 9 pkt |

## A. Opór zastępczy dwójnika [βi ∥ R] (1 p.)

Dwójnik AB: źródło prądowe sterowane \(\beta i\) (romb) połączone
**równolegle** z oporem \(R\); prąd sterujący \(i\) to **prąd portowy**
(wpływający do zacisku \(A\)).

KCL węzła górnego: prąd portowy \(i\) rozdziela się na prąd oporu \(i_R\)
i prąd gałęzi źródła sterowanego. Źródło sterowane (grot zgodny z prądem
portowym) **pobiera** \(\beta i\), więc:

\[
i = i_R + \beta i \quad\Rightarrow\quad i_R = i(1+\beta)
\]

Napięcie portowe to spadek na \(R\):

\[
u = i_R R = i(1+\beta) R
\quad\Rightarrow\quad
R_{AB} = \frac{u}{i} = R(1+\beta) = R + \beta R
\]

**Odpowiedź: 1 i 2** (obie opcje są identyczne: \(R(1+\beta) = R+\beta R\)).

Kontrola: \(\beta = 0\) daje \(R\) ✔. Dystraktor \(R(1-\beta)\) (opcja 3) to
błąd znaku przy KCL — źródło sterowane **dodaje** prąd do oporu, więc opór
zastępczy rośnie, a nie maleje. Opcja 7 („zależy od prądu \(i\)”) jest
fałszywa, bo \(i\) skraca się z równania.

## B. Układ z oporem nieliniowym RN (1 p.)

Układ: po lewej \(J \parallel R\) z \(E\) w szynie górnej (do portu), port
\(A\)–\(B\) z napięciem \(U\); po prawej \(R\) (prąd \(I\)) szeregowo z
\(R_N\).

Prawdziwe są **dwie** opcje:

1. **dwójnik na lewo od AB można zastąpić źródłem Nortona** ✔ — dwójnik lewy
   jest **liniowy** (\(J\), \(R\), \(E\)), a każdy dwójnik liniowy ma
   zastępcze źródło Nortona (i Thévenina);
2. **gdy celem jest obliczenie \(U\), dwójnik na prawo od AB można zastąpić
   elementem równoważnym** ✔ — do wyznaczenia napięcia portowego wystarczy
   **charakterystyka** dwójnika prawego; każdy element o tej samej
   charakterystyce \(i(u)\) jest jego zastępczy (równoważny).

Fałszywe:

- 3 — twierdzenie Tellegena jest **globalne** (cały układ, bilans mocy);
- 4 — \(U = (R+R_N)I\) traktuje \(R_N\) jak opór omowy; \(R_N\) zależy od
  punktu pracy, więc tak zapisać nie można;
- 5 — zasada superpozycji **nie** obowiązuje w układzie z elementem
  nieliniowym;
- 6 — dwójnik lewy zawiera źródła (\(J\), \(E\)) — prawem Ohma się nie
  opisuje.

**Odpowiedź: 1, 2.**

## C. Od czego zależy napięcie U na źródle prądowym J2 (1 p.)

Układ: \(J_1\) (lewa gałąź), \(E\) szeregowo w szynie górnej, \(R_1\)
(gałąź środkowa), \(J_2\) poziomo w szynie górnej (z napięciem \(U\)),
\(R_2\) (gałąź prawa).

Prąd przez gałąź \(E\) jest wymuszony przez \(J_1\) (jedyna droga), a źródło
napięciowe szeregowo z idealnym źródłem prądowym **nie wpływa na prądy i
napięcia pozostałej części obwodu**. KCL węzła nad \(R_1\):

\[
J_1 = \frac{V_C}{R_1} + J_2 \quad\Rightarrow\quad V_C = (J_1 - J_2) R_1
\]

KCL węzła nad \(R_2\): \(V_D = J_2 R_2\). Napięcie na \(J_2\):

\[
U = V_D - V_C = J_2 R_2 - (J_1 - J_2) R_1
\]

Wniosek:

- \(U\) **zależy od \(J_1\)** (opcja 1 ✔),
- \(U\) **zależy od \(R_1\)** (opcja 2 ✔),
- \(U\) **nie zależy od \(E\)** (opcja 4 fałszywa — \(E\) znika z równań,
  bo siedzi szeregowo z idealnym źródłem prądowym),
- \(U\) **zależy od \(J_2\)** (opcja 5 fałszywa) i od \(R_2\), ale nie od
  wszystkich elementów (opcja 6 fałszywa); \(U \ne 0\) (opcja 3 fałszywa).

**Odpowiedź: 1, 2.**

## D. Wzmacniacz operacyjny — cztery opory, dwa istotne (1 p.)

Układ (wzmacniacz niienwertujący): źródło \(E\) do masy; przez \(R_2\)
do wejścia \(+\); \(R_1\) od wejścia \(-\) do masy; \(R_3\) w pętli
sprzężenia zwrotnego (wyjście–wejscie \(-\)); \(R_4\) od wyjścia do masy;
\(U\) na wyjściu.

Zasady wzmacniacza idealnego: \(u_+ = u_-\), \(i_+ = i_- = 0\).

- Przez \(R_2\) (szeregowo z wejściem \(+\)) nie płynie prąd → brak
  spadku → \(u_+ = E\).
- \(u_- = u_+ = E\); prąd w gałęzi \(R_1\): \(\dfrac{E}{R_1}\) — ten sam
  płynie przez \(R_3\) (bo \(i_- = 0\)):
  \(U = E + \dfrac{E}{R_1} R_3 = E\left(1 + \dfrac{R_3}{R_1}\right)\).
- \(R_4\) obciąża idealne wyjście wzmacniacza — nie zmienia \(U\).

Na \(U\) wpływają więc **tylko \(R_1\) i \(R_3\)**.

**Odpowiedź: 1, 2 (R1 i R3).**

## E. Natężenia I1 i I2 (1 p.)

Trzy obszary (subobwody) połączone przewodami; do węzła środkowego
\(C\) dopływają \(I_1\) (od lewego) i \(I_2\) (od prawego — strzałka
skierowana do \(C\)), a przewód pionowy odprowadza ich sumę do obszaru
dolnego, gdzie rozchodzi się na \(1\,\mathrm{A}\) i \(2\,\mathrm{A}\).

KCL w węźle \(C\):

\[
I_1 + I_2 = i_{pion}
\]

KCL w obszarze dolnym:

\[
i_{pion} = 1\,\mathrm{A} + 2\,\mathrm{A} = 3\,\mathrm{A}
\]

Z warunku \(I_1 = I_2 = I\):

\[
2I = 3\,\mathrm{A} \quad\Rightarrow\quad I = 1{,}5\,\mathrm{A}
\]

**Odpowiedź: 1 (1,5 A).**

Dystraktory: \(3\,\mathrm{A}\) to cała suma (nie połowa); \(-1{,}5\,\mathrm{A}\)
— ten sam rachunek z przeciwnym zwrotem strzałek; „za mało danych” jest
fałszywe, bo KCL wystarcza.

## F. Superpozycja: składowa prądu I od źródła J1 (1 p.)

Układ: \(J_1\) (gałąź lewa, grot w dół) równolegle z \(R_1\); \(R_2\)
poziomo; \(E\) (gałąź prawa, grot w górę) z prądem \(I\) skierowanym w dół;
\(J_2\) (gałąź skrajna prawa).

Liczymy wkład od **samego \(J_1\)**: \(E \to\) zwarcie, \(J_2 \to\) przerwa.

Zostaje: \(J_1\) (grot w dół — **pobiera** prąd z węzła górnego) zasilające
\(R_1 \parallel R_2\) (przez zwarcie \(E\) prawy koniec \(R_2\) leży na
szynie). KCL:

\[
J_1 + V\left(\frac{1}{R_1} + \frac{1}{R_2}\right) = 0
\quad\Rightarrow\quad
V = -J_1 \frac{R_1 R_2}{R_1+R_2}
\]

Prąd \(I\) płynie w dół przez zwarcie (odcinek \(R_2\) — szyna):

\[
I = \frac{V}{R_2} = -J_1 \frac{R_1}{R_1+R_2}
\]

**Odpowiedź: 1 (\(-J_1 \dfrac{R_1}{R_1+R_2}\)).**

Uwaga na znak: ujemny, bo \(J_1\) z grotami w dół wysysa prąd z węzła —
potencjał węzła jest ujemny, a prąd w zwarciu płynie przeciwnie do
umownego zwrotu \(I\). Dystraktor z \(R_2\) w liczniku (opcja 2) to
pomylenie gałęzi dzielnika.

## G. Moc maksymalna w oporze R (2 p.)

Dwójnik zasilający (od zacisku \(A\) do \(B\)): \(6\,\mathrm{k\Omega}\)
bezpośrednio między zaciskami, oraz gałąź \(3\,\mathrm{k\Omega}\) — źródło
prądowe \(4\,\mathrm{mA}\) (grot w dół) również między zaciskami; odbiornik
\(R\) na zaciskach \(A\)–\(B\).

**Krok 1 — SEM Thévenina** (port otwarty): całe \(4\,\mathrm{mA}\) płynie
pętlą \(3\,\mathrm{k\Omega}\)–\(6\,\mathrm{k\Omega}\), więc na
\(6\,\mathrm{k\Omega}\) odkłada się:

\[
|E_T| = 4\,\mathrm{mA} \cdot 6\,\mathrm{k\Omega} = 24\,\mathrm{V}
\]

**Krok 2 — opór Thévenina** (źródło \(4\,\mathrm{mA}\) przerwanie): od
portu widać \(6\,\mathrm{k\Omega}\) (gałąź z przerwanym źródłem nie
przewodzi):

\[
R_T = 6\,\mathrm{k\Omega}
\]

**Krok 3 — moc maksymalna** (dopasowanie \(R = R_T\)):

\[
P_{\max} = \frac{E_T^2}{4 R_T} = \frac{24^2}{4 \cdot 6000} = 24\,\mathrm{mW}
\]

**Odpowiedź: 1 (24 mW).**

Kontrola metodą Nortona: przy zwarciu portowym zwarcie **równoległego
\(6\,\mathrm{k\Omega}\)** sprawia, że całe \(4\,\mathrm{mA}\) źródła płynie
pętlą \(3\,\mathrm{k\Omega}\)–zwarcie (żadna część nie rozdziela się na
\(6\,\mathrm{k\Omega}\)):

\[
J_N = 4\,\mathrm{mA}, \qquad
P_{\max} = \frac{J_N^2 R_T}{4} = \frac{(4\,\mathrm{mA})^2 \cdot 6\,\mathrm{k\Omega}}{4} = 24\,\mathrm{mW}\ ✔
\]

## H. Charakterystyka dwójnika z diodą idealną (1 p.)

Dwójnik AB: \([D \parallel 1\,\mathrm{mA}]\) szeregowo z \([1\,\mathrm{V}
\parallel{}- 1\,\mathrm{k\Omega}]\); dioda: anoda od strony \(A\); \(i\) —
prąd wpływający do \(A\), \(u\) — napięcie portowe.

Dwa stany diody idealnej:

- **dioda zatkana** (\(u \le 0\)): prąd dwójnika wyznacza wyłącznie
  źródło \(1\,\mathrm{mA}\) (dioda = przerwa, a źródło prądowe narzuca
  prąd gałęzi):

\[
i = 1\,\mathrm{mA} \quad (u \le 0)
\]

— poziomy odcinek \(i = 1\,\mathrm{mA}\) w trzeciej/pierwszej ćwiartce
lewej strony osi;

- **dioda przewodząca** (\(u \ge 0\)): dioda = zwarcie, dwójnik to
  \([1\,\mathrm{V} + 1\,\mathrm{k\Omega}]\) z prądem źródła
  \(1\,\mathrm{mA}\) „w tle”:

\[
u = 1\,\mathrm{k\Omega} \cdot i - 1\,\mathrm{V}
\quad\Rightarrow\quad
i = 1\,\mathrm{mA} + \frac{u}{1\,\mathrm{k\Omega}}
\]

— prosta o nachyleniu \(1\,\mathrm{mA/V}\) wychodząca z punktu
\((0,\,1\,\mathrm{mA})\), przechodząca przez \((1\,\mathrm{V},\,
2\,\mathrm{mA})\).

Charakterystykę „pozioma \(1\,\mathrm{mA}\) + załamanie w \((0,\,
1\,\mathrm{mA})\) w prostą o nachyleniu \(1\,\mathrm{mA/V}\)” przedstawia
**wykres 1**.

**Odpowiedź: 1.**

Dlaczego pozostałe nie: wykres 3 to ta sama prosta, ale bez poziomego
odcinka \(1\,\mathrm{mA}\) (brak źródła prądowego); wykres 2 to lustrzane
odbicie (dioda złączona przeciwnie i źródło \(-1\,\mathrm{mA}\)); wykresy
4 i 5 mają pionowe odcinki — to cecha źródła napięciowego (idealnego) w
dwójniku, a nie prądowego.

## Kontrola wyników

| Pyt. | Wynik | Klucz |
|---|---|---|
| A | \(R(1+\beta)\) | ✔ (opcje 1 i 2) |
| B | 1, 2 | ✔ |
| C | 1, 2 | ✔ |
| D | R1 i R3 | ✔ (opcje 1 i 2) |
| E | 1,5 A | ✔ |
| F | \(-J_1 R_1/(R_1+R_2)\) | ✔ |
| G | 24 mW | ✔ |
| H | wykres 1 | ✔ |

Wszystkie wyniki zgadzają się z kluczem (pogrubione odpowiedzi w pliku
`PELP1_21Z_A_2_klucz.pdf`).
