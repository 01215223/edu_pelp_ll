# Test 1 PELP1 (03.11.2021, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_21Z_A_1_klucz.pdf`](../PELP1_21Z_A_1_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H | Σ |
|---|---|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1, 2 | 1, 2 | 1 | 1 | 1 | 1 | 1 | 9 pkt |

## A. Opór zastępczy dwójnika [gu ∥ G] (1 p.)

Dwójnik AB: źródło prądowe sterowane \(gu\) (romb) połączone **równolegle**
z konduktancją \(G\) między zaciskami \(A\) i \(B\); napięcie sterujące \(u\)
to napięcie portowe.

Prąd płynący do zacisku \(A\) rozdziela się na gałąź konduktancji i gałąź
źródła sterowanego, przy czym prąd źródła sterowanego **sumuje się** z prądem
konduktancji (zwroty zgodne dla napięcia portowego):

\[
i_{AB} = Gu + gu = (G+g)\,u
\]

\[
R_{AB} = \frac{u}{i_{AB}} = \frac{1}{G+g}
\]

**Odpowiedź: 1 (\(1/(g+G)\)).**

Kontrola: \(g = 0\) daje \(1/G = R\) ✔ (sama konduktancja). Dystraktory
\(1/(G-g)\) i \(1/(g-G)\) to wariant z przeciwnym zwrotem źródła sterowanego
(grot rombu w przeciwną stronę); \(gG/(g-G)\) — błąd rachunkowy przy
składaniu konduktancji. Zauważ: \(g\) ma wymiar konduktancji [S], więc
\(g+G\) składa się poprawnie.

## B. Układ z oporem nieliniowym RN (1 p.)

Układ: \(J \parallel R_N\) po lewej, \(E\) w górnej szynie, port \(A\)–\(B\),
po prawej dwa opory \(R\) równolegle; \(I\) to prąd w górnej szynie **między
tymi dwoma oporami** (płynie w prawo, do drugiego z nich).

Prawdziwe są **dwie** opcje:

1. **do obliczenia prądu \(I\) można użyć dzielnika prądowego** ✔ — prąd
   dopływający do węzła górnego rozdziela się na dwie **równe** gałęzie
   \(R \parallel R\); dzielnik prądowy daje \(I = \tfrac{1}{2} i_A\)
   (gałąź „dalsza” dostaje połowę);
2. **nie obowiązuje zasada superpozycji** ✔ — w układzie jest element
   nieliniowy (\(R_N\)), więc odpowiedzi nie można składać z wkładów
   poszczególnych źródeł.

Fałszywe:

- 3 — twierdzenie Tellegena obowiązuje w **każdym** układzie (wynika z
  samej topologii i bilansu mocy);
- 4 — prądowe prawo Kirchhoffa to aksjomat teorii obwodów, obowiązuje
  zawsze;
- 5 — dwójnik z \(R_N\) (elementem nieliniowym) **nie** ma liniowego
  zastępczego źródła Thévenina;
- 6 — \(R_N\) z definicji nie spełnia prawa Ohma.

**Odpowiedź: 1, 2.**

## C. Od czego zależy napięcie U na źródle prądowym J (1 p.)

Układ: \(J\) (z napięciem \(U\)) po lewej; \(R_1\) i \(E_1\) szeregowo w
górnej szynie; po prawej \(R_2 \parallel E_2\) między szyną górną a dolną.

Źródło prądowe \(J\) wymusza swój prąd w jedynej dostępnej drodze: przez
\(R_1\) i \(E_1\) do węzła prawego. Węzeł prawy jest przyłączony do
**idealnego źródła \(E_2\)**, które narzuca jego potencjał niezależnie od
\(R_2\) (przez \(R_2\) płynie po prostu inny prąd — pochodzący od \(E_2\)).

Napięcie na \(J\) (idąc od masy w lewo):

\[
U = E_2 \pm E_1 + J R_1
\]

Wniosek:

