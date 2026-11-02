# Test 1 PELP1 (20.05.2020, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_20L_A_1_klucz.pdf`](../PELP1_20L_A_1_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (wyróżnione
pogrubieniem); do testu docelowego wybierana jest jedna z nich.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 i 2 | 1 i 2 | 1 | 1 | 1 | 1 i 2 | 1 |

## A. Opór zastępczy dwójnika AB (1 p.)

Dwójnik: opór \(R\) połączony równolegle ze źródłem napięciowym sterowanym
prądem (CCVS) o napięciu \(ri\). Prąd sterujący \(i\) płynie górnym przewodem
do zacisku „+” źródła.

- Napięcie na dwójniku (na obu gałęziach równoległych): \(u = r i\),
  stąd \(i = u/r\).
- Prąd wchodzący do dwójnika: \(i_{AB} = \dfrac{u}{R} + i = u\left(\dfrac{1}{R} + \dfrac{1}{r}\right)\).
- Opór zastępczy:
  \[
  R_{AB} = \frac{u}{i_{AB}} = \frac{1}{\frac{1}{R} + \frac{1}{r}} = \frac{rR}{r+R}
  \]

**R_z = rR/(r+R)** (odpowiedź 1).

## B. Układ z oporem nieliniowym RN (1 p.)

Obwód: lewa część (E, R, J) liniowa, w części prawej opór nieliniowy \(R_N\)
połączony równolegle z \(R\); \(I\) to prąd płynący w dół przez \(R\).

Zdania prawdziwe:

1. **Zasada Tellegena obowiązuje** — wynika wprost z praw Kirchhoffa, więc
   obowiązuje w każdym obwodzie, także nieliniowym (odpowiedź 1).
2. **Dwójnik na lewo od AB można zastąpić źródłem Nortona** — jest to dwójnik
   liniowy (E, R, J), a każdy liniowy dwójnik ma równoważnik Nortona
   (odpowiedź 2).

Zdania fałszywe:

- 3. superpozycja — nie obowiązuje, bo w obwodzie jest element nieliniowy;
- 4. dzielnik prądowy — dotyczy tylko gałęzi liniowych;
- 5. prawo Ohma — \(R_N\) go nie spełnia.

**Odpowiedzi: 1 i 2.**

## C. Napięcie U na źródle prądowym (1 p.)

Układ: trzy gałęzie pionowe między górnym węzłem a dolną szyną —
\(E_1\), \(R\), \(E_2\). Źródło \(J\) znajduje się w górnej gałęzi poziomej;
napięcie \(U\) mierzone jest na tym źródle prądowym (plus przy węźle nad
\(E_1\)). \(R\) i \(E_2\) mają połączone górne zaciski.

Kluczowa obserwacja: **źródło idealne E1 przybija potencjał swojego górnego
węzła**, a źródło \(E_2\) przybija potencjał węzła wspólnego dla \(R\) i
\(E_2\). Zatem:

\[
U = \varphi_{\text{nad }E_1} - \varphi_{\text{nad }E_2} = E_1 - E_2
\]

Wartości \(J\) i \(R\) nie wpływają na \(U\) (źródło prądowe jedynie wymusza
prąd, a opór \(R\) — przy znanym napięciu \(E_2\) na nim — jedynie prąd w
swojej gałęzi).

- Odpowiedź 1 prawdziwa: \(U\) zależy tylko od \(E_1\) i \(E_2\);
- Odpowiedź 2 prawdziwa: \(U\) nie zależy od \(J\).

**Odpowiedzi: 1 i 2.**

## D. Wzmacniacz operacyjny — napięcie U (1 p.)

Układ: źródło \(E\) przyłączone do wejścia, wzmacniacz ze sprzężeniem zwrotnym
przez \(R_1\), opór \(R_2\) przy wyjściu, \(U\) mierzone na zaciskach
wyjściowych (obwód otwarty — bez obciążenia).

Dla wzmacniacza idealnego (nieskończone wzmocnienie, zerowy prąd wejściowy):
napięcia na obu wejściach są równe, a w konsekwencji napięcie wyjściowe
równa się \(E\). Przez \(R_2\) nie płynie prąd (wyjście otwarte), więc spadek
na nim jest zerowy; prąd wejściowy również jest zerowy, więc \(R_1\) nie
wpływa na wynik.

\[
U = E
\]

**U = E** (odpowiedź 1) — niezależnie od skończonych wartości \(R_1\), \(R_2\).

## E. Połączenia równoległe w sieci pięciu oporów (1 p.)

