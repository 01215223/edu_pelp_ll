# PELP1 — Test 1 poprawka, wariant A_2 (11.12.2024) — rozwiązania

**Plik źródłowy:** [`PELP1_24Z_A_2_klucz.pdf`](../PELP1_24Z_A_2_klucz.pdf)

> Klucz w tym pliku może mieć więcej niż jedną odpowiedź prawidłową na pytanie (zaznaczonych pogrubieniem); do testu docelowego wybierano jedną prawidłową i trzy nieprawidłowe.

## Tabela odpowiedzi

| Pyt. | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Odp. | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Pkt  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |

---

## A. Opór zastępczy dwójnika AB (1 p.)

**Odpowiedź: 1 — \( R(1-k) \)**

Dwójnik AB: szeregowe połączenie rezystora \( R \) (górny przewód, od A) i **źródła napięciowego sterowanego napięciem** (VCVS) o wartości \( k u \) (romb, grot w górę, gałąź pionowa), do B. Napięcie sterujące \( u \) to napięcie **na rezystorze \( R \)**, z grotem zwróconym ku źródłu (strzałka pod \( R \) w lewo — \( u = \varphi_M - \varphi_A \), czyli \( u = -iR \)).

Krok 1 — prąd portu \( i \) płynie przez \( R \) (od A do węzła M), więc \( \varphi_A - \varphi_M = iR \).

Krok 2 — źródło sterowane ma wartość \( k u = -k i R \); jego grot wskazuje M (góra), więc \( \varphi_M - \varphi_N = k u = -k i R \).

Krok 3 — napięcie dwójnika (przez \( R \), źródło i przewód do B):

\[
u_{AB} = (\varphi_A - \varphi_M) + (\varphi_M - \varphi_N) + 0 = iR - k i R = iR(1-k)
\]

Stąd:

\[
R_{AB} = \frac{u_{AB}}{i} = R(1-k)
\]

**Kontrola:** dla \( k = 0 \) zostaje samo \( R \) ✓. Odpowiedź 2 (\( R(1+k) \)) to ten sam układ z przeciwnym grotem źródła sterowanego; odpowiedź 3 (\( R(k-1) \)) to błąd znaku; 4 i 5 to „rodzina równoległa" — dystraktory z innego archetypu.

---

## B. Bilans mocy z oporem nieliniowym (1 p.)

**Odpowiedź: 1 — zasady Tellegena**

Treść: źródło dostarcza 10 W, opór nieliniowy \( R_N \) pobiera 6 W — jaka zasada pozwala obliczyć moc \( P_R \)?

Zasada Tellegena (bilans mocy) mówi, że suma mocy wszystkich elementów obwodu wynosi zero — **bez względu na to, czy elementy są liniowe**:

\[
P_R = 10\ \text{W} - 6\ \text{W} = 4\ \text{W}
\]

Dlaczego nie pozostałe:
- superpozycja — wymaga liniowości, a \( R_N \) jest nieliniowy;
- kompensacja — służy do zastępowania gałęzi źródłem, nie do bilansu mocy;
- „niezbędna jest wartość R" — fałsz: moc wynika z bilansu, nie z \( U^2/R \).

**To jest cała siła Tellegena:** odpowiedź bez znajomości charakterystyki elementu nieliniowego.

---

## C. Od czego zależy prąd I (1 p.)

**Odpowiedź: 1 — nie zależy od wartości R2**

Topologia: \( R_1 \) — lewa gałąź pionowa; \( E \) — środkowa gałąź pionowa (grot w górę); \( R_2 \) — górny przewód poziomy; \( J \) — prawa gałąź pionowa (grot w górę); prąd \( I \) — w **gołym przewodzie** łączącym szczyt \( R_1 \) ze szczytem \( E \) (strzałka w prawo).

Krok 1 — szczyt \( R_1 \) jest połączony gołym przewodem ze szczytem \( E \), więc to jeden węzeł, a źródło \( E \) narzuca jego potencjał: \( \varphi = E \).

Krok 2 — prąd przez \( R_1 \) (jedyna droga z jego szczytu to przewód z \( I \)):

\[
I = \frac{E}{R_1}
\]

Krok 3 — prawa strona (\( R_2 \) i \( J \)) to **bramka prądowa**: \( J \) wtłacza prąd przez \( R_2 \) do węzła \( E \) niezależnie od wartości \( R_2 \), a ten prąd wpływa do źródła \( E \), które go „połyka". Na prąd \( I \) nie ma to wpływu.

Wnioski: \( I = E/R_1 \) — **nie zależy od \( R_2 \)** (odpowiedź 1 ✓), nie zależy od \( J \), \( I \neq 0 \), jest w pełni określone.

---

