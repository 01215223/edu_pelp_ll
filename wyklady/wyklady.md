# Komentarz do wykładów PELP1

Ten dokument to **studenckie objaśnienie pięciu wykładów** z Podstaw elektroniki i teorii
obwodów (PELP1, Instytut Systemów Elektronicznych PW, dr inż. Ł. Maślikowski):

| Wykład | Data | Temat | Slajdów |
|---|---|---|---|
| W1 | 6.10.2021 | Modele elementów | 17 |
| W2 | 3.03.2021 | Prawa i zasady obwodowe | 16 |
| W3 | 10.03.2021 | Elementy zastępcze | 18 |
| W4 | 17.03.2021 | Elementy nieliniowe · wzmacniacz operacyjny · moc | 17 |
| W5 | 24.03.2021 | Sygnały okresowe i ich parametry | 17 |

Nie jest to streszczenie „slajd po slajdzie”. Każde pojęcie z wykładu jest tu
**przetłumaczone na język zadań**: co dokładnie znaczy definicja, jak wygląda
rachunek, gdzie student najczęściej traci punkty, i — najważniejsze — **jak
używa się twierdzeń i zasad** (superpozycji, kompensacji, ruchliwości źródeł,
Thévenina/Nortona, Tellegena) w konkretnym obwodzie.

Odsyłacze w nawiasach kwadratowych wskazują slajd źródłowy, np. `[W3/s.14]`
to slajd 14 wykładu 3. Na końcu jest **indeks wszystkich 85 slajdów** z
odesłaniem do sekcji komentarza.

::: ciekawostka Dlaczego „komentarz”, a nie skrypt
Slajdy są bardzo gęste: jedna plansza = jedna definicja albo jedna zasada, bez
przykładu rachunkowego (na wykładzie przykład jest liczony ustnie). Ten
dokument uzupełnia je o to, czego na slajdach nie ma: **rachunki, sprawdzenia,
kontrprzykłady i typowe pomyłki**. Wszystkie przykłady są policzone do końca i
sprawdzone drugą metodą — tak, jak trzeba to robić na kolokwium.
:::

## Jak czytać ten komentarz

Trzy poziomy lektury:

* **przed wykładem / w trakcie** — czytaj ramki **Definicja** i
  **Wzór**; to jest dokładnie treść slajdu w jednym akapicie;
* **przed kolokwium** — czytaj ramki **Metoda**, **Przykład**
  i **Pułapka**; to esencja rachunkowa;
* **w trakcie rozwiązywania** — rozdział 6 („jak korzystam z twierdzeń”) i
  rozdział 7 (ściąga) to zestaw procedur i wzorów pod ręką.

Notacja jest ta sama co na slajdach: mała litera = przebieg zmienny
($u = u(t)$), wielka litera = wartość stała lub parametr ($I = \mathrm{const}$).
Wartości liczbowe podano w jednostkach SI z przedrostkami ($\mathrm{k\Omega}$,
$\mathrm{mA}$), a w obliczeniach pośrednich — bez przedrostków, żeby nie mnożyć
błędów rzędu.

::: zapamietaj Trzy pytania, które zadaj sobie przed każdym zadaniem
1. **Czy obwód jest liniowy?** (czy są elementy nieliniowe, diody, źródła sterowane)
2. **Ile jest źródeł niezależnych** i czy szukam jednej wielkości, czy wszystkich?
3. **Czego szukam: prądu/napięcia, mocy, czy punktu pracy?** (moc i punkt pracy
   rządzą się innymi prawami niż prądy i napięcia)

Odpowiedź na te trzy pytania wskazuje metodę — dokładnie temu służy tabela
decyzyjna w §6.2.
:::

## Mapa wykładów

| Wykład | Co naprawdę ustala | Co z tego wynika w zadaniach |
|---|---|---|
| W1 | model elementu skupionego, strzałkowanie, równania elementów | każdy dalszy rachunek opiera się na poprawnym zapisie $u = Ri$ albo $u = -Ri$ |
| W2 | MPK/OPK, połączenia, dzielniki, kompensacja, ruchliwość źródeł, superpozycja | kompletny układ równań obwodu i pierwsze „skróty” obliczeniowe |
| W3 | dwójnik zastępczy, $R_z$, zamiana źródeł, Thévenin/Norton | redukcja całego obwodu do jednego źródła rzeczywistego |
| W4 | WO, elementy nieliniowe, moc, dopasowanie | punkt pracy, moc chwilowa, moc dysponowana |
| W5 | sygnały okresowe: wartość średnia, RMS, współczynniki | jak z przebiegu zrobić liczbę (moc, wskazanie miernika) |

## 1. Wykład 1 — modele elementów

### 1.1 Od równań Maxwella do elementu skupionego

Wykład zaczyna się od równań Maxwella `[W1/s.3]` i natychmiast je „wyłącza” —
nie po to, żeby ich nie znać, ale żeby pokazać, **na jakim uproszczeniu stoi
cała teoria obwodów**: na założeniu pola **quasi-stacjonarnego** `[W1/s.4]`.

::: def Definicja — element skupiony
Element skupiony to model **jednej** właściwości fizycznej (rezystancji,
pojemności, indukcyjności, źródła). Właściwość jest „zamknięta” w elemencie,
element kontaktuje się ze światem wyłącznie przez **zaciski**, a zależność
między wielkościami na zaciskach opisuje **równanie elementu**. Nie opisujemy
położenia elementów w przestrzeni — tylko **sposób ich połączenia**.
:::

::: metoda Kiedy wolno użyć modelu skupionego
Warunek praktyczny: **największy wymiar układu $l$ musi być znacznie mniejszy
od długości fali** $\lambda = c/f$ (dla pól w powietrzu) lub $\lambda = v/f$
w ośrodku. Jeżeli $l \lesssim \lambda/10$, model skupiony jest dobry; w
przeciwnym razie trzeba modelu o **stałych rozłożonych** (linia długa).
:::

Liczby, które warto pamiętać:

| Częstotliwość | Długość fali $\lambda$ | Wniosek dla płytki drukowanej 10 cm |
|---|---|---|
| 50 Hz | 6000 km | element skupiony — zawsze |
| 1 MHz | 300 m | element skupiony |
| 30 MHz | 10 m | na granicy (10 cm to $\lambda/100$) |
| 1 GHz | 30 cm | **nie** — 10 cm to już $\lambda/3$, potrzebna linia |

To właśnie dlatego na schematach z wykładu można „zwierać” przewody: przy
50 Hz potencjał wzdłuż przewodu jest ten sam **w każdej chwili**.

### 1.2 Klasyfikacja elementów — cztery osie

`[W1/s.7]` Slajd podaje cztery niezależne podziały. Każdy z nich ma
bezpośrednie znaczenie rachunkowe:

| Podział | Kategorie | Co z tego wynika |
|---|---|---|
| liczba zacisków | dwójniki, czwórniki (wielowrotniki) | dwójnik opisują dwa parametry $u$, $i$; czwórnik — cztery |
| stacjonarność | stacjonarne / niestacjonarne | równanie o **stałych** współczynnikach (można używać $R$, $C$, $L$ jako liczb) |
| liniowość | liniowe / nieliniowe | **tylko liniowe** podlegają superpozycji, Théveninowi, zamianie źródeł |
| aktywność | aktywne / pasywne | aktywne mogą oddawać energię; pasywne tylko pobierać (albo oddawać zmagazynowaną) |

Dodatkowo slajd wprowadza pojęcie elementu **bezźródłowego**: takiego, który
może przyjąć stan $u = 0$, $i = 0$ — nawet jeśli w jego wnętrzu **są** źródła.
To nie jest to samo co „pasywny”: dwójnik ze źródłem sterowanym jest
bezźródłowy, ale bywa aktywny (potrafi oddać moc — patrz §3.4).

::: pulapka „Liniowy” nie znaczy „prosty”
Liniowość to własność **równania**, nie wyglądu charakterystyki. Opór liniowy
ma prostą charakterystykę, ale źródło napięciowe $u = E$ też jest liniowe
(choć jego charakterystyka jest pozioma). Z kolei dioda jest nieliniowa mimo
prostego, „klockowego” opisu. Gdy w obwodzie jest dioda, **superpozycja i
Thévenin nie obowiązują dla całości obwodu** — dzieli się go na część liniową
i nieliniową (§4.7).
:::

### 1.3 Strzałkowanie i równania elementów

To jest miejsce, w którym traci się najwięcej punktów za „dobry wynik ze złym
znakiem”. Slajdy `[W1/s.5, s.12]` i `[W2/s.6]` mówią to samo z dwóch stron:

::: def Definicja — dwie konwencje strzałkowania
* **Strzałki przeciwne** (konwencja odbiornikowa, „naturalna” dla $R$):
  strzałka napięcia wskazuje **wyższy potencjał**, strzałka prądu — kierunek
  ruchu ładunków dodatnich. Wtedy $u = Ri$, $p = ui > 0$ — element pobiera moc.
* **Strzałki zgodne** (konwencja nadawcza): wtedy w równaniu elementu
  biernego **pojawia się minus**: $u = -Ri$, a moc pobierana $p = -ui$.
:::

Dla źródeł jest **odwrotnie**: równanie źródła definiujemy przy strzałkach
**zgodnych** (napięcie źródła i prąd źródła w tę samą stronę), bo wtedy
$p_o = ei > 0$ oznacza, że źródło **oddaje** moc do obwodu.

::: wzor Równania elementów a strzałkowanie
**Opór:** przy strzałkach **przeciwnych** $u = Ri$; przy strzałkach
**zgodnych** $u = -Ri$.

**Źródła** (definicja przy strzałkach **zgodnych**): napięciowe $u = E$,
prądowe $i = J$.
:::

::: przyklad Przykład 1.1 — ten sam opór, dwa zapisy
Opór $R = 4\ \Omega$ włączono w obwód tak, że prąd $i = 2\ \mathrm{A}$ płynie
zgodnie ze strzałką napięcia (strzałki zgodne). Ile wynosi $u$ i moc?

**Rachunek (wariant „zgodny”):** $u = -Ri = -4 \cdot 2 = -8\ \mathrm{V}$.
Moc pobierana $p = -ui = -(-8)(2) = 16\ \mathrm{W} > 0$ — opór pobiera moc,
czyli wszystko się zgadza. Napięcie $u = -8$ V oznacza po prostu, że
rzeczywisty potencjał wyższy jest **po stronie końcówki, od której strzałka
wychodzi** — czyli wymuszona strzałka jest „odwrócona” wobec rzeczywistości.

**Kontrola:** ten sam opór w konwencji przeciwnej: $u = 8$ V, $p = ui = 16$ W.
Moc wyszła ta sama (moc nie zależy od strzałkowania — iloczyn dwóch zmian
znaku), a napięcie różni się tylko znakiem. **Wniosek: zawsze sprawdzaj, czy
moc w oporze wychodzi dodatnia.** To najszybszy test poprawności strzałek.
:::

::: zapamietaj Zasada trzech kroków przy zapisie równania elementu
1. Zastrzałkuj prąd i napięcie (arbitralnie, ale konsekwentnie).
2. Sprawdź, czy strzałki są **przeciwne** czy **zgodne**.
3. Jeśli zgodne — wstaw minus. Dla źródeł: minus wtedy, gdy strzałki są
   **przeciwne**.
:::

### 1.4 Źródła idealne

`[W1/s.9–10]` Idealne źródło napięciowe ma charakterystykę $u = E$: napięcie
**nie zależy** od prądu, prąd dostosowuje się do obwodu. Idealne źródło prądowe
ma $i = J$: prąd nie zależy od napięcia, napięcie dostosowuje się do obwodu.

Z tych definicji wynikają **zakazy**, które na kolokwium wracają jako pytania
o „sprzeczność”:

::: pulapka Czego nie wolno robić ze źródłami idealnymi
* **Nie wolno zwierąć idealnego źródła napięciowego** ($u = E$ i $u = 0$
  jednocześnie — sprzeczność, prąd nieograniczony).
* **Nie wolno rozwierać idealnego źródła prądowego** ($i = J$ i $i = 0$).
* **Nie wolno łączyć równolegle** dwóch i.ź.n. o **różnych** wartościach
  (to jak zwarcie między nimi). Tak samo nie wolno łączyć **szeregowo** i.ź.p.
  o różnych wartościach.
* Łączyć **szeregowo** można dowolne i.ź.n. (napięcia się sumują), a
  **równolegle** — dowolne i.ź.p. (prądy się sumują) `[W3/s.11]`.
:::

::: przyklad Przykład 1.2 — dlaczego „równolegle dwa E” to błąd
Dwa idealne źródła $E_1 = 5\ \mathrm{V}$ i $E_2 = 3\ \mathrm{V}$ połączono
równolegle. Z prawa napięciowego Kirchhoffa dla oczka złożonego z tych dwóch
źródeł: $E_1 - E_2 = 0 \Rightarrow 5 - 3 = 0$ — sprzeczność. Model jest
błędny, bo pominęliśmy rezystancje wewnętrzne: **każde rzeczywiste źródło ma
$R_w$** i wtedy prąd wynosi $i = (E_1 - E_2)/(R_{w1} + R_{w2})$. Dla
$R_{w1} = R_{w2} = 0{,}5\ \Omega$: $i = 2/1 = 2\ \mathrm{A}$ — źródło o
wyższym napięciu **ładuje** drugie.
:::

### 1.5 Dwójniki bierne: R, zwarcie, rozwarcie, C i L

`[W1/s.11–14]`

::: def Definicja — opór (rezystor)
Element modelujący **wydzielanie ciepła** pod wpływem prądu. Charakterystyka
$u = f_R(i)$ musi być: ciągła, spełniać $ui \ge 0$ (przy strzałkach
przeciwnych), oraz $ui = 0 \Leftrightarrow u = 0 \wedge i = 0$. Opór liniowy:
$u = Ri$, równoważnie $i = Gu$ z $G = 1/R$ [S].
:::

Granice modelu są bardzo użyteczne rachunkowo:

| Element graniczny | Definicja | Równoważny | Kiedy używać |
|---|---|---|---|
| zwarcie | $u = 0$, prąd dowolny | $E = 0$, $R \to 0$, $G \to \infty$ | wyłączone źródło napięciowe, „zwarty” kondensator w stanie ustalonym |
| rozwarcie | $i = 0$, napięcie dowolne | $J = 0$, $R \to \infty$, $G \to 0$ | wyłączone źródło prądowe, „przerwa” w obwodzie |

::: pulapka Kondensator i cewka w prądzie stałym
Dla prądu stałego w **stanie ustalonym**: $i_C = C\,\mathrm{d}u/\mathrm{d}t = 0$
— **kondensator jest rozwarciem**; $u_L = L\,\mathrm{d}i/\mathrm{d}t = 0$ —
**cewka jest zwarciem** `[W1/s.14]`. Uwaga na sformułowanie: to dotyczy
**stanu ustalonego**, a nie chwili bezpośrednio po przełączeniu — wtedy
kondensator zachowuje napięcie, a cewka prąd.
:::

::: przyklad Przykład 1.3 — stan ustalony z C i L
Obwód: $E = 12\ \mathrm{V}$ zasila szereg $R_1 = 2\ \mathrm{k\Omega}$,
$C = 10\ \mathrm{\mu F}$, $R_2 = 4\ \mathrm{k\Omega}$, a równolegle do $R_2$
cewka $L = 5\ \mathrm{mH}$.

**Pytanie:** jakie są prądy i napięcia w stanie ustalonym prądu stałego?

**Rozwiązanie:** $C \to$ rozwarcie (gałąź z $C$ i $R_2$ nie przewodzi),
$L \to$ zwarcie (zwiera $R_2$). Obwód redukuje się do $E$ i $R_1$:
$i = E/R_1 = 12/2000 = 6\ \mathrm{mA}$, $u_{R1} = 12\ \mathrm{V}$, napięcie na
zwarciu $u_L = 0$, napięcie na $C$: $u_C = E - u_{R1} = 0$ (bo cały spadek jest
na $R_1$). Moc: $P = E i = 72\ \mathrm{mW}$, cała w $R_1$:
$i^2 R_1 = (6\ \mathrm{mA})^2 \cdot 2\ \mathrm{k\Omega} = 72\ \mathrm{mW}$ ✔
:::

### 1.6 Źródła rzeczywiste

`[W1/s.15–16]` Rzeczywiste źródło napięciowe: $u = e - R_w i$ (napięcie spada
ze wzrostem pobieranego prądu), model = i.ź.n. $E$ **szeregowo** z $R_w$.
Rzeczywiste źródło prądowe: $i = j - G_w u$, model = i.ź.p. $J$ **równolegle**
z $G_w$.

::: metoda Wyznaczanie $R_w$ z dwóch punktów charakterystyki
Z charakterystyki $u(i) = E - R_w i$: nachylenie prostej to $-R_w$.
W praktyce wystarczą dwa pomiary: $(i_1, u_1)$ i $(i_2, u_2)$:
$$
R_w = \frac{u_1 - u_2}{i_2 - i_1}, \qquad E = u_1 + R_w i_1
$$
Trzeci, kontrolny punkt: **prąd zwarcia** $i_z = E/R_w$, napięcie **stanu
jałowego** $u_0 = E$.
:::

::: przyklad Przykład 1.4 — ogniwo 1,5 V pod obciążeniem
Ogniwo: napięcie jałowe $u_0 = 1{,}50\ \mathrm{V}$; przy poborze
$i = 0{,}50\ \mathrm{A}$ napięcie spada do $1{,}35\ \mathrm{V}$.

$R_w = (1{,}50 - 1{,}35)/0{,}50 = 0{,}3\ \Omega$.

Prąd zwarcia: $i_z = E/R_w = 1{,}50/0{,}3 = 5\ \mathrm{A}$ — i to jest odpowiedź
na pytanie „dlaczego nie wolno zwierać baterii”: moc w $R_w$ wyniosłaby
$i_z^2 R_w = 7{,}5\ \mathrm{W}$ (i cała w ogniwie).

Moc oddawana do obciążenia $R_0 = 1\ \Omega$: $i = 1{,}5/1{,}3 = 1{,}154\ \mathrm{A}$,
$P = i^2 R_0 = 1{,}33\ \mathrm{W}$, sprawność $\eta = R_0/(R_0 + R_w) = 77\%$.
:::

### 1.7 Czwórniki i źródła sterowane

`[W1/s.17]` Cztery typy źródeł sterowanych — warto zapamiętać nie nazwy, a
**jednostkę współczynnika**, bo ona mówi wszystko:

