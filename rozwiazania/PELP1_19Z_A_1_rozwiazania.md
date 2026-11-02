# Test 1 PELP1 (30.10.2019, wariant A) — pełne rozwiązania

Rozwiązania do pliku [`PELP1_19Z_A_1_klucz.pdf`](../PELP1_19Z_A_1_klucz.pdf).
W kluczu każde pytanie może mieć więcej niż jedną odpowiedź prawidłową (są one
wyróżnione pogrubieniem); do testu docelowego wybierana jest jedna z nich.
Poniżej pełny rachunek krok po kroku.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | Σ |
|---|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 | 1 | 1 (≈2) | 1 | 1 i 2 | 1 | 9 pkt |

## A. Napięcie na oporze 10 Ω po zastąpieniu 2 Ω zwarciem (1 p.)

Obwód to jedna pętla szeregową: źródło prądowe 1 A, opór 10 Ω, opór 2 Ω,
źródło napięciowe 6 V.

- Źródło prądowe **wymusza** prąd 1 A w całej pętli — niezależnie od tego,
  co jeszcze jest w szeregu (2 Ω, 6 V, zwarcie — bez znaczenia).
- Napięcie na 10 Ω: \(U = 1\,\mathrm{A} \cdot 10\,\Omega = 10\,\mathrm{V}\).

Po zastąpieniu 2 Ω zwarciem prąd nadal wynosi 1 A, więc napięcie na 10 Ω
**nie zmieni się** (odpowiedź 1).

## B. Wkład źródła E w prąd I — superpozycja (1 p.)

Źródła J (prądowe), R i E połączone są równolegle; I to prąd przez R.

Superpozycja: wyłączamy źródło prądowe J (zastępujemy je **przerwą**).
Zostaje samo źródło E przyłączone bezpośrednio do R:

\[
I_E = \frac{E}{R}
\]

Wkład od E: **E/R** (odpowiedź 1).

## C. SEM źródła zastępczego Thévenina (1 p.)

10 V — 4 Ω (szereg) — węzeł; z węzła 6 Ω do dolnej szyny; z węzła 12 Ω
poziomo do zacisku wyjściowego (obwód otwarty).

- Zaciski wyjściowe są otwarte → przez 12 Ω nie płynie prąd → **brak spadku
  napięcia na 12 Ω**, więc \(E_{th}\) równa się napięciu na węźle.
- Prąd w pętli: \(I = \frac{10\,\mathrm{V}}{4\,\Omega + 6\,\Omega} = 1\,\mathrm{A}\).
- \(E_{th} = I \cdot 6\,\Omega = 6\,\mathrm{V}\).

**E_th = 6 V** (odpowiedź 1).

## D. Równanie lewego oczka (1 p.)

Lewe oczko zawiera źródło 5 V, opór 3 Ω (prąd I1) i opór 7 Ω (prąd I2).
Idąc po oczku zgodnie z kierunkiem napięcia źródła:

\[
5\,\mathrm{V} + 7\,\Omega \cdot I_2 - 3\,\Omega \cdot I_1 = 0
\]

To **odpowiedź 1**. Uwaga: odpowiedź 2 (\(3\Omega I_1 - 5\,\mathrm{V} = 7\Omega I_2\))
jest z tego samego równania przekształcona algebraicznie — w kluczu obie są
pogrubione jako prawidłowe.

## E. Moc oddawana przez źródło napięciowe (2 p.)

Stan ustalony DC: **cewki = zwarcie, kondensatory = przerwa**.

- Kondensator 10 µF w szereg z prawą częścią obwodu (20 kΩ, 1 µF, 50 mH)
  → przerwa → ta część **nie przewodzi prądu stałego**.
- Zostaje: 10 V — 1 kΩ — (4 kΩ + zwarta cewka 10 mH) = 5 kΩ.
- \(I = \frac{10\,\mathrm{V}}{5\,\mathrm{k}\Omega} = 2\,\mathrm{mA}\)
- \(P = U \cdot I = 10\,\mathrm{V} \cdot 2\,\mathrm{mA} = 20\,\mathrm{mW}\)

**P = 20 mW** (odpowiedź 1).

## F. Opory równoległe w obwodzie DC (1 p.)

Zawsze prawdziwe:

1. **W małym oporze wydziela się większa moc niż w dużym** — bo
   \(P = U^2/R\) przy wspólnym napięciu U.
2. **Na wszystkich oporach występuje takie samo napięcie** — to definicja
   połączenia równoległego.

W kluczu obie odpowiedzi (1 i 2) są pogrubione.

## G. Prąd przez opór 3 Ω (2 p.)

Topologia (węzły: T — górna szyna, D — dolna szyna, M — środek):
- 6 Ω: T→M, 3 Ω: T→M (równolegle), 4 Ω: M→D,
- 12 Ω: T→D, 16 Ω: T→D, źródło 12 V: T→D.

Rachunek:

1. Gałąź środkowa: \(6\,\Omega \parallel 3\,\Omega = 2\,\Omega\), szeregowo
   z 4 Ω → \(R_{gałązi} = 6\,\Omega\).
2. Prąd gałęzi: \(I_{g} = \frac{12\,\mathrm{V}}{6\,\Omega} = 2\,\mathrm{A}\).
3. Podział prądu między 6 Ω i 3 Ω:
   \[
   I_{3\Omega} = I_g \cdot \frac{6\,\Omega}{6\,\Omega + 3\,\Omega}
   = 2\,\mathrm{A} \cdot \tfrac{2}{3} = \tfrac{4}{3}\,\mathrm{A}
   \]

**I(3 Ω) = 4/3 A ≈ 1,33 A** (odpowiedź 1).

## Kontrola wyników

Wszystkie powyższe wyniki zgodne z kluczem (odpowiedzi pogrubione w
`PELP1_19Z_A_1_klucz.pdf`): A1, B1, C1, D1/D2, E1, F1/F2, G1.
