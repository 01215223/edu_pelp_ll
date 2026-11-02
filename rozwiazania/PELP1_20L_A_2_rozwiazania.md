# Test 1 PELP1 (10.06.2020, poprawka A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_20L_A_2_klucz.pdf`](../PELP1_20L_A_2_klucz.pdf).

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 i 2 | 1 | 1 | 1 | 1 | 1 |

## A. Opór zastępczy dwójnika AB (1 p.)

Dwójnik: opór \(R\) połączony równolegle ze źródłem prądowym sterowanym
napięciem (VCCS) o prądzie \(gu\) — prąd źródła zwrócony przeciwnie do
prądu portowego.

- Napięcie na obu gałęziach: \(u\).
- Prąd wchodzący do dwójnika: \(i_{AB} = u/R - gu = u(1/R - g)\).
- Opór zastępczy:
  \[
  R_{AB} = \frac{u}{i_{AB}} = \frac{1}{\frac{1}{R}-g} = \frac{R}{1-gR}
  \]

Odpowiedzi 1 i 2 są równoważne algebraicznie (\(\frac{R}{1-gR} =
\frac{1}{1/R-g}\)) — obie są prawidłowe.

**R_z = R/(1−gR)** (odpowiedzi 1 i 2).

## B. Napięcie U na źródle prądowym (1 p.)

Układ: trzy gałęzie pionowe między górnym węzłem a dolną szyną:
(\(E_1\) + \(R\) szeregowo), \(J\) oraz \(E_2\). Źródło \(J\) jest
połączone równolegle z idealnym źródłem \(E_2\); napięcie \(U\) mierzone
jest na \(J\) (plus u góry).

Idealne źródło \(E_2\) **przybija** napięcie na równoległym do niego
źródle \(J\):

\[
U = E_2
\]

Nie zależy od \(J\), \(E_1\) ani \(R\) (gałąź \(E_1\)+\(R\) tylko
pobiera prąd z węzła, którego potencjał jest przybity).

- Odpowiedź 1 prawdziwa: \(U\) zależy tylko od \(E_2\);
- Odpowiedź 2 prawdziwa: \(U\) nie zależy od \(J\).

**Odpowiedzi: 1 i 2.**

## C. Wzmacniacz operacyjny — napięcie U (1 p.)

Źródło \(E\) przyłożone do wejścia wzmacniacza, sprzężenie zwrotne przez
\(R_1\), opór \(R_2\) przy wyjściu, \(U\) mierzone na wyjściu (bez
obciążenia).

Wzmacniacz idealny: zerowy prąd wejściowy, napięcia wejściowe równe.
Konsekwencja: napięcie wyjściowe równa się \(E\). Przez \(R_2\) nie płynie
prąd (wyjście otwarte), a spadek na \(R_1\) nie zmienia napięcia wejściowego
(zerowy prąd wejściowy) — skończone wartości oporów nie wpływają na \(U\).

\[
U = E
\]

**U = E** (odpowiedź 1) — niezależnie od wartości \(R_1\), \(R_2\).

## D. Połączenia równoległe w sieci pięciu oporów (1 p.)

Węzły: \(D\) (górny lewy), \(A\) (górny środkowy), \(B\) (górny prawy),
\(C\) (dolna szyna). Przewód omijający łączy \(A\) z \(B\) (opór 2 jest
zwarł!).

- 1: \(D \to A\); 2: \(A \to B\) (zwarty — nie liczy się);
- 3: \(D \to C\); 4: \(A \to C\); 5: \(B \to C\) — a ponieważ \(A = B\),
  to **4 i 5 łączą tę samą parę węzłów** — są równoległe;
- 3 łączy \(D\) z \(C\) — \(D\) to inny węzeł, więc 3 nie tworzy pary.

**Odpowiedź: tylko (4 i 5)** — opcja 1.

## E. Źródło Thévenina równoważne dwójnikowi AB (1 p.)

Dwójnik: źródło prądowe \(2\,\mathrm{mA}\) w szereg z konduktancją
\(2\,\mathrm{mS}\); ta gałąź jest połączona równolegle z konduktancją
\(2\,\mathrm{mS}\) między zaciskami \(A\) i \(B\).