| Typ | Równanie | Jednostka | Warunek wejściowy | Typowe zastosowanie |
|---|---|---|---|---|
| napięciowe sterowane napięciowo (VCVS) | $u_2 = k u_1$ | V/V | $i_1 = 0$ | wzmacniacz operacyjny, wzmacniacz napięciowy |
| prądowe sterowane napięciowo (VCCS) | $i_2 = g u_1$ | A/V = S | $i_1 = 0$ | tranzystor polowy, transkonduktancja |
| napięciowe sterowane prądowo (CCVS) | $u_2 = r i_1$ | V/A = $\Omega$ | $u_1 = 0$ | przetwornik prąd–napięcie, transrezystancja |
| prądowe sterowane prądowo (CCCS) | $i_2 = \beta i_1$ | A/A | $u_1 = 0$ | tranzystor bipolarny |

::: uwaga Dlaczego „$i_1 = 0$” albo „$u_1 = 0$”
To jest część definicji, nie uproszczenie: **idealne** źródło sterowane ma
wejście, które nie pobiera prądu (VCVS, VCCS) albo nie ma na nim napięcia
(CCVS, CCCS). Dzięki temu źródło sterowane nie obciąża obwodu sterującego.
W zadaniach: **nie licz prądu wejściowego źródła sterowanego** — on jest zerowy
z definicji; jeśli policzysz niezerowy, to znaczy, że pomyliłeś zaciski.
:::

::: przyklad Przykład 1.5 — VCVS w praktyce
Dane: $u_1 = 0{,}5\ \mathrm{V}$, $k = 20$ (VCVS). Wtedy $u_2 = 20 \cdot 0{,}5 = 10\ \mathrm{V}$.
Jeżeli to źródło zasila $R = 1\ \mathrm{k\Omega}$, to prąd wyjściowy
$i_2 = 10/1000 = 10\ \mathrm{mA}$ **płynie przez obciążenie i przez samo źródło
(końcówką masy)**, a nie przez wejście — wejście pobiera $i_1 = 0$. Moc
dostarczona do obciążenia: $P = u_2^2/R = 0{,}1\ \mathrm{W}$.
:::

::: ciekawostka Gdzie w obwodzie „ukrywa się” źródło sterowane
* **Wzmacniacz operacyjny** to VCVS o $k \to \infty$ `[W4/s.3]`.
* **Tranzystor bipolarny** (małosygnałowo) to CCCS o $\beta \approx 100$–$500$.
* **Tranzystor polowy** to VCCS o $g_m$ w mS.
* **Przetwornik U/I** i **I/U** w miernictwie to odpowiednio VCCS i CCVS.
:::

### 1.8 Ćwiczenia do wykładu 1

::: przyklad Ćwiczenie 1.1
Opór $R = 10\ \Omega$ ma zastrzałkowany prąd $i = -0{,}5\ \mathrm{A}$ i napięcie
$u$ zgodne ze strzałką prądu. Ile wynosi $u$ oraz moc?

**Odpowiedź:** strzałki zgodne $\Rightarrow u = -Ri = -10 \cdot (-0{,}5) = 5\ \mathrm{V}$.
Moc pobierana $p = -ui = -(5)(-0{,}5) = 2{,}5\ \mathrm{W} > 0$ ✔ (a nie $-2{,}5$ W —
to jest właśnie test znaku).
:::

::: przyklad Ćwiczenie 1.2
Dwa ogniwa: $E_1 = 9\ \mathrm{V}$, $R_{w1} = 1\ \Omega$ oraz $E_2 = 6\ \mathrm{V}$,
$R_{w2} = 2\ \Omega$, połączone równolegle zaciskami „+”. Jaki prąd popłynie
między nimi i w którą stronę?

**Odpowiedź:** oczko zawiera oba źródła przeciwsobnie, więc
$i = (E_1 - E_2)/(R_{w1} + R_{w2}) = 3/3 = 1\ \mathrm{A}$ — od źródła $E_1$ do
$E_2$, czyli $E_1$ **oddaje** moc, a $E_2$ ją **pobiera** (jest ładowane).
Napięcie na zaciskach wspólnych: $u = E_1 - R_{w1} i = 9 - 1 = 8\ \mathrm{V}$
(sprawdzenie: $u = E_2 + R_{w2} i = 6 + 2 = 8\ \mathrm{V}$ ✔).
:::

::: przyklad Ćwiczenie 1.3
W obwodzie z Przykładu 1.3 po bardzo długim czasie zwieramy $R_1$. Co się
stanie z napięciem na kondensatorze w stanie ustalonym?

**Odpowiedź:** źródło zostaje zwarte przez $R_1$ (gałąź $C$–$R_2$ nadal
rozwarta przez $C$), więc $u_C = 0$. Wniosek ogólny: w stanie ustalonym prądu
stałego kondensator „widzi” jedynie obwód otwarty — napięcie na nim ustala
reszta obwodu, a nie sam kondensator.
:::

## 2. Wykład 2 — prawa i zasady obwodowe

### 2.1 Cztery słowa, które trzeba rozróżniać

`[W2/s.3]` Zanim napisze się pierwsze równanie, trzeba wiedzieć, co jest czym:

::: def Definicja — słownik obwodu
* **gałąź** — dwójnik (albo wrota wielowrotnika) opisany **jednym** prądem
  i **jednym** napięciem;
* **węzeł** — połączenie zacisków elementów; **wszystkie punkty węzła mają ten
  sam potencjał**; do węzła zalicza się przewody, a także **zwarcie**;
* **obwód** (droga krążenia) — zamknięta droga po **niepowtarzających się**
  gałęziach i węzłach; może zawierać **rozwarcie**;
* **oczko** — obwód w sieci planarnej, wewnątrz którego **nie ma żadnej
  gałęzi**.
:::

Różnica „obwód vs oczko” jest istotna: prawo napięciowe Kirchhoffa wolno
napisać dla **dowolnego** obwodu (np. dużego, obejmującego kilka oczek), ale
**niezależnych** równań jest dokładnie $M$ = liczba **oczek**. Jeżeli napiszesz
równanie dla obwodu złożonego z dwóch oczek, dostaniesz kombinację liniową
dwóch równań oczkowych — nie nową informację.

::: pulapka Węzeł „w szerszym sensie”
Dwa zaciski połączone **zworem** to **jeden** węzeł. Student, który policzy je
jako dwa, dostanie $N$ o jeden za dużo — a co za tym idzie, jedno równanie za
dużo i układ sprzeczny albo zależny. Zanim policzysz węzły, **dorysuj zwory
jako punkty**.
:::

### 2.2 I prawo Kirchhoffa (MPK) — prądy

`[W2/s.4]`

::: wzor MPK (KCL)
Suma algebraiczna natężeń prądów wpływających do **zamkniętego obszaru** jest
równa zeru. Prądy wpływające zapisujemy ze znakiem $+$, wypływające z $-$:
$$
\sum_{k} \pm i_k = 0
$$
Szczególnym przypadkiem obszaru jest **węzeł**; wtedy liczba równań wynosi
$N - 1$ ($N$ — liczba węzłów).
:::

Dlaczego $N-1$, a nie $N$: suma wszystkich $N$ równań węzłowych daje $0 = 0$
(każdy prąd pojawia się dwa razy z przeciwnymi znakami). Równania są
**liniowo zależne** — jedno trzeba odrzucić.

::: metoda Jak nie pomylić się w znakach MPK
1. Zastrzałkuj **wszystkie** prądy w obwodzie (na schemacie, ołówkiem).
2. Wybierz obszar (węzeł) i zaznacz go kółkiem.
3. Dla każdej gałęzi dochodzącej do węzła: strzałka **do** węzła = $+$,
   **od** węzła = $-$.
4. Zapisz równanie i **od razu sprawdź**, że każdy prąd występuje w nim raz.
:::

### 2.3 II prawo Kirchhoffa (OPK) — napięcia

`[W2/s.5]`

::: wzor OPK (KVL)
Suma algebraiczna napięć wokół **zamkniętej drogi krążenia** jest równa zeru.
Napięcia zastrzałkowane **zgodnie** z przyjętym kierunkiem krążenia — znak $+$,
przeciwnie — znak $-$. Liczba niezależnych równań: $M$ = liczba oczek.
:::

::: pulapka OPK a zwrot źródła
Najczęstszy błąd: potraktowanie źródła jak oporu. Reguła praktyczna przy
krążeniu: **wchodzisz do źródła od „+” i wychodzisz od „−” → zapisujesz
$+E$** (wzniesienie potencjału); wchodzisz od „−” → $-E$. Dla oporu: idziesz
**zgodnie** z prądem → spadek $-Ri$; przeciwnie → $+Ri$. Zanotuj to raz na
marginesie i nie wymyślaj od nowa przy każdym zadaniu.
:::

### 2.4 Pełna procedura: $N-1$ + $M$ + równania elementów

`[W2/s.7]` Algorytm z wykładu jest „bezpieczny”: daje komplet równań, których
nie trzeba się domyślać. Poniżej pełne przejście na jednym obwodzie — ten sam
obwód będzie potem służył do superpozycji (§2.10) i Thévenina (§3.6).

::: figura figury/obwod.svg | Obwód odniesienia: $E_1 = 12$ V, $R_1 = 2\ \Omega$, $R_2 = 3\ \Omega$, $E_2 = 4$ V, $R_3 = 2\ \Omega$. Węzły $N = 2$ (A i masa), oczka $M = 2$.
:::

::: przyklad Przykład 2.1 — komplet równań i rozwiązanie
**Krok 1. Strzałkowanie.** Prądy gałęziowe: $I_1$ (lewa gałąź, do góry),
$I_2$ (środkowa, w dół), $I_3$ (prawa, do góry). Napięcie węzła A względem
masy: $V$.

**Krok 2. MPK w węźle A** ($N - 1 = 1$ równanie): prądy wpływające to $I_1$
i $I_3$, wypływający to $I_2$:
$$
I_1 = I_2 + I_3
$$

**Krok 3. Równania elementów** (strzałki: $I_1$ do góry przez $E_1$ i $R_1$,
$I_2$ w dół przez $R_2$, $I_3$ do góry przez $R_3$ i $E_2$):
$$
I_1 = \frac{E_1 - V}{R_1}, \qquad I_2 = \frac{V}{R_2}, \qquad I_3 = \frac{V - E_2}{R_3}
$$

**Krok 4. Podstawienie do MPK** (jedno równanie, jedna niewiadoma $V$):
$$
\frac{12 - V}{2} = \frac{V}{3} + \frac{V - 4}{2}
$$
Mnożymy przez 6: $3(12 - V) = 2V + 3(V-4)$, czyli $36 - 3V = 5V - 12$, stąd
$V = 6\ \mathrm{V}$.

**Krok 5. Prądy:** $I_1 = (12-6)/2 = 3\ \mathrm{A}$, $I_2 = 6/3 = 2\ \mathrm{A}$,
$I_3 = (6-4)/2 = 1\ \mathrm{A}$. Kontrola MPK: $3 = 2 + 1$ ✔

**Krok 6. OPK** — dwa oczka, dla kontroli.

Oczko lewe:
$$
E_1 - R_1 I_1 - R_2 I_2 = 12 - 2\cdot3 - 3\cdot2 = 0 \;✔
$$
Oczko prawe:
$$
R_2 I_2 - E_2 - R_3 I_3 = 3\cdot2 - 4 - 2\cdot1 = 0 \;✔
$$
:::

::: zapamietaj Kolejność, która zawsze działa
1. policz $N$ i $M$ (po dorysowaniu zwor!),
2. zastrzałkuj prądy **wszystkich** gałęzi,
3. zapisz $N-1$ równań MPK,
4. zapisz $M$ równań OPK (albo od razu podstaw równania elementów),
5. rozwiąż i **sprawdź** drugim prawem, którego nie użyłeś do rozwiązania.
:::

### 2.5 Dwa skróty: superbęzeł i superoczko

`[W2/s.9]` Slajd mówi o „pomijaniu równań”. Praktycznie chodzi o dwa przypadki,
w których idealne źródło psuje standardowy schemat równań:

::: metoda Superbęzeł — gdy w węźle jest idealne źródło napięciowe
Jeśli między dwoma węzłami jest **idealne źródło napięciowe**, to napięcie
między nimi jest **znane** ($u = E$), a prąd przez źródło jest niewiadomą, dla
której nie ma równania elementu. Wtedy:
* **pomijamy** równanie prądowe tych węzłów,
* piszemy **jedno** równanie prądowe dla obszaru obejmującego oba węzły
  (superbęzeł),
* dodajemy równanie więzów: $V_1 - V_2 = \pm E$.
:::

::: przyklad Przykład 2.2 — superbęzeł
Między węzłami 1 i 2 jest idealne źródło $E = 6\ \mathrm{V}$ (+ w stronę węzła 1).
Do węzła 1 dochodzi $R_1 = 2\ \Omega$ do masy, do węzła 2 — $R_2 = 4\ \Omega$
do masy; do węzła 2 wpływa idealne źródło prądowe $J = 6\ \mathrm{A}$.

**Superbęzeł (1+2):** prądy wypływające: $V_1/R_1 + V_2/R_2 = J$:
$$
\frac{V_1}{2} + \frac{V_2}{4} = 6, \qquad V_1 - V_2 = 6
$$
Podstawiamy $V_1 = V_2 + 6$: $(V_2+6)/2 + V_2/4 = 6 \Rightarrow 0{,}75V_2 + 3 = 6
\Rightarrow V_2 = 4\ \mathrm{V}$, $V_1 = 10\ \mathrm{V}$.

**Kontrola:** prądy w oporach $5\ \mathrm{A} + 1\ \mathrm{A} = 6\ \mathrm{A} = J$ ✔
Prąd **źródła**: z MPK dla węzła 1 wynika $i_E = -5\ \mathrm{A}$ (źródło pobiera
5 A skierowane „w górę” — płynie przez nie 5 A w dół).
:::

::: metoda Superoczko — gdy oczka mają wspólne idealne źródło prądowe
Jeśli dwa sąsiednie oczka mają **wspólną gałąź z idealnym źródłem prądowym**,
nie można napisać dla nich zwykłych równań OPK (nieznane jest napięcie na
źródle). Wtedy:
* piszemy równanie OPK dla **oczka zewnętrznego** (obejmującego oba oczka),
* dodajemy równanie źródła: różnica prądów oczkowych = $\pm J$.
:::

::: przyklad Przykład 2.3 — superoczko
Obwód: lewa gałąź $E = 12\ \mathrm{V}$ i $R_1 = 2\ \Omega$;
gałąź środkowa: idealne źródło prądowe $J = 1\ \mathrm{A}$ (w dół);
prawa gałąź: $R_2 = 6\ \Omega$.

Prądy oczkowe $i_a$ (lewe oczko) i $i_b$ (prawe), oba zgodnie z ruchem
wskazówek zegara. Prąd środkowej gałęzi w dół to $i_a - i_b$, więc:
$$
i_a - i_b = J = 1
$$
Superoczko (zewnętrzne): $E - R_1 i_a - R_2 i_b = 0 \Rightarrow 2i_a + 6i_b = 12
\Rightarrow i_a + 3i_b = 6$.
Stąd $i_b + 1 + 3i_b = 6 \Rightarrow i_b = 1{,}25\ \mathrm{A}$,
$i_a = 2{,}25\ \mathrm{A}$.

**Kontrola węzłowa:** $V = R_1 i_a = 2 \cdot 2{,}25 = 4{,}5$ V oraz
$V = R_2 i_b = 6 \cdot 1{,}25 = 7{,}5$ V — **nie zgadza się!** Poprawka: prąd
$i_a$ płynie w lewym oczku **w górę** w gałęzi lewej, więc napięcie węzła
$V = E - R_1 i_a = 12 - 4{,}5 = 7{,}5$ V ✔ Teraz zgadza się z $R_2 i_b$.
To jest właśnie moment, w którym warto **zawsze** sprawdzić wynik drugą metodą.
:::

::: uwaga Morał z Przykładu 2.3
Błąd nie był rachunkowy, a **interpretacyjny**: prąd oczkowy nie jest prądem
gałęzi „w tę stronę, którą chcesz”. Jeden rzut oka na kontrolę węzłową go
wychwycił. Własność, którą warto wykorzystać: **napięcie między dwoma węzłami
musi wyjść takie samo, liczone każdą drogą** — to najszybszy test poprawności.
:::

### 2.6 Równania elementów a strzałkowanie — ściąga błędów

`[W2/s.6]` Najczęstsze pomyłki zebrane w jednej tabeli:

| Sytuacja | Poprawnie | Typowy błąd |
|---|---|---|
| opór, strzałki przeciwne | $u = Ri$ | minus „na wszelki wypadek” |
| opór, strzałki zgodne | $u = -Ri$ | $u = Ri$ i ujemna moc w oporze |
| źródło napięciowe, prąd zgodny z $E$ | $u = E$, moc oddawana $p_o = Ei$ | $p = ui$ i ujemna moc |
| źródło prądowe, prąd $J$ | $i = J$ | liczenie prądu z napięcia |
| moc w oporze | $p = Ri^2 = Gu^2 = u^2/R$ — **zawsze dodatnia** | $p = ui$ bez sprawdzenia znaków |
| źródło sterowane | wejście: $i_1 = 0$ lub $u_1 = 0$ | doliczanie prądu wejściowego |

### 2.7 Dzielniki napięciowy i prądowy

`[W2/s.12–13]`

::: figura figury/dzielniki.svg | Dzielnik napięciowy (prąd wspólny, napięcia dzielą się jak rezystancje) i dzielnik prądowy (napięcie wspólne, prądy dzielą się jak konduktancje).
:::

::: wzor Dzielniki
**Napięciowy** (dwa opory szeregowo, dzieli napięcie $U$):
$$
U_1 = U \frac{R_1}{R_1 + R_2} = U \frac{G_2}{G_1 + G_2}
$$
dla wielu oporów szeregowo: $U_1 = U \dfrac{R_1}{\sum R_n}$.

**Prądowy** (dwa opory równolegle, dzieli prąd $I$):
$$
I_1 = I \frac{G_1}{G_1 + G_2} = I \frac{R_2}{R_1 + R_2}
$$
dla wielu oporów równolegle: $I_1 = I \dfrac{G_1}{\sum G_n}$.
:::

::: pulapka Dzielnik przestaje działać, gdy dołączysz obciążenie
Dzielnik $R_1 = R_2 = 10\ \mathrm{k\Omega}$, $U = 12\ \mathrm{V}$ daje
$U_1 = 6\ \mathrm{V}$ **bez obciążenia**. Po dołączeniu $R_0 = 10\ \mathrm{k\Omega}$
równolegle do $R_2$: $R_2 \| R_0 = 5\ \mathrm{k\Omega}$, więc
$U_1 = 12 \cdot 5/(10+5) = 4\ \mathrm{V}$ — **spadek o 33 %**.
Wniosek projektowy: dzielnikiem można zasilać tylko odbiornik o rezystancji
**znacznie większej** od $R_2$ (albo trzeba użyć źródła zastępczego, §3.6).
:::