- \(U\) **zależy od \(E_1\)** (opcja 1 ✔),
- \(U\) **nie zależy od \(R_2\)** (opcja 2 ✔ — bo \(R_2\) jest równoległe
  do idealnego źródła \(E_2\), które „nie puszcza” napięcia węzła).

Fałszywe: \(U \ne 0\) (3); \(U\) **zależy** od \(E_2\) (4); **zależy** od
\(J\) (5); nie od wszystkich elementów — \(R_2\) nie występuje (6).

**Odpowiedź: 1, 2.**

To ten sam motyw co w teście z 24.03.2021 (pytanie C): **idealne źródło
napięciowe w równoległości z oporem kasuje wpływ tego oporu na napięcia**.

## D. Wzmacniacz operacyjny — od czego zależy U (1 p.)

Układ: \(J \parallel R_1\) przy wejściowym węźle; stąd \(R_2\) do wejścia
\(+\); \(R_3\) (z dodatkowym oporem) w pętli sprzężenia zwrotnego do wejścia
\(-\); \(U\) na wyjściu.

Wzmacniacz idealny: \(i_+ = i_- = 0\), \(u_+ = u_-\).

- Przez \(R_2\) (szeregowo z wejściem \(+\)) **nie płynie prąd** → brak
  spadku → \(u_+\) równa się napięciu węzła \(J \parallel R_1\), czyli
  \(J R_1\).
- \(u_+ = u_- = J R_1\); w pętli sprzężenia zwrotnego nie płynie prąd
  (\(i_- = 0\)) → brak spadków na \(R_3\) (i każdym oporze pętli) →
  \(U = J R_1\).

Na \(U\) wpływa więc **tylko \(R_1\)**.

**Odpowiedź: 1 (tylko R1).**

## E. Natężenie prądu I (1 p.)

Na górnym przewodzie wymuszony prąd \(1\,\mathrm{A}\) dopływa do węzła, na
dolnym \(2\,\mathrm{A}\) — oba „wpadają” do przewodu łączącego (prąd
poprzeczny \(I\) skierowany w dół):

\[
I = 1\,\mathrm{A} + 2\,\mathrm{A} = 3\,\mathrm{A}
\]

**Odpowiedź: 1 (3 A).**

KCL nie potrzebuje znajomości elementów — dlatego opcje „nie da się
określić bez znajomości elementów/napięć” są fałszywe. Dystraktor \(-3\,\mathrm{A}\)
to ten sam bilans z przeciwnym zwrotem strzałki \(I\).

## F. Superpozycja: składowa napięcia U od źródła J (1 p.)

Układ: cztery gałęzie pionowe: \(E_1\) (lewa), \(E_2\) (strzałka w dół),
\(R_2\) (z napięciem \(U\)) i \(J\) (prawa); \(R_1\) poziomo między
gałęziami \(E_1\) i \(E_2\); górna szyna łączy wszystkie gałęzie.

Liczymy wkład od **samego \(J\)**: \(E_1 \to\) zwarcie, \(E_2 \to\) zwarcie.
Wtedy górna szyna jest przez zwarcie \(E_2\) połączona bezpośrednio z szyną
dolną — **cały port (wraz z \(R_2\)) jest zwarty**, a prąd \(J\) krąży
wyłącznie w pętli \(J\)–zwarcie:

\[
U^{(J)} = 0
\]

**Odpowiedź: 1 (0).**

Dystraktory \(\pm J R_1 R_2/(R_1+R_2)\) to klasyczny błąd: traktowanie
\(R_2\) jak części dzielnika, podczas gdy zwarcie źródła \(E_2\) kładzie się
**równolegle** do \(R_2\) i wyzeruje napięcie.

## G. Moc maksymalna w oporze R (2 p.)

Dwójnik zasilający: źródło \(6\,\mathrm{V}\) szeregowo z \(6\,\mathrm{k\Omega}\),
\(3\,\mathrm{k\Omega}\) równolegle z portem \(A\)–\(B\); odbiornik \(R\).

**Krok 1 — SEM Thévenina** (dzielnik 6k–3k):