## D. Wzmacniacz operacyjny — napięcie U (1 p.)

**Odpowiedź: 1 — \( -\dfrac{E}{3} \)**

Układ: wzmacniacz odwracający — wejście (−) zasilane przez \( 3R \) ze źródła \( E \); wejście (−) dodatkowo oporem \( 2R \) do masy; sprzężenie zwrotne oporem \( R \) z wyjścia; wejście (+) na masie; \( U \) — napięcie wyjściowe.

Krok 1 — wejście (+) na masie i pętla zamknięta ⇒ masa urojona:

\[
u_- = u_+ = 0
\]

Krok 2 — KCL w węźle (−) (prądy wejściowe wzmacniacza zerowe):

\[
\frac{E - 0}{3R} + \frac{U - 0}{R} + \frac{0 - 0}{2R} = 0
\]

(ostatni składnik — prąd przez \( 2R \) — wynosi zero, bo oba końce są na masie urojonej).

Krok 3:

\[
\frac{E}{3R} = -\frac{U}{R} \quad\Rightarrow\quad U = -\frac{E}{3}
\]

**Kontrola:** to klasyczny wzmacniacz odwracający o wzmocnieniu \( -R_{spr}/R_{we} = -R/(3R) = -1/3 \). Opór \( 2R \) to dystraktor — wisi między masą urojoną a masą i nie płynie nim żaden prąd.

---

## E. Natężenie prądu I (1 p.)

**Odpowiedź: 1 — układ jest sprzeczny**

Figura: trzy obszary (górny, dolny-lewy, dolny-prawy) i węzeł centralny. Strzałki:
- górny → centralny: \( 1\ \text{A} \),
- dolny-lewy → centralny: \( I \),
- dolny-prawy → centralny: \( 3\ \text{A} \),
- dolny-lewy → górny: \( 1\ \text{A} \),
- górny → dolny-prawy: \( 2\ \text{A} \),
- dolny-lewy ↔ dolny-prawy: bez etykiety.

Krok 1 — KCL w górnym obszarze: wpływający prąd z dolnego-lewego to \( 1\ \text{A} \), a wypływają \( 1\ \text{A} \) (do środka) i \( 2\ \text{A} \) (do dolnego-prawego):

\[
1 = 1 + 2 = 3 \quad\Rightarrow\quad \text{sprzeczność}
\]

Krok 2 — kontrola przez środek: \( 1 + I + 3 = 0 \Rightarrow I = -4\ \text{A} \) — i właśnie to jest pułapka (odpowiedź 2): rachunek „działa", ale obwód jako całość nie istnieje, więc żadna wartość \( I \) nie jest odpowiedzią.

**Wskazówka (kompendium §7.3):** przy figurach z prądami zawsze najpierw sprawdź bilans każdego obszaru — jeśli którykolwiek nie domyka się jednoznacznie (suma wymuszonych prądów ≠ 0), poprawna odpowiedź to „układ jest sprzeczny".

---

## F. Superpozycja — składowa od E1 (1 p.)

**Odpowiedź: 1 — \( \dfrac{E_1}{R_1} \)**

Topologia: \( E_1 \) (skrajna lewa gałąź, grot w górę) z \( R_1 \) w górnym przewodzie; \( E_2 \) (druga gałąź pionowa, grot w dół) — nad nim mierzony prąd \( I \) (strzałka w dół); \( R_2 \) — trzecia gałąź pionowa; \( J \) — skrajna prawa gałąź pionowa.

Superpozycja — tylko źródło \( E_1 \):
- \( E_2 \to \) zwarcie,
- \( J \to \) rozwarcie.

Obwód redukuje się do: \( E_1 \) — \( R_1 \) — węzeł szczytu \( E_2 \), z którego na dół idzie **zwarcie** (zwarzone \( E_2 \)) do dolnej szyny. Zwarcie wymusza \( \varphi = 0 \) w tym węźle, więc całe napięcie \( E_1 \) odkłada się na \( R_1 \):

\[
I = \frac{E_1}{R_1}
\]

Prąd płynie w dół przez gałąź \( E_2 \) (zgodnie ze strzałką \( I \)) — zgodnie z pętlą: \( E_1 \to R_1 \to \) zwarcie \( \to \) dół.

**Kontrola:** w wyniku nie ma śladu \( E_2 \), \( J \), \( R_2 \) ✓. Dystraktory \( \pm E_1\frac{R_1+R_2}{R_1 R_2} \) to pomyłka „dzielenia przez opór równoważny zamiast samego \( R_1 \)"; 0 — błąd „źródło w środku nic nie wnosi".

---

## G. Moc maksymalna w oporze R (2 p.)

**Odpowiedź: 1 — \( 8\ \text{mW} \)**