::: przyklad Przykład 2.4 — dzielnik prądowy z kontrolą
$I = 6\ \mathrm{mA}$ dzielone między $R_1 = 2\ \mathrm{k\Omega}$ i
$R_2 = 3\ \mathrm{k\Omega}$ (równolegle).
$$
I_1 = I\frac{R_2}{R_1+R_2} = 6 \cdot \frac{3}{5} = 3{,}6\ \mathrm{mA},
\qquad I_2 = 2{,}4\ \mathrm{mA}
$$
**Kontrola napięciowa:** $I_1 R_1 = 3{,}6 \cdot 2 = 7{,}2\ \mathrm{V}$ oraz
$I_2 R_2 = 2{,}4 \cdot 3 = 7{,}2\ \mathrm{V}$ ✔ (to jest warunek „to samo
napięcie na obu oporach”).
:::

### 2.8 Zasada kompensacji

`[W2/s.14]`

::: def Definicja — zasada kompensacji
Prądy ani napięcia w układzie **nie zmienią się**, jeżeli dowolną gałąź:
* na której występuje napięcie $u$ — zastąpimy **źródłem napięciowym $E = u$**,
* przez którą płynie prąd $i$ — zastąpimy **źródłem prądowym $J = i$**.

Zasada obowiązuje **także dla obwodów nieliniowych** (jeśli rozwiązanie jest
jednoznaczne).
:::

Dwa wnioski praktyczne, które na kolokwium są warte punktów:

1. **Punkty o tym samym potencjale można zewrzeć** (bo napięcie między nimi
   $u = 0$ = źródło o $E = 0$ = zwarcie).
2. **Gałąź bezprądową można rozewrzeć** (bo $i = 0$ = źródło o $J = 0$ =
   rozwarcie).

::: przyklad Przykład 2.5 — mostek w równowadze
Mostek: $R_1 = 10\ \Omega$, $R_2 = 20\ \Omega$, $R_3 = 20\ \Omega$,
$R_4 = 40\ \Omega$, w przekątnej $R_5 = 50\ \Omega$ (rysunek w §3.3).
Warunek równowagi: $R_1/R_2 = R_3/R_4$, czyli $10/20 = 20/40$ ✔ — mostek jest
**zrównoważony**, więc przez $R_5$ **nie płynie prąd**.

**Konsekwencja 1 (kompensacja):** gałąź $R_5$ można **rozewrzeć** — wynik się
nie zmieni: $R_z = (R_1 + R_3) \| (R_2 + R_4) = 30 \| 60 = 20\ \Omega$.

**Konsekwencja 2:** węzły C i D mają **ten sam potencjał**, więc można je
**zewrzeć**: $R_z = (R_1 \| R_2) + (R_3 \| R_4) = 6{,}\overline{6} + 13{,}\overline{3} = 20\ \Omega$
✔ Obie drogi dają to samo — i **od wartości $R_5$ wynik nie zależy**.
:::

::: pulapka Kiedy kompensacji nie wolno użyć
Zasada kompensacji **nie mówi**, że dowolną gałąź można zastąpić źródłem
dowolnej wartości — tylko że źródło musi mieć wartość **aktualnie panującego**
$u$ lub $i$. Jeżeli w zadaniu zmieniasz obwód **i** szukasz nowego rozwiązania,
kompensacja nic nie da: nowy stan ma nowe $u$, $i$.
:::

### 2.9 Zasada ruchliwości źródeł

`[W2/s.15]`

::: def Definicja — ruchliwość źródeł
* **Prądy** w obwodzie nie zmienią się, jeśli do **wszystkich** gałęzi
  dołączonych do wybranego węzła włączymy szeregowo **identyczne źródła
  napięciowe** o tym samym zwrocie względem węzła.
* **Napięcia** w układzie nie zmienią się, jeśli do **każdej** gałęzi
  wybranego obwodu dołączymy równolegle **identyczne źródło prądowe** o
  zwrocie zgodnym z kierunkiem krążenia.
:::

::: figura figury/przesuniecie.svg | Przesunięcie źródła przez węzeł: źródło z gałęzi 1 „przenosi się” do gałęzi 2 ze **zwrotem odwróconym** względem wspólnego węzła. Prądy gałęzi (2 A) pozostają bez zmian.
:::

::: przyklad Przykład 2.6 — sprawdzenie ruchliwości źródła na liczbach
**Przed:** między węzłami A i B dwie gałęzie: (1) $E = 10\ \mathrm{V}$
(+ do A) i $R_1 = 2\ \Omega$, (2) $R_2 = 3\ \Omega$.
Węzeł A: $(V - E)/R_1 + V/R_2 = 0 \Rightarrow (V - 10)/2 + V/3 = 0
\Rightarrow 3V - 30 + 2V = 0 \Rightarrow V = 6\ \mathrm{V}$.
Prądy: $i_1 = (6-10)/2 = -2\ \mathrm{A}$ (czyli 2 A w dół), $i_2 = 6/3 = 2\ \mathrm{A}$.