\[
E_T = 6\,\mathrm{V} \cdot \frac{3}{6+3} = 2\,\mathrm{V}
\]

**Krok 2 — opór Thévenina** (źródło 6 V zwarte):

\[
R_T = 6\,\mathrm{k\Omega} \parallel 3\,\mathrm{k\Omega} = 2\,\mathrm{k\Omega}
\]

**Krok 3 — moc maksymalna** (dopasowanie \(R = R_T\)):

\[
P_{\max} = \frac{E_T^2}{4 R_T} = \frac{2^2}{4 \cdot 2000} = 0{,}5\,\mathrm{mW}
\]

**Odpowiedź: 1 (1/2 mW).**

Kontrola: moc przy zwarciu portowym wyniosłaby \(6^2/6\,\mathrm{k\Omega} =
6\,\mathrm{mW}\); moc maksymalna (na \(R_T\)) musi być 4 razy mniejsza od
mocy zwarciowej źródła idealnego i mniejsza od mocy oddawanej do samego
\(R_T\) — \(\tfrac{1}{2}\,\mathrm{mW}\) spełnia oba warunki.

## H. Charakterystyka dwójnika z diodą idealną (1 p.)

Dwójnik AB: \([D \parallel 1\,\mathrm{k\Omega}]\) szeregowo z
\([1\,\mathrm{V} \parallel 1\,\mathrm{k\Omega}]\); dioda: anoda od strony
\(A\); źródło \(1\,\mathrm{V}\) zwrócone przeciwnie do napięcia portowego
(znak „\(+\)” po stronie \(B\)); \(u\) — napięcie portowe, \(i\) — prąd
wpływający do \(A\).

Źródło idealne \(1\,\mathrm{V}\) w równoległości z oporem narzuca na drugim
bloku stały spadek, więc **cały dwójnik zachowuje się jak \([D \parallel
1\,\mathrm{k\Omega}]\) przesunięty o \(-1\,\mathrm{V}\)**:

- **dioda przewodzi** (\(i \ge 0\)): dioda idealna = zwarcie → \(v_1 = 0\)
  → \(u = -1\,\mathrm{V}\); prąd dowolny nieujemny — **pionowa półprosta
  przy \(u = -1\,\mathrm{V}\) skierowana w górę**;
- **dioda zatkana** (\(u < -1\,\mathrm{V}\)): prąd płynie przez
  \(1\,\mathrm{k\Omega}\) pierwszego bloku:

\[
i = \frac{u+1}{1\,\mathrm{k\Omega}}
\]

— **prosta o nachyleniu \(1\,\mathrm{mA/V}\) przechodząca przez punkt
\((-1\,\mathrm{V},\,0)\)**, rozciągnięta w trzecią ćwiartkę.

Taki kształt (pionowy promień w górę + prosta o nachyleniu \(1\,\mathrm{mA/V}\)
odchylona o \(-1\,\mathrm{V}\)) ma **wykres 1**.

**Odpowiedź: 1.**

Dlaczego pozostałe nie: wykresy 3 i 5 mają punkt załamania w
\((-1\,\mathrm{V},0)\), ale 3 kończy się odcinkiem poziomym (dioda nigdy nie
zwiera), a 5 ma promień skierowany **w dół** (dioda złączona przeciwnie);
wykres 2 to lustrzane odbicie (nachylenie ujemne), a 4 ma promień w dół od
punktu \((0,-1\,\mathrm{mA})\).

## Kontrola wyników

| Pyt. | Wynik | Klucz |
|---|---|---|
| A | \(1/(G+g)\) | ✔ |
| B | 1, 2 | ✔ |
| C | 1, 2 | ✔ |
| D | tylko R1 | ✔ |
| E | 3 A | ✔ |
| F | 0 | ✔ |
| G | 1/2 mW | ✔ |
| H | wykres 1 | ✔ |

Wszystkie wyniki zgadzają się z kluczem (pogrubione odpowiedzi w pliku
`PELP1_21Z_A_1_klucz.pdf`).