Węzły: \(T\) (górna szyna — bo górne zaciski 3, 1 i 5 są połączone
przewodem omijającym), \(M\) (węzeł między 1 i 2, u dołu dołącza 4),
\(B\) (dolna szyna).

- 1: \(T \to M\), 2: \(M \to T\) — **równoległe** (ta sama para węzłów);
- 3: \(T \to B\), 5: \(T \to B\) — **równoległe**;
- 4: \(M \to B\) — nie ma pary.

**Odpowiedź: (1 i 2) oraz (3 i 5)** — opcja 1.

## F. Źródło Nortona równoważne dwójnikowi AB (1 p.)

Dwójnik: idealne źródło napięciowe \(2\,\mathrm{V}\) z oporem \(1\,\mathrm{k}\Omega\)
połączonym równolegle, a następnie \(2\,\mathrm{k}\Omega\) szeregowo do zacisku
\(A\) (dolna szyna do \(B\)).

**SEM zastępcza (napięcie otwartych zacisków):** przy otwartych zaciskach
przez \(2\,\mathrm{k}\Omega\) nie płynie prąd, więc
\(E_T = U_{AB}^{(oc)} = 2\,\mathrm{V}\).

**Opór wewnętrzny:** wyłączamy źródło \(2\,\mathrm{V}\) (zastępujemy je
zwarciem) — zwarcie to zwiera także \(1\,\mathrm{k}\Omega\), więc od zacisków
AB widać tylko \(2\,\mathrm{k}\Omega\): \(R_T = 2\,\mathrm{k}\Omega\).

**Parametry Nortona:**
\[
J = \frac{E_T}{R_T} = \frac{2\,\mathrm{V}}{2\,\mathrm{k}\Omega} = 1\,\mathrm{mA},
\qquad
G = \frac{1}{R_T} = \frac{1}{2\,\mathrm{mS}}
\]

**J = 1 mA, G = 1/2 mS** (odpowiedź 1).

## G. Który dwójnik jest bezźródłowy (1 p.)

Pięć dwójników: 1) \(R\) ∥ źródło sterowane \(ku\); 2) dioda \(D\) ∥ źródło
\(E>0\); 3) \(R\) ∥ \(E>0\); 4) dioda \(D\) ∥ \(E>0\) (inny zwrot źródła);
5) \(E>0\) ∥ źródło sterowane \(ri\).

Zgodnie z kluczem prawidłowe są odpowiedzi **1 i 2**. Uwaga interpretacyjna:
przy ścisłej definicji „bezźródłowy = nie zawiera żadnego źródła (ani
niezależnego, ani sterowanego)” żaden z pięciu dwójników nie spełnia
definicji (każdy zawiera źródło — wówczas poprawna byłaby odpowiedź 6).
Klucz dopuszcza 1 i 2 — dwójnik 1 spełnia kryterium podręcznikowe
„charakterystyka \(i(u)\) przechodzi przez początek układu współrzędnych”
(brak niezależnego źródła energii: przy \(u=0\) także \(i=0\)), a dwójnik 2
bywa traktowany jako model rzeczywistej diody. To znana niespójność tego
klucza — na egzaminie należy czytać schematy, nie numerację.

**Odpowiedzi według klucza: 1 i 2.**

## H. Maksymalna moc w oporze R (2 p.)

Układ: źródło \(2\,\mathrm{V}\) z oporem \(2\,\mathrm{k}\Omega\) równolegle,
następnie \(2\,\mathrm{k}\Omega\) szeregowo do węzła \(A\); obciążenie
\(R\) między \(A\) i \(B\) (dolna szyna).

- \(E_T = U_{oc} = 2\,\mathrm{V}\) (przy otwartych zaciskach brak prądu
  przez szeregowy \(2\,\mathrm{k}\Omega\)).
- \(R_T = 2\,\mathrm{k}\Omega\) (wyłączenie źródła \(2\,\mathrm{V}\) zwarciem
  zwiera równoległy \(2\,\mathrm{k}\Omega\); od zacisków widać sam opór
  szeregowy).

Moc maksymalna przy \(R = R_T\):
\[
P_{\max} = \frac{E_T^2}{4 R_T} = \frac{(2\,\mathrm{V})^2}{4 \cdot 2\,\mathrm{k}\Omega}
= 0{,}25\,\mathrm{mW}
\]

**P_max = 0,25 mW** (odpowiedź 1).

## Kontrola wyników

Wszystkie wyniki zgodne z kluczem: A1, B1/B2, C1/C2, D1, E1, F1, G1/G2
(niespójność opisana wyżej), H1.
