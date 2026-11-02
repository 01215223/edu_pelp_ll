# Test 1 PELP2 (24.03.2021, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_21L_A_1_klucz.pdf`](../PELP1_21L_A_1_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H | Σ |
|---|---|---|---|---|---|---|---|---|---|
| Odp. | 1, 2 | 1 | 1, 2, 3 | 1, 2 (wykreślone) | 1 | 1 | 1 | 1 | 9 pkt |

## A. Opór zastępczy dwójnika z szeregowym źródłem sterowanym (1 p.)

Dwójnik AB: opór \(R\) i źródło napięciowe sterowane \(ku\) połączone
**szeregowo** między zaciskami \(A\) i \(B\); napięcie sterujące \(u\) to
napięcie na zaciskach dwójnika (\(+\) przy \(A\)), a biegunowość źródła
sterowanego jest zwrócona **przeciwnie** do napięcia portowego.

Prąd \(i\) płynie przez oba elementy szeregowo. Napięcie portowe:

\[
u = iR - ku
\]

(źródło sterowane odejmuje się od spadku na oporze). Stąd:

\[
u(1+k) = iR
\quad\Rightarrow\quad
R_{AB} = \frac{u}{i} = \frac{R}{1+k} = \frac{R}{k+1}
\]

**Odpowiedź: 1 i 2** (obie opcje są identyczne: \(R/(k+1) = R/(1+k)\)).

Kontrola: \(k = 0\) daje \(R\) ✔ (samo źródło wyłączone). Opcja 7,
\(R(k+1)\), dotyczy zwrotu źródła sterowanego „zgodnego” — to odpowiedź
testu z 19.05.2021 (pytanie A tamtego testu). Opcja 12 („zależy od \(u\)”)
jest fałszywa, bo \(u\) skraca się z równania — opór zastępczy jest stały,
mimo że w środku dwójnika jest źródło sterowane napięciem.

## B. Opór statyczny i dynamiczny elementu nieliniowego (1 p.)

Charakterystyka elementu:

- poziomy odcinek \(i = 0\) dla \(u \le 1\,\mathrm{V}\) (próg),
- pierwszy rosnący odcinek od \((1\,\mathrm{V}, 0)\) do
  \((3\,\mathrm{V}, 1\,\mathrm{mA})\) o nachyleniu
  \(\tfrac{1}{2}\,\mathrm{mA/V}\),
- dalej odcinek bardziej stromy (od \(u = 3\,\mathrm{V}\)).

Element podłączono do **idealnego źródła napięciowego 2 V** — punkt pracy
leży pionie \(u = 2\,\mathrm{V}\), czyli na pierwszym rosnącym odcinku:

\[
i = \tfrac{1}{2}\,\mathrm{mS} \cdot (2 - 1)\,\mathrm{V} = 0{,}5\,\mathrm{mA}
\]

- **Opór statyczny**: \(R_s = \dfrac{u}{i} = \dfrac{2\,\mathrm{V}}{0{,}5\,\mathrm{mA}} = 4\,\mathrm{k\Omega}\),
- **Opór dynamiczny**: \(R_d = \dfrac{du}{di} = \dfrac{1}{0{,}5\,\mathrm{mS}} = 2\,\mathrm{k\Omega}\).

**Odpowiedź: 1 (\(R_s = 4\,\mathrm{k\Omega}\), \(R_d = 2\,\mathrm{k\Omega}\)).**

## C. Od czego zależy napięcie U na źródle prądowym J1 (1 p.)

Układ: \(J_1\) (z napięciem \(U\)) równolegle z \(R_1\) po lewej; \(R_2\)
poziomo u góry; \(E\) pionowo po prawej; \(J_2\) szeregowo w dolnym przewodzie.

Kluczowa obserwacja: gałąź \(R_2\)–\(E\)–\(J_2\) jest **szeregową bramką
prądową** — jej prąd jest wymuszony przez idealne źródło \(J_2\), więc ani
\(R_2\), ani \(E\) nie zmieniają prądu tej gałęzi. Bilans prądów węzła
górnego:

\[
J_1 = \frac{U}{R_1} + J_2
\quad\Rightarrow\quad
U = R_1\,(J_1 - J_2)
\]

Wniosek:

- \(U\) **zależy od \(R_1\)** (opcja 1 ✔),
- \(U\) **zależy od \(J_1\)** (opcja 2 ✔),
- \(U\) **nie zależy od \(R_2\)** (opcja 3 ✔ — bo \(R_2\) siedzi w bramce
  prądowej).

Pozostałe opcje fałszywe: \(U \ne 0\) (4); \(U\) **zależy** od \(J_2\)
(5 — fałszywa); \(U\) nie zależy od \(E\) (6 — fałszywa); „od wszystkich” (7)
— fałszywa, bo \(R_2\) i \(E\) nie występują we wzorze.

**Odpowiedź: 1, 2, 3.**

To najważniejsza lekcja tej grupy zadań: **decyduje topologia, a nie typ
elementu** — źródło napięciowe raz ustala napięcia, a innym razem ( szeregowo
z idealnym źródłem prądowym) nie ma żadnego wpływu.

## D. Wzmacniacz operacyjny — od czego zależy U (1 p.)

Pytanie **wykreślone w kluczu czerwonym „X”** (pytanie wadliwe, wycofane z
testu). Klucz zaznacza odpowiedzi **1 (R3)** i **2 (R4)**.

Układ: wzmacniacz operacyjny; \(E \parallel R_1\) przy wejściu \(-\);
\(R_2\) między wejściem \(+\) a masą; \(R_4\) w pętli sprzężenia zwrotnego;
\(R_3\) szeregowo z wyjściem; \(U\) — napięcie wyjściowe.

Dla wzmacniacza idealnego obowiązują zawsze dwie zasady:
\(u_+ = u_-\) oraz \(i_+ = i_- = 0\). Z nich wynika, że **nie wpływają** na
napięcia te opory, przez które nie płynie prąd: opór szeregowy z wejściem
\(+\) (tu \(R_2\)) ani opór równoległy do idealnego źródła. Napięcie
wyjściowe kształtują opory **pętli sprzężenia zwrotnego** — stąd w kluczu
\(R_3\) i \(R_4\).

Uwaga: analiza narysowanego dokładnie schematu daje wynik niezgodny z
oznaczeniem klucza (przy nieobciążonym wyjściu prąd wymuszony płynie pętlą
sprzężenia, a spadek na \(R_3\) nie przekłada się na \(U\) na zacisku
wyjściowym) — najpewniej dlatego pytanie wykreślono.

## E. Połączenia równoległe w sieci pięciu elementów (1 p.)

Węzły sieci: **górny-lewy** łączy elementy 3 (od góry), 1 (od lewej) i 5
(od lewej); **środkowy** łączy elementy 1 (od prawej), 4 (od góry) i 2 (od
lewej); **szyna dolna** łączy dolne końce elementów 3 i 4 oraz prawe końce
elementów 2 i 5.

Czyli:

- element 2: środkowy ↔ szyna; element 4: środkowy ↔ szyna → **równoległe**,
- element 3: górny-lewy ↔ szyna; element 5: górny-lewy ↔ szyna →
  **równoległe**,
- element 1: górny-lewy ↔ środkowy — unikalna para węzłów, nic mu nie
  odpowiada.

**Odpowiedź: 1 — (2 i 4) oraz (3 i 5).**

## F. Wydajność Nortona dwójnika z źródłem sterowanym 3i (1 p.)

Dwójnik AB: trzy gałęzie **równoległe** między zaciskami \(A\) (szyna górna)
i \(B\) (szyna dolna): źródło prądowe \(1\,\mathrm{mA}\) (w górę), opór
\(2\,\mathrm{k\Omega}\) (z prądem \(i\) skierowanym w dół) oraz źródło
sterowane \(3i\) (w dół).

Przy **zwarciu A–B** napięcie na wszystkich gałęziach równoległych wynosi
zero:

\[
i = 0 \quad\Rightarrow\quad 3i = 0 \quad\Rightarrow\quad \text{źródło sterowane gaśnie}
\]

W obwodzie zwarciowym zostaje tylko niezależne źródło \(1\,\mathrm{mA}\),
którego prąd nie ma innej drogi niż zwarcie:

\[
|J_N| = 1\,\mathrm{mA}
\]

Znak: źródło \(1\,\mathrm{mA}\) pompuje prąd od \(B\) do \(A\), więc prąd
wpływający do zacisku \(A\) (przy umownym zwrocie odniesienia \(J_N\)) jest
ujemny:

\[
J_N = -1\,\mathrm{mA}
\]

**Odpowiedź: 1 (−1 mA).**

Reguła ogólna: **zwarcie portowe zeruje napięcia sterujące równoległych
źródeł napięciowo sterowanych** — źródło „gaśnie” i obwód robi się
trywialny. Dystraktory 6 mA / −6 mA to policzenie \(3i\) przy \(i\) wziętym
z innego stanu obwodu.

## G. Superpozycja: składowa napięcia U od źródła E1 (1 p.)

Układ: \(E_1\) w gałęzi lewej; \(R_1\) poziomo (napięcie \(U\) na \(R_1\),
strzałka w lewo — „\(+\)” przy prawym węźle); \(E_2 \parallel R_2 \parallel J\)
między prawym węzłem a szyną.

Zasada superpozycji — liczymy wkład **samego \(E_1\)**:

- \(E_2 \to\) **zwarcie** — kluczowy moment: zwarcie \(E_2\) zwiera
  równoległy do niego \(R_2\), więc \(R_2\) **znika z obwodu**;
- \(J \to\) **przerwa**.

Zostaje jedno oczko: \(E_1\) – \(R_1\) – zwarcie (w miejscu \(R_2\)) – szyna:

\[
i = \frac{E_1}{R_1}, \qquad U^{(E_1)} = -i \cdot R_1 = -E_1
\]

(minus bierze się ze zwrotu strzałki \(U\): prąd płynie od lewego węzła do
prawego, więc potencjał prawego końca \(R_1\) jest niższy).

**Odpowiedź: 1 (−E1).**

Najczęstszy błąd w tej rodzinie zadań: dystraktory
\(\pm E_1 R_1/(R_1+R_2)\) (opcje 3 i 4) to wynik zapomnienia, że **zwarcie
źródła napięciowego usuwa wszystko, co z nim jest równoległe** — w tym
\(R_2\). Nie ma tu żadnego dzielnika napięcia.

## H. Moc maksymalna w oporze R (2 p.)

Dwójnik zasilający: źródło \(4\,\mathrm{V}\) szeregowo z \(1\,\mathrm{k\Omega}\),
a \(3\,\mathrm{k\Omega}\) równolegle z portem \(A\)–\(B\); \(R\) to odbiornik
na zaciskach \(A\)–\(B\).

**Krok 1 — SEM Thévenina** (port otwarty, bez \(R\)). Dzielnik
napięcia \(1\,\mathrm{k\Omega}\)–\(3\,\mathrm{k\Omega}\):

\[
E_T = 4\,\mathrm{V} \cdot \frac{3}{1+3} = 3\,\mathrm{V}
\]

**Krok 2 — opór Thévenina** (źródło 4 V zastąpione zwarciem):

\[
R_T = 1\,\mathrm{k\Omega} \parallel 3\,\mathrm{k\Omega} = 0{,}75\,\mathrm{k\Omega}
\]

**Krok 3 — moc maksymalna** (przy \(R = R_T\)):

\[
P_{\max} = \frac{E_T^2}{4 R_T} = \frac{3^2}{4 \cdot 750} = 3\,\mathrm{mW}
\]

**Odpowiedź: 1 (3 mW).**

Kontrola: moc przy zwarciu \(E^2/R_s = 16\,\mathrm{mW}\) — moc maksymalna
musi być od niej mniejsza, i jest (3 < 16). Dystraktory 12 mW i 16 mW to
moce nieosiągalne dla odbiornika.

## Kontrola wyników

| Pyt. | Wynik | Klucz |
|---|---|---|
| A | \(R/(k+1)\) | ✔ (opcje 1 i 2) |
| B | 4 kΩ i 2 kΩ | ✔ |
| C | 1, 2, 3 | ✔ |
| D | R3 i R4 (pytanie wykreślone) | ✔ (opcje 1 i 2) |
| E | (2 i 4) oraz (3 i 5) | ✔ |
| F | −1 mA | ✔ |
| G | −E1 | ✔ |
| H | 3 mW | ✔ |

Wszystkie wyniki zgadzają się z kluczem (pogrubione odpowiedzi w pliku
`PELP1_21L_A_1_klucz.pdf`).