**Po** (źródło przeniesione do gałęzi 2, ze zwrotem odwróconym — „+” do B,
czyli $E' = -10\ \mathrm{V}$ widziane od A): $V'/R_1 + (V' + 10)/R_2 = 0
\Rightarrow 3V' + 2V' + 20 = 0 \Rightarrow V' = -4\ \mathrm{V}$.
Prądy: $i_1' = -4/2 = -2\ \mathrm{A}$ ✔, $i_2' = (-4 + 10)/3 = 2\ \mathrm{A}$ ✔

**Wniosek:** prądy identyczne, napięcia węzłów **nie** — i o to chodzi:
zasada zachowuje **prądy** (przy przesuwaniu źródeł napięciowych), a nie
potencjały.
:::

::: uwaga Po co komu ta zasada
Do **uproszczenia struktury**: źródło „siedzące” w gałęzi, której nie da się
połączyć szeregowo/równolegle z niczym, można rozdzielić do gałęzi bocznych i
w ten sposób uzyskać układ, w którym działa dzielnik albo zamiana źródeł.
Druga typowa sytuacja: przeniesienie źródła pozwala **uniknąć superbęzła**
(§2.5). To zasada „kosmetyczna”, ale często skraca rachunek o połowę.
:::

### 2.10 Zasada superpozycji

`[W2/s.16]` To najczęściej używana i najczęściej **nadinterpretowana** zasada
w całym wykładzie. Definicja jest precyzyjna:

::: def Definicja — zasada superpozycji
W układzie **liniowym** dowolne napięcie $u$ lub prąd $i$ jest **sumą
składowych** pochodzących od każdego źródła niezależnego **z osobna**:
$$
u = \sum_{n=1}^{N} u^{(n)}, \qquad i = \sum_{n=1}^{N} i^{(n)}
$$
gdzie $N$ to liczba źródeł **niezależnych**.
:::

::: metoda Algorytm superpozycji (krok po kroku)
1. Policz **źródła niezależne** — to jest liczba podukładów $N$.
2. Zbuduj podukład $n$: działa tylko źródło $n$; pozostałe **źródła niezależne
   wyłącz**:
   * źródło napięciowe $E \to$ **zwarcie** ($E = 0$),
   * źródło prądowe $J \to$ **rozwarcie** ($J = 0$).
3. **Źródeł sterowanych nie wyłączaj** i **nie twórz dla nich podukładów** —
   występują w każdym podukładzie, z tym samym współczynnikiem.
4. W każdym podukładzie policz szukaną składową $u^{(n)}$ lub $i^{(n)}$
   (najprostszą metodą: dzielnik, $R_z$, prawo Ohma).
5. Zsumuj składowe **algebraicznie** (z ich znakami, w przyjętym strzałkowaniu).
6. **Sprawdź** wynik metodą, która nie używa superpozycji (MPK/OPK, bilans mocy).
:::

::: figura figury/superpozycja.svg | Ten sam obwód w trzech stanach: pełny oraz dwa podukłady superpozycji. Wyłączone źródło napięciowe zastępujemy **zwarciem**, nie „wykasowaniem gałęzi”.
:::

::: pulapka Trzy grzechy superpozycji
1. **Zwarcie zamiast rozwarcia.** Wyłączone źródło *napięciowe* → **zwarcie**;
   wyłączone źródło *prądowe* → **rozwarcie**. Odwrotnie niż podpowiada intuicja.
2. **Tworzenie podukładu dla źródła sterowanego.** Źródło sterowane **nie jest
   niezależne** — zostaje w każdym podukładzie. Jeśli je wyłączysz, wynik będzie
   błędny (a często „prawie dobry”, co jest najgorsze).
3. **Superpozycja mocy.** Moc **nie** podlega superpozycji
   ($P \ne P^{(1)} + P^{(2)}$), bo $P = u^2/R$ jest **nieliniową** funkcją
   napięcia. Slajd mówi to wprost ostatnim zdaniem.
:::

::: przyklad Przykład 2.7 — superpozycja w obwodzie odniesienia
Wracamy do obwodu z §2.4 ($E_1 = 12$ V, $R_1 = 2\ \Omega$, $R_2 = 3\ \Omega$,
$E_2 = 4$ V, $R_3 = 2\ \Omega$). Szukamy napięcia $V$ w węźle A. Są **dwa**
źródła niezależne, więc dwa podukłady.

**Podukład 1: działa tylko $E_1$** ($E_2 \to$ zwarcie).
$$
\frac{12 - V'}{2} = \frac{V'}{3} + \frac{V'}{2}
\;\Rightarrow\; 3(12 - V') = 2V' + 3V' \;\Rightarrow\; V' = 4{,}5\ \mathrm{V}
$$
Prądy: $I_1' = (12-4{,}5)/2 = 3{,}75\ \mathrm{A}$,
$I_2' = 1{,}5\ \mathrm{A}$, $I_3' = 2{,}25\ \mathrm{A}$.

**Podukład 2: działa tylko $E_2$** ($E_1 \to$ zwarcie).
$$
\frac{0 - V''}{2} = \frac{V''}{3} + \frac{V'' - 4}{2}
\;\Rightarrow\; -3V'' = 2V'' + 3V'' - 12 \;\Rightarrow\; V'' = 1{,}5\ \mathrm{V}
$$
Prądy: $I_1'' = (0-1{,}5)/2 = -0{,}75\ \mathrm{A}$,
$I_2'' = 0{,}5\ \mathrm{A}$, $I_3'' = (1{,}5-4)/2 = -1{,}25\ \mathrm{A}$.

**Suma:**
$$
V = 4{,}5 + 1{,}5 = 6\ \mathrm{V}, \quad
I_1 = 3{,}75 - 0{,}75 = 3\ \mathrm{A}, \quad
I_2 = 1{,}5 + 0{,}5 = 2\ \mathrm{A}, \quad
I_3 = 2{,}25 - 1{,}25 = 1\ \mathrm{A}
$$
Wszystko zgadza się z rozwiązaniem z §2.4 ✔ — a rachunek w każdym podukładzie
był **prostszy** niż w obwodzie pełnym (jeden opór mniej).
:::

::: przyklad Przykład 2.8 — superpozycja ze źródłem sterowanym
Obwód: $E = 10\ \mathrm{V}$, $R_1 = 1\ \Omega$ (szeregowo ze źródłem),
węzeł A, $R_2 = 4\ \Omega$ do masy, oraz **źródło sterowane** VCCS pobierające
z węzła A prąd $i_s = g V$, gdzie $g = 0{,}75\ \mathrm{S}$. Do węzła A wpływa
ponadto idealne źródło prądowe $J = 2\ \mathrm{A}$.

**Dwa źródła niezależne** ($E$ i $J$) → dwa podukłady; źródło sterowane
zostaje w obu.

Podukład 1 ($E$, $J \to$ rozwarcie):
$$
\frac{10 - V'}{1} = \frac{V'}{4} + 0{,}75V' \;\Rightarrow\; 10 = 2V' \;\Rightarrow\; V' = 5\ \mathrm{V}
$$
Podukład 2 ($J$, $E \to$ zwarcie):
$$
\frac{0 - V''}{1} + 2 = \frac{V''}{4} + 0{,}75V'' \;\Rightarrow\; 2 = 2V'' \;\Rightarrow\; V'' = 1\ \mathrm{V}
$$
Suma: $V = 6\ \mathrm{V}$.

**Kontrola (bez superpozycji):** $\frac{10-6}{1} + 2 = 6 \ \mathrm{A}$ wpływające;
wypływające: $6/4 + 0{,}75\cdot 6 = 1{,}5 + 4{,}5 = 6\ \mathrm{A}$ ✔

**Gdyby ktoś wyłączył źródło sterowane w jednym z podukładów:**
$V' = 10/1{,}25 = 8$ V lub $V' = 10/2{,}5$... wynik byłby inny niż 6 V —
i to jest właśnie typowy „prawie dobry” błąd.
:::

::: przyklad Przykład 2.9 — dlaczego moc NIE podlega superpozycji
W obwodzie z Przykładu 2.7 moc w $R_2$ wynosi
$P = V^2/R_2 = 36/3 = 12\ \mathrm{W}$.

Suma mocy „składowych”: $P' + P'' = (4{,}5)^2/3 + (1{,}5)^2/3 = 6{,}75 + 0{,}75
= 7{,}5\ \mathrm{W} 
e 12\ \mathrm{W}$.

Skąd różnica? Bo $P = (u^{(1)} + u^{(2)})^2/R = P' + P'' + \mathbf{2u^{(1)}u^{(2)}/R}$
— brakuje **członu mieszanego** $2 \cdot 4{,}5 \cdot 1{,}5/3 = 4{,}5$ W, i
faktycznie $7{,}5 + 4{,}5 = 12$ W ✔

**Wniosek praktyczny:** superpozycją liczymy **prądy i napięcia**, a moc
liczymy **na końcu**, z gotowego napięcia lub prądu.
:::

::: uwaga Kiedy superpozycja to najlepszy wybór
* jest **dużo** źródeł niezależnych, a obwód jest „modularny” (każde źródło
  widzi prosty dzielnik),
* szukamy **wpływu jednego konkretnego źródła** („ile od $E_1$, a ile od $J$”),
* obwód ma kilka źródeł pracujących w różnych warunkach (np. sygnał + offset).
:::

### 2.11 Ćwiczenia do wykładu 2

::: przyklad Ćwiczenie 2.1
W węźle spotykają się cztery gałęzie; prądy zastrzałkowane **do** węzła:
$1\ \mathrm{A}$, $2\ \mathrm{A}$ oraz **od** węzła: $4\ \mathrm{A}$ i $i$.
Ile wynosi $i$?

**Odpowiedź:** $1 + 2 - 4 - i = 0 \Rightarrow i = -1\ \mathrm{A}$; prąd płynie
faktycznie **do** węzła z natężeniem 1 A.
:::

::: przyklad Ćwiczenie 2.2
Dzielnik: $U = 24\ \mathrm{V}$, $R_1 = 6\ \mathrm{k\Omega}$, $R_2 = 3\ \mathrm{k\Omega}$.
Jakie jest napięcie na $R_2$ bez obciążenia i po dołączeniu $R_0 = 3\ \mathrm{k\Omega}$?

**Odpowiedź:** bez obciążenia $U_2 = 24 \cdot 3/9 = 8\ \mathrm{V}$;
z obciążeniem $R_2 \| R_0 = 1{,}5\ \mathrm{k\Omega}$, $U_2 = 24 \cdot 1{,}5/7{,}5
= 4{,}8\ \mathrm{V}$ (spadek o 40 %). Wniosek: im mniejszy $R_0$ względem $R_2$,
tym większy błąd.
:::

::: przyklad Ćwiczenie 2.3
Dwa źródła: $E = 6\ \mathrm{V}$ szeregowo z $R_1 = 1\ \Omega$ oraz
$J = 3\ \mathrm{A}$ równolegle do $R_2 = 2\ \Omega$; oba zasilają wspólny węzeł.
Policz napięcie węzła **superpozycją**.

**Odpowiedź:** podukład 1 ($E$): $(6 - V')/1 = V'/2 \Rightarrow V' = 4\ \mathrm{V}$;
podukład 2 ($J$): $3 = V''/2 + V''/1 \Rightarrow V'' = 2\ \mathrm{V}$;
razem $V = 6\ \mathrm{V}$. Kontrola: $(6-6)/1 + 3 = 3$ A wpływające,
$6/2 = 3$ A wypływające ✔
:::

::: przyklad Ćwiczenie 2.4
W obwodzie z Przykładu 2.7 prąd $I_2 = 2\ \mathrm{A}$ płynie przez
$R_2 = 3\ \Omega$ w dół. Zastąp gałąź $R_2$ źródłem prądowym zgodnie z zasadą
kompensacji i sprawdź, czy napięcie węzła A się zmieni.

**Odpowiedź:** $J_2 = 2\ \mathrm{A}$ **w dół** (od A do masy). Równanie węzła:
$$
\frac{12 - V}{2} = 2 + \frac{V - 4}{2}
\;\Rightarrow\; 12 - V = 4 + V - 4
\;\Rightarrow\; V = 6\ \mathrm{V}
$$
napięcie **takie samo**, a prądy pozostałych gałęzi ($I_1 = 3$ A, $I_3 = 1$ A)
również się nie zmieniły ✔

**Wniosek:** kompensacja pozwala **zamienić opór na źródło** bez zmiany stanu
obwodu — to jest wygodne, gdy chcemy policzyć coś „wokół” tej gałęzi albo
zastosować superpozycję do obwodu, w którym jedno źródło jest już „prawie
wyłączone”.
:::

## 3. Wykład 3 — elementy zastępcze

### 3.1 Po co dwójnik zastępczy i co przy tym ginie

`[W3/s.3–4]`

::: def Definicja — dwójnik zastępczy
Dwójnik zastępczy to dwójnik o **możliwie prostej strukturze**, mający
**takie same równania zaciskowe** $u(i)$ i $i(u)$ jak dwójnik oryginalny.
Równoważność jest **zaciskowa**: dotyczy tylko tego, co widać z zacisków.
:::

Cztery konsekwencje, które trzeba znać, bo wynikają z nich pytania testowe
`[W3/s.4]`:

1. struktura wewnętrzna jest **inna** — nawet gdy wartości elementów są te same,
   to są **inne elementy** (inaczej połączone);
2. prądy i napięcia **wewnątrz** dwójnika oryginalnego **nie mają sensu**
   wewnątrz dwójnika zastępczego (nie ma tam tych węzłów i gałęzi);
3. dwójnik zastępczy może wewnętrznie **rozpraszać inną moc** niż oryginalny;
4. ale **suma algebraiczna mocy pobranej i rozproszonej jest taka sama**.

::: przyklad Przykład 3.1 — moc, która „znika”
Dwa opory $R_1 = R_2 = 10\ \Omega$ połączone równolegle, napięcie $U = 10\ \mathrm{V}$.
Oryginał: $P_1 = P_2 = U^2/R = 10\ \mathrm{W}$ — razem $20\ \mathrm{W}$.
Dwójnik zastępczy: $R_z = 5\ \Omega$, $P = U^2/R_z = 20\ \mathrm{W}$ ✔
Moc **całkowita** ta sama, ale w dwójniku zastępczym nie ma „$P_1$” ani „$P_2$” —
jest jedno $P = 20\ \mathrm{W}$. Dlatego nie wolno liczyć mocy pojedynczego
elementu **po** wykonaniu zamiany.
:::

### 3.2 Pięć reguł bezpiecznej zamiany

`[W3/s.5–6]` Zamiana jest prosta, ale można nią **zniszczyć zadanie**:

::: metoda Reguły
1. Zamieniaj **między dwoma wybranymi węzłami**.
2. Te węzły muszą **istnieć przed i po** zamianie (nie mogą zniknąć).
3. Nie **„gub” wielkości szukanej** — jeśli szukasz prądu w gałęzi, nie
   zwijaj tej gałęzi (chyba że policzysz wielkość zaciskową i wrócisz do
   struktury oryginalnej).
4. Zamiana obejmująca **wielkość sterującą** źródła sterowanego jest dozwolona
   tylko wtedy, gdy obejmuje **także samo źródło**.
5. Zamiana nie może doprowadzić do **utraty wielkości sterującej** źródła,
   które zostaje poza zamienianym dwójnikiem.
:::

::: pulapka Klasyczny błąd z reguły 4
Masz źródło sterowane napięciowo, sterowane napięciem $u_x$ na oporze $R_x$.
Chcesz zwinąć $R_x$ razem z sąsiednim oporem, żeby uprościć obwód. **Nie
wolno**: po zwarciu $R_x$ zniknie napięcie $u_x$, a źródło sterowane zostanie
„bez sygnału”. Poprawnie: albo zwijaj tak, żeby $R_x$ pozostał, albo użyj
zewnętrznego pobudzenia $u_x$ i policz $R_z$ metodą z §3.4.
:::

### 3.3 Opór zastępczy: definicja, łączenia, gwiazda–trójkąt

`[W3/s.7–9]`

::: wzor Opór zastępczy z definicji
Do zacisków dwójnika przyłączamy **zewnętrzne** źródło napięcia $u_x$, które
wywołuje prąd zaciskowy $i_x$. Wtedy
$$
R_z = \frac{u_x}{i_x}, \qquad G_z = \frac{i_x}{u_x}
$$
Wszystkie źródła **niezależne** wewnątrz dwójnika są **wyłączone**
($E \to$ zwarcie, $J \to$ rozwarcie); **źródła sterowane zostają**.
:::

::: wzor Łączenia i przekształcenie Y–Δ
połączenie **szeregowe**: $R_z = \sum R_n$; połączenie **równoległe**:
$G_z = \sum G_n$ (dla dwóch oporów: $R_z = \dfrac{R_1R_2}{R_1+R_2}$).
$$
Y \to \Delta: \;\; R_{xy} = \frac{R_xR_y + R_yR_z + R_zR_x}{R_z}
\qquad
\Delta \to Y: \;\; R_x = \frac{R_{xy}R_{zx}}{R_{xy}+R_{yz}+R_{zx}}
$$
:::

::: uwaga Jak zapamiętać Y–Δ bez wkuwania
Wzór $\Delta\to Y$ ma w liczniku **iloczyn dwóch boków wychodzących z węzła
$x$**, a w mianowniku **sumę wszystkich trzech**. Wzór $Y\to\Delta$ to
odwrotność: w liczniku suma **iloczynów par**, w mianowniku bok **przeciwny**
do szukanego. Kontrola: dla trzech równych oporów $R$: $\Delta\to Y$ daje
$R^2/3R = R/3$, a $Y\to\Delta$ daje $3R^2/R = 3R$ ✔ (trójkąt z $3R$ jest
równoważny gwieździe z $R$).
:::

::: figura figury/mostek.svg | Mostek niezrównoważony: żadnej pary oporów nie da się połączyć ani szeregowo, ani równolegle. Ratunek: przekształcenie Δ→Y.
:::

::: przyklad Przykład 3.2 — $R_z$ mostka przez Δ→Y
Dane: $R_1 = 10\ \Omega$ (A–C), $R_2 = 20\ \Omega$ (A–D), $R_3 = 30\ \Omega$
(C–B), $R_4 = 40\ \Omega$ (D–B), $R_5 = 50\ \Omega$ (C–D). Szukamy $R_z$
między A i B.

**Krok 1.** Trójkąt tworzą $R_1$, $R_2$, $R_5$ (węzły A, C, D). Suma:
$10 + 20 + 50 = 80\ \Omega$.
$$
R_A = \frac{R_1R_2}{\sum} = \frac{200}{80} = 2{,}5\ \Omega, \quad
R_C = \frac{R_1R_5}{\sum} = \frac{500}{80} = 6{,}25\ \Omega, \quad
R_D = \frac{R_2R_5}{\sum} = \frac{1000}{80} = 12{,}5\ \Omega
$$

**Krok 2.** Gwiazda dała nowy węzeł N. Gałęzie: C–B: $R_C + R_3 = 36{,}25\ \Omega$;
D–B: $R_D + R_4 = 52{,}5\ \Omega$; te dwie są **równolegle**:
$$
36{,}25 \| 52{,}5 = \frac{36{,}25 \cdot 52{,}5}{88{,}75} = 21{,}44\ \Omega
$$

**Krok 3.** Szeregowo z $R_A$:
$$
R_z = 2{,}5 + 21{,}44 = 23{,}94\ \Omega
$$

**Kontrola (metoda $u_x/i_x$):** przyłożenie $1\ \mathrm{A}$ do zacisków A–B daje
$u_x = 23{,}94\ \mathrm{V}$ — wynik identyczny ✔ (a rachunek numeryczny jest tu
niezależnym sprawdzeniem, bo nie używa Δ→Y).
:::

::: figura figury/delta_y.svg | Przekształcenie trójkąt–gwiazda i z powrotem. Strzałkę „⇄” czytaj: oba trójniki są równoważne **zaciskowo** (x, y, z), nie wewnętrznie.
:::

::: pulapka Kiedy Δ→Y, a kiedy Y→Δ
Wybieraj to przekształcenie, które **usuwa węzeł** (Δ→Y) albo **usuwa oczko**
(Y→Δ). W mostku węzeł C i D są „zawieszone” między dwoma oporami — usunięcie
węzła C (Δ→Y) natychmiast daje szeregowo-równoległy układ. Odwrotny kierunek
(Y→Δ) przydaje się, gdy w gwieździe jest **źródło** (bo w trójkącie źródło
zniknie z drogi obliczeń).
:::

### 3.4 Opór zastępczy dwójnika ze źródłem sterowanym

`[W3/s.10]` Dwójnik **bez źródeł niezależnych**, ale ze źródłami sterowanymi,
jest nadal **elementem bezźródłowym** — ma sensowny $R_z$. Nie da się go jednak
policzyć „zwijaniem”, bo źródło sterowane nie pozwala na proste łączenie.

::: metoda Metoda $u_x / i_x$
1. Wyłącz źródła niezależne (jeśli są) — źródła sterowane **zostają**.
2. Przyłącz do zacisków **zewnętrzne** źródło $u_x$.
3. Zaznacz prąd $i_x$ **wpływający** do zacisku (zgodny ze zwrotem $u_x$).
4. Zapisz równania Kirchhoffa **względem $u_x$ i $i_x$** (traktuj je jak
   symbole, nie liczby).
5. Wyznacz stosunek $R_z = u_x/i_x$.
:::

::: przyklad Przykład 3.3 — dodatni i ujemny $R_z$
Dwójnik: opór $R = 1\ \mathrm{k\Omega}$ oraz równolegle źródło sterowane VCCS
o wydajności $g u_x$, gdzie $u_x$ to napięcie **na zaciskach dwójnika**,
$g = 2\ \mathrm{mS}$.

**Wariant A — VCCS pobiera prąd z zacisku A (płynie A→B):**
$$
i_x = \frac{u_x}{R} + g u_x = u_x\left(\frac{1}{1000} + 0{,}002\right)
\;\Rightarrow\; R_z = \frac{1}{0{,}001 + 0{,}002} = 333\ \Omega
$$

**Wariant B — VCCS wtłacza prąd do zacisku A (płynie B→A):**
$$
i_x = \frac{u_x}{R} - g u_x = u_x\left(0{,}001 - 0{,}002\right)
\;\Rightarrow\; R_z = \frac{1}{0{,}001 - 0{,}002} = -1000\ \Omega
$$

**Interpretacja:** $R_z < 0$ znaczy, że dwójnik **oddaje** moc do źródła $u_x$
zamiast ją pobierać — jest **aktywny**, mimo że nie ma w nim żadnego źródła
niezależnego. Taki dwójnik nie da się zrealizować pasywnie (potrzebne jest
zasilanie źródła sterowanego).
:::

::: pulapka $R_z$ ujemne nie jest błędem rachunku
Jeśli wyjdzie $-1000\ \Omega$ i wynik „nie ma sensu fizycznego” — to nie znaczy,
że jest zły. Znaczy, że dwójnik jest aktywny. W zadaniach testowych taka
odpowiedź bywa **poprawna**. Ale uwaga: dla $R_z < 0$ **nie** stosuje się
wzorów na dopasowanie (§4.9) — maksimum mocy nie istnieje.
:::

### 3.5 Zamiana źródeł

`[W3/s.11–13]`

::: wzor Łączenie i zamiana źródeł
**Łączenie tego samego rodzaju (ze zwrotami!):** źródła napięciowe
szeregowo $E_z = \sum E_n$; źródła prądowe równolegle $J_z = \sum J_n$.
**Źródło rzeczywiste napięciowe $\leftrightarrow$ prądowe:**
$$
J = \frac{E}{R_w}, \quad G_w = \frac{1}{R_w}
\qquad\Longleftrightarrow\qquad
E = \frac{J}{G_w}, \quad R_w = \frac{1}{G_w}
$$
:::

::: uwaga Dwie „dziwne” reguły z $[W3/s.12]$
* Idealne źródło napięciowe **równolegle** z dowolnym elementem (byle nie
  drugim i.ź.n. o innej wartości) = **to samo źródło**. Element równoległy nie
  ma wpływu na napięcie zaciskowe.
* Idealne źródło prądowe **szeregowo** z dowolnym elementem (byle nie drugim
  i.ź.p. o innej wartości) = **to samo źródło**. Element szeregowy nie ma
  wpływu na prąd.
* W obu przypadkach element „znikający” **nie znika z bilansu mocy** — on
  nadal istnieje, tylko nie wpływa na wielkości zaciskowe.
:::

::: przyklad Przykład 3.4 — łańcuch zamian
Źródło rzeczywiste: $E = 24\ \mathrm{V}$, $R_w = 6\ \Omega$, obciążone
$R_0 = 3\ \Omega$.

**Droga 1 (bez zamiany):** $I = 24/9 = 2{,}\overline{6}\ \mathrm{A}$,
$U = I R_0 = 8\ \mathrm{V}$.

**Droga 2 (zamiana):** $J = E/R_w = 4\ \mathrm{A}$, $G_w = 1/6\ \mathrm{S}$
(6 Ω równolegle). Równolegle z $R_0$: $R = 6 \| 3 = 2\ \Omega$. Napięcie:
$U = J R = 4 \cdot 2 = 8\ \mathrm{V}$ ✔ Prąd obciążenia:
$I = U/R_0 = 8/3 = 2{,}\overline{6}\ \mathrm{A}$ ✔

**Droga 3 (z powrotem do napięciowego):** $E' = J R = 8\ \mathrm{V}$,
$R_w' = 2\ \Omega$ — i to jest **już źródło Thévenina** tego układu (§3.6).
:::

### 3.6 Twierdzenie Thévenina i Nortona

`[W3/s.14–18]` To najważniejsze twierdzenie całego wykładu — i najczęściej
egzaminowane.

::: def Definicja — twierdzenie Thévenina
Dowolny **rezystancyjny dwójnik liniowy** (inny niż idealne źródło prądowe)
o zaciskach A–B można zastąpić **rzeczywistym źródłem napięciowym**:
* $E_T$ = napięcie na **rozwartych** zaciskach A–B,
* $R_W$ = opór zastępczy dwójnika po **wyłączeniu** wszystkich źródeł
  niezależnych (źródła sterowane zostają).
:::

::: def Definicja — twierdzenie Nortona
Dowolny **rezystancyjny dwójnik liniowy** (inny niż idealne źródło napięciowe)
o zaciskach A–B można zastąpić **rzeczywistym źródłem prądowym**:
* $J_N$ = prąd płynący między **zwartymi** zaciskami A–B,
* $G_W = 1/R_W$ = przewodność zastępcza po wyłączeniu źródeł niezależnych.
:::

::: wzor Związek parametrów
$$
E_T = \frac{J_N}{G_W} = J_N R_W \qquad \Longleftrightarrow \qquad J_N = \frac{E_T}{R_W}
$$
Wystarczy więc policzyć **dwa z trzech** parametrów $E_T$, $J_N$, $R_W$.
:::

::: figura figury/thevenin.svg | Dwójnik oryginalny i jego równoważnik Thévenina z dołączonym obciążeniem $R_2$. Zaciski A–B „widzą” dokładnie to samo.
:::

::: metoda Który parametr liczyć najłatwiej ($[W3/s.16]$)
* do zacisków dochodzi **opór szeregowy** → łatwiej $E_T$ (bo przez rozwarcie
  nie płynie prąd i część spadków znika),
* między zaciskami jest **opór równoległy** → łatwiej $J_N$ (bo zwarcie zeruje
  napięcie i część prądów znika),
* w układzie jest **wiele źródeł niezależnych** → najpierw $R_W$ (wyłączanie
  źródeł redukuje obwód do samych oporów).
:::

::: przyklad Przykład 3.5 — komplet parametrów $E_T$, $J_N$, $R_W$
Obwód odniesienia z §2.4, zaciski A–B utworzone **po wyjęciu** $R_2$
(czyli dwójnik: $E_1$, $R_1$ w lewej gałęzi; $R_3$, $E_2$ w prawej).

**$E_T$ — z definicji (zaciski rozwarte):** w obwodzie płynie jeden prąd
oczkowy, $i = (E_1 - E_2)/(R_1 + R_3) = (12 - 4)/4 = 2\ \mathrm{A}$ (zgodnie
z $E_1$). Wtedy
$$
E_T = E_1 - R_1 i = 12 - 2\cdot 2 = 8\ \mathrm{V}
$$
Kontrola z prawej gałęzi: $E_2 + R_3 i = 4 + 4 = 8\ \mathrm{V}$ ✔

**$J_N$ — z definicji (zaciski zwarte):** zwarcie zwiera węzeł A z masą, więc
$$
J_N = \frac{E_1}{R_1} + \frac{E_2}{R_3} = \frac{12}{2} + \frac{4}{2} = 8\ \mathrm{A}
$$
(dwa źródła „pchają” prąd do zwarcia w tę samą stronę).

**$R_W$ — po wyłączeniu źródeł:** $E_1$ i $E_2$ to zwarcia, więc z zacisków
A–B widać $R_1$ **równolegle** do $R_3$:
$$
R_W = R_1 \| R_3 = \frac{2\cdot2}{4} = 1\ \Omega
$$

**Kontrola spójności:** $E_T = J_N R_W = 8 \cdot 1 = 8\ \mathrm{V}$ ✔

**Zastosowanie:** po dołączeniu $R_2 = 3\ \Omega$:
$I = E_T/(R_W + R_2) = 8/4 = 2\ \mathrm{A}$, $U = I R_2 = 6\ \mathrm{V}$,
$P = I^2 R_2 = 12\ \mathrm{W}$ — dokładnie jak w §2.4 ✔
:::

::: pulapka Znaki przy $E_T$ i $J_N$
* $E_T$ zastrzałkowujemy **od B do A** (albo odwrotnie — byle konsekwentnie
  na schemacie; wynik może wyjść ujemny i to jest OK).
* $J_N$ zastrzałkowujemy **od A do B przez zwarcie**.
* Jeżeli liczysz $R_W = E_T/J_N$, to $E_T$ i $J_N$ muszą być zastrzałkowane
  **przeciwnie** względem siebie (każde na swoim schemacie). Inaczej dostaniesz
  $R_W < 0$ bez powodu.
:::

::: przyklad Przykład 3.6 — dwójnik ze źródłem sterowanym: $R_W$ ujemne
Dwójnik z Przykładu 3.3 w wariancie B ($R = 1\ \mathrm{k\Omega}$ równolegle
z VCCS $g u_x$, $g = 2\ \mathrm{mS}$, prąd wtłaczany do zacisku).

Zaciski **rozwarte**: przez $R$ płynie tylko prąd źródła sterowanego? Nie —
przy rozwarciu $u_x$ jest napięciem na $R$, a prąd źródła sterowanego zależy od
$u_x$: jedyne równanie to $u_x/R - g u_x = 0 \Rightarrow u_x(0{,}001-0{,}002)=0
\Rightarrow u_x = 0$. Czyli $E_T = 0\ \mathrm{V}$ — co jest typowe dla
dwójników **aktywnych** ze sprzężeniem dodatnim.

Wtedy z $E_T = J_N R_W$ przy $E_T = 0$ mamy $J_N = 0$ i $R_W$ trzeba wyznaczyć
**osobno**, z definicji ($u_x/i_x$) — i wychodzi $-1\ \mathrm{k\Omega}$.
**Wniosek:** dla dwójnika ze źródłami sterowanymi **nigdy** nie zakładaj, że
$E_T \ne 0$; licz $R_W$ z pobudzenia.
:::

::: uwaga Po co komu Thévenin, jeśli można rozwiązać układ równań
Bo zamienia **cały obwód w dwa parametry**. Zysk jest ogromny, gdy:
* do zacisków dołączamy **wiele różnych** obciążeń (liczymy raz, stosujemy wiele razy),
* obciążenie jest **nieliniowe** (dioda) — wtedy jedyne sensowne podejście (§4.7),
* szukamy **maksimum mocy** (§4.9),
* trzeba **szybko** podać wynik bez rozwiązywania układu 4 równań.
:::

### 3.7 Ćwiczenia do wykładu 3

::: przyklad Ćwiczenie 3.1
Trzy opory: $6\ \Omega$, $3\ \Omega$ i $2\ \Omega$ połączone równolegle.
Ile wynosi $R_z$?

**Odpowiedź:** $G_z = 1/6 + 1/3 + 1/2 = 1\ \mathrm{S} \Rightarrow R_z = 1\ \Omega$.
(Równoległe łączenie liczy się wygodniej w konduktancjach — to ta sama
obserwacja, co dzielnik prądowy.)
:::

::: przyklad Ćwiczenie 3.2
Dwójnik: źródło $E = 10\ \mathrm{V}$ z $R_w = 2\ \Omega$ w gałęzi, do zacisków
A–B dołączony opór $R = 8\ \Omega$, a do zacisku A dochodzi jeszcze opór
$R_p = 4\ \Omega$ do masy. Policz $E_T$, $R_W$, a potem prąd w $R$.

**Odpowiedź:** $E_T$ (rozwarcie A–B): dzielnik $R_w$ z $R_p$:
$E_T = 10 \cdot 4/6 = 6{,}\overline{6}\ \mathrm{V}$, $R_W = R_w \| R_p = 1{,}\overline{3}\ \Omega$.
Prąd w $R = 8\ \Omega$: $I = 6{,}\overline{6}/(1{,}\overline{3}+8) = 0{,}714\ \mathrm{A}$.
:::

::: przyklad Ćwiczenie 3.3
Dwie gałęzie połączone równolegle między zaciskami A–B:
$E_1 = 6\ \mathrm{V}$ z $R_1 = 2\ \Omega$ oraz $E_2 = 2\ \mathrm{V}$
z $R_2 = 2\ \Omega$ (oba źródła z „+” zwróconym do A).
Policz $E_T$, $J_N$, $R_W$ i sprawdź spójność.

**$E_T$ (A–B rozwarte):** prąd płynie jednym oczkiem, źródła działają
przeciwnie w oczku, więc $i = (6-2)/4 = 1\ \mathrm{A}$; z gałęzi 1:
$E_T = E_1 - R_1 i = 6 - 2 = 4\ \mathrm{V}$ (z gałęzi 2: $E_2 + R_2 i = 2 + 2 = 4\ \mathrm{V}$ ✔).

**$J_N$ (A–B zwarte):** oba źródła tłoczą prąd do zwarcia w tę samą stronę:
$J_N = 6/2 + 2/2 = 4\ \mathrm{A}$.

**$R_W$ (źródła zwarte):** $R_1 \| R_2 = 1\ \Omega$.

**Spójność:** $E_T = J_N R_W = 4 \cdot 1 = 4\ \mathrm{V}$ ✔

**Obciążenie $R = 4\ \Omega$:** $I = 4/(1+4) = 0{,}8\ \mathrm{A}$,
$U = 3{,}2\ \mathrm{V}$, $P = 2{,}56\ \mathrm{W}$.
:::

::: uwaga Co pokazuje Ćwiczenie 3.3
To nie jest żart — tak wygląda typowy błąd na kolokwium: „policzyłem $J_N$,
policzyłem $R_W$, wynik gotowy”. Kontrola $E_T = J_N R_W$ kosztuje 10 sekund i
wychwytuje pomyłkę natychmiast. Metody Thévenina i Nortona są **dwiema
stronami tego samego twierdzenia** — muszą dać ten sam obwód.
:::

## 4. Wykład 4 — elementy nieliniowe, wzmacniacz operacyjny, moc

### 4.1 Wzmacniacz operacyjny jako źródło sterowane o $k \to \infty$

`[W4/s.3]` Wykład definiuje WO **granicznie**: to źródło napięciowe sterowane
napięciem $u_1 = u_+ - u_-$ o wzmocnieniu $k \to \infty$. Przy skończonym $k$
charakterystyka $u_2(u_1)$ to bardzo stroma prosta; przy $k\to\infty$ — prosta
**pionowa w zerze**.

::: przyklad Przykład 4.1 — dlaczego $u_1 \approx 0$
Realny WO: $k = 10^5$, zasilanie $\pm 12\ \mathrm{V}$. Dopóki wzmacniacz nie jest
nasycony, $|u_2| \le 12\ \mathrm{V}$, więc
$$
|u_1| = \frac{|u_2|}{k} \le \frac{12}{10^5} = 0{,}12\ \mathrm{mV}
$$
To jest **120 mikrowoltów** — mniej niż błąd napięcia niezrównoważenia
typowych WO. Dlatego w modelu idealnym przyjmuje się $u_1 = 0$: to nie
uproszczenie „dla wygody”, ale konsekwencja $k\to\infty$.
:::

::: def Definicja — idealny WO w zamkniętej pętli ujemnego sprzężenia
$$
i_+ = i_- = 0, \qquad u_1 = u_+ - u_- = 0
$$
a $u_2$ oraz $i_2$ **dostosowują się** do reszty obwodu (prąd $i_2$ wraca do
wzmacniacza końcówką masy).
:::

::: pulapka Kiedy te równania NIE obowiązują
* **Brak ujemnego sprzężenia** (albo sprzężenie dodatnie) — WO pracuje jako
  komparator, $u_1 \ne 0$, wyjście „przykleja się” do szyny zasilania.
* **Nasycenie** — jeżeli z równań wychodzi $|u_2| > U_{zas}$, to WO jest
  nasycony i $u_1 = 0$ przestaje być prawdą (jest to wtedy $u_1 = U_{zas}/k$).
  Dlatego po każdym wyniku **sprawdź zakres** $|u_2| \le U_{zas}$.
:::

### 4.2 Wzmacniacz odwracający i nieodwracający — wyprowadzenie

::: figura figury/wo.svg | Dwie konfiguracje WO z ujemnym sprzężeniem. Węzeł wejścia odwracającego jest w obu przypadkach „wirtualną masą” (odwracający) albo „wirtualną kopią” $u_i$ (nieodwracający).
:::

::: metoda Jak liczyć układ z WO (3 kroki)
1. Wpisz warunki idealnego WO: $i_+ = i_- = 0$, $u_+ = u_-$.
2. Zapisz **MPK** w węźle, do którego dochodzi sprzężenie (tam wchodzi $R_1$
   i $R_2$) — prąd wejściowy wzmacniacza jest zerowy, więc suma prądów
   w $R_1$ i $R_2$ wynosi zero.
3. Rozwiąż liniowe równanie na $u_2$.
:::

::: przyklad Przykład 4.2 — odwracający
Dane: $R_1 = 10\ \mathrm{k\Omega}$ (od $u_i$ do węzła $u_-$),
$R_2 = 100\ \mathrm{k\Omega}$ (od $u_-$ do wyjścia), wejście $+$ do masy.

Ponieważ $u_+ = 0$ i $u_+ = u_-$, mamy $u_- = 0$ (**wirtualna masa**).
MPK w węźle $u_-$ (prąd z $u_i$ przez $R_1$ + prąd z $u_2$ przez $R_2$ = 0):
$$
\frac{u_i - 0}{R_1} + \frac{u_2 - 0}{R_2} = 0
\;\Rightarrow\;
u_2 = -\frac{R_2}{R_1}u_i = -10\,u_i
$$
Dla $u_i = 0{,}2\ \mathrm{V}$: $u_2 = -2\ \mathrm{V}$ ✔ (znak minus = odwrócenie
fazy). Kontrola zakresu: $|{-2}| < 12$ — wzmacniacz liniowy ✔

**Uwaga o prądach:** przez $R_1$ płynie $i = 0{,}2/10\ \mathrm{k} = 20\ \mathrm{\mu A}$
i **ten sam** prąd płynie przez $R_2$ (bo do węzła $u_-$ nic nie wpływa).
Napięcie na $R_2$: $20\ \mathrm{\mu A} \cdot 100\ \mathrm{k\Omega} = 2\ \mathrm{V}$ ✔
:::

::: przyklad Przykład 4.3 — nieodwracający
Ten sam układ, ale $u_i$ podane na wejście $+$, a $R_1$ idzie od węzła $u_-$
do masy.

$u_+ = u_i$, więc $u_- = u_i$. Dzielnik napięciowy z wyjścia na wejście $-$:
$$
u_- = u_2\frac{R_1}{R_1 + R_2} = u_i
\;\Rightarrow\;
u_2 = u_i\left(1 + \frac{R_2}{R_1}\right) = 11\,u_i
$$
Dla $u_i = 0{,}2\ \mathrm{V}$: $u_2 = 2{,}2\ \mathrm{V}$. Wzmocnienie 11 = $1 + 100/10$
— **nigdy mniejsze od 1**, w przeciwieństwie do konfiguracji odwracającej
(tam $|k|$ może być mniejsze od 1).
:::

::: przyklad Przykład 4.4 — nasycenie
Odwracający z $R_2/R_1 = 10$, zasilanie $\pm 12\ \mathrm{V}$. Dla jakiego $u_i$
wzmacniacz wchodzi w nasycenie?

Warunek liniowy: $|u_2| = 10|u_i| \le 12 \Rightarrow |u_i| \le 1{,}2\ \mathrm{V}$.
Dla $u_i = 2\ \mathrm{V}$ równanie daje $u_2 = -20\ \mathrm{V}$ — **niemożliwe**,
więc $u_2 = -12\ \mathrm{V}$ (nasycenie), a $u_- \ne 0$ (wynosi wtedy
$u_2 R_1/(R_1+R_2) + \ldots$ — i cała analiza liniowa przestaje obowiązywać).
:::

### 4.3 Opór nieliniowy: $R_s$ i $R_d$

`[W4/s.5]`

::: def Definicja — opór statyczny i dynamiczny
W punkcie pracy $(U_0, I_0)$ leżącym na charakterystyce.

Opór **statyczny** (sieczna z początku układu):
$$
R_s = \frac{U_0}{I_0}, \qquad G_s = \frac{I_0}{U_0}
$$
Opór **dynamiczny** (styczna w punkcie pracy):
$$
R_d = \left.\frac{\mathrm{d}u}{\mathrm{d}i}\right|_{(U_0,I_0)}, \qquad
G_d = \left.\frac{\mathrm{d}i}{\mathrm{d}u}\right|_{(U_0,I_0)}
$$
Dla oporu liniowego $R_s = R_d = R$.
:::

::: figura figury/nieliniowy.svg | Po lewej: $R_s$ (sieczna od zera) i $R_d$ (styczna w punkcie pracy). Po prawej: punkt pracy jako przecięcie charakterystyki obciążenia z prostą oporu źródła zastępczego.
:::

::: przyklad Przykład 4.5 — $R_s$ i $R_d$ z charakterystyki
Dioda w punkcie pracy $U_0 = 0{,}8\ \mathrm{V}$, $I_0 = 20\ \mathrm{mA}$;
w tym punkcie nachylenie charakterystyki $\mathrm{d}i/\mathrm{d}u = 200\ \mathrm{mA/V}$.

$$
R_s = \frac{0{,}8}{0{,}020} = 40\ \Omega, \qquad
R_d = \frac{1}{0{,}200} = 5\ \Omega
$$
Różnica jest ogromna (8×) — i to jest sedno: **w małosygnałowym modelu diody**
używa się $R_d$ (5 Ω), a do punktu pracy — $R_s$ (40 Ω). Podstawienie jednego
zamiast drugiego to najczęstszy błąd w zadaniach z diodą.
:::

### 4.4 Dioda idealna i metoda dwustanowa

`[W4/s.6]` Dioda idealna (zwarciowo-rozwarciowa), przy prądzie zastrzałkowanym
w kierunku przewodzenia: $i = 0$ dla $u < 0$ oraz $u = 0$ dla $i > 0$.

::: metoda Metoda dwustanowa (zawsze działa)
1. **Załóż stan 1** (dioda przewodzi): zastąp diodę **zwarciem**, policz $i$.
   Jeśli $i > 0$ — założenie poprawne, koniec.
2. Jeśli $i < 0$ — założenie **fałszywe**. **Załóż stan 2** (dioda zatkana):
   zastąp ją **rozwarciem**, policz $u$. Jeśli $u < 0$ — poprawne.
3. Jeżeli oba warunki „nie wychodzą”, w zadaniu jest błąd (albo dioda jest
   w stanie granicznym $i = 0$, $u = 0$).
:::

::: przyklad Przykład 4.6 — metoda dwustanowa
**Wariant A:** $E = 5\ \mathrm{V}$, $R = 1\ \mathrm{k\Omega}$, dioda w kierunku
przewodzenia.
Załóżmy przewodzenie (zwarcie): $i = (5 - 0)/1000 = 5\ \mathrm{mA} > 0$ ✔
Stan poprawny: $i = 5\ \mathrm{mA}$, $u_D = 0$.

**Wariant B:** $E = -3\ \mathrm{V}$, reszta bez zmian.
Załóżmy przewodzenie: $i = -3/1000 = -3\ \mathrm{mA} < 0$ ✘
Załóżmy zatkanie (rozwarcie): $i = 0$, $u_D = E = -3\ \mathrm{V} < 0$ ✔
Stan poprawny: $i = 0$, $u_D = -3\ \mathrm{V}$.

**Wniosek:** dioda „nie przewodzi prądu wstecz”, ale **napięcie na niej jest**
— równe napięciu reszty obwodu.
:::

### 4.5 Składanie charakterystyk

`[W4/s.7–8]` Gdy elementów nieliniowych jest kilka, nie da się ich „zwinąć” —
składa się **charakterystyki**:

* **równolegle**: dla każdego $u$ **sumujemy prądy** elementów,
* **szeregowo**: dla każdego $i$ **sumujemy napięcia** elementów.

::: uwaga Kolejność osi ma znaczenie
Równolegle sumujemy prądy (bo napięcie jest wspólne) — czyli pracujemy „w
funkcji $u$”. Szeregowo sumujemy napięcia (bo prąd jest wspólny) — pracujemy
„w funkcji $i$”. Jeśli charakterystyka jest podana jako $i(u)$, a łączymy
szeregowo, trzeba ją **odwrócić** (albo sumować w poziomie, nie w pionie).
:::

### 4.6 Układ z jednym elementem nieliniowym — schemat postępowania

`[W4/s.9–11]` To jest **najważniejsza procedura** wykładu 4:

::: metoda Cztery kroki dla jednego elementu nieliniowego
1. **Podziel obwód** na część liniową i element nieliniowy, połączone
   zaciskami A–B.
2. Część liniową zastąp **źródłem Thévenina** ($E_T$, $R_W$) lub Nortona.
3. Wyznacz **punkt pracy** jako przecięcie charakterystyki źródła
   ($i = E_T/R_W - u/R_W$ — tzw. **prosta oporu**) z charakterystyką elementu
   nieliniowego.
4. Wróć do oryginalnego obwodu i **z zasadą kompensacji** policz pozostałe
   napięcia i prądy (element nieliniowy zastąp źródłem $E = U_0$ lub $J = I_0$).
:::

::: przyklad Przykład 4.7 — dioda odcinkowo-liniowa na tle Thévenina
Część liniowa: $E_T = 2\ \mathrm{V}$, $R_W = 100\ \Omega$. Obciążenie: dioda
modelowana odcinkowo-liniowo: $u_D = U_0 + R_d i$ z $U_0 = 0{,}7\ \mathrm{V}$,
$R_d = 10\ \Omega$ (dla $i > 0$).

**Punkt pracy** (przecięcie prostej oporu z charakterystyką):
$$
i = \frac{E_T - U_0}{R_W + R_d} = \frac{2 - 0{,}7}{110} = 11{,}8\ \mathrm{mA},
\qquad u_D = 0{,}7 + 10 \cdot 0{,}0118 = 0{,}818\ \mathrm{V}
$$
**Kontrola:** $u_D = E_T - R_W i = 2 - 100 \cdot 0{,}0118 = 0{,}818\ \mathrm{V}$ ✔
Oraz $i > 0$ — założenie przewodzenia poprawne ✔

**Bilans mocy (Tellegen):** źródło oddaje $P = E_T i = 23{,}6\ \mathrm{mW}$;
$R_W$ pochłania $i^2R_W = 14{,}0\ \mathrm{mW}$; dioda $u_D i = 9{,}7\ \mathrm{mW}$;
suma $14{,}0 + 9{,}7 = 23{,}7\ \mathrm{mW}$ ✔ (różnica 0,1 mW to zaokrąglenia).
:::

::: przyklad Przykład 4.8 — powrót do wnętrza obwodu (kompensacja)
Część liniowa z Przykładu 4.7 niech ma postać: $E = 6\ \mathrm{V}$ z
$R_1 = 50\ \Omega$ szeregowo, a do zacisków A–B dołączony jest opór
$R_p = 100\ \Omega$.

**Parametry zastępcze:** przy rozwartych zaciskach A–B działa zwykły dzielnik,
więc
$$
E_T = E\cdot\frac{R_p}{R_1 + R_p} = 6\cdot\frac{100}{150} = 4\ \mathrm{V},
\qquad R_W = R_1 \| R_p = 33{,}3\ \Omega
$$

**Punkt pracy** (dioda $0{,}7\ \mathrm{V} + 10\ \Omega$, jak w Przykładzie 4.7):
$$
i = \frac{4 - 0{,}7}{33{,}3 + 10} = 76{,}2\ \mathrm{mA},
\qquad u_D = 0{,}7 + 10\cdot0{,}0762 = 1{,}46\ \mathrm{V}
$$

**Powrót do wnętrza (kompensacja):** dioda jest teraz źródłem
$U_0 = 1{,}46\ \mathrm{V}$, więc obwód liniowy rozwiązuje się jednym
dzieleniem: prąd $i$ płynie przez $R_1$, zatem napięcie węzła pośredniego
$V = E - R_1 i = 6 - 50\cdot0{,}0762 = 2{,}19\ \mathrm{V}$, a prąd w $R_p$
wynosi $V/R_p = 21{,}9\ \mathrm{mA}$; reszta ($54{,}3\ \mathrm{mA}$) płynie
do diody ✔ (KCL: $76{,}2 = 21{,}9 + 54{,}3$).

**Po co to wszystko:** bez kompensacji trzeba by rozwiązywać układ nieliniowy
od nowa dla każdej wielkości wewnętrznej. Z kompensacją — jedno prawo Ohma.
:::

### 4.7 Moc: chwilowa, w oporze, w źródłach

`[W4/s.12–13]`

::: wzor Moc chwilowa
Przy strzałkach **przeciwnych** (konwencja odbiornikowa) moc pobierana przez
element wynosi
$$
p = ui
$$
i wtedy: $p > 0$ — element **pobiera** moc, $p < 0$ — element **oddaje** moc.
Moc **oddawana** przez element to $p_o = -ui$.

Dla oporu: $p = ui = Ri^2 = Gu^2 = \dfrac{u^2}{R}$ — **zawsze dodatnia**
(opór nigdy nie oddaje mocy).
Dla źródeł idealnych: $p_o = ei$ (napięciowe), $p_o = ju$ (prądowe).
:::

::: przyklad Przykład 4.9 — bilans mocy w obwodzie odniesienia
Obwód z §2.4: $E_1 = 12\ \mathrm{V}$, $I_1 = 3\ \mathrm{A}$;
$E_2 = 4\ \mathrm{V}$, $I_3 = 1\ \mathrm{A}$; $R_1 = 2\ \Omega$, $I_1 = 3\ \mathrm{A}$;
$R_2 = 3\ \Omega$, $I_2 = 2\ \mathrm{A}$; $R_3 = 2\ \Omega$, $I_3 = 1\ \mathrm{A}$.

**Opory (zawsze pobierają):**
$P_{R1} = I_1^2R_1 = 9 \cdot 2 = 18\ \mathrm{W}$;
$P_{R2} = I_2^2R_2 = 4 \cdot 3 = 12\ \mathrm{W}$;
$P_{R3} = I_3^2R_3 = 1 \cdot 2 = 2\ \mathrm{W}$; razem $32\ \mathrm{W}$.

**Źródła:** $E_1$ oddaje $P = E_1 I_1 = 36\ \mathrm{W}$.
Źródło $E_2$: prąd $I_3 = 1\ \mathrm{A}$ płynie przez nie **w stronę zacisku „+”**,
czyli źródło **pobiera** moc $4 \cdot 1 = 4\ \mathrm{W}$ (jest ładowane).

**Bilans:** $36 = 32 + 4$ ✔
:::

::: def Definicja — zasada Tellegena
Suma mocy chwilowych pobieranych przez **wszystkie** elementy układu jest
w każdej chwili równa zeru.
:::

::: uwaga Tellegen jako narzędzie kontroli
Zasada Tellegena jest najszybszym testem poprawności rozwiązania: wystarczy
policzyć moce wszystkich elementów. **Jeżeli bilans nie wychodzi, to nie jest
błąd zaokrągleń — to błąd znaku lub błąd prądu.** Dodatkowa korzyść: zasada
nie wymaga liniowości obwodu (obowiązuje też z diodami i źródłami sterowanymi).
:::

### 4.8 Dopasowanie energetyczne

`[W4/s.15–17]`

::: wzor Dopasowanie i moc dysponowana
Rzeczywiste źródło $E_T$, $R_W$ zasila obciążenie $R_0$:
$$
P(R_0) = \left(\frac{E_T}{R_W + R_0}\right)^2 R_0
\qquad\Rightarrow\qquad
\frac{\mathrm{d}P}{\mathrm{d}R_0} = 0 \;\Rightarrow\; R_0 = R_W
$$
Moc w stanie dopasowania (**moc dysponowana**):
$$
P_{dysp} = \frac{E_T^2}{4R_W} = \frac{J_N^2}{4G_W}
$$
Sprawność przy dopasowaniu: $\eta = \dfrac{P_{R_0}}{P_{całk}} = 50\%$.
:::

::: figura figury/dopasowanie.svg | Moc w obciążeniu w funkcji $R_0/R_W$: maksimum przy $R_0 = R_W$, wartość $P_{dysp} = E_T^2/(4R_W)$.
:::

::: przyklad Przykład 4.10 — dopasowanie w obwodzie odniesienia
Dwójnik z §3.6: $E_T = 8\ \mathrm{V}$, $R_W = 1\ \Omega$.
$P_{dysp} = 64/4 = 16\ \mathrm{W}$ przy $R_0 = 1\ \Omega$.

Sprawdzenie wprost: $I = 8/2 = 4\ \mathrm{A}$, $P = 16 \cdot 1 = 16\ \mathrm{W}$ ✔
Sprawność: źródło oddaje $8 \cdot 4 = 32\ \mathrm{W}$, w obciążeniu 16 W → $\eta = 50\%$ ✔

Dla $R_2 = 3\ \Omega$: $P = 12\ \mathrm{W}$ — **mniej** niż $P_{dysp}$, ale
sprawność $12/16 = 75\%$. To jest klasyczny kompromis: maksimum mocy **nie**
jest maksimum sprawności.
:::

::: pulapka Dopasowanie ≠ dobry projekt
W energetyce dopasowanie ($\eta = 50\%$) jest nieakceptowalne — połowa mocy
zostałaby w źródle. W elektronice sygnałowej (antena, tor audio, linia
transmisyjna) dopasowanie jest **konieczne**, bo chodzi o **moc sygnału**, a
nie o sprawność. Zadanie „dobierz $R_0$” **zawsze** znaczy „maksimum mocy”,
a nie „maksimum sprawności” — chyba że w treści napisano inaczej.
:::

::: uwaga Kiedy wzór $R_0 = R_W$ nie działa
* gdy $R_W \le 0$ (dwójnik aktywny, §3.4) — funkcja $P(R_0)$ nie ma maksimum
  w $R_0 > 0$;
* gdy obciążenie jest **nieliniowe** — nie ma „$R_0$”, jest punkt pracy;
* gdy źródło ma **ograniczenie** ($R_0$ musi być z zakresu) — maksimum wypada
  na granicy przedziału, nie w $R_W$.
:::

### 4.9 Ćwiczenia do wykładu 4

::: przyklad Ćwiczenie 4.1
WO w konfiguracji nieodwracającej: $R_1 = 1\ \mathrm{k\Omega}$,
$R_2 = 47\ \mathrm{k\Omega}$, $u_i = 20\ \mathrm{mV}$. Ile wynosi $u_2$?
Czy wzmacniacz z zasilaniem $\pm 5\ \mathrm{V}$ będzie liniowy?

**Odpowiedź:** $k = 1 + 47/1 = 48$, $u_2 = 48 \cdot 20\ \mathrm{mV} = 0{,}96\ \mathrm{V}$
— mieści się w $\pm 5\ \mathrm{V}$ ✔
:::

::: przyklad Ćwiczenie 4.2
Dioda idealna, $E = 10\ \mathrm{V}$, $R_1 = 1\ \mathrm{k\Omega}$ szeregowo,
$R_2 = 4\ \mathrm{k\Omega}$ do masy, dioda **równolegle do $R_2$** (katoda do
masy, anoda do węzła). Ile wynosi napięcie węzła?

**Odpowiedź:** załóżmy przewodzenie (dioda = zwarcie): węzeł jest zwarty do
masy → $u = 0$, prąd diody $i_D = (10-0)/1000 = 10\ \mathrm{mA} > 0$ ✔
Stan poprawny: $u = 0$, prąd przez $R_1$ wynosi 10 mA, cały płynie przez diodę,
$R_2$ jest zwarty (0 mA). Wniosek: dioda „odbiera” cały prąd.
:::

::: przyklad Ćwiczenie 4.3
Ten sam układ, ale dioda odwrócona (anoda do masy). Ile wynosi $u$?

**Odpowiedź:** przewodzenie niemożliwe (dioda spolaryzowana zaporowo dla
dodatniego $u$). Zatkanie: dzielnik $R_1$–$R_2$ daje
$u = 10 \cdot 4/5 = 8\ \mathrm{V} > 0$ — dioda zatkana, bo $u_D = -u < 0$ ✔
Wniosek: **kierunek diody zmienia wynik z 0 V na 8 V**.
:::

::: przyklad Ćwiczenie 4.4
Źródło $E_T = 12\ \mathrm{V}$, $R_W = 4\ \Omega$; obciążenie $R_0$.
Policz $P$ dla $R_0 = 2, 4, 8\ \Omega$ i wskaż maksimum.

**Odpowiedź:** $P = 144 R_0/(4+R_0)^2$: dla 2 Ω → $288/36 = 8\ \mathrm{W}$;
dla 4 Ω → $576/64 = 9\ \mathrm{W}$; dla 8 Ω → $1152/144 = 8\ \mathrm{W}$.
Maksimum przy $R_0 = R_W = 4\ \Omega$, $P_{dysp} = E_T^2/(4R_W) = 9\ \mathrm{W}$ ✔
Charakterystyka jest **symetryczna względem $R_W$** — dlatego 2 Ω i 8 Ω dają
tyle samo.
:::

## 5. Wykład 5 — sygnały okresowe i ich parametry

### 5.1 Definicja i parametry opisu

`[W5/s.3]`

::: def Definicja — sygnał okresowy
Sygnał $x(t)$ jest okresowy, jeśli istnieje $T > 0$ takie, że dla każdej chwili
$t$:
$$
x(t) = x(t + T)
$$
Najmniejsze takie $T$ to **okres**; $f = 1/T$, $\omega = 2\pi f = 2\pi/T$.
:::

::: wzor Postać sinusoidalna
$$
x(t) = X_0 + X_m \sin(\omega t + \varphi)
$$
$X_0$ — **składowa stała** (poziom odniesienia), $X_m > 0$ — **amplituda**,
$\omega$ — pulsacja [rad/s], $\varphi$ — faza początkowa.
:::

::: figura figury/sygnaly.svg | Trzy podstawowe przebiegi okresowe: prostokątny, trójkątny, sinusoidalny, z zaznaczonym poziomem odniesienia $X_0$, amplitudą $X_m$, okresem $T$ i szerokością impulsu $t_1 = \delta T$.
:::

### 5.2 Parametry amplitudowe i czasowe

`[W5/s.8–12]` Slajdy rozróżniają aż sześć „wielkości amplitudowych” — i to jest
źródłem nieporozumień:

| Symbol | Nazwa | Definicja | Uwaga |
|---|---|---|---|
| $X_0$ | poziom odniesienia (bazowy) | poziom, od którego liczy się amplitudę | **nie** musi być średnią! |
| $X_1$ | poziom wierzchołka | wartość szczytowa impulsu | $X_1 = X_0 + X_m$ |
| $X_m$ | amplituda impulsu | maksymalne odchylenie od $X_0$ | $X_m > 0$ z definicji |
| $X_{min}$, $X_{max}$ | wartości ekstremalne | z przebiegu rzeczywistego | uwzględniają asymetrię |
| $X_{pp}$ | wartość międzyszczytowa | $X_{max} - X_{min}$ | dla symetrii $= 2X_m$ |
| $\delta$ | wypełnienie (duty) | $t_1/T$ | $t_1 = \delta T$, $t_0 = (1-\delta)T$ |
| $t_n$, $t_o$ | czas narastania/opadania | czasy między 10 % a 90 % | dotyczą przebiegów rzeczywistych |

::: pulapka $X_0$ to nie „średnia”
Dla sinusoidy $X_0$ **jest** średnią. Dla prostokąta z wypełnieniem $\delta$:
$$
\bar{x} = X_0 + X_m(2\delta - 1)
$$
czyli średnia równa się $X_0$ **tylko dla** $\delta = 50\%$. Dla $\delta = 25\%$
i $X_0 = 2$ V, $X_m = 3$ V: $\bar{x} = 2 + 3(0{,}5 - 1) = 0{,}5\ \mathrm{V}$.
:::

### 5.3 Wartość średnia

`[W5/s.13–15]`

::: wzor Wartość średnia
**Odcinkami stała** (suma pól pod przebiegiem):
$$
\bar{x} = \frac{1}{T}\sum_k S_k = \frac{1}{T}\left[X_1(t_1 - t_0) + X_2(t_2 - t_1) + \ldots\right]
$$
**Ciągła** (granica sumy, czyli całka):
$$
\bar{x} = \frac{1}{T}\int_{t_0}^{t_0+T} x(t)\,\mathrm{d}t
= \lim_{\Delta t \to 0}\frac{1}{T}\sum_k x(t_k)\Delta t
$$
:::

::: uwaga Interpretacja geometryczna i praktyczna
Wartość średnia to **pole pod przebiegiem** (z znakami! pola pod osią są
ujemne) podzielone przez okres. Dla przebiegu **symetrycznego względem zera**
wynosi 0 — i to jest najczęstsza odpowiedź w zadaniach testowych. Dla przebiegu
jednopołówkowo wyprostowanego: $\bar{x} = X_m/\pi \approx 0{,}318X_m$; dla
dwupołówkowo: $2X_m/\pi \approx 0{,}637X_m$.
:::

### 5.4 Wartość skuteczna (RMS)

`[W5/s.16–17]`

::: def Definicja — wartość skuteczna
$$
X_{sk} = \sqrt{\overline{x^2}} = \sqrt{\frac{1}{T}\int_{t_0}^{t_0+T} x^2(t)\,\mathrm{d}t}
$$
Nazywana RMS (*root mean square*): pierwiastek ze **średniej kwadratu**.
:::

::: wzor RMS dla podstawowych przebiegów
**Sinusoida** $x = X_m\sin\omega t$:
$$
X_{sk} = \frac{X_m}{\sqrt{2}} \approx 0{,}707X_m
$$
**Prostokąt symetryczny:** $X_{sk} = X_m$. **Trójkąt symetryczny:**
$X_{sk} = \dfrac{X_m}{\sqrt{3}} \approx 0{,}577X_m$.

**Sinusoida z offsetem** (składowa stała $X_0$):
$$
X_{sk} = \sqrt{X_0^2 + \frac{X_m^2}{2}}
$$
:::

Wyprowadzenie dla sinusoidy (to jest na slajdzie i warto je rozumieć, a nie
wkuwać): $x^2 = X_m^2\sin^2\omega t = \frac{X_m^2}{2}(1 - \cos 2\omega t)$;
średnia składnika $\cos 2\omega t$ wynosi 0, więc $\overline{x^2} = X_m^2/2$,
czyli $X_{sk} = X_m/\sqrt{2}$ ✔

::: przyklad Przykład 5.1 — prostokąt z wypełnieniem 25 %
Przebieg: $X_0 = 2\ \mathrm{V}$, $X_m = 3\ \mathrm{V}$, $\delta = 25\%$.
Wartości: $+5\ \mathrm{V}$ przez $0{,}25T$, $-1\ \mathrm{V}$ przez $0{,}75T$.

**Średnia:** $\bar{x} = 5\cdot0{,}25 + (-1)\cdot0{,}75 = 1{,}25 - 0{,}75 = 0{,}5\ \mathrm{V}$

**RMS:** $X_{sk}^2 = 25\cdot0{,}25 + 1\cdot0{,}75 = 7 \Rightarrow X_{sk} = 2{,}646\ \mathrm{V}$

**Średnia wyprostowana:** $|x|$: $5\cdot0{,}25 + 1\cdot0{,}75 = 2\ \mathrm{V}$

**Współczynniki:** $k_k = 2{,}646/2 = 1{,}323$; $k_a = 5/2{,}646 = 1{,}890$

**Moc w $R = 1\ \Omega$:** $P = X_{sk}^2/R = 7\ \mathrm{W}$ — a nie $0{,}5^2/R = 0{,}25\ \mathrm{W}$
(średnia!) ani $2^2/R$ (średnia wyprostowana). **Tylko RMS daje moc.**
:::

### 5.5 Pozostałe parametry i współczynniki

`[W5/s.17]`

| Parametr | Definicja | Sinus | Prostokąt ($\delta=0{,}5$) | Trójkąt |
|---|---|---|---|---|
| średnia $\bar{x}$ | $\overline{x}$ | $0$ | $0$ | $0$ |
| skuteczna $X_{sk}$ | $\sqrt{\overline{x^2}}$ | $0{,}707X_m$ | $X_m$ | $0{,}577X_m$ |
| średnia wyprostowana $X_{św}$ | $\overline{|x|}$ | $0{,}637X_m$ | $X_m$ | $0{,}5X_m$ |
| szczytowa $X_p$ | $\max|x|$ | $X_m$ | $X_m$ | $X_m$ |
| międzyszczytowa $X_{pp}$ | $\max x - \min x$ | $2X_m$ | $2X_m$ | $2X_m$ |
| kształtu $k_k$ | $X_{sk}/X_{św}$ | $1{,}11$ | $1$ | $1{,}155$ |
| szczytu $k_a$ | $X_p/X_{sk}$ | $1{,}414$ | $1$ | $1{,}732$ |

::: uwaga Co te współczynniki mówią fizycznie
* $k_k$ (**kształtu**) odróżnia **kształt** przebiegu: im bardziej „szpiczasty”,
  tym $k_k$ większy (sinus 1,11; trójkąt 1,155; piła ≈ 1,15; przebieg
  wąskich impulsów — dużo więcej).
* $k_a$ (**szczytu**, crest factor) mówi, **ile razy szczyt przekracza RMS** —
  to jest parametr ważny dla izolacji i przetworników ADC (sinus 1,41;
  prostokąt 1; impulsy — nawet 10).
* Dla **każdego** przebiegu: $X_{pp} = 2X_p$ tylko przy symetrii; ogólnie
  $X_{pp} \ne 2X_{sk}$ i to jest typowa pułapka w pytaniach.
:::

### 5.6 Moc średnia — łącznik z wykładem 4

::: wzor Moc średnia w oporze
$$
P = \frac{1}{T}\int_0^T \frac{u^2(t)}{R}\,\mathrm{d}t = \frac{U_{sk}^2}{R} = I_{sk}^2 R = U_{sk}I_{sk}\cos\varphi
$$
Dla przebiegów okresowych **moc liczy się z wartości skutecznych**, nie ze
średnich ani szczytowych.
:::

::: przyklad Przykład 5.2 — od przebiegu do mocy
Grzałka $R = 50\ \Omega$ zasilana napięciem sinusoidalnym o wartości skutecznej
$230\ \mathrm{V}$ (to jest ta „sieciowa” wartość!). Amplituda:
$U_m = 230\sqrt{2} = 325\ \mathrm{V}$; międzyszczytowa $650\ \mathrm{V}$.
$$
P = \frac{230^2}{50} = 1058\ \mathrm{W}
$$
Gdyby ktoś podstawił amplitudę, dostałby $325^2/50 = 2113\ \mathrm{W}$ — **dwa
razy za dużo**. To jest najbardziej kosztowny błąd w całym rozdziale.
:::

::: pulapka Multimetr „True RMS” a multimetr tani
Tani miernik cyfrowy mierzy **wartość średnią wyprostowaną** i mnoży ją przez
$1{,}11$ (współczynnik kształtu sinusoidy). Dla sinusoidy wynik jest poprawny,
dla prostokąta **zawyża** ($1{,}11X_m$ zamiast $X_m$), a dla impulsów — zaniża
drastycznie. Miernik z **True RMS** liczy naprawdę $\sqrt{\overline{x^2}}$.
Praktyczny wniosek: dla przebiegów odkształconych trzeba mieć True RMS albo
liczyć ręcznie.
:::

### 5.7 Ćwiczenia do wykładu 5

::: przyklad Ćwiczenie 5.1
Sinusoida o $X_m = 10\ \mathrm{V}$ i składowej stałej $X_0 = 4\ \mathrm{V}$.
Policz $X_{sk}$, $X_{pp}$ i moc w $R = 8\ \Omega$.

**Odpowiedź:** $X_{sk} = \sqrt{16 + 100/2} = \sqrt{66} = 8{,}12\ \mathrm{V}$;
$X_{pp} = 2X_m = 20\ \mathrm{V}$; $P = 66/8 = 8{,}25\ \mathrm{W}$.
(Uwaga: składowa stała **zwiększa** RMS — nie można jej pominąć.)
:::

::: przyklad Ćwiczenie 5.2
Prostokąt symetryczny $\pm 5\ \mathrm{V}$, wypełnienie 50 %. Co wskaże
(a) woltomierz True RMS, (b) tani woltomierz (średniej wyprostowanej)?

**Odpowiedź:** (a) $5\ \mathrm{V}$; (b) $1{,}11 \cdot 5 = 5{,}55\ \mathrm{V}$ —
błąd $+11\%$. Dla sinusoidy oba pokazują tyle samo, dlatego ten błąd łatwo
przeoczyć.
:::

::: przyklad Ćwiczenie 5.3
Impulsy: $0\ \mathrm{V}$ przez $0{,}9T$ i $10\ \mathrm{V}$ przez $0{,}1T$.
Policz średnią, RMS i $k_a$.

**Odpowiedź:** $\bar{x} = 1\ \mathrm{V}$; $X_{sk} = \sqrt{100 \cdot 0{,}1} = 3{,}162\ \mathrm{V}$;
$k_a = 10/3{,}162 = 3{,}16$; $k_k = 3{,}162/1 = 3{,}162$.
Wniosek: wąskie impulsy mają **duży** współczynnik szczytu — dlatego mierniki
o małym zakresie szczytowym „gubią” takie przebiegi.
:::

## 6. Jak korzystam z twierdzeń i zasad

Ten rozdział jest odpowiedzią na pytanie „**po co** mi te wszystkie zasady”.
Każda z nich jest narzędziem, które zamienia jeden trudny obwód w drugi,
łatwiejszy — albo pozwala **sprawdzić** wynik. Poniżej: najpierw decyzja
(które narzędzie), potem pełne przykłady użycia, na końcu lista kontrolna.

### 6.1 Pięć pytań przed pierwszym równaniem

::: metoda Diagnoza obwodu
1. **Liniowy czy nie?** Jest dioda, tranzystor, element nieliniowy? → superpozycja,
   Thévenin i zamiana źródeł **nie** obowiązują dla całości; dziel obwód (§4.6).
2. **Ile źródeł niezależnych?** 1 → nie ma czego superponować; 2–3 → superpozycja
   bywa najszybsza; dużo → może lepiej Thévenin.
3. **Co szukam?** jedną wielkość → Thévenin/Norton; wszystkie prądy → MPK/OPK
   albo metoda oczkowa; moc → najpierw $u$ lub $i$, potem moc.
4. **Są źródła sterowane?** → nie wolno ich wyłączać; $R_z$ i $R_W$ liczy się
   przez pobudzenie $u_x/i_x$ (§3.4, §3.6).
5. **Czy wielkość sterująca przetrwa uproszczenie?** (reguła 4 z §3.2).
:::

### 6.2 Tabela decyzyjna: obwód → metoda

| Sytuacja w zadaniu | Najlepsza metoda | Dlaczego |
|---|---|---|
| dwa–trzy źródła niezależne, obwód „modularny” | **superpozycja** | każdy podukład to dzielnik |
| pytanie „ile pochodzi od $E_1$, a ile od $J$” | **superpozycja** | daje odpowiedź wprost |
| jedna szukana wielkość na zaciskach | **Thévenin / Norton** | redukcja do 2 parametrów |
| obciążenie nieliniowe (dioda) | **Thévenin + prosta oporu** | jedyna sensowna droga |
| „dobierz $R_0$ na maksimum mocy” | **Thévenin + $R_0 = R_W$** | wzór wymaga $E_T$, $R_W$ |
| obwód z mostkiem / trójkątem oporów | **Δ→Y** | usuwa węzeł |
| źródło „zawadza” w gałęzi | **ruchliwość źródeł** | przenosi problem w inne miejsce |
| układ nierozwiązywalny „wprost” (superbęzeł) | **superbęzeł / superoczko** | omija brak równania elementu |
| trzeba sprawdzić wynik | **Tellegen (bilans mocy)** | niezależna kontrola |
| obwód nieliniowy, ale szukamy tylko punktu pracy | **metoda graficzna** | przecięcie charakterystyk |
| przebieg okresowy → liczba | **RMS** (§5.4) | tylko RMS daje moc |

### 6.3 Superpozycja — trzy pełne użycia

#### 6.3.1 Dwa źródła, dwa dzielniki

::: przyklad Przykład 6.1 — superpozycja z dzielnikami
Obwód: $E = 12\ \mathrm{V}$ z $R_1 = 3\ \Omega$ do węzła A, $R_2 = 6\ \Omega$
z węzła A do masy, oraz idealne źródło prądowe $J = 1\ \mathrm{A}$ wtłaczające
prąd do węzła A.

**Podukład 1 ($E$; $J \to$ rozwarcie):** czysty dzielnik napięciowy
$$
V' = E\frac{R_2}{R_1+R_2} = 12\cdot\frac{6}{9} = 8\ \mathrm{V}
$$
**Podukład 2 ($J$; $E \to$ zwarcie):** źródło prądowe obciążone $R_1 \| R_2$
$$
V'' = J\,(R_1\|R_2) = 1\cdot 2 = 2\ \mathrm{V}
$$
**Suma:** $V = 10\ \mathrm{V}$.

**Kontrola (MPK w węźle A):**
$$
\frac{12-10}{3} + 1 = 1{,}67\ \mathrm{A}\ (\text{wplywa}), \qquad \frac{10}{6} = 1{,}67\ \mathrm{A}\ (\text{wyplywa})\;✔
$$

**Moce (Tellegen):** $E$ oddaje $12 \cdot 0{,}667 = 8\ \mathrm{W}$,
$J$ oddaje $10 \cdot 1 = 10\ \mathrm{W}$; opory: $R_1$: $0{,}667^2\cdot3 = 1{,}33\ \mathrm{W}$,
$R_2$: $16{,}67\ \mathrm{W}$; suma $18\ \mathrm{W}$ ✔
:::

::: uwaga Dlaczego superpozycja wygrywa w tym zadaniu
W obwodzie pełnym trzeba rozwiązać jedno równanie z trzema oporami; w każdym
podukładzie — jedno mnożenie (dzielnik albo $R$-zastępczą). Przy trzech źródłach
zysk rośnie: **3 proste zadania zamiast 1 trudnego** — i mniejsze ryzyko błędu
algebraicznego.
:::

#### 6.3.2 Superpozycja ze źródłem sterowanym

::: przyklad Przykład 6.2 — źródło sterowane zostaje w obu podukładach
Obwód: $E = 8\ \mathrm{V}$ z $R_1 = 2\ \Omega$ do węzła A, $R_2 = 4\ \Omega$
z A do masy, VCCS pobierające z A prąd $i_s = 0{,}25 V$, oraz
$J = 2\ \mathrm{A}$ wtłaczające prąd do A.

**Podukład 1 ($E$; $J$ rozwarte, VCCS działa):**
$$
\frac{8 - V'}{2} = \frac{V'}{4} + 0{,}25V'
\;\Rightarrow\; 4 - 0{,}5V' = 0{,}5V' \;\Rightarrow\; V' = 4\ \mathrm{V}
$$
**Podukład 2 ($J$; $E$ zwarte, VCCS działa):**
$$
-\frac{V''}{2} + 2 = \frac{V''}{4} + 0{,}25V''
\;\Rightarrow\; 2 = V'' \;\Rightarrow\; V'' = 2\ \mathrm{V}
$$
**Suma:** $V = 6\ \mathrm{V}$.

**Kontrola:**
$$
\frac{8-6}{2} + 2 = 3\ \mathrm{A}\ (\text{wplywa}), \qquad \frac{6}{4} + 0{,}25\cdot 6 = 1{,}5 + 1{,}5 = 3\ \mathrm{A}\ (\text{wyplywa})\;✔
$$
:::

::: pulapka Co byłoby, gdyby VCCS „zniknął” w podukładzie 2
Wtedy $V'' = 2/(0{,}5 + 0{,}25) = 2{,}67$ V i suma dałaby $6{,}67$ V zamiast 6 V.
Błąd 11 % — trudny do wykrycia „na oko”, łatwy do wykrycia kontrolą MPK.
:::

#### 6.3.3 Kiedy superpozycja jest zabroniona

::: przyklad Przykład 6.3 — dioda łamie superpozycję
Obwód: dwa źródła w szeregu $E_1 = 2\ \mathrm{V}$ i $E_2 = -1\ \mathrm{V}$
(przeciwsobnie), opór $R = 1\ \mathrm{k\Omega}$ i **dioda rzeczywista**
odcinkowo-liniowa $u_D = 0{,}7\ \mathrm{V} + 10\ \Omega\cdot i$.

**Obwód pełny:**
$$
i = \frac{2 - 1 - 0{,}7}{1000 + 10} = \frac{0{,}3}{1010} = 0{,}297\ \mathrm{mA}
$$

**„Superpozycja” (błędna):**
* tylko $E_1$: $i' = (2-0{,}7)/1010 = 1{,}287\ \mathrm{mA}$,
* tylko $E_2$: dioda zatkana ($u_D < 0$) → $i'' = 0$,
* suma: $1{,}287\ \mathrm{mA}$ — **4,3 raza za dużo!**

**Przyczyna:** dioda **zmienia stan** (przewodzi / nie przewodzi) i jej
charakterystyka nie jest liniowa. Zasada superpozycji obowiązuje wyłącznie
w obwodach **liniowych** `[W2/s.16]`.

**Co robić zamiast tego:** podzielić obwód na część liniową (oba źródła i $R$)
i nieliniową (dioda), zwinąć część liniową do Thévenina
($E_T = 1\ \mathrm{V}$, $R_W = 1\ \mathrm{k\Omega}$) i rozwiązać **jeden**
układ z diodą (§4.6). Wtedy wynik jest poprawny.
:::

::: zapamietaj Trzy warunki stosowalności superpozycji
1. obwód **liniowy** (żadnych diod, tranzystorów, elementów nieliniowych),
2. wyłączamy tylko źródła **niezależne**,
3. sumujemy **prądy i napięcia** — nigdy moce.
:::

### 6.4 Thévenin jako narzędzie: nieliniowe obciążenie i dobór punktu pracy

::: przyklad Przykład 6.4 — dioda LED zasilana z dwójnika
Część liniowa (dwa źródła, trzy opory — wynik zwijania): $E_T = 3\ \mathrm{V}$,
$R_W = 50\ \Omega$. Obciążenie: dioda LED modelowana jako $u_D = 1{,}8\ \mathrm{V} + 20\ \Omega\cdot i$.

**Punkt pracy bez rezystora dodatkowego:**
$$
i = \frac{3 - 1{,}8}{50 + 20} = \frac{1{,}2}{70} = 17{,}1\ \mathrm{mA}
\qquad
u_D = 1{,}8 + 20\cdot0{,}0171 = 2{,}14\ \mathrm{V}
$$
**Zadanie projektowe:** dobrać rezystor szeregowy $R_0$, aby prąd wynosił
dokładnie $10\ \mathrm{mA}$:
$$
10\ \mathrm{mA} = \frac{3 - 1{,}8}{50 + 20 + R_0}
\;\Rightarrow\;
R_0 = \frac{1{,}2}{0{,}01} - 70 = 50\ \Omega
$$
**Kontrola:** $i = 1{,}2/120 = 10\ \mathrm{mA}$ ✔; moc w diodzie
$u_D i = (1{,}8 + 0{,}2)\cdot0{,}01 = 20\ \mathrm{mW}$; moc w $R_0$: 5 mW.
:::

::: uwaga Dlaczego to jest „théveninowskie” myślenie
Trzy źródła i pięć oporów po stronie liniowej **zniknęły** — zostały dwa
parametry. Każda zmiana obciążenia (inna dioda, inny $R_0$, inny prąd) to teraz
**jedno dzielenie**, a nie rozwiązywanie układu od nowa. Dokładnie po to jest to
twierdzenie.
:::

### 6.5 Kompensacja i ruchliwość źródeł — na liczbach

Te dwie zasady są najczęściej „pomijane” przez studentów, bo wydają się
oczywiste. Tymczasem one **skracają** rachunek i pozwalają sprawdzić wynik.
Poniżej jedno zadanie rozwiązane najpierw „wprost”, a potem obiema zasadami.

::: przyklad Przykład 6.5 — trzy gałęzie równolegle
Między węzłami A i B (B = masa) trzy gałęzie:
(1) $E = 12\ \mathrm{V}$ (+ do A) i $R_1 = 6\ \Omega$,
(2) $R_2 = 3\ \Omega$,
(3) $R_3 = 6\ \Omega$.
Szukane: napięcie $V$ węzła A i prądy gałęzi.

**Wprost (MPK w węźle A):**
$$
\frac{V - 12}{6} + \frac{V}{3} + \frac{V}{6} = 0
\;\Rightarrow\; V - 12 + 2V + V = 0 \;\Rightarrow\; V = 3\ \mathrm{V}
$$
Prądy (od A do B): $i_1 = (3-12)/6 = -1{,}5\ \mathrm{A}$ (czyli 1,5 A **do** A),
$i_2 = 3/3 = 1\ \mathrm{A}$, $i_3 = 3/6 = 0{,}5\ \mathrm{A}$.
Kontrola MPK: wpływające $1{,}5\ \mathrm{A}$ = wypływające $1 + 0{,}5$ ✔
:::

::: przyklad Przykład 6.6 — to samo przez ruchliwość źródła
Przenieśmy $E$ z gałęzi 1 do **wszystkich** gałęzi (ze zwrotem odwróconym
względem węzła A), a gałąź 1 zostawmy bez źródła. Nowe równanie węzła:
$$
\frac{V'}{6} + \frac{V' + 12}{3} + \frac{V' + 12}{6} = 0
\;\Rightarrow\; V' + 2V' + 24 + V' + 12 = 0 \;\Rightarrow\; V' = -9\ \mathrm{V}
$$
Prądy: $i_1 = -9/6 = -1{,}5\ \mathrm{A}$ ✔, $i_2 = (-9+12)/3 = 1\ \mathrm{A}$ ✔,
$i_3 = (-9+12)/6 = 0{,}5\ \mathrm{A}$ ✔

**Wniosek:** prądy **identyczne**, potencjał węzła przesunięty o $-12\ \mathrm{V}$
($3 - 12 = -9$). To jest dokładnie treść zasady: invariance dotyczy **prądów**,
a nie potencjałów.

**Kiedy to się przydaje:** gdy po przesunięciu źródła gałęzie 2 i 3 stają się
**identyczne strukturalnie** (same opory), można je zwijać równolegle bez
obawy, że „zgaśnie” źródło sterujące inne gałęzie.
:::

::: przyklad Przykład 6.7 — kompensacja jako zamiana oporu na źródło
W obwodzie z Przykładu 6.5 przez $R_2$ płynie $1\ \mathrm{A}$ od A do B.
Zastąpmy gałąź $R_2$ źródłem prądowym $J_2 = 1\ \mathrm{A}$ (od A do B):
$$
\frac{V'' - 12}{6} + 1 + \frac{V''}{6} = 0
\;\Rightarrow\; V'' - 12 + 6 + V'' = 0 \;\Rightarrow\; V'' = 3\ \mathrm{V}
$$
Napięcie węzła **się nie zmieniło**, prądy pozostałych gałęzi też nie ✔

**Po co:** żeby np. policzyć wpływ *tylko* tego prądu na resztę obwodu
(superpozycja z „zamrożoną” gałęzią) albo sprawdzić, że rozwiązanie jest
wewnętrznie spójne: skoro $J_2 = 1$ A jest **także** prądem wyliczonym z $V$,
to podstawienie musi dać to samo $V$. To jest **samosprawdzające się** równanie
— tania kontrola wyniku.
:::

::: uwaga Kolejność narzędzi w praktyce
1. Policz, ile jest **źródeł niezależnych** i **węzłów**.
2. Jeśli obwód jest zbyt „posplatany” (mostek), użyj **Δ→Y** albo **Thévenina**
   dla fragmentu.
3. **Ruchliwość źródeł** stosuj wtedy, gdy źródło siedzi w gałęzi, która
   przeszkadza w zwijaniu oporów.
4. **Kompensację** traktuj jak narzędzie **kontroli** albo przygotowania obwodu
   do superpozycji — nie jak metodę rozwiązania „od zera”.
:::

### 6.6 Tellegen jako kontrola wyniku

::: przyklad Przykład 6.6 — jak bilans mocy wychwytuje błąd znaku
W obwodzie odniesienia (§2.4) student policzył $I_2 = -2\ \mathrm{A}$ (błąd
strzałkowania) i „sprawdził” MPK: $3 = -2 + 1$ ✘ — MPK już nie przechodzi.
Załóżmy jednak, że pomylił się subtelniej: $I_3 = -1\ \mathrm{A}$ i $I_2 = 4\ \mathrm{A}$
(MPK: $3 = 4 - 1$ ✔ przechodzi!).

**Bilans mocy:** opory: $18 + 4^2\cdot3 + 2 = 68\ \mathrm{W}$;
$E_1$ oddaje 36 W; $E_2$: $I_3 = -1$ A, więc moc $4\cdot(-1) = -4\ \mathrm{W}$
(oddaje 4 W). Bilans: $36 + 4 = 40 \ne 68$ ✘ **Błąd wykryty.**

Poprawnie: $18 + 12 + 2 = 32$ oraz $36 - 4 = 32$ ✔
:::

::: metoda Trzy niezależne kontrole (w tej kolejności)
1. **MPK/OPK** — najszybsze, ale sprawdza tylko równania, które sam napisałeś
   (powtarza ten sam błąd założenia).
2. **Bilans mocy (Tellegen)** — niezależny od równań; wykrywa błędy znaków i
   wartości prądów.
3. **Druga metoda** (np. Thévenin vs węzłowa) — najsilniejsza, bo używa innego
   modelu rozumowania. Stosuj, gdy wynik jest „podejrzany” albo gdy zadanie jest
   warte dużo punktów.
:::

### 6.7 Trzy zadania „egzaminacyjne” z pełnymi rozwiązaniami

::: przyklad Zadanie 6.1 — $R_z$ dwójnika ze źródłem sterowanym
Dwójnik: $R_1 = 1\ \mathrm{k\Omega}$ od A do B, $R_2 = 2\ \mathrm{k\Omega}$
od A do B, oraz VCCS pobierające z A prąd $g u_x$ ($g = 1\ \mathrm{mS}$),
gdzie $u_x$ to napięcie A–B.

**Rozwiązanie:** przyłóż $u_x$ do A–B; prąd $i_x$ wpływający do A:
$$
i_x = \frac{u_x}{R_1} + \frac{u_x}{R_2} + g u_x = u_x(1 + 0{,}5 + 1)\ \mathrm{mS}
$$
$$
R_z = \frac{1}{2{,}5\ \mathrm{mS}} = 400\ \Omega
$$
**Uwaga:** źródło sterowane **nie** jest wyłączane — i właśnie dlatego $R_z$
nie jest równe $1\ \mathrm{k}\|2\ \mathrm{k} = 667\ \Omega$.
:::

::: przyklad Zadanie 6.2 — Thévenin, dopasowanie, moc
Dwójnik: $E = 24\ \mathrm{V}$ z $R_1 = 6\ \Omega$ do węzła X; $R_2 = 12\ \Omega$
z X do masy; $R_3 = 4\ \Omega$ od X do zacisku A; B = masa.
Policz $E_T$, $R_W$, $P_{dysp}$ i prąd w obciążeniu $R_0 = R_W$.

**$E_T$ (A rozwarte):** dzielnik $R_1$–$R_2$ daje $V_X = 24\cdot12/18 = 16\ \mathrm{V}$;
przez $R_3$ nie płynie prąd, więc $E_T = V_X = 16\ \mathrm{V}$.

**$R_W$ (źródło zwarte):** $R_1\|R_2 + R_3 = 4 + 4 = 8\ \Omega$.

**$P_{dysp}$:** $E_T^2/(4R_W) = 256/32 = 8\ \mathrm{W}$ przy $R_0 = 8\ \Omega$.

**Prąd przy dopasowaniu:** $I = 16/(8+8) = 1\ \mathrm{A}$; $P = 1^2\cdot8 = 8\ \mathrm{W}$ ✔
Sprawność: źródło (zastępcze) oddaje $16\cdot1 = 16\ \mathrm{W}$ → $\eta = 50\%$ ✔
:::

::: przyklad Zadanie 6.3 — superpozycja, która nie działa, i co zrobić
Obwód: $E_1 = 6\ \mathrm{V}$ i $E_2 = 3\ \mathrm{V}$ w szeregu (przeciwsobnie),
$R = 1\ \mathrm{k\Omega}$, dioda **idealna** w kierunku przewodzenia dla $E_1$.

**Prawidłowo:** napięcie wypadkowe $E_1 - E_2 = 3\ \mathrm{V}$ (dodatnie) →
dioda przewodzi → $i = 3\ \mathrm{V}/1\ \mathrm{k\Omega} = 3\ \mathrm{mA}$.

**„Superpozycja”:** tylko $E_1$: $i' = 6\ \mathrm{mA}$; tylko $E_2$: dioda
zatkana → $i'' = 0$; suma $6\ \mathrm{mA}$ ≠ $3\ \mathrm{mA}$ ✘

**Dlaczego:** zmiana stanu diody (przewodzi / nie przewodzi) to nieliniowość.
**Co zrobić:** metoda dwustanowa (§4.4). Wniosek: w obwodach z diodą
superpozycji **nie stosujemy** — nawet gdy „prawie wychodzi”.
:::

### 6.8 Lista kontrolna przed oddaniem zadania

::: zapamietaj Dwanaście punktów
1. Czy wszystkie prądy są zastrzałkowane na schemacie?
2. Czy równanie elementu ma właściwy znak (strzałki zgodne/przeciwne)?
3. Czy źródła sterowane **nie** zostały wyłączone?
4. Czy $N-1$ i $M$ policzone po dorysowaniu zwor?
5. Czy jednostki są spójne (mA vs A, kΩ vs Ω)?
6. Czy moc w każdym oporze wyszła dodatnia?
7. Czy bilans mocy (Tellegen) się zgadza?
8. Czy wynik ma sens rzędu wielkości (np. 1,5 V z ogniwa nie da 15 A w 1 kΩ)?
9. Przy Théveninie: czy $E_T = J_N R_W$ się zgadza?
10. Przy superpozycji: czy podukłady mają właściwe wartości wyłączonych źródeł?
11. Przy WO: czy $|u_2| \le U_{zas}$ (brak nasycenia)?
12. Przy sygnałach: czy użyto RMS (a nie średniej) do mocy?
:::

## 7. Ściąga

### 7.1 Formułownik — wszystko z pięciu wykładów

**Elementy i ich równania** `[W1]`

| Element | Równanie | Uwaga |
|---|---|---|
| opór | $u = Ri$, $i = Gu$, $G = 1/R$ | strzałki **przeciwne**; przy zgodnych minus |
| zwarcie / rozwarcie | $u = 0$ / $i = 0$ | $E = 0$ / $J = 0$ |
| pojemność | $q = Cu$, $i = C\frac{\mathrm{d}u}{\mathrm{d}t}$, $w_C = \frac{1}{2}CU^2$ | w DC (ustalony) = rozwarcie |
| indukcyjność | $\psi = Li$, $u = L\frac{\mathrm{d}i}{\mathrm{d}t}$, $w_L = \frac{1}{2}LI^2$ | w DC (ustalony) = zwarcie |
| źródło rzeczywiste napięciowe | $u = E - R_w i$ | $i_z = E/R_w$ |
| źródło rzeczywiste prądowe | $i = J - G_w u$ | $u_0 = J/G_w$ |
| VCVS / VCCS / CCVS / CCCS | $u_2 = ku_1$ / $i_2 = gu_1$ / $u_2 = ri_1$ / $i_2 = \beta i_1$ | [V/V] [S] [Ω] [A/A] |

**Prawa i połączenia** `[W2]`

| Zagadnienie | Wzór |
|---|---|
| MPK | $\sum \pm i_k = 0$; $N-1$ równań |
| OPK | $\sum \pm u_k = 0$; $M$ równań |
| dzielnik napięciowy | $U_1 = U\frac{R_1}{R_1+R_2} = U\frac{G_2}{G_1+G_2}$ |
| dzielnik prądowy | $I_1 = I\frac{G_1}{G_1+G_2} = I\frac{R_2}{R_1+R_2}$ |
| superpozycja | $u = \sum_n u^{(n)}$; $E\to$ zwarcie, $J\to$ rozwarcie; **moc nie** |
| kompensacja | gałąź ↔ źródło $E = u$ lub $J = i$ |
| ruchliwość źródeł | identyczne źródła w **wszystkich** gałęziach węzła = stan bez zmian |

**Elementy zastępcze** `[W3]`

| Zagadnienie | Wzór |
|---|---|
| $R_z$ z definicji | $R_z = u_x/i_x$ (źródła niezależne wyłączone) |
| szeregowo / równolegle | $R_z = \sum R_n$ / $G_z = \sum G_n$ |
| Y→Δ | $R_{xy} = \frac{R_xR_y + R_yR_z + R_zR_x}{R_z}$ |
| Δ→Y | $R_x = \frac{R_{xy}R_{zx}}{R_{xy}+R_{yz}+R_{zx}}$ |
| zamiana źródeł | $J = E/R_w$, $G_w = 1/R_w$ |
| Thévenin | $E_T = u_{AB}$ (rozwarte), $R_W = R_z$ (źródła off) |
| Norton | $J_N = i_{AB}$ (zwarte), $G_W = 1/R_W$ |
| związek | $E_T = J_N R_W$ |

**Nieliniowe i WO** `[W4]`

| Zagadnienie | Wzór |
|---|---|
| opór statyczny / dynamiczny | $R_s = U_0/I_0$, $R_d = \mathrm{d}u/\mathrm{d}i$ |
| dioda idealna | $i = 0$ dla $u<0$; $u = 0$ dla $i>0$ |
| prosta oporu | $i = \frac{E_T}{R_W} - \frac{u}{R_W}$ |
| idealny WO w pętli | $i_+ = i_- = 0$, $u_+ = u_-$ |
| odwracający / nieodwracający | $u_2 = -\frac{R_2}{R_1}u_i$ / $u_2 = \left(1+\frac{R_2}{R_1}\right)u_i$ |
| moc chwilowa | $p = ui$; $p_o = -ui$ |
| dopasowanie | $R_0 = R_W$; $P_{dysp} = \frac{E_T^2}{4R_W} = \frac{J_N^2}{4G_W}$ |

**Sygnały** `[W5]`

| Parametr | Wzór / wartość |
|---|---|
| średnia | $\bar{x} = \frac{1}{T}\int x\,\mathrm{d}t$; prostokąt: $X_0 + X_m(2\delta-1)$ |
| RMS | $X_{sk} = \sqrt{\overline{x^2}}$; sinus $X_m/\sqrt{2}$; trójkąt $X_m/\sqrt{3}$ |
| średnia wyprostowana | $X_{św} = \overline{|x|}$; sinus $2X_m/\pi$ |
| kształtu / szczytu | $k_k = X_{sk}/X_{św}$; $k_a = X_p/X_{sk}$ |
| moc | $P = U_{sk}^2/R$ |

### 7.2 Dwadzieścia zdań-pułapek

1. **Wartość średnia napięcia sieciowego 230 V to 230 V.** — fałsz; 230 V to **RMS**, amplituda 325 V, średnia 0.
2. **Moc podlega superpozycji.** — fałsz; podlega jej prąd i napięcie, moc nie.
3. **Źródło sterowane należy wyłączyć przy superpozycji.** — fałsz; zostaje w każdym podukładzie.
4. **Przy liczeniu $R_z$ wyłączamy też źródła sterowane.** — fałsz; tylko niezależne.
5. **Kondensator w stanie ustalonym prądu stałego to rozwarcie.** — prawda.
6. **Cewka w stanie ustalonym prądu stałego to rozwarcie.** — fałsz; zwarcie.
7. **Dwa idealne źródła napięciowe można łączyć równolegle.** — tylko o **tej samej** wartości; inaczej model jest sprzeczny.
8. **$E_T = J_N R_W$.** — prawda, przy przeciwnym zastrzałkowaniu obu wielkości.
9. **$R_W$ dwójnika ze źródłem sterowanym bywa ujemne.** — prawda.
10. **Dopasowanie daje maksimum sprawności.** — fałsz; daje maksimum mocy, $\eta = 50\%$.
11. **$R_s = R_d$ dla oporu nieliniowego.** — fałsz; równość zachodzi tylko dla liniowego.
12. **WO w pętli zawsze ma $u_1 = 0$.** — fałsz; tylko przy ujemnym sprzężeniu i bez nasycenia.
13. **Wzmacniacz odwracający może mieć wzmocnienie 0,5.** — prawda ($R_2 < R_1$).
14. **Wzmacniacz nieodwracający może mieć wzmocnienie 0,5.** — fałsz; minimum to 1.
15. **W mostku zrównoważonym opór w przekątnej nie wpływa na $R_z$.** — prawda (kompensacja).
16. **Suma mocy wszystkich elementów obwodu wynosi zero (Tellegen).** — prawda, w każdej chwili.
17. **Dwójnik zastępczy ma takie same prądy wewnętrzne jak oryginał.** — fałsz; równoważność jest tylko zaciskowa.
18. **Superpozycja obowiązuje w obwodzie z diodą, jeśli dioda przewodzi w obu podukładach.** — fałsz; zasada wymaga liniowości, nie „tego samego stanu”.
19. **Współczynnik kształtu sinusoidy wynosi 1,11.** — prawda ($0{,}707/0{,}637$).
20. **$X_{pp} = 2X_{sk}$ dla każdego przebiegu.** — fałsz; tylko przy symetrii i nie dla każdego kształtu (dla sinusoidy $2X_m = 2\sqrt{2}X_{sk}$).

### 7.3 Indeks: temat → slajd → sekcja

Indeks pozwala czytać dokument „równolegle” do slajdów: szukasz tematu
ze slajdu i przechodzisz do sekcji komentarza.

**Wykład 1 — modele elementów**

| Temat | Slajd | Sekcja |
|---|---|---|
| równania Maxwella jako punkt wyjścia | W1/s.3 | §1.1 |
| pole quasi-stacjonarne, element skupiony | W1/s.4 | §1.1 |
| prąd, napięcie, strzałkowanie | W1/s.5 | §1.3 |
| konwencja oznaczeń ($u$ vs $U$) | W1/s.6 | wstęp |
| klasyfikacja elementów | W1/s.7 | §1.2 |
| równania elementów | W1/s.8 | §1.3 |
| idealne źródło napięciowe | W1/s.9 | §1.4 |
| idealne źródło prądowe | W1/s.10 | §1.4 |
| opór, warunki charakterystyki | W1/s.11 | §1.5 |
| prawo Ohma, $G$ | W1/s.12 | §1.5 |
| zwarcie i rozwarcie | W1/s.13 | §1.5 |
| pojemność i indukcyjność | W1/s.14 | §1.5 |
| rzeczywiste źródło napięciowe | W1/s.15 | §1.6 |
| rzeczywiste źródło prądowe | W1/s.16 | §1.6 |
| źródła sterowane (4 typy) | W1/s.17 | §1.7 |

**Wykład 2 — prawa i zasady obwodowe**

| Temat | Slajd | Sekcja |
|---|---|---|
| słownik: gałąź, węzeł, obwód, oczko | W2/s.3 | §2.1 |
| I prawo Kirchhoffa | W2/s.4 | §2.2 |
| II prawo Kirchhoffa | W2/s.5 | §2.3 |
| równania elementów a strzałkowanie | W2/s.6 | §1.3, §2.6 |
| procedura $N-1$ + $M$ | W2/s.7 | §2.4 |
| przykład pełny | W2/s.8 | §2.4 |
| pomijanie równań (superbęzeł/superoczko) | W2/s.9 | §2.5 |
| połączenia szeregowe i równoległe | W2/s.10 | §3.3 |
| trójkąt i gwiazda | W2/s.11 | §3.3 |
| dzielnik napięciowy | W2/s.12 | §2.7 |
| dzielnik prądowy | W2/s.13 | §2.7 |
| zasada kompensacji | W2/s.14 | §2.8 |
| zasada ruchliwości źródeł | W2/s.15 | §2.9 |
| zasada superpozycji | W2/s.16 | §2.10 |

**Wykład 3 — elementy zastępcze**

| Temat | Slajd | Sekcja |
|---|---|---|
| dwójnik zastępczy — definicja | W3/s.3 | §3.1 |
| następstwa zamiany | W3/s.4 | §3.1 |
| reguły stosowania zamiany | W3/s.5–6 | §3.2 |
| $R_z$ z definicji | W3/s.7 | §3.3 |
| szereg, równolegle | W3/s.8 | §3.3 |
| przekształcenie Y–Δ | W3/s.9 | §3.3 |
| $R_z$ ze źródłem sterowanym | W3/s.10 | §3.4 |
| łączenie źródeł tego samego rodzaju | W3/s.11 | §3.5 |
| źródło równolegle/szeregowo z elementem | W3/s.12 | §3.5 |
| zamiana źródeł rzeczywistych | W3/s.13 | §3.5 |
| twierdzenie Thévenina | W3/s.14 | §3.6 |
| twierdzenie Nortona | W3/s.15 | §3.6 |
| uwagi praktyczne (co liczyć) | W3/s.16 | §3.6 |
| $E_T$ i $J_N$ z definicji | W3/s.17 | §3.6 |
| $R_W$ z definicji | W3/s.18 | §3.6 |

**Wykład 4 — elementy nieliniowe, WO, moc**

| Temat | Slajd | Sekcja |
|---|---|---|
| WO — otwarta pętla | W4/s.3 | §4.1 |
| WO — zamknięta pętla | W4/s.4 | §4.1 |
| opór nieliniowy, $R_s$, $R_d$ | W4/s.5 | §4.3 |
| dioda idealna | W4/s.6 | §4.4 |
| składanie charakterystyk (równolegle) | W4/s.7 | §4.5 |
| składanie charakterystyk (szeregowo) | W4/s.8 | §4.5 |
| układ z jednym elementem nieliniowym | W4/s.9 | §4.6 |
| metoda prostej oporu | W4/s.10 | §4.6 |
| metoda rzutowania przebiegu | W4/s.11 | §4.6 |
| moc chwilowa | W4/s.12 | §4.7 |
| moc w oporze i źródłach | W4/s.13 | §4.7 |
| zasada Tellegena | W4/s.14 | §4.7 |
| problem dopasowania | W4/s.15 | §4.8 |
| warunek dopasowania | W4/s.16 | §4.8 |
| moc dysponowana | W4/s.17 | §4.8 |

**Wykład 5 — sygnały okresowe**

| Temat | Slajd | Sekcja |
|---|---|---|
| sygnał okresowy — definicja | W5/s.3 | §5.1 |
| przebiegi podstawowe | W5/s.4 | §5.1 |
| sinusoida, prostokąt, trójkąt | W5/s.5–7 | §5.1 |
| parametry amplitudowe | W5/s.8–9 | §5.2 |
| przebieg nieidealny ($X_{pp}$) | W5/s.10 | §5.2 |
| parametry czasowe ($\delta$, $t_n$) | W5/s.11–12 | §5.2 |
| wartość średnia (odcinkami stała) | W5/s.13 | §5.3 |
| wartość średnia (ciągła) | W5/s.14–15 | §5.3 |
| wartość skuteczna (RMS) | W5/s.16 | §5.4 |
| zestawienie parametrów i współczynników | W5/s.17 | §5.5 |

### 7.4 Jak korzystać z tego dokumentu razem z resztą materiałów

W repozytorium są trzy uzupełniające się opracowania — warto ich używać
razem:

* **`kompendium/index.html`** — pełny skrypt + 252 pytania z kluczy +
  formułownik. Otwieraj, gdy potrzebna jest **definicja** albo pytanie testowe
  na dany temat.
* **`teoria/index.html`** — teoria Testu 1 z **omówionymi** pytaniami i
  dystraktorami. Otwieraj, gdy chcesz zobaczyć, **jak pyta egzamin**.
* **`szybkie/szybkie.pdf`** — 11 archetypów zadań + budżet czasu. Otwieraj, gdy
  ćwiczysz **tempo** rozwiązywania.
* **ten dokument** — komentarz do **wykładów** + pełne przykłady użycia
  twierdzeń. Otwieraj, gdy nie rozumiesz, *dlaczego* dana metoda działa.

::: zapamietaj Jedno zdanie na koniec
Twierdzenia i zasady nie są „dodatkiem” do praw Kirchhoffa — są **sposobem
unikania** ich rozwiązywania. Thévenin redukuje obwód do dwóch liczb,
superpozycja dzieli jedno trudne zadanie na kilka łatwych, kompensacja i
ruchliwość źródeł pozwalają obejść przeszkodę, a Tellegen mówi, czy wynik ma
sens. Kto to rozumie, ten na kolokwium liczy mniej, a sprawdza więcej.
:::