**SEM zastępcza:** napięcie otwartych zacisków. Zapis bilansu prądów
(\(V_B = 0\)):
- węzeł \(A\): \((V_N - V_A) \cdot 2\,\mathrm{mS} = V_A \cdot 2\,\mathrm{mS}\)
  (port otwarty), stąd \(V_N = 2 V_A\);
- węzeł \(N\): \(2\,\mathrm{mA} = (V_N - V_A) \cdot 2\,\mathrm{mS} = V_A \cdot 2\,\mathrm{mS}\),
  stąd \(V_A = 1\,\mathrm{V}\).

Zatem \(E_T = 1\,\mathrm{V}\).

**Opór wewnętrzny:** wyłączenie źródła prądowego (przerwa) odcina gałąź
szeregową — od zacisków widać tylko równoległe \(2\,\mathrm{mS}\):
\(R_T = 1/(2\,\mathrm{mS}) = 1/2\,\mathrm{k}\Omega\).

**E = 1 V, R = 1/2 kΩ** (odpowiedź 1).

## F. Maksymalna moc w oporze R (2 p.)

Układ: źródło prądowe \(2\,\mathrm{mA}\) z oporem \(2\,\mathrm{k}\Omega\)
równolegle, następnie \(2\,\mathrm{k}\Omega\) szeregowo do zacisku \(A\);
obciążenie \(R\) między \(A\) i \(B\).

- \(E_T = U_{oc} = 2\,\mathrm{mA} \cdot 2\,\mathrm{k}\Omega = 4\,\mathrm{V}\)
  (przy otwartym porcie cały prąd źródła płynie przez równoległy opór,
  brak spadku na szeregowym);
- \(R_T = 2\,\mathrm{k}\Omega + 2\,\mathrm{k}\Omega = 4\,\mathrm{k}\Omega\)
  (wyłączenie źródła prądowego — przerwa — zostawia oba opory szeregowo).

Moc maksymalna:
\[
P_{\max} = \frac{E_T^2}{4 R_T} = \frac{(4\,\mathrm{V})^2}{4 \cdot 4\,\mathrm{k}\Omega}
= 1\,\mathrm{mW}
\]

**P_max = 1 mW** (odpowiedź 1).

## G. Charakterystyka dwójnika AB z diodą (2 p.)

Dwójnik: dioda idealna \(D\) (katoda od strony zacisku \(A\)) w szereg z
oporem \(1\,\mathrm{k}\Omega\), a następnie równolegle połączenie źródła
\(1\,\mathrm{V}\) i oporu \(1\,\mathrm{k}\Omega\) do zacisku \(B\).
Napięcie \(u = V_A - V_B\), prąd \(i\) wchodzi przez \(A\).

Przyjmijmy \(V_B = 0\). Źródło \(1\,\mathrm{V}\) przybija potencjał węzła
\(M\) (za oporem): \(V_M = 1\,\mathrm{V}\).

- **Prąd \(i > 0\) (od A do B):** dioda jest spolaryzowana zaporowo
  (katoda przy \(A\)) — **prąd nie płynie**: \(i = 0\) dla \(u > 1\,\mathrm{V}\).
- **Prąd \(i < 0\) (od B do A):** dioda przewodzi (zwarcie); prąd płynie
  przez \(1\,\mathrm{k}\Omega\), a napięcie maleje:
  \[
  u = 1\,\mathrm{V} + i \cdot 1\,\mathrm{k}\Omega, \qquad i < 0
  \]
  czyli charakterystyka to odcinek prostej o nachyleniu \(-1\,\mathrm{mS}\)
  przechodzący przez punkt \((u, i) = (1\,\mathrm{V}, 0)\).

Zatem: \(i = 0\) dla \(u \ge 1\,\mathrm{V}\), a dla \(u < 1\,\mathrm{V}\)
linia \((u-1)/1\mathrm{k}\) — charakterystyka nr 1 na rysunkach odpowiedzi.

**Odpowiedź: wykres 1.**

## Kontrola wyników

Wszystkie wyniki zgodne z kluczem: A1/A2, B1/B2, C1, D1, E1, F1, G1.