Topologia: opór \( 4\ \text{k}\Omega \) równolegle ze źródłem prądowym \( 4\ \text{mA} \) (grot w górę) — dwie lewe gałęzie pionowe; z ich wspólnego szczytu opór \( 4\ \text{k}\Omega \) w górnym przewodzie do zacisku A; B na dolnej szynie; obciążenie \( R \) między A i B.

Krok 1 — napięcie rozwarcia (R odłączone): przez górny \( 4\ \text{k}\Omega \) nie płynie prąd (zacisk A otwarty), więc całe \( 4\ \text{mA} \) źródła płynie przez lewy \( 4\ \text{k}\Omega \):

\[
U_{oc} = 4\ \text{mA} \cdot 4\ \text{k}\Omega = 16\ \text{V}
\]

Krok 2 — opór Thévenina (źródło prądowe rozwieramy): z portu A-B widak szereg dwóch \( 4\ \text{k}\Omega \):

\[
R_T = 4\ \text{k}\Omega + 4\ \text{k}\Omega = 8\ \text{k}\Omega
\]

Krok 3 — moc maksymalna:

\[
P_{max} = \frac{U_{oc}^2}{4 R_T} = \frac{256}{32\,000} = 8\ \text{mW}
\]

**Kontrola:** dystraktor 16 mW to \( U_{oc}^2/R_T \) (moc przy zwarciu) albo wynik z pominięciem jednego \( 4\ \text{k}\Omega \) w \( R_T \); 32 mW — \( U_{oc}^2 \cdot R_T \) z błędnym wymiarem; 4 mW i 2 mW — źle policzone \( U_{oc} \).

---

## H. SEM źródła Thévenina dwójnika AB (1 p.)

**Odpowiedź: 1 — \( 1\ \text{V} \)**

Dwójnik AB: szereg — źródło \( 2\ \text{V} \) (grot w lewo, biegun + od strony źródła sterowanego), potem **źródło napięciowe sterowane napięciem** \( 3u \) (romb, grot w górę), potem \( 2\ \text{k}\Omega \), do B. Napięciem sterującym \( u \) jest **napięcie portu** (strzałka w górę od B do A).

Stan jałowy (rozwarte zaciski A-B): prąd dwójnika \( i = 0 \), więc:
- na \( 2\ \text{k}\Omega \) nie ma spadku: \( \varphi_N = \varphi_B \),
- źródło sterowane ma wartość \( 3u = 3 U_{oc} \), a jego grot wskazuje węzeł po stronie źródła 2 V: \( \varphi_M - \varphi_N = 3 U_{oc} \),
- źródło 2 V (grot w lewo, + od strony M): \( \varphi_M - \varphi_A = 2 \), czyli \( \varphi_A - \varphi_M = -2 \).

Równanie na napięcie rozwarcia:

\[
U_{oc} = \varphi_A - \varphi_B = (\varphi_A - \varphi_M) + (\varphi_M - \varphi_N) = -2 + 3 U_{oc}
\]

\[
U_{oc} - 3U_{oc} = -2 \quad\Rightarrow\quad -2 U_{oc} = -2 \quad\Rightarrow\quad U_{oc} = 1\ \text{V}
\]

**Kontrola podstawienia:** \( U_{oc} = 1\ \text{V} \Rightarrow \) źródło sterowane \( = 3\ \text{V} \); spadki: \( -2 + 3 = 1 \) ✓. To zadanie na równanie na „samą szukaną" (kompendium §5.2): obwód ze źródłem sterowanym wielkością, której szukasz, zawsze rozwiąż jednym równaniem, a nie „po kolei".

---

## Kontrola wyników

| Pyt. | Odpowiedź | Szybki test poprawności |
|------|-----------|--------------------------|
| A | \( R(1-k) \) | \( u_{AB} = iR + ku = iR - kiR \) (źródło przeciw) |
| B | 1 | Tellegen: \( P_R = 10 - 6 = 4\ \text{W} \), bez liniowości |
| C | 1 | \( I = E/R_1 \); \( R_2 \) i \( J \) to bramka poza pętlą |
| D | \( -E/3 \) | masa urojona; \( E/(3R) + U/R = 0 \) |
| E | sprzeczny | górny obszar: \( 1 \neq 1+2 \); pułapka \( I = -4 \) A |
| F | \( E_1/R_1 \) | \( E_2 \) zwarte, \( J \) rozwarte; zwarcie wymusza \( \varphi = 0 \) |
| G | 8 mW | \( U_{oc} = 16\ \text{V} \), \( R_T = 8\ \text{k}\Omega \); \( 256/32\,000 \) |
| H | 1 V | \( U_{oc} = -2 + 3U_{oc} \Rightarrow U_{oc} = 1 \) |
