# Kompendium PELP1 — podstawy elektroniki i teoria obwodów

<p class="lead">Kompletny materiał do kolokwium wykładowego z przedmiotu <b>PELP1</b>, opracowany na podstawie 35 kluczy odpowiedzi z lat 2019–2026 (252 pytania). Układ rozdziałów odpowiada faktycznej strukturze egzaminu: <b>Test 1</b> to teoria obwodów, <b>Test 2</b> to metrologia i miernictwo. Każdy rozdział kończy się odniesieniem do konkretnych pytań z kluczy, a na końcu znajduje się filtrowany bank wszystkich 252 pytań.</p>

<div class="meta"><span><b>Źródła:</b> 35 plików PDF z kluczami (2019–2026)</span><span><b>Pytania:</b> 252</span><span><b>Czas testu:</b> 35 min</span><span><b>Zakres:</b> 2 testy × 7–8 pytań</span></div>

## 0. Jak korzystać z kompendium

### 0.1 Format kolokwium — co warto wiedzieć z góry

Z nagłówków kluczy wynika stały schemat egzaminu:

| Cecha | Test 1 (teoria obwodów) | Test 2 (miernictwo) |
|---|---|---|
| Liczba pytań | 7–8 (A–H) | 6–7 (A–G) |
| Punktacja | 7×1 p. + 1×2 p. = 9 p. | 5×1 p. + 1–2×2 p. = 8–9 p. |
| Czas | 35 min na cały test | 35 min na cały test |
| Forma | jedna poprawna odpowiedź, 4–8 dystraktorów | j.w. |
| Pomoce | tylko prosty kalkulator naukowy | j.w. |

::: uwaga O czym mówią nagłówki kluczy
W kluczach źródłowych **każde pytanie może mieć więcej niż jedną odpowiedź prawidłową** i więcej niż trzy nieprawidłowe — do docelowego testu wybiera się z nich dokładnie jedną prawidłową i trzy nieprawidłowe. Dlatego w aneksie (§12) przy części pytań widnieje kilka numerów odpowiedzi: wszystkie one są prawidłowe w wersji „klucza”, a w teście na kartę wpisujesz tę jedną, która pojawi się w Twoim arkuszu.
:::

::: uwaga Skąd pochodzi ta teoria
W repozytorium były wyłącznie **klucze odpowiedzi** (35 plików PDF, 2019–2026) — bez slajdów wykładowych i bez treści zadań poza pytaniami testowymi. Dlatego teoria została odtworzona tak, aby **pokryć dokładnie te kompetencje, które sprawdzają pytania**: każdy wzór, reguła i przykład ma odpowiednik w co najmniej jednym pytaniu z kluczy (w ramkach „Jak to jest pytane” podaję liczbę pytań i schemat). Tam, gdzie klucz dopuszcza kilka odpowiedzi lub sam jest niespójny (dwa sposoby liczenia niepewności, inny zapis tego samego wyniku), zaznaczam to wprost — bo na kolokwium właśnie takie niuanse decydują o punkcie.
:::

::: ciekawostka Dwie wersje tego samego tekstu
Obok tego pliku (`index.html`, wersja do przeglądania z wyszukiwarką i filtrowaniem banku pytań) leży **`kompendium.pdf`** — 43-stronicowy wydruk A4 z tym samym tekstem, gotowy do druku lub czytania na telefonie. Oba pliki powstają z jednego źródła (`kompendium.md`), więc treść jest identyczna.
:::

::: ciekawostka Siostrzany dokument: samo szybkie liczenie
Do tego kompendium dołączony jest drugi, krótszy plik — **`szybkie/szybkie.pdf`** (14 stron): *Szybkie rozwiązywanie obwodów*. Zamiast teorii są tam **archetypy zadań z Testu 1** (opór zastępczy ze źródłem sterowanym, Thévenin–Norton, moc maksymalna, PPK, superpozycja, wzmacniacz operacyjny, punkt pracy z wykresu, rozpoznawanie połączeń), każde z wycinkiem oryginalnego zadania z klucza, rachunkiem krok po kroku i listą pułapek. Kompendium odpowiada na pytanie *dlaczego tak*, tamten dokument — *jak to policzyć w 60 sekund*.
:::

::: metoda Jak pracować z tym tekstem
1. Przeczytaj rozdział teoretyczny i **przelicz samodzielnie** każdy wzór na prostym przykładzie liczbowym.
2. Zajrzyj do §12, odfiltruj pytania z danego tematu (jest tam wyszukiwarka), przeczytaj treści i ustal, *jaki schemat rozumowania* kryje się za pytaniem.
3. Wróć do rozdziału i sprawdź, czy potrafisz odtworzyć rozumowanie bez zaglądania.
4. Na koniec przejdź przez §11 (formułownik) — to materiał na ostatnie 20 minut przed testem.
:::

### 0.2 Mapa tematów — co realnie pojawia się na kolokwium

Poniższa tabela powstała przez sklasyfikowanie wszystkich 252 pytań z kluczy. Kolejność jest zgodna z częstością — pierwsze pozycje to tematy, które **na pewno** spotkasz.

<!--TOPICMAP-->

::: zapamietaj Trzy wnioski z rozkładu tematów
1. **Około 45 % Testu 1** to rachunek na dwójnikach: rezystancja zastępcza, superpozycja, Thévenin/Norton, dopasowanie, punkt pracy elementu nieliniowego. To prawie zawsze te same schematy z innymi liczbami.
2. **Ponad połowa Testu 2** to „policz niepewność i porównaj”: niepewność graniczna przyrządu, dobór zakresu, niepewność złożona, zaokrąglanie. Tu wygrywa rutyna rachunkowa, nie intuicja.
3. **Oscyloskop** pojawia się w każdym prawie teście, ale zawsze w tej samej formule: „do czego służy / której cechy nie ma / który rodzaj wybrać”.
:::

### 0.3 Plan powtórki na trzy dni

::: metoda Dzień 1 — teoria obwodów „na sucho”
Przeczytaj §1–§3, a potem **na kartce** wyprowadź: dzielnik napięcia i prądu, wzór Millmana, $R_z$ dwójnika ze źródłem $gu$, $P_{\max}=E_T^2/(4R_T)$. Zajrzyj do banku pytań i odfiltruj „Opór zastępczy”, „Superpozycja”, „Thévenin” — przeczytaj treści, nie rozwiązuj.
:::

::: metoda Dzień 2 — metrologia i rachunek
§6–§9 plus przeliczenie **wszystkich** przykładów z §10.2 (Z9–Z18) bez patrzenia na rozwiązania. Kluczowa umiejętność: policzyć $\Delta_g$ dla czterech przyrządów w 3 minuty i porównać.
:::

::: metoda Dzień 3 — symulacja kolokwium
Wybierz z banku dwa testy (jeden „Test 1”, jeden „Test 2”), ustaw 35 minut, rozwiąż na kartce, potem sprawdź z aneksem. Powtórz z drugą parą testów. Na koniec przejrzyj §11.3 (pułapki) i §11.1–11.2 (formułownik).
:::

---

## 1. Elementy, wielkości i konwencje

### 1.1 Wielkości fizyczne, jednostki i strzałki

Podstawowe wielkości obwodowe definiuje się przez pracę i ładunek:

$$i(t)=\frac{\mathrm{d}q}{\mathrm{d}t}\ \text{[A]},\qquad
u(t)=\frac{\mathrm{d}w}{\mathrm{d}q}\ \text{[V]},\qquad
p(t)=\frac{\mathrm{d}w}{\mathrm{d}t}=u(t)\,i(t)\ \text{[W]}$$

Energia pobrana w przedziale czasu to $w=\int_{t_1}^{t_2}p(t)\,\mathrm{d}t$; w obwodzie prądu stałego $W=P\,t$ (watosekunda, 1 Wh = 3600 J).

::: def Konwencja strzałek (umowa odbiornika i źródła)
* **Odbiornik** — strzałki $u$ i $i$ są **zgodne** (prąd „wpływa” zaciskiem o wyższym potencjale). Wtedy $p=ui>0$ oznacza pobieranie energii.
* **Źródło** — strzałki $u$ i $i$ są **przeciwne**. Wtedy $p=ui<0$ w umowie odbiornika, czyli element energię oddaje.

Ta sama reguła pozwala jednym wzorem $p=ui$ opisać cały obwód: suma $p$ po wszystkich elementach jest równa zeru (zasada Tellegena, §3.2).
:::

::: figura figury/konwencje.svg | Rys. 1.1. Strzałki zgodne w odbiorniku i przeciwne w źródle — jedyna konwencja potrzebna do bilansu mocy.
:::

**Jednostki i przedrostki.** Wyniki niemal zawsze podaje się w mA, kΩ, mW — a wzory działają na jednostkach podstawowych. Bezpiecznikiem jest rachunek na jednostkach:

$$1\ \mathrm{k\Omega\cdot mA}=10^3\,\Omega\cdot10^{-3}\,\mathrm{A}=1\ \mathrm{V},\qquad
1\ \mathrm{mA^2\cdot k\Omega}=10^{-6}\cdot10^{3}\ \mathrm{W}=1\ \mathrm{mW}$$

::: pulapka Najczęstsza pomyłka rachunkowa
Mieszanie kΩ i mA bez przeliczenia daje wynik przesunięty o trzy rzędy wielkości — a w testach dystraktory są często właśnie takie (np. $0{,}5$ mW vs $500$ mW). Zawsze zapisz jednostkę obok liczby, zanim wpiszesz odpowiedź.
:::

### 1.2 Model elementu skupionego

Teoria obwodów nie opisuje pola elektromagnetycznego w przestrzeni — zastępuje je **elementami skupionymi** połączonymi przewodami idealnymi.

::: def Element skupiony
Element skupiony to wydzielony obszar, w którym:
* wymiary są małe w porównaniu z długością fali (a więc zmiany pola zachodzą w całym obszarze praktycznie **równocześnie** — pomijamy opóźnienia propagacji),
* **równania elementu nie zawierają zmiennych przestrzennych** $x,y,z$ — zależą tylko od czasu,
* pole elektryczne jest potencjalne (bezwirowe), więc napięcie między zaciskami ma jednoznaczną wartość,
* ładunek nie gromadzi się w węzłach, co daje prądowe prawo Kirchhoffa.

Dopiero z tych założeń wynikają prawa Kirchhoffa, pojęcie dwójnika i cała analiza obwodowa.
:::

::: klucz Jak to jest pytane (2 pytania w bazie)
„Które stwierdzenie jest prawdziwe dla **każdego** elementu skupionego?” — prawidłowe są zdania: *równania elementu nie zawierają zmiennych przestrzennych (x, y, z)* oraz *zmiany pola elektromagnetycznego zachodzące wewnątrz obszaru elementu są pomijalnie małe*. Nieprawdziwe są zdania o zerowym polu elektrycznym, o pomijalnie małym polu magnetycznym czy o „stałym ładunku wewnątrz elementu”.
:::

**Klasyfikacja elementów** (przydaje się w pytaniach o dwójniki — §5.1):

| Kryterium | Rodzaje | Przykład / skutek |
|---|---|---|
| Charakter | źródłowe (aktywne) / bezźródłowe (pasywne) | źródło $E$ / rezystor |
| Liniowość | liniowe / nieliniowe | $R=\text{const}$ / dioda, żarówka |
| Inercja | bezinercyjne / z pamięcią | $R$ / $C$ (pamięta $u$), $L$ (pamięta $i$) |
| Sterowanie | niesterowane / sterowane | $E$, $J$ / źródła $g u$, $\beta i$ |
| Zmienność w czasie | stacjonarne / niestacjonarne | $R$ / termistor grzany |

### 1.3 Prawo Ohma, rezystancja, konduktancja, moc

$$u=Ri,\qquad i=Gu,\qquad G=\frac{1}{R}\ \text{[S]}$$

$$p=u i=R i^{2}=\frac{u^{2}}{R}=G u^{2}$$

Energia w rezystorze jest **zawsze** dodatnia (zamiana na ciepło) — to element rozpraszający. Moc znamionowa decyduje o dopuszczalnym prądzie; przekroczenie prowadzi do zniszczenia.

::: uwaga Rezystancja jako parametr materiałowy
$R=\varrho\,l/S$ — opór rośnie z długością i maleje z przekrojem; $\varrho$ zależy od temperatury (dla metali rośnie, dla półprzewodników maleje). Stąd w pytaniach o „element nieliniowy” pojawia się żarówka i termistor: ich $R$ nie jest stała, więc **nie wolno** stosować do nich prawa Ohma w postaci $u=Ri$ z jednym $R$, ani zasady superpozycji.
:::

**Szeregowe i równoległe łączenie rezystorów** — dwa fakty, które trzeba znać na pamięć:

$$R_{\text{sz}}=\sum_k R_k,\qquad \frac{1}{R_{\text{równ}}}=\sum_k G_k=\sum_k\frac{1}{R_k},\qquad
R_1\|R_2=\frac{R_1R_2}{R_1+R_2}$$

::: zapamietaj Dwa zdania-pułapki z kluczy
* **Szeregowo**: prąd jest wspólny, napięcia dzielą się proporcjonalnie do $R$ → **w większym oporze większa moc** ($p=Ri^2$) i większe napięcie.
* **Równolegle**: napięcie jest wspólne, prądy dzielą się odwrotnie proporcjonalnie do $R$ → **w mniejszym oporze większa moc** ($p=u^2/R$).
:::

### 1.4 Łączenie rezystorów, gwiazda–trójkąt, dzielniki

::: figura figury/szeregowo_rownolegle.svg | Rys. 1.2. Połączenie szeregowe (wspólny prąd) i równoległe (wspólne napięcie).
:::

**Dzielnik napięcia** (dwa opory w szeregu, wyjście na $R_2$):

$$U_2=E\,\frac{R_2}{R_1+R_2}$$

**Dzielnik prądu** (dwa opory równolegle, prąd gałęzi $R_1$):

$$I_1=J\,\frac{R_2}{R_1+R_2}=J\,\frac{G_1}{G_1+G_2}$$

::: figura figury/dzielniki.svg | Rys. 1.3. Dzielnik napięcia i dzielnik prądu — wzory wynikają wprost z NPK i PPK.
:::

::: pulapka Dzielnik obciążony
Wzór dzielnika napięcia obowiązuje tylko dla **stanu jałowego** (brak obciążenia). Po podłączeniu odbiornika $R_o$ do wyjścia liczymy $R_2\|R_o$ — napięcie spada. Na tym polega *błąd metody pobrania* przy pomiarze woltomierzem (§8.1): woltomierz dołącza się równolegle i zawsze nieco obciąża obwód.
:::

**Przekształcenie gwiazda ⇄ trójkąt** (trzy opory, których nie da się zwinąć szeregowo ani równolegle):

$$R_A=\frac{R_{AB}R_{CA}}{R_{AB}+R_{BC}+R_{CA}},\qquad
R_B=\frac{R_{AB}R_{BC}}{\Sigma},\qquad R_C=\frac{R_{BC}R_{CA}}{\Sigma}$$

$$R_{AB}=\frac{R_AR_B+R_BR_C+R_CR_A}{R_C},\qquad
R_{BC}=\frac{\Sigma'}{R_A},\qquad R_{CA}=\frac{\Sigma'}{R_B}$$

gdzie $\Sigma=R_{AB}+R_{BC}+R_{CA}$ oraz $\Sigma'=R_AR_B+R_BR_C+R_CR_A$.

::: figura figury/gwiazda_trojkat.svg | Rys. 1.4. Trójkąt (Δ) i gwiazda (Y) — równoważność trójzaciskową stosuje się tylko do obliczeń zewnętrznych.
:::

::: metoda Rozpoznawanie połączeń — procedura na 10 sekund
Zadanie „połączenie równoległe występuje między parami elementów” zawsze sprowadza się do jednego testu: **dwa elementy są równoległe, gdy ich końce są przyłączone do tych samych dwóch węzłów** (a więc mają identyczne napięcie), a **szeregowe, gdy łączy je węzeł, do którego nic więcej nie dochodzi** (płynie przez nie ten sam prąd). Zaznacz ołówkiem węzły i sprawdzaj pary — nie sugeruj się geometrią rysunku, bo rysunki w kluczach są celowo „poskręcane”.
:::

### 1.5 Elementy zachowawcze w obwodzie prądu stałego

$$i_C=C\frac{\mathrm{d}u_C}{\mathrm{d}t},\qquad u_L=L\frac{\mathrm{d}i_L}{\mathrm{d}t},\qquad
w_C=\tfrac12Cu_C^{2},\qquad w_L=\tfrac12Li_L^{2}$$

W **stanie ustalonym prądu stałego** pochodne są zerowe, więc:

::: zapamietaj Reguła, która rozwiązuje połowę „dziwnych” zadań
* **Kondensator w stanie ustalonym prądu stałego = rozwarcie** (nie płynie przez niego prąd, odkłada się na nim napięcie).
* **Cewka w stanie ustalonym prądu stałego = zwarcie** (nie odkłada się na niej napięcie, płynie przez nią prąd).

W obwodach z rysunków z $C$, $L$ i wieloma oporami wystarczy więc **usunąć** gałęzie z kondensatorami i **zwarć** gałęzie z cewkami — i liczyć zwykły obwód rezystancyjny. To dokładnie ten trik, który rozwiązuje zadania typu „ile wynosi moc oddawana przez źródło” w obwodzie z $10\ \mu$F, $50$ mH itd.
:::

### 1.6 Rezystancja zastępcza dwójnika i dwójniki ze źródłami sterowanymi

::: def Rezystancja zastępcza (wejściowa) dwójnika
$$R_z=\frac{u}{i}$$
gdzie $u$ to napięcie wymuszające na zaciskach, a $i$ to prąd wpływający. Wyznaczamy ją **wymuszając** dowolne $u$ (albo $i$) i obliczając odpowiedź; stosunek jest niezależny od wartości wymuszenia, o ile dwójnik jest liniowy.
:::

W praktyce najpewniejsza jest metoda „wymuś $u$, policz $i$”:

1. Przyłóż do zacisków $A$–$B$ napięcie $u$ (albo wpędź prąd $i$).
2. Zapisz $i$ jako funkcję $u$ (PPK/NPK, prawo Ohma).
3. $R_z=u/i$; jeśli w wyrażeniu zostaje $u$, dwójnik **nie jest** rezystancyjny liniowy (jest nieliniowy albo opisany ujemną rezystancją).

::: figura figury/dwojnik_sterowany.svg | Rys. 1.5. Równoległe połączenie konduktancji $G$ ze źródłem prądu sterowanym napięciem $gu$. Prąd $i=Gu-gu$ nie znika po podzieleniu przez $u$, więc dwójnik ma rezystancję ujemną.
:::

Dla układu z rysunku 1.5:

$$i=Gu-gu=(G-g)u\quad\Longrightarrow\quad R_z=\frac{1}{G-g}=\frac{R}{1-gR}$$

::: uwaga Dwie postacie tego samego wyniku
Odpowiedzi w kluczach podają czasem $\dfrac{1}{G-g}$, a czasem $\dfrac{R}{1-gR}$ — to **ta sama liczba**, bo $G=1/R$. Gdy widzisz taką parę w dystraktorach, wiedz, że jedna z nich jest prawdopodobnie prawidłowa, a druga to jej „bliźniak” pojawiający się w innym wariancie testu. Analogicznie $\dfrac{R}{1-k}$ (wzmocnienie $k$ źródła sterowanego) odpowiada $\dfrac{1}{G-g}$ przy $k=gR$.
:::

Gdy $g>G$ (wzmocnienie źródła sterowanego przewyższa konduktancję), $R_z<0$ — dwójnik jest **aktywny** i może dostarczać energię; taki układ nazywa się konwerterem rezystancji ujemnej (NIC). To dlatego pytania o „dwójnik bezźródłowy” i „źródło Thévenina” mają warianty: dwójnik ze źródłem sterowanym nie jest bezźródłowy, ale **wciąż** można go zastąpić źródłem Thévenina/Nortona, bo jest liniowy (§5.1).

---

## 2. Prawa Kirchhoffa i analiza obwodów

### 2.1 Prawa Kirchhoffa w praktyce

::: def Prawa Kirchhoffa
* **PPK (prądowe)**: suma prądów wpływających do węzła równa się sumie wypływających — $\sum \pm i_k=0$.
* **NPK (napięciowe)**: suma napięć wzdłuż oczka zamkniętego równa się zeru — $\sum \pm u_k=0$.

Obowiązują w **każdym** obwodzie skupionym — także z elementami nieliniowymi i niestacjonarnymi (w przeciwieństwie do superpozycji, §3.1).
:::

**Jak pisać równania węzła i oczka bez błędów znaków.** Trzy żelazne kroki:

1. Zaznacz strzałki wszystkich prądów i napięć (na rysunku lub obok).
2. Wybierz umowę: dla węzła „wpływające dodatnie”, dla oczka obieg zgodny z ruchem wskazówek zegara.
3. Konsekwentnie stosuj umowę: prąd wypływający wpisz z minusem; napięcie źródła, które w kierunku obiegu „pcha” prąd, wpisz dodatnio.

::: figura figury/thevenin_norton.svg | Rys. 2.1. Typowy dwójnik oraz jego dwa równoważniki — do nich wracamy w §3.3.
:::

Dla klasycznego układu powtarzanego w kluczach (dwa źródła $5$ V i $10$ V, opory $3\ \Omega$, $7\ \Omega$, $10\ \Omega$, prądy $I_1,I_2,I_3$, węzeł $A$):

* **Równanie węzła $A$**: dwa prądy wpływają, jeden wypływa → $I_3=I_1+I_2$.
* **Równanie lewego oczka** (obieg zgodny z $I_1$): $3\ \Omega\cdot I_1-5\ \text{V}=7\ \Omega\cdot I_2$, równoważnie $5\ \text{V}+7\ \Omega\cdot I_2-3\ \Omega\cdot I_1=0$ oraz $-5\ \text{V}+7\ \Omega\cdot I_2-3\ \Omega\cdot I_1=0$ — w kluczu wszystkie te trzy zapisy uznano za prawidłowe, bo różnią się tylko stroną równania, nie treścią.

::: metoda Rachunek kontrolny: liczba równań
Dla obwodu o $w$ węzłach i $g$ gałęziach układamy $w-1$ równań PPK oraz $g-(w-1)$ równań NPK. Jeśli liczba równań nie zgadza się z liczbą niewiadomych, w obwodzie jest źródło idealne wymuszające dodatkowe ograniczenie (np. dwa idealne źródła prądowe szeregowo → **układ sprzeczny**, co jest jedną z częstych odpowiedzi).
:::

::: klucz Jak to jest pytane (13 pytań w bazie)
Dwa schematy:
* *„Które równanie opisuje węzeł A / lewe oczko?”* — sprawdzaj **znaki** i to, czy opór przy prądzie jest właściwy ($3\ \Omega$ przy $I_1$, $7\ \Omega$ przy $I_2$).
* *„Natężenie prądu I wynosi…”* — to zwykle jedno PPK w węźle z trzema znanymi prądami; wynik bywa ujemny (kierunek przeciwny do strzałki). Odpowiedź „układ jest sprzeczny” wybieraj **tylko** wtedy, gdy dwa idealne źródła prądowe o różnych wydajnościach są w jednej gałęzi szeregowej.
:::

### 2.2 Metody analizy obwodów

**a) Zwijanie (przekształcenia równoważne).** Redukuj opory do jednego, policz prąd główny, potem „rozwiń” obwód wracając do kolejnych gałęzi. Najszybsza metoda dla drabinek i mostków.

**b) Metoda potencjałów węzłowych / twierdzenie Millmana.** Dla dwóch węzłów, między którymi wisi $n$ gałęzi z konduktancjami $G_k$ i źródłami $E_k$, $J_k$:

$$U_{AB}=\frac{\sum_k \left(G_kE_k+J_k\right)}{\sum_k G_k}$$

::: zapamietaj Kiedy opór „nie wpływa” na napięcie
To sedno całej rodziny pytań typu *„na napięcie $U$ wpływa wartość oporu: tylko $R_3$ / żadnego / każdego”*:
* Jeżeli gałąź zawiera **idealne źródło napięciowe**, to napięcie między jej końcami jest **ustalone** przez to źródło — opór w tej gałęzi nie zmienia napięcia, tylko prąd w niej płynący. Zatem opory w gałęziach równoległych do idealnego źródła **nie wpływają** na napięcie węzła.
* Jeżeli gałąź zawiera **idealne źródło prądowe**, to prąd tej gałęzi jest ustalony — element szeregowo z nim nie zmienia prądu, ale **zmienia** napięcie na źródle prądowym (bo $u_J$ = suma spadków w pętli).
* Wniosek praktyczny: w liczniku Millmana liczą się tylko gałęzie ze źródłami **i** konduktancją; gałęzie z samym idealnym $E$ (bez $R$) „przybijają” napięcie do $E$ i wtedy **żaden** opór nie wpływa na $U$.
:::

**c) Metoda oczkowa.** Prądy oczkowe, macierz rezystancji oczkowych; wygodna, gdy oczek jest mało.

**d) Metoda superpozycji** (§3.1), **twierdzenie Thévenina/Nortona** (§3.3), **twierdzenie o kompensacji**.

::: uwaga Kolejność wyboru metody (na czas testu)
1. Widzisz jedną niewiadomą i dwa węzły → **Millman**.
2. Pytanie o „wpływ parametru” → analiza **jakościowa** (co jest ustalone przez źródło idealne), nie rachunek.
3. Pytanie o „moc maksymalną w $R$” → **Thévenin + dopasowanie** (§3.4).
4. Pytanie o „składową od jednego źródła” → **superpozycja** (§3.1).
5. Pytanie o charakterystykę dwójnika z diodą → **dwa przypadki** (§4.3).
:::

### 2.3 Źródła rzeczywiste i łączenie źródeł

::: def Źródło rzeczywiste
* Napięciowe: $E$ (SEM) szeregowo z oporem wewnętrznym $R_w$; napięcie na zaciskach $u=E-R_w i$.
* Prądowe: $J$ równolegle z konduktancją $G_w=1/R_w$; prąd na zaciskach $i=J-G_w u$.
:::

$$E=J\,G_w^{-1}=J\,R_w,\qquad R_w=\frac{1}{G_w},\qquad
P_{\text{dysp}}=\frac{E^{2}}{4R_w}=\frac{J^{2}R_w}{4}$$

::: figura figury/zrodla_laczenie.svg | Rys. 2.2. Dozwolone łączenie źródeł: szereg napięciowych, równoległe prądowych.
:::

::: pulapka Czego nie wolno łączyć
* **Dwa idealne źródła napięciowe równolegle** o różnych SEM → sprzeczność z NPK (napięcie musiałoby być jednocześnie równe obu wartościom). Dozwolone tylko dla identycznych SEM (dwa „sztywne” napięcia).
* **Dwa idealne źródła prądowe szeregowo** o różnych $J$ → sprzeczność z PPK.
* Dwa idealne źródła napięciowe **szeregowo** → SEM sumują się (z uwzględnieniem biegunów). Dwa idealne źródła prądowe **równolegle** → wydajności sumują się.
* Rzeczywiste źródła (z $R_w$) można łączyć dowolnie — opór wewnętrzny „rozwiązuje” sprzeczność.
:::

Dodatkowo warto pamiętać o **zasadzie przesuwania („ruchliwości”) źródeł**: źródło napięciowe można przenieść przez węzeł do wszystkich gałęzi z nim połączonych (z zachowaniem SEM), a źródło prądowe „rozprowadzić” między węzły. To narzędzie rzadko jest niezbędne na kolokwium, ale pojawia się jako dystraktor („można przekształcić w jedno źródło, korzystając z zasady ruchliwości”) — jest prawdziwe tylko wtedy, gdy źródła nie są idealne i sprzeczne.

---

## 3. Zasady i twierdzenia

### 3.1 Zasada superpozycji

::: def Zasada superpozycji
W obwodzie **liniowym** odpowiedź (prąd lub napięcie dowolnej gałęzi) jest sumą algebraiczną odpowiedzi pochodzących od każdego źródła działającego **osobno**. Pozostałe źródła wyłącza się: idealne źródło napięciowe → **zwarcie**, idealne źródło prądowe → **rozwarcie**.
:::

Procedura (5 kroków):

1. Zostaw jedno źródło, pozostałe wyłącz zgodnie z regułą.
2. Policz szukaną wielkość (najczęściej zwijanie oporów lub dzielnik).
3. Powtórz dla każdego źródła.
4. Zsumuj **z zachowaniem znaków** (kierunek strzałki!).
5. Sprawdź sens: składowa może być zerowa (np. w zrównoważonym mostku).

::: pulapka Cztery rzeczy, których superpozycja nie robi
1. **Nie stosuje się do mocy** — $P\neq P_1+P_2$, bo moc jest kwadratowa. Superponujemy prądy i napięcia, moc liczymy na końcu.
2. **Nie działa w obwodach nieliniowych** — z elementem nieliniowym (dioda, żarówka, opór nieliniowy) superpozycja jest niedozwolona.
3. Nie wolno „wyłączać” źródła w sposób tworzący sprzeczność (np. zwarć dwóch źródeł o różnych SEM).
4. Wyłączenie źródła **nie** oznacza usunięcia jego oporu wewnętrznego — $R_w$ zostaje.
:::

::: figura figury/dzielniki.svg | Rys. 3.1. Najczęstszy schemat superpozycji: po wyłączeniu $E$ zostaje dzielnik prądu — składowa prądu od $J$ ma postać $\pm J\frac{R_2}{R_1+R_2}$ (lub $\pm J\frac{R_1}{R_1+R_2}$ — zależnie od tego, o który prąd pytamy).
:::

::: klucz Jak to jest pytane (14 pytań w bazie)
* „Jaki jest wkład do natężenia prądu $I$ pochodzący od źródła $8$ V?” → wyłącz drugie źródło, policz prąd w gałęzi z $6\ \Omega$, podaj **z nazwą źródła**, nie sumę.
* „Składowa napięcia $U$ pochodząca od źródła $J$ wynosi…” → odpowiedzi mają postać $\pm J\frac{R_2}{R_1+R_2}$, $\pm J\frac{R_1R_2}{R_1+R_2}$ lub $0$. Zero pojawia się, gdy źródło jest „zwarte” przez idealne źródło napięciowe w równoległej gałęzi — wtedy jego wkład do danego napięcia jest zerowy.
* Dystraktor „w tym obwodzie nie wolno stosować zasady superpozycji” jest prawidłowy **tylko** dla obwodów z elementem nieliniowym (i właśnie dlatego w zadaniach z oporem nieliniowym jest poprawną odpowiedzią).
:::

### 3.2 Zasada Tellegena

::: def Zasada Tellegena
Dla dowolnego obwodu skupionego, przy dowolnie przyjętych (byle zgodnych z PPK) prądach i napięciach spełniających NPK:
$$\sum_{k} u_k\, i_k = 0$$
Oznacza to bilans mocy: moc oddawana przez źródła = moc pobierana przez odbiorniki.
:::

::: zapamietaj Zakres stosowalności — pytanie „tylko w obwodach...”
Zasada Tellegena obowiązuje w obwodach **skupionych** i to **wszystkich**: liniowych i nieliniowych, stacjonarnych i niestacjonarnych, ze źródłami i bez. Nie obowiązuje w obwodach o parametrach rozłożonych. W pytaniu „Zasada Tellegena obowiązuje tylko w obwodach: liniowych / stacjonarnych / bezźródłowych / **skupionych**” prawidłowa jest zawsze odpowiedź *skupionych*.
:::

Praktyczne zastosowanie w zadaniach: jeśli źródło dostarcza $10$ W, a opór nieliniowy pobiera $6$ W, to **na pozostałym oporze $R$ wydziela się $4$ W** — bez znajomości $R$ i bez liczenia prądów. To dokładnie pytanie *„Moc pobieraną przez opór $R$ można obliczyć na podstawie: zasady Tellegena”*.

### 3.3 Twierdzenie Thévenina i Nortona

::: def Twierdzenie Thévenina / Nortona
Każdy **liniowy** dwójnik (z dowolną liczbą źródeł i źródeł sterowanych) można zastąpić:
* źródłem napięciowym $E_T$ szeregowo z $R_T$ (Thévenin), gdzie $E_T$ = napięcie stanu jałowego na zaciskach, $R_T$ = rezystancja wejściowa przy wyłączonych źródłach niezależnych;
* źródłem prądowym $J_N$ równolegle z $R_T$ (Norton), gdzie $J_N$ = prąd zwarcia zacisków.

Zachodzi $E_T=J_NR_T$, $R_T=U_{AB}^{\text{jałowe}}/I_{AB}^{\text{zwarcie}}$.
:::

::: figura figury/thevenin_norton.svg | Rys. 3.2. Dwójnik liniowy i jego dwa równoważniki — identyczne zaciskowo, więc dla dowolnego obciążenia dają ten sam prąd i napięcie.
:::

**Procedura liczenia (3 minuty na pytanie):**

1. Odłącz obciążenie (zaciski $A$–$B$ wolne).
2. Policz $E_T=U_{AB}$ (stan jałowy) — najczęściej dzielnik napięcia lub Millman.
3. Wyzeruj źródła niezależne ($E\to$ zwarcie, $J\to$ rozwarcie), **zostaw** źródła sterowane.
4. Policz $R_T$ widzianą z zacisków.
5. Jeśli potrzebny Norton: $J_N=E_T/R_T$.

::: pulapka Trzy błędy w Théveninie
1. **Zwarcie źródła prądowego** zamiast rozwarcia (i odwrotnie) — najczęstsza pomyłka.
2. **Usunięcie źródła sterowanego** — źródła sterowanego nie wolno „wyłączać”; ono zostaje i to ono daje $R_T$ ujemne lub zależne od $g$.
3. Mylenie $R_T$ z oporem obciążenia — moc $P=E_T^{2}/(4R_T)$ wydziela się **w obciążeniu** przy $R=R_T$, a nie w $R_T$ (w $R_T$ wydziela się taka sama moc, ale to moc tracona wewnątrz dwójnika).
:::

::: klucz Jak to jest pytane (11 pytań w bazie)
* *„Ile wynosi SEM zastępczego źródła Thévenina?”* — licz stan jałowy; przy źródle sterowanym $gu$ w poprzek $R_1$ wynik ma postać $E(1\pm gR_1)$ lub $E/(1\pm gR_1)$.
* *„Jaka jest wydajność prądowa $J_N$ w źródle Nortona?”* — wynik ma postać $J$, $J(1\pm r/R_1)$, $J/(1+r/R_2)$ itd. Uwaga na znak: jeśli przez $R_1$ płynie prąd „odwrotny”, $J_N$ bywa ujemne.
* *„Elementem równoważnym zaciskowo dwójnikowi $AB$ jest rzeczywiste źródło napięciowe o parametrach $E=\dots$, $R=\dots$”* — dwie liczby do policzenia: $U_{AB}$ jałowe i $R_T$.
:::

### 3.4 Dopasowanie odbiornika i moc dysponowana

::: def Moc dysponowana i dopasowanie
**Moc dysponowana** dwójnika to największa moc, jaką można zeń pobrać:
$$P_{\text{dysp}}=\frac{E_T^{2}}{4R_T}=\frac{J_N^{2}R_T}{4}$$
Osiąga się ją przy **dopasowaniu**, tj. gdy $R_{\text{obc}}=R_T$. Sprawność wynosi wtedy $50\%$ (połowa mocy wydziela się w $R_T$).
:::

**Wyprowadzenie w dwóch linijkach** (warto umieć, bo pozwala uniknąć błędu):

$$P(R)=\frac{E_T^{2}R}{(R_T+R)^{2}},\qquad
\frac{\mathrm{d}P}{\mathrm{d}R}=0\ \Longrightarrow\ R=R_T,\qquad
P_{\max}=\frac{E_T^{2}}{4R_T}$$

::: figura figury/thevenin_norton.svg | Rys. 3.3. Moc w obciążeniu jest największa, gdy $R=R_T$; wtedy $P_{\max}=E_T^2/(4R_T)$.
:::

::: metoda Schemat rozwiązywania zadań „moc maksymalna w $R$”
1. Zastąp cały obwód **na lewo od $R$** źródłem Thévenina ($E_T$, $R_T$).
2. Sprawdź, czy w treści jest „$R$ dobrano tak, aby moc była maksymalna” → to znaczy $R=R_T$.
3. Wstaw do $P=E_T^{2}/(4R_T)$ i przelicz jednostki (kΩ·mA → V).

Uwaga na wariant z **dwójnikiem zawierającym $R$ także po prawej stronie**: jeśli $R$ jest częścią dwójnika, to najpierw „wyciągnij” $R$ z obwodu i policz $E_T$, $R_T$ dla reszty.
:::

::: klucz Jak to jest pytane (13 pytań w bazie)
Odpowiedzi są zawsze ułamkami typu $\frac{3}{10}$ mW, $\frac{15}{8}$ mW, $0{,}25$ mW, $1$ mW — czyli wynikiem dzielenia $E_T^{2}/(4R_T)$ z „brzydkimi” wartościami. Praktyka: licz na ułamkach zwykłych, nie zaokrąglaj w połowie drogi.
:::

---

## 4. Elementy nieliniowe

### 4.1 Element nieliniowy: opór statyczny i dynamiczny

::: def Dwa opory jednego punktu
* **Opór statyczny** (sieczny): $R_s=\dfrac{U}{I}$ — w punkcie pracy $(U,I)$.
* **Opór dynamiczny** (różniczkowy): $R_d=\left.\dfrac{\mathrm{d}u}{\mathrm{d}i}\right|_{P}$ — odwrotność nachylenia stycznej do charakterystyki w punkcie pracy.

Dla elementu liniowego $R_s=R_d=R$. Dla nieliniowego różnią się — i to jest cała treść pytania.
:::

::: figura figury/nieliniowy.svg | Rys. 4.1. Punkt pracy $P$ jako przecięcie charakterystyki elementu z prostą obciążenia. $R_s$ to nachylenie siecznej $0\!-\!P$, $R_d$ — stycznej w $P$.
:::

**Jak to policzyć w zadaniu:**

1. Znajdź punkt pracy $P=(U,I)$ — z przecięcia charakterystyki z prostą obciążenia.
2. $R_s=U/I$ (iloraz współrzędnych punktu).
3. $R_d=\Delta u/\Delta i$ — nachylenie charakterystyki **w otoczeniu** $P$: dla charakterystyki odcinkowo liniowej nachylenie tego odcinka, na którym leży $P$.
4. Jeśli odcinek jest **pionowy** → $R_d=\infty$ (idealne źródło napięciowe). Jeśli **poziomy** → $R_d=0$ (idealne źródło prądowe).

::: klucz Jak to jest pytane (17 pytań w bazie!)
Schemat: element nieliniowy o charakterystyce łamanej podłączony do źródła (idealnego lub rzeczywistego) o znanej wartości. Odpowiedzi to pary „$R_s$ i $R_d$”.

* Źródło **prądowe** idealne o wydajności $3$ mA wymusza prąd $I=3$ mA → z charakterystyki odczytujesz $U$, więc $R_s=U/I$ (np. $4\ \text{V}/3\ \text{mA}=1{,}33\ \text{k}\Omega$).
* Źródło **napięciowe** idealne o SEM $2$ V wymusza $U=2$ V → odczytujesz $I$.
* Źródło **rzeczywiste** — punkt pracy to przecięcie charakterystyki z prostą $i=(E-u)/R_w$ (albo $u=(J-i)/G_w$); nigdy nie wymuszaj wartości, bo żadna nie jest ustalona.

Wartości $R_d=\infty$ lub $R_d=0$ są w kluczach bardzo częste — jeśli w punkcie pracy charakterystyka ma odcinek pionowy/poziomy, odpowiedź jest „natychmiastowa”.
:::

::: pulapka Statyczny ≠ dynamiczny
Wartość $R_s$ **nie** mówi nic o $R_d$. Dwa elementy mogą mieć identyczny $R_s$ i różne $R_d$ (np. $R_s$ z siecznej przecinającej „schodki”). Zawsze czytaj, o który opór pytanie.
:::

**Kształty charakterystyk, które trzeba rozpoznawać** (pytanie *„która charakterystyka opisuje opór nieliniowy?”*):

| Element | Charakterystyka $i(u)$ | Cechy |
|---|---|---|
| Rezystor liniowy | prosta przez początek układu | $R=\text{const}$ |
| Opór nieliniowy (np. żarówka, termistor) | krzywa, symetryczna lub nie | $R_s(u)\neq\text{const}$ |
| Dioda idealna | zero dla $u<0$, pionowa dla $u>0$ | „zwarciowo-rozwarciowa” |
| Dioda rzeczywista | wykładnicza, prąd wsteczny mały | nieliniowa, asymetryczna |
| Cewka/kondensator | charakterystyka nie jest jednoznaczna (histereza / pamięć) | elementy z pamięcią |

### 4.2 Punkt pracy — metoda graficzna

Prosta obciążenia dla źródła rzeczywistego napięciowego $(E,R_w)$:

$$i=\frac{E-u}{R_w}\quad\Longrightarrow\quad i(0)=\frac{E}{R_w}\ \ (\text{przy }u=0),\qquad
u(0)=E\ \ (\text{przy }i=0)$$

Dla źródła prądowego rzeczywistego $(J,G_w)$:

$$i=J-G_w u$$

::: metoda Uniwersalny algorytm dla obwodu z elementem nieliniowym
1. **Odłącz** element nieliniowy; policz $E_T$ i $R_T$ reszty obwodu (Thévenin).
2. Prosta obciążenia: $u=E_T-R_T i$ — wygodna, bo nie zależy od kształtu charakterystyki.
3. Punkt pracy = przecięcie prostej z charakterystyką.
4. Odczytaj $U$, $I$; policz $R_s$, $R_d$ i (jeśli trzeba) moc $P=UI$.
:::

### 4.3 Dioda idealna i dwójniki z diodą

::: def Dioda idealna zwarciowo-rozwarciowa
Model dwustanowy:
* $u_D>0$ (polaryzacja przewodzenia) → **zwarcie**, $u_D=0$, $i_D\ge 0$;
* $i_D<0$ byłoby potrzebne → **rozwarcie**, $i_D=0$, $u_D\le 0$.

Charakterystyka: pionowa półprosta dla $u>0$ i pozioma dla $u<0$.
:::

::: figura figury/dioda.svg | Rys. 4.2. Charakterystyka diody idealnej i schemat postępowania z diodą w obwodzie.
:::

::: metoda Analiza obwodu z diodą — metoda „założ i sprawdź”
1. Załóż stan **A**: dioda przewodzi (zastąp zwarciem). Policz $i_D$.
2. Jeśli $i_D>0$ — założenie poprawne, koniec.
3. Jeśli $i_D<0$ — założenie fałszywe: załóż stan **B** (rozwarcie). Policz $u_D$.
4. Jeśli $u_D<0$ — poprawne; jeśli $u_D>0$ — wróć do punktu 1 (obwód mógł być źle zredukowany).

Charakterystyka **dwójnika** $u_{AB}(i)$ z diodą to sklejenie charakterystyk obu stanów. Dlatego w kluczach odpowiedzią jest jeden z pięciu wykresów: zawsze zwróć uwagę na **przesunięcie** załamania (wynika z $E$ w gałęzi) i na **nachylenie** odcinków (wynika z $R$).
:::

::: pulapka Dioda a superpozycja
Obecność diody czyni obwód nieliniowym → **nie wolno** stosować superpozycji ani twierdzenia Thévenina *do całości* obwodu z diodą. Wolno natomiast policzyć Thévenina dla części liniowej (bez diody) i potem rozwiązać graficznie — to standardowa, poprawna droga.
:::

### 4.4 Dwójniki ze źródłami sterowanymi (powtórka w kontekście)

Dwójnik zawierający źródło sterowane jest **liniowy** (bo zależność jest liniowa), ale **aktywny** — może mieć $R_z<0$ (§1.6). Konsekwencje egzaminacyjne:

* można dla niego stosować superpozycję, Thévenina, Nortona;
* **nie** jest dwójnikiem bezźródłowym;
* moc dysponowana może być duża, a „rezystancja” ujemna — nie dziwić się minusowi w wyniku.

---

## 5. Dwójniki i czwórniki

### 5.1 Klasyfikacja dwójników

::: def Podział dwójników
* **Bezźródłowy (pasywny)** — zbudowany wyłącznie z $R$, $L$, $C$ (i ewentualnie elementów nieliniowych bezźródłowych). Nie zawiera żadnego źródła, nawet sterowanego.
* **Źródłowy (aktywny)** — zawiera co najmniej jedno źródło (niezależne lub sterowane).
* **Liniowy / nieliniowy** — ze względu na charakter charakterystyki zewnętrznej $u=f(i)$.
* **Odwracalny** — po zamianie zacisków charakterystyka się nie zmienia (np. sam rezystor).
:::

::: klucz Jak to jest pytane (4 pytania w bazie)
„Dwójnikiem bezźródłowym jest dwójnik: …” — prawidłowa jest ta figura, na której **nie ma żadnego źródła** (ani okręgu ze strzałką, ani rombu źródła sterowanego). Najczęstszy dystraktor to dwójnik ze źródłem sterowanym — wygląda „pasywnie”, ale źródłem jest.
:::

**Charakterystyka zewnętrzna dwójnika** to zależność $u(i)$ na zaciskach. Dla dwójnika liniowego jest to prosta $u=E_T-R_T i$ — czyli *dokładnie* charakterystyka źródła rzeczywistego. Dlatego:

$$u=E_T-R_Ti\ \Longleftrightarrow\ \text{źródło }(E_T,R_T)\ \Longleftrightarrow\ \text{źródło }(J_N=E_T/R_T,\ G_T=1/R_T)$$

Nachylenie charakterystyki zewnętrznej = $-R_T$; przecięcie z osią $u$ = $E_T$; przecięcie z osią $i$ = $J_N$. To pozwala „odczytać” równoważnik z wykresu bez liczenia.

### 5.2 Czwórniki

Czwórnik ma dwie pary zacisków (wejściowa, wyjściowa). Opisuje się go macierzą parametrów (np. łańcuchowych $A$, admitancyjnych $Y$, impedancyjnych $Z$):

$$\begin{bmatrix}u_1\\ i_1\end{bmatrix}=
\begin{bmatrix}A & B\\ C & D\end{bmatrix}
\begin{bmatrix}u_2\\ -i_2\end{bmatrix}$$

::: zapamietaj Co jest zawsze prawdziwe
Dla czwórnika zbudowanego z elementów połączonych **szeregowo** na drodze przepływu prądu (jeden wspólny przewód) prąd wpływający równa się wypływającemu: $i_1=i_2$ — to nic innego jak PPK dla całego czwórnika jako „superwęzła”. Równość $u_1=u_2$ zachodzi tylko wtedy, gdy między zaciskami nie ma spadku napięcia (brak elementu szeregowego albo zwieranie). Rozstrzygnięcie zawsze wynika z PPK/NPK, nie z pamięci.
:::

::: klucz Jak to jest pytane (1 pytanie w bazie)
„Przedstawiony czwórnik jest częścią większego układu, a $R>0$. Które wyrażenie jest zawsze prawdziwe?” — PPK daje $i_1=i_2$; odpowiedzi typu $u_2=Ri_2$, $i_2>0$ są prawdziwe tylko przy dodatkowych założeniach o kierunkach i znaku prądu, więc „zawsze” odpada.
:::

---

## 6. Pomiary: błąd, niepewność, metody

### 6.1 Błąd i niepewność — pojęcia podstawowe

::: def Błąd a niepewność
* **Błąd bezwzględny**: $\Delta x=x_{\text{ws}}-x_{\text{wz}}$; **błąd względny**: $\delta=\Delta x/x_{\text{wz}}$.
* Błąd **systematyczny** — powtarzalne odchylenie w jedną stronę (np. obciążenie obwodu przez przyrząd); daje się skorygować.
* Błąd **przypadkowy** — rozrzut wyników; opisywany statystycznie.
* **Niepewność** nie jest błędem! To parametr opisujący **rozrzut** (przedział), w którym z danym prawdopodobieństwem znajduje się wartość prawdziwa.
:::

::: def Cztery rodzaje niepewności (i jak je rozpoznać)
* **Standardowa $u(x)$** — wynik pomiaru wyrażony jako **odchylenie standardowe**. Typ A: z serii pomiarów (statystyka). Typ B: z danych producenta/klasy przyrządu (np. z niepewności granicznej i założonego rozkładu).
* **Graniczna $\Delta_g$** — maksymalne odchylenie graniczne przyrządu wg jego specyfikacji; „najgorszy przypadek”. Można ją przeliczyć na standardową, znając rozkład błędu: dla **równomiernego** $u=\Delta_g/\sqrt{3}\approx0{,}58\,\Delta_g$; dla **normalnego** przyjmuje się, że $\Delta_g$ odpowiada $3\sigma$, czyli $u=\Delta_g/3$.
* **Rozszerzona $U$** — $U=k\,u_c$; dla $k=2$ odpowiada prawdopodobieństwu ok. $95\%$ (rozkład normalny). Jest szczególnym przypadkiem niepewności granicznej — tak też bywa formułowana poprawna odpowiedź.
* **Złożona $u_c$** — niepewność wielkości mierzonej pośrednio, złożona z niepewności składników wg modelu pomiaru (§6.3). **Zależy od modelu** — to najczęstsza prawidłowa odpowiedź na pytanie „niepewność złożona pomiaru…”.
:::

::: klucz Jak to jest pytane (17 pytań w bazie)
Pytania są zawsze testem zdań-definicji. Zestaw prawdziwych zdań z kluczy:

* „niepewność standardowa to niepewność wyrażona jako odchylenie standardowe”,
* „niepewność standardowa wykorzystywana jest przy obliczaniu niepewności złożonej”,
* „niepewność rozszerzona = niepewność standardowa pomnożona przez współczynnik”,
* „niepewność rozszerzona określa przedział, który z przyjętym prawdopodobieństwem obejmuje wartość prawdziwą” (uwaga: **nie** „na pewno obejmuje”),
* „niepewność graniczna może być interpretowana jako szczególny przypadek niepewności rozszerzonej”,
* „niepewność graniczna może być przeliczona na standardową, jeśli rozkład błędu jest równomierny”,
* „niepewność złożona zależy od modelu pomiaru”, „niepewność względna ułatwia orientacyjne porównanie dokładności różnych wielkości”,
* „przy ustalonym zakresie niepewność graniczna **względna** rośnie, gdy wartość mierzona maleje”.

Zdania fałszywe (dystraktory): „niepewność to średnia wartość błędu”, „zawsze stanowi sumę niepewności składowych”, „zawsze jest typu A”, „określa przedział, który **na pewno** obejmuje wartość prawdziwą”, „dla przyrządu cyfrowego zawsze równa się jedności najmłodszej cyfry”.
:::

### 6.2 Metody pomiarowe

| Metoda | Istota | Przykład z życia laboratorium |
|---|---|---|
| **Bezpośrednia** | porównanie wskazania przyrządu z wzorcem | długość linijką, temperatura termometrem |
| **Pośrednia prosta (skojarzeniowa)** | wynik z prostego wzoru z wielkości mierzonych wprost | moc $P=UI$ z woltomierza i amperomierza |
| **Pośrednia złożona (pochodna)** | wynik wymaga kilku etapów lub zależności złożonej | rezystancja metodą techniczną $R=U/I$ z korektą, wyznaczanie parametrów z charakterystyki |
| **Zerowa kompensacyjna** | doprowadzenie różnicy do zera przez regulację napięcia kompensującego | kompensator napięcia stałego |
| **Zerowa porównawcza** | zrównoważenie mostka (wzorzec + przekładnia) | **mostek Wheatstone'a** |
| **Różnicowa** | pomiar małej różnicy dwóch wielkości | pomiar przyrostu rezystancji |
| **Podstawienia** | podmiana obiektu na wzorzec przy tym samym wskazaniu | kalibracja wagą |
| **Wychyłowa** | odczyt wychylenia (obarczona błędem metody pobrania) | woltomierz analogowy |

::: klucz Jak to jest pytane (1 pytanie wprost o metodę + 21 pytań o błąd metody pobrania)
Trzy powtarzalne pytania (i ich odpowiedzi z kluczy):

1. *„Pomiar oporu metodą techniczną (U, I, prawo Ohma) to pomiar…”* → **pośredni złożony (pochodny)**; dystraktory: „pośredni prosty”, „skojarzeniowy”, „bezpośredni prosty”.
2. *„Pomiar oporu mostkiem Wheatstone'a to pomiar metodą…”* → **zerową porównawczą** (nie „kompensacyjną”! kompensacyjna to kompensator, nie mostek).
3. *„Który z pomiarów nie jest pomiarem pośrednim prostym?”* → ten, który jest **bezpośredni** (linijka, termometr, ciśnieniomierz, higrometr).
:::

### 6.3 Niepewność złożona — rachunek

::: def Prawo propagacji niepewności
Dla modelu $y=f(x_1,\dots,x_n)$ o **nieskorelowanych** wejściach:
$$u_c(y)=\sqrt{\sum_{i=1}^{n}\left(\frac{\partial f}{\partial x_i}\right)^{2}u^{2}(x_i)}$$
:::

Dwa praktyczne szczególne przypadki — to one występują w kluczach:

$$\text{iloczyn/iloraz: } \delta_c(y)=\sqrt{\sum_i \delta_i^{2}},
\qquad\text{suma/różnica: } u_c(y)=\sqrt{\sum_i u_i^{2}}$$

::: uwaga Metoda różniczki zupełnej to inna metoda
W kluczach rozróżnia się **dwie** metody i to jest źródłem części dystraktorów:

* **różniczka zupełna (przypadek najgorszy, „graniczny”)**:
$$\Delta y=\sum_i\left|\frac{\partial f}{\partial x_i}\right|\Delta x_i \quad\Longrightarrow\quad (\text{dla iloczynu})\ \ \delta=\sum_i |\delta_i|$$
* **nieskorelowane (statystyczna, „w kwadracie”)**: pierwiastki z sumy kwadratów, jak wyżej.

Dla $P=RI^{2}$ i $\delta_R=\delta_I=0{,}5\%$: różniczka zupełna daje $0{,}5\%+2\cdot0{,}5\%=1{,}5\%$, a metoda dla nieskorelowanych $\sqrt{0{,}5^2+1{,}0^2}\approx1{,}12\%$. To wyjaśnia, dlaczego w jednym teście prawidłowa jest odpowiedź „żadna z pozostałych” (bo $1{,}5\%$ nie ma na liście), a w innym — odpowiedź $1{,}12\%$.
:::

::: metoda Algorytm na każde zadanie „mierzona pośrednio…”
1. Zapisz model, np. $U=E-RI$ albo $P=U^{2}/R$.
2. Policz pochodne cząstkowe.
3. Zamień niepewności względne na bezwzględne ($u=\delta\cdot x$, $\Delta=\delta\cdot x$).
4. Złóż: pierwiastki z kwadratów (nieskorelowane) **albo** suma modułów (różniczka zupełna) — zależnie od treści.
5. Podaj wynik z jednostką; sprawdź rząd wielkości (np. $0{,}1$ V przy $10$ V i $1\%$ to sens, $10$ V — nie).
:::

::: pulapka Pułapka „1% na wszystkim”
Przy modelu $U=E-RI$ z $E=10$ V, $R=2$ kΩ, $I=1$ mA i $1\%$ na każdym z trzech składników niepewność **nie** wynosi $3\%$ ani $1\%$: składniki $RI$ są małe w porównaniu z $E$, więc dominuje niepewność $E$. Wynik to $u(U)\approx0{,}104$ V (czyli $\approx1{,}04\%$).
:::

### 6.4 Zaokrąglanie wyniku i zapis niepewności

**Zasady (spójne z kluczami):**

1. Niepewność podajemy z **1–2 cyframi znaczącymi** (w kluczach spotyka się oba warianty — patrz uwaga niżej); przy zaokrąglaniu „w górę”, aby nie zaniżać niepewności.
2. Wynik zaokrąglamy do tego samego miejsca dziesiętnego, co niepewność.
3. Jednostkę piszemy raz, po nawiasie: $(1{,}83\pm0{,}05)$ V.

::: uwaga Dwie szkoły widoczne w kluczach
Ten sam typ zadania rozwiązano raz z niepewnością do 1 cyfry znaczącej, raz do 2:

| Wskazanie | $\Delta_g$ przed zaokrągleniem | Odpowiedź w kluczu |
|---|---|---|
| $1{,}8261$ V | $0{,}04131$ V | $(1{,}83\pm0{,}05)$ V |
| $1{,}226$ mA | $0{,}1631$ mA | $(1{,}23\pm0{,}17)$ mA |
| $1{,}1534$ mA | $0{,}032823$ mA | $(1{,}15\pm0{,}04)$ mA |
| $1{,}1536$ mA | $0{,}015236$ mA | $(1{,}154\pm0{,}016)$ mA |
| $9{,}632$ V | $0{,}03436$ V | $(9{,}63\pm0{,}04)$ V |
| $8{,}627$ V | $0{,}1143$ V | $(8{,}63\pm0{,}12)$ V |
| $10{,}483$ V | $0{,}3143$ V | $(10{,}5\pm0{,}4)$ V |

Wniosek praktyczny: wybieraj odpowiedź, w której **liczba cyfr znaczących niepewności mieści się w przedziale 1–2, a wynik jest zaokrąglony do jej rzędu**. Dystraktory zawsze „grzeszą” jednym z tych dwóch warunków (np. $(1{,}8261\pm0{,}0413)$ — ani wynik, ani niepewność nie są zaokrąglone).
:::

### 6.5 Opracowanie serii pomiarów

Dla $n$ pomiarów $x_1,\dots,x_n$:

$$\bar{x}=\frac{1}{n}\sum_i x_i,\qquad
s=\sqrt{\frac{1}{n-1}\sum_i\left(x_i-\bar{x}\right)^{2}},\qquad
u(\bar{x})=\frac{s}{\sqrt{n}}$$

$s$ to **odchylenie standardowe pojedynczego pomiaru** (niepewność typu A pojedynczego wyniku), $s/\sqrt{n}$ — **odchylenie standardowe średniej**.

::: przyklad Cztery pomiary: 10,80 V; 11,10 V; 10,90 V; 11,20 V
$\bar{x}=11{,}00$ V. Odchylenia: $-0{,}20$; $+0{,}10$; $-0{,}10$; $+0{,}20$ → suma kwadratów $=0{,}10$ → $s=\sqrt{0{,}10/3}=0{,}183$ V. Odchylenie średniej: $s/\sqrt{4}=0{,}0913\approx0{,}092$ V. Dokładnie te dwie liczby (0,183 V i 0,092 V) są prawidłowymi odpowiedziami w kluczu.
:::

::: pulapka Dzielnik $n$ czy $n-1$?
W mianowniku pod pierwiastkiem jest $n-1$ (próba, estymator nieobciążony). Dzielenie przez $n$ zaniża wynik — dystraktory $0{,}158$ V i $0{,}163$ V w kluczu to właśnie skutek dzielenia przez $n$ i przez $n$ z błędnym zaokrągleniem.
:::

---

## 7. Przyrządy pomiarowe i ich niepewność

### 7.1 Przyrządy analogowe (elektromechaniczne)

::: def Klasa dokładności
Klasa $k$ (0,1; 0,2; 0,5; 1; 1,5; 2,5) oznacza, że **niepewność graniczna** odnosi się do **całego zakresu**, nie do wskazania:
$$\Delta_g=\frac{k}{100}\,X_{z},\qquad
\delta_g=\frac{\Delta_g}{X_{m}}=\frac{k\,X_z}{100\,X_m}$$
gdzie $X_z$ — zakres (napięcie/prąd zakresowy), $X_m$ — wartość mierzona.
:::

::: zapamietaj Dwa wnioski, które dają punkty
1. $\Delta_g$ **nie zależy** od wskazania (dla ustalonego zakresu) — jest stała.
2. $\delta_g$ **maleje** ze wzrostem wskazania → mierzymy **przy jak największym wychyleniu** (w górnej części skali), bo wtedy $\delta_g$ jest najmniejsza.
:::

::: przyklad Klasa nie zawsze wygrywa — pomiar 2 V (klucz: 23Z_B_2, pyt. E)
Który przyrząd da **największą** niepewność graniczną?
* analogowy kl. $0{,}5$, zakres $10$ V → $\Delta_g=0{,}05\cdot10=0{,}05$ V
* analogowy kl. $0{,}1$, zakres $20$ V → $\Delta_g=0{,}001\cdot20=0{,}02$ V
* cyfrowy $0{,}2\%$ + 2 cyfry, zakres $9{,}99$ V → $0{,}004+2\cdot0{,}01=0{,}024$ V
* cyfrowy $0{,}7\%$ + 5 cyfr, zakres $19{,}999$ V → $0{,}014+5\cdot0{,}001=0{,}019$ V

Najgorszy jest analogowy kl. $0{,}5$ na zakresie $10$ V ($0{,}05$ V) — **gorszy klasa, ale mniejszy zakres nie ratuje sytuacji**, bo $0{,}5\%$ z $10$ V to więcej niż $0{,}1\%$ z $20$ V. Wniosek: nigdy nie odpowiadaj „bo ma najlepszą klasę” — zawsze licz $\Delta_g$.
:::

::: przyklad Klasa 0,1 na zakresie 30 V — dla jakiego napięcia $\delta_g=2\%$?
$\Delta_g=0{,}001\cdot30=0{,}03$ V. Warunek $0{,}03/U=0{,}02$ → $U=1{,}5$ V. (Odpowiedź z klucza: 1,5 V.)
:::

### 7.2 Przyrządy cyfrowe

::: def Niepewność graniczna przyrządu cyfrowego
$$\Delta_g=a\%\,X_m+b\%\,X_z \qquad\text{albo}\qquad \Delta_g=a\%\,X_m+n\cdot \text{cyfra}$$
gdzie $a$ — niepewność członu wzmocnienia (od wartości mierzonej), $b$ — niepewność zera (od zakresu), „cyfra” — wartość jednostki najmłodszej cyfry (rozdzielczość), $n$ — liczba cyfr.
:::

::: figura figury/niepewnosc_wykresy.svg | Rys. 7.1. Charakterystyki niepewności przyrządu cyfrowego przy ustalonym zakresie: $\Delta_g$ rośnie liniowo z $|x|$ (od $b\%\,X_z$), natomiast $\delta_g=a\%+b\%\,X_z/|x|$ maleje hiperbolicznie do asymptoty $a\%$.
:::

**Kształty charakterystyk — do zapamiętania na obrazkach** (pytanie „który wykres…”):

| Wielkość | Zależność od $|x|$ (stały zakres) | Kształt |
|---|---|---|
| $\Delta_g(x)$ | $a|x|+bX_z$ — liniowa rosnąca, start w $bX_z>0$ | prosta |
| $\delta_g(x)$ | $a+bX_z/|x|$ — malejąca hiperbola → asymptota $a$ | hiperbola |
| $u(x)=\Delta_g/\sqrt3$ (rozkład równomierny) | liniowa rosnąca | prosta |
| $u_{\text{rel}}(x)$ | malejąca hiperbola | hiperbola |

::: uwaga Zakres pomiarowy a niepewność
* Przy ustalonej wartości mierzonej $X_m$: **zmniejszenie zakresu** zwykle zmniejsza $\Delta_g$ (mniejszy człon $b\%X_z$ i mniejsza cyfra), ale nie zawsze — jeśli dominuje człon $a\%X_m$, zysk jest mały.
* Przy ustalonym zakresie: $\delta_g$ **rośnie**, gdy $X_m$ maleje (bo człon zera jest stały).
* $\Delta_g$ **nie** rośnie, gdy $X_m$ maleje — jest stały lub maleje (człon $a X_m$).
:::

::: klucz Jak to jest pytane (8 pytań o wykresy + 4 o zdania)
* „Który wykres przedstawia **względną** niepewność graniczną / **standardową względną**…” → hiperbola malejąca (dąży do stałej).
* „Który wykres przedstawia **niepewność graniczną** (bezwzględną)…” → prosta rosnąca, zaczynająca się powyżej zera.
* „Przy ustalonym zakresie $\delta_g$ rośnie, gdy $X_m$ maleje” → zdanie prawdziwe w każdej wersji testu.
:::

### 7.3 Dobór przyrządu i zakresu

::: metoda Algorytm porównania woltomierzy/amperomierzy
1. Dla każdej opcji policz $\Delta_g$ **w jednostkach napięcia/prądu**.
2. Analog: $\Delta_g=\frac{k}{100}X_z$.
3. Cyfrowy: $\Delta_g=a\%\,X_m+b\%\,X_z$ lub $a\%\,X_m+n\cdot$cyfra (cyfra = $X_z$/liczba ostatniego miejsca).
4. Porównaj liczby; wybierz **najmniejszą** (albo największą, jeśli pytanie o „największą niepewność”).
5. Sprawdź, czy wartość mierzona mieści się w zakresie (dla $12$ V zakres $0\ldots9{,}99$ V odpada!).
:::

::: przyklad Pomiar 12 V — który woltomierz najlepszy? (klucz: 19Z_B_1, pyt. C)
* Cyfrowy $0{,}2\%$ + 1 cyfra, zakres $000{,}0\ldots199{,}9$ V: cyfra $=0{,}1$ V → $\Delta_g=0{,}024+0{,}1=0{,}124$ V
* Cyfrowy $1\%$ + 5 cyfr, zakres $00{,}00\ldots19{,}99$ V: cyfra $=0{,}01$ V → $\Delta_g=0{,}12+0{,}05=0{,}17$ V
* Analogowy kl. 1, zakres 30 V: $\Delta_g=0{,}30$ V
* Analogowy kl. 0,2, zakres 100 V: $\Delta_g=0{,}20$ V

Najmniejsza: **0,124 V** → pierwszy woltomierz. Widać, że w cyfrowych decyduje liczba cyfr (rozdzielczość), a w analogowych — iloczyn klasy i zakresu.
:::

::: przyklad Pomiar 18 V (klucz: 19Z_B_2, pyt. C)
* Analogowy kl. 0,1, zakres 100 V → $0{,}10$ V
* Cyfrowy $0{,}2\%$ + 1 cyfra, zakres $199{,}9$ V → $0{,}036+0{,}1=0{,}136$ V
* Cyfrowy $1\%$ + 1 cyfra, zakres $19{,}99$ V → $0{,}18+0{,}01=0{,}19$ V
* Analogowy kl. 0,5, zakres 30 V → $0{,}15$ V

Najmniejsza: **0,10 V** → analogowy kl. 0,1 na zakresie 100 V. Ten sam typ zadania, inna odpowiedź — bo zmieniły się liczby. **Nigdy nie odpowiadaj z pamięci.**
:::

---

## 8. Pomiary rezystancji

### 8.1 Metoda techniczna i błąd metody pobrania

::: def Metoda techniczna
Pomiar pośredni: mierzymy napięcie $U$ na rezystorze i prąd $I$ przez niego płynący, a wynik liczymy z prawa Ohma $R=U/I$. Niepewność (i błąd systematyczny) wynika z tego, że przyrządy **pobierają** część energii obwodu.
:::

::: figura figury/metoda_techniczna.svg | Rys. 8.1. Dwa układy pomiarowe: a) z poprawnym pomiarem napięcia, b) z poprawnym pomiarem prądu. Żaden nie jest „idealny” — wybór zależy od wartości $R_x$.
:::

| Układ | Co mierzy przyrząd | Wynik obliczony | Błąd względny |
|---|---|---|---|
| **a) poprawny pomiar napięcia** (V przed A) | V: $U_x$; A: $I_x+I_V$ | $R'=\dfrac{R_xR_V}{R_x+R_V}$ | $\dfrac{\Delta R}{R}\approx-\dfrac{R_x}{R_V}$ |
| **b) poprawny pomiar prądu** (A przed V) | A: $I_x$; V: $U_x+U_A$ | $R'=R_x+R_A$ | $\dfrac{\Delta R}{R}\approx+\dfrac{R_A}{R_x}$ |

::: zapamietaj Reguła wyboru układu
Błąd obu metod jest równy co do modułu, gdy
$$R_x=\sqrt{R_AR_V}$$
Dla $R_x<\sqrt{R_AR_V}$ lepszy jest układ **a)** (poprawny pomiar napięcia), dla $R_x>\sqrt{R_AR_V}$ — układ **b)** (poprawny pomiar prądu). Intuicja: dużej rezystancji nie obciąża woltomierz, małej — nie psuje amperomierz.
:::

::: przyklad $R_x=10$ kΩ, $R_A=1\ \Omega$, $R_V=1$ MΩ (klucz: 24Z_B_1, pyt. B)
$\sqrt{R_AR_V}=\sqrt{1\cdot10^{6}}=1$ kΩ. Ponieważ $R_x=10$ kΩ $>1$ kΩ → wybieramy układ z poprawnym pomiarem prądu, a błąd wynosi
$$\frac{\Delta R}{R}\approx\frac{R_A}{R_x}=\frac{1}{10\,000}=0{,}01\%.$$
Odpowiedź z klucza: **0,01 %**.
:::

::: przyklad $R_x=3{,}3$ kΩ, $R_V=10$ MΩ, $R_A=10\ \Omega$ (klucz: 20Z_B_2, pyt. F)
$\sqrt{10\cdot10^{7}}=10$ kΩ. Teraz $R_x=3{,}3$ kΩ $<10$ kΩ → lepszy układ **z poprawnym pomiarem napięcia**. (Klucz: „metoda techniczna z poprawnym pomiarem napięcia”.)
:::

::: def Błąd metody pobrania (obciążenie przyrządem)
* **Woltomierz** dołączony równolegle obciąża węzeł: względny błąd napięcia wynosi w przybliżeniu
$$\delta U\approx-\frac{R_T}{R_T+R_V},$$
gdzie $R_T$ to rezystancja zastępcza widziana z zacisków woltomierza. Błąd jest **największy tam, gdzie $R_T$ jest największe** (o największej impedancji węzeł).
* **Amperomierz** włączony szeregowozwiększa rezystancję gałęzi: $\delta I\approx-\dfrac{R_A}{R_A+R_{\text{gałęzi}}}$ — błąd największy w gałęzi o **najmniejszej** rezystancji.
:::

::: klucz Jak to jest pytane (21 pytań w bazie)
Powtarzalny schemat: drabinka rezystorów (np. $R, 2R, R, 2R$), pytanie „dla którego węzła/gdzie błąd metody pobrania jest największy/najmniejszy”. Rozwiązanie: **policz rezystancję zastępczą widzianą z punktu pomiaru** (przy wyłączonym źródle) i wybierz węzeł o skrajnej wartości. W pytaniach o amperomierz — wybierz gałąź o najmniejszej rezystancji.
:::

### 8.2 Mostek Wheatstone'a

::: figura figury/mostek.svg | Rys. 8.2. Mostek Wheatstone'a zasilany napięciem $U_{AB}$; wskaźnikiem zera (galwanometrem) wykrywamy równowagę.
:::

Warunek równowagi (prąd galwanometru zerowy):

$$R_1R_x=R_2R_0\qquad\Longrightarrow\qquad R_x=R_0\,\frac{R_2}{R_1}$$

::: def Dlaczego to metoda zerowa **porównawcza**
W równowadze nie mierzymy żadnego napięcia ani prądu — doprowadzamy wskazanie do zera, a wynik zależy **wyłącznie od stosunku oporów** $R_2/R_1$ i wartości wzorca $R_0$. Napięcie zasilania, czułość i charakterystyki przyrządów nie wpływają na wynik → bardzo mały błąd systematyczny. Porównujemy z wzorcem (stąd „porównawcza”), a nie kompensujemy napięcia (to inna metoda — kompensacyjna).
:::

**Zakres pomiarowy** reguluje się przekładnią $R_2/R_1$:

$$R_{x,\max}=R_{0,\max}\cdot\frac{R_2}{R_1}$$

::: przyklad Zakres 0…20 MΩ przy $R_0=0\ldots10$ kΩ
Potrzebujemy $\dfrac{R_2}{R_1}=\dfrac{20\ \text{M}\Omega}{10\ \text{k}\Omega}=2000$. Warunek spełnia np. $R_1=10\ \Omega$, $R_2=20$ kΩ (klucz: 20Z_B_1, pyt. E — prawidłowa jest ta para, która daje właściwą przekładnię i sensowne wartości bezwzględne).
:::

::: przyklad Zakres 0…20 Ω przy $R_0=0\ldots10$ kΩ
Teraz $\dfrac{R_2}{R_1}=\dfrac{20\ \Omega}{10\ 000\ \Omega}=0{,}002$ → np. $R_1=100$ kΩ, $R_2=200\ \Omega$ (klucz: 24Z_B_2, pyt. B). Wniosek: dla **małych** $R_x$ przekładnia jest „odwrotna” (duży $R_1$, mały $R_2$), dla **dużych** — $R_2\gg R_1$.
:::

::: uwaga Gdzie mostek wygrywa, a gdzie przegrywa
* Wygrywa: pomiar w szerokim zakresie (**także wtedy, gdy wzorzec różni się od mierzonej wartości o wiele rzędów wielkości** — bo różnicę „nadrabia” przekładnia), duża dokładność, niezależność od napięcia zasilania.
* Przegrywa: bardzo małe rezystancje (rezystancje przewodów i styków są porównywalne z $R_x$) → wtedy metoda **czteroprzewodowa** (Kelvina) lub mostek Thomsona; bardzo duże rezystancje → problemy z upływnościami (lepszy mostek rezystancyjno-pojemnościowy).
:::

### 8.3 Metoda czteroprzewodowa (Kelvina)

Dwa przewody doprowadzają prąd, dwa osobne — mierzą napięcie. Spadki napięcia na przewodach prądowych nie wchodzą do wyniku, bo przez przewody napięciowe nie płynie prąd. Stosowana dla rezystancji rzędu miliomów i mniejszych.

---

## 9. Oscyloskop

### 9.1 Tor sygnału i podstawowe nastawy

::: def Co robi oscyloskop
Przetwarza sygnał napięciowy na obraz $u(t)$: wejście → tłumik/wzmacniacz → sprzężenie (AC/DC/GND) → przetwornik ADC (w oscyloskopie cyfrowym) → pamięć → układ wyzwalania → ekran. Skale: **V/dz** (wzmocnienie) i **s/dz** (podstawa czasu).
:::

::: uwaga Parametry, o które pytają najczęściej
* **Pasmo** $B$ i **czas narastania**: $t_r\approx0{,}35/B$ — oscyloskop musi mieć pasmo co najmniej $3$–$5\times$ szersze niż mierzony sygnał.
* **Rezystancja i pojemność wejściowa** (typowo $1$ MΩ $\|$ kilkanaście pF) — wraz z sondą tworzą dzielnik; sonda 10:1 zwiększa rezystancję i obciąża obwód znacznie mniej.
* **Rozdzielczość pionowa** — liczba bitów ADC (8 bitów = 256 poziomów).
* **Pamięć** — liczba próbek: $N=f_s\cdot t_{\text{okna}}$.
:::

### 9.2 Sprzężenie wejścia: DC, AC, GND

::: figura figury/sprzezenie.svg | Rys. 9.1. W trybie AC kondensator wejściowy odcina składową stałą, więc mała składowa zmienna może być obserwowana przy dużym wzmocnieniu.
:::

| Tryb | Co widzisz | Kiedy używać |
|---|---|---|
| **DC** | pełny sygnał (składowa stała + zmienna) | pomiar wartości napięcia stałego, obserwacja całego przebiegu |
| **AC** | sygnał z **odciętą składową stałą** (filtr górnoprzepustowy) | mała składowa zmienna na tle dużej stałej; usunięcie stałej |
| **GND** | linię poziomu zerowego | ustawienie poziomu odniesienia (0 V) na ekranie |

::: klucz Jak to jest pytane (w każdym prawie teście)
* „Do czego służy tryb AC sprzężenia?” → **do oglądania małej składowej zmiennej na tle dużej składowej stałej** oraz **do usunięcia z sygnału składowej stałej** (oba zdania są w kluczach prawidłowe).
* Dystraktory: „do usunięcia składowej zmiennej”, „do oglądania małej składowej stałej na tle dużej zmiennej”, „do wyzwalania siecią 50 Hz” (to AC LINE, nie sprzężenie!).
* „Tryb DC może służyć do…” → obserwacji obu składowych **i** pomiaru napięcia stałego.
:::

### 9.3 Wyzwalanie (trigger)

::: def Wyzwalanie
Układ wyzwalania „zamraża” zapis w chwili spełnienia warunku: poziom + zbocze (narastające/opadające) + źródło. Bez wyzwalania obraz okresowy „pływa” po ekranie.
:::

* **Źródła:** kanał 1/2 (wewnętrzne), wejście zewnętrzne EXT, **AC LINE** (sygnał sieci 50 Hz — do obserwacji przebiegów zsynchronizowanych z siecią).
* **Tryby:** AUTO (odświeża obraz nawet bez wyzwolenia), NORMAL (czeka na wyzwolenie), SINGLE (jeden zapis — do zdarzeń jednorazowych).
* **Dodatkowo:** sprzężenie wyzwalania (DC/AC/LF-reject/HF-reject), holdoff, wyzwalanie po zboczu/logiczne/szeregowe (MSO).

::: klucz Jak to jest pytane
„Do czego służy tryb AC LINE wyzwalania?” → **do zewnętrznego wyzwalania oscyloskopu sygnałem sieci energetycznej 50 Hz**. To pytanie-myłka: brzmi jak sprzężenie AC (patrz §9.2), ale dotyczy **źródła wyzwalania**.
:::

### 9.4 Rodzaje oscyloskopów

| Rodzaj | Zasada | Mocna strona | Ograniczenie |
|---|---|---|---|
| **Analogowy** | wzmocnienie + lampa z luminofor | wierność, brak przetwarzania | **brak**: podglądu „przeszłości” (pre-trigger), zapisu, automatycznych pomiarów; trudne przebiegi jednorazowe |
| **DSO** (z pamięcią cyfrową) | ADC + pamięć + procesor | pre-trigger, przebiegi jednorazowe, autopomiary, USB, matematyka | zależny od ADC (kwantyzacja, aliasing) |
| **DPO** (cyfrowy luminofor) | histogram/intensywność zdarzeń | **rzadkie anomalie** w powtarzalnym przebiegu, „intensywność” jak w analogu | drogi |
| **DSO z próbkowaniem bezpośrednim** (sampling, stroboskopowy) | próbkowanie w **czasie równoważnym** | **najszersze pasmo** (dziesiątki GHz), pomiar bardzo krótkich zboczy | tylko sygnały **powtarzalne**; wrażliwy kanał wejściowy |
| **MSO** (mixed signal) | kanały analogowe + cyfrowe | korelacja czasowa zdarzeń cyfrowych z reakcją analogową | — |
| **MDO** | oscyloskop + analizator widma | widmo + przebieg jednocześnie | — |

::: klucz Jak to jest pytane (17 pytań w bazie)
Cztery schematy i ich odpowiedzi:

1. „Której cechy **nie ma** oscyloskop **analogowy**?” → brak pre-trigger („przeszłości”), brak zapisu na USB, brak automatycznych pomiarów. (Obecność triggera, wyzwalania zewnętrznego, sprzężenia AC i sondy **ma**.)
2. „Której cechy **nie ma** oscyloskop **cyfrowy**?” → „żadna z pozostałych odpowiedzi nie jest prawidłowa” (ma wszystko z listy).
3. „Rzadkie anomalie w powtarzalnym przebiegu” → **DPO**. „Bardzo krótki czas narastania impulsu powtarzalnego” → **sampling**. „Korelacja sekwencji logicznych z reakcją analogową” → **MSO**. „Widmo RF synchronicznie z przebiegiem” → **MDO**.
4. „Zwiększenie liczby bitów ADC 8 → 12” → **mniejsze zniekształcenia od kwantyzacji**. „Zwiększenie częstości próbkowania” → **mniejsze zniekształcenia od próbkowania w czasie** oraz **szybsze zapełnianie pamięci próbek** (oba zdania bywają prawidłowe).
:::

### 9.5 Przetwornik ADC: kwantyzacja, próbkowanie, pamięć

::: def Trzy niezależne źródła zniekształceń
1. **Kwantyzacja (pion)** — $n$ bitów daje $2^{n}$ poziomów; błąd $\pm\tfrac12$ LSB. Zwiększenie $n$ o 1 bit → 2× mniejsza LSB (ok. 6 dB lepszy stosunek sygnał/szum).
2. **Próbkowanie (poziom)** — $f_s<2f_{\max}$ powoduje **aliasing** (pozorne niskie częstotliwości). Zwiększenie $f_s$ zmniejsza zniekształcenia w dziedzinie czasu.
3. **Pamięć** — przy stałej liczbie próbek szybsze próbkowanie skraca okno obserwacji; przy stałym oknie — szybciej zapełnia pamięć i zwiększa strumień danych.
:::

::: pulapka Co „nie” zmienia liczba bitów
Zwiększenie liczby bitów **nie** zwiększa pasma analogowego, **nie** zwiększa zakresu napięć wejściowych, **nie** zwiększa rezystancji wejściowej i **nie** zmniejsza zniekształceń pochodzących z próbkowania w czasie. To najczęstsze dystraktory.
:::

---

## 10. Zadania rozwiązane

Poniżej 18 zadań — wszystkie oparte na rzeczywistych pytaniach z kluczy (podaję plik/oznaczenie), z pełnym rachunkiem. Zadania z rysunkami obwodów rozwiązywane są „na wzorach”, bo w kluczach rysunki są tylko w PDF.

### 10.1 Rachunek obwodów

::: przyklad Z1. Rezystancja zastępcza dwójnika ze źródłem sterowanym
**Pytanie (typ A, 14 pytań w bazie).** Dwójnik: rezystor $R$ równolegle ze źródłem prądu $gu$ (rys. 1.5). Opór zastępczy wynosi?

**Rozwiązanie.** Wymuszamy napięcie $u$ na zaciskach. Prąd rezystora: $u/R=Gu$. Prąd źródła: $gu$ (w stronę zacisków). Prąd wypływający z zacisków: $i=Gu-gu=(G-g)u$. Stąd $R_z=u/i=1/(G-g)$, czyli równoważnie $R/(1-gR)$ — bo $G=1/R$.

**Odpowiedź:** $\dfrac{1}{G-g}$ (a gdy $g>G$ — wartość ujemna; dwójnik jest aktywny).
:::

::: przyklad Z2. Punkt pracy elementu nieliniowego
**Pytanie (typ B, 17 pytań w bazie).** Element nieliniowy o charakterystyce łamanej podłączono do idealnego źródła prądowego $3$ mA; w punkcie pracy $U=4$ V, a nachylenie charakterystyki w tym punkcie odpowiada $0{,}5$ kΩ. Podaj $R_s$ i $R_d$.

**Rozwiązanie.** Źródło prądowe wymusza $I=3$ mA, więc $R_s=U/I=4\ \text{V}/3\ \text{mA}=1{,}33$ kΩ. Nachylenie w punkcie pracy to $R_d=0{,}5$ kΩ (odczyt ze stycznej/odcinka).

**Odpowiedź:** $R_s=1{,}33$ kΩ, $R_d=0{,}5$ kΩ. (Ten wariant pojawia się w kluczach 21L_A_2, 25Z_A_1 i in.)
:::

::: przyklad Z3. Dopasowanie i moc maksymalna
**Pytanie (typ G, 13 pytań w bazie).** Opór $R$ dobrano tak, by wydzielała się w nim maksymalna moc. Obwód widziany z zacisków $R$ ma $E_T=6$ V i $R_T=10$ kΩ. Ile wynosi $P_{\max}$?

**Rozwiązanie.** Dopasowanie: $R=R_T=10$ kΩ, zatem
$$P_{\max}=\frac{E_T^{2}}{4R_T}=\frac{36\ \text{V}^2}{40\ \text{k}\Omega}=0{,}9\ \text{mW}=\frac{9}{10}\ \text{mW}.$$

**Odpowiedź:** $0{,}9$ mW (w kluczach odpowiedzi są podawane jako ułamki: $\tfrac{3}{10}$, $\tfrac{6}{10}$, $\tfrac{15}{8}$ mW — dlatego warto liczyć dokładnie).
:::

::: przyklad Z4. Moc dysponowana źródła z twierdzenia Nortona
**Pytanie (typ G/H).** W obwodzie z rysunku $J=4$ mA, $R_1=1$ kΩ, $R_2=2$ kΩ, $r=1$ kΩ. Oblicz moc dysponowaną dwójnika $AB$ (wskazówka: użyj twierdzenia Nortona).

**Rozwiązanie.** (1) Zwarcie zacisków — prąd $J_N$ to prąd zwarcia, czyli $J$ pomniejszony o prąd odpływający przez gałęzie boczne, wg dzielnika prądowego; (2) $R_T$ to rezystancja widziana z $AB$ przy rozwartym źródle $J$, czyli $r+(R_1\|R_2)$; (3) $P_{\text{dysp}}=J_N^{2}R_T/4$.

**Odpowiedź:** w kluczu — $4$ mW (odpowiedź 1). Kluczowe kroki są zawsze te same: **$J_N$ → $R_T$ → $J_N^2R_T/4$**.
:::

::: przyklad Z5. Wkład źródła w metodzie superpozycji
**Pytanie (typ F, 13 pytań w bazie).** W układzie z dwoma źródłami napięciowymi $e_1$, $e_2$ i dwoma prądowymi $j_1$, $j_2$ (dane: $e_1=1$ V, $e_2=2$ V, $j_1=1$ A, $j_2=2$ A, $R_1=1$ kΩ, $R_2=2$ kΩ) policz wkład do napięcia $u$ pochodzący od $e_2$.

**Rozwiązanie.** Wyłączamy $e_1$ (zwarcie), $j_1$ i $j_2$ (rozwarcie). Zostaje dzielnik z $R_1$ i $R_2$ zasilany z $e_2$; szukane napięcie to $e_2\frac{R_1}{R_1+R_2}=2\cdot\frac{1}{3}=\frac{2}{3}$ V (albo z minusem — zależnie od strzałki na rysunku).

**Odpowiedź:** $\frac{2}{3}$ V. **Uwaga na znak**: to najczęstsza przyczyna utraty punktu w tym typie zadania.
:::

::: przyklad Z6. Prawo Kirchhoffa — równanie węzła
**Pytanie (typ D).** W węźle $A$ spotykają się trzy prądy $I_1$, $I_2$, $I_3$; dwa pierwsze wpływają do węzła, trzeci wypływa. Które równanie opisuje węzeł?

**Rozwiązanie.** PPK: suma wpływających = suma wypływających → $I_1+I_2=I_3$.

**Odpowiedź:** $I_3=I_1+I_2$ (zapis równoważny: $I_3-I_1-I_2=0$). Odpowiedzi typu $I_3=I_2-I_1$ lub $\sum I_k=0$ bez znaków są nieprawidłowe.
:::

::: przyklad Z7. Natężenie prądu z PPK
**Pytanie (typ E, 11 pytań w bazie).** W węźle znane są trzy prądy: $2$ A wpływa, $1$ A wpływa, $0{,}5$ A wypływa. Ile wynosi czwarty prąd wypływający $I$?

**Rozwiązanie.** $I=2+1-0{,}5=2{,}5$ A.

**Odpowiedź:** $2{,}5$ A. Gdy wynik wychodzi ujemny, oznacza to, że prąd ma kierunek przeciwny do strzałki — i tak też bywa w odpowiedziach (np. $-1$ A).
:::

::: przyklad Z8. Układ z diodą idealną — dwa przypadki
**Pytanie (typ G/H, 5 pytań).** Dioda idealna jest w gałęzi równoległej z rezystorem $R$, całość zasilana ze źródła $E$ przez $R_1$. Podaj charakterystykę dwójnika $AB$.

**Rozwiązanie.** Przypadek 1: dioda przewodzi → gałąź diody jest zwarciem, więc $u_{AB}=0$ i każdy prąd może płynąć (charakterystyka pionowa). Przypadek 2: dioda zaporowa → gałąź odcięta, dwójnik to $R$, więc $u_{AB}=Ri$ (prosta o nachyleniu $R$). Charakterystyka dwójnika to sklejenie obu półprostych w punkcie załamania $u=E\frac{R}{R_1+R}$.

**Odpowiedź:** wykres z pionowym odcinkiem przy $u=0$ (stan przewodzenia) i prostym odcinkiem o nachyleniu $R$ dla $u$ większego od napięcia załamania.
:::

### 10.2 Metrologia — niepewność i dobór przyrządu

::: przyklad Z9. Zaokrąglenie wyniku pomiaru
**Pytanie (typ D, 11 pytań).** Woltomierz cyfrowy wskazał $1{,}8261$ V, a niepewność graniczna przed zaokrągleniem wyniosła $0{,}04131$ V. Podaj poprawny zapis.

**Rozwiązanie.** Niepewność zaokrąglamy „w górę” do 1–2 cyfr znaczących: $0{,}04131\to0{,}05$ V. Wynik zaokrąglamy do tego samego miejsca: $1{,}8261\to1{,}83$ V.

**Odpowiedź:** $(1{,}83\pm0{,}05)$ V. Dystraktory $(1{,}83\pm0{,}04)$ V (za mała niepewność) i $(1{,}8261\pm0{,}0413)$ V (brak zaokrąglenia) są błędne.
:::

::: przyklad Z10. Analogowy: klasa i zakres
**Pytanie (typ B, 2 pytania).** Woltomierz analogowy klasy $0{,}1$ pracuje na zakresie $0\ldots30$ V. Dla jakiego napięcia niepewność względna wynosi $2\%$?

**Rozwiązanie.** $\Delta_g=\frac{0{,}1}{100}\cdot30=0{,}03$ V. $\delta_g=\Delta_g/U=0{,}02$ → $U=0{,}03/0{,}02=1{,}5$ V.

**Odpowiedź:** $1{,}5$ V. Warto zauważyć: na końcu zakresu ($30$ V) $\delta_g=0{,}1\%$, a przy $1{,}5$ V już $2\%$ — dwadzieścia razy gorzej.
:::

::: przyklad Z11. Cyfrowy: niepewność opisana dwoma członami
**Pytanie (typ B).** Woltomierz cyfrowy: $0{,}8\%$ wartości mierzonej $+0{,}09$ V, zakres $0\ldots20$ V. Dla jakiego napięcia $\delta_g=2\%$?

**Rozwiązanie.** $0{,}02\,U=0{,}008\,U+0{,}09$ → $0{,}012\,U=0{,}09$ → $U=7{,}5$ V.

**Odpowiedź:** $7{,}5$ V. Sprawdzenie: $\Delta_g=0{,}008\cdot7{,}5+0{,}09=0{,}15$ V, a $0{,}15/7{,}5=2\%$ ✔.
:::

::: przyklad Z12. Dobór woltomierza — cztery opcje
**Pytanie (typ C).** Pomiar $12$ V. Który woltomierz da najmniejszą niepewność graniczną?
a) cyfrowy $0{,}2\%+1$ cyfra, zakres $000{,}0\ldots199{,}9$ V;
b) cyfrowy $1\%+5$ cyfr, zakres $00{,}00\ldots19{,}99$ V;
c) analogowy kl. $1$, zakres $30$ V;
d) analogowy kl. $0{,}2$, zakres $100$ V.

**Rozwiązanie.**
a) $0{,}002\cdot12+1\cdot0{,}1=0{,}024+0{,}1=0{,}124$ V;
b) $0{,}01\cdot12+5\cdot0{,}01=0{,}12+0{,}05=0{,}17$ V;
c) $0{,}01\cdot30=0{,}30$ V;
d) $0{,}002\cdot100=0{,}20$ V.

**Odpowiedź:** a) — $0{,}124$ V. W cyfrowych decyduje liczba cyfr (rozdzielczość), w analogowych — klasa × zakres.
:::

::: przyklad Z13. Metoda techniczna — który układ i jaki błąd
**Pytanie (typ B/E).** $R_x=10$ kΩ, $R_A=1\ \Omega$, $R_V=1$ MΩ. Wybierz układ pomiarowy i podaj błąd względny.

**Rozwiązanie.** $\sqrt{R_AR_V}=1$ kΩ $<R_x$ → układ z poprawnym pomiarem prądu. Błąd: $\Delta R/R\approx R_A/R_x=1/10\,000=0{,}01\%$.

**Odpowiedź:** układ b), błąd $0{,}01\%$.
:::

::: przyklad Z14. Mostek — dobór zakresu
**Pytanie (typ E).** Mostek z opornikiem dekadowym $R_0=0\ldots10$ kΩ. Jak dobrać $R_1$, $R_2$, aby zakres wynosił $0\ldots20$ MΩ?

**Rozwiązanie.** $R_{x,\max}=R_{0,\max}R_2/R_1$ → $20\cdot10^{6}=10^{4}\cdot R_2/R_1$ → $R_2/R_1=2000$. Warunek spełnia np. $R_1=10\ \Omega$, $R_2=20$ kΩ.

**Odpowiedź:** para o przekładni $2000$ — w kluczu $R_1=10\ \Omega$, $R_2=20$ kΩ.
:::

::: przyklad Z15. Statystyka serii pomiarów
**Pytanie (typ F).** Cztery pomiary: $10{,}80$; $11{,}10$; $10{,}90$; $11{,}20$ V. Podaj odchylenie standardowe pojedynczego pomiaru i średniej.

**Rozwiązanie.** $\bar{x}=11{,}00$ V; $\sum(x_i-\bar{x})^2=0{,}04+0{,}01+0{,}01+0{,}04=0{,}10$;
$s=\sqrt{0{,}10/3}=0{,}183$ V; $s/\sqrt{4}=0{,}0913\approx0{,}092$ V.

**Odpowiedź:** $s\approx0{,}183$ V, $u(\bar{x})\approx0{,}092$ V.
:::

::: przyklad Z16. Niepewność złożona dla iloczynu: $U=RI$
**Pytanie (typ G).** $R=2$ kΩ, $I=1$ mA; $\Delta_g(R)=0{,}12$ kΩ, $\Delta_g(I)=0{,}08$ mA. Oblicz $u(U)$.

**Rozwiązanie.** $\Delta_g$ przeliczamy na standardowe: $u=\Delta_g/\sqrt3$ (rozkład równomierny):
$$u(R)=\frac{0{,}12\ \text{k}\Omega}{\sqrt3}=0{,}0693\ \text{k}\Omega,\qquad
u(I)=\frac{0{,}08\ \text{mA}}{\sqrt3}=0{,}0462\ \text{mA}$$
Pochodne: $\partial U/\partial R=I=1$ mA, $\partial U/\partial I=R=2$ kΩ, więc wkłady wynoszą
$$1\ \text{mA}\cdot0{,}0693\ \text{k}\Omega=0{,}0693\ \text{V},\qquad
2\ \text{k}\Omega\cdot0{,}0462\ \text{mA}=0{,}0924\ \text{V}$$
$$u(U)=\sqrt{0{,}0693^2+0{,}0924^2}\ \text{V}=0{,}1155\ \text{V}$$
**Odpowiedź:** $0{,}1155$ — dokładnie ta liczba jest w kluczu (25Z_B_1, pyt. G, w woltach; w teście 23Z_B_2, pyt. G ta sama wartość pojawia się z jednostką mV, co jest omyłką arkusza, bo $U=RI=2$ V i niepewność $0{,}1155$ mV byłaby 1700 razy mniejsza niż wynika z danych).
:::

::: przyklad Z17. Niepewność złożona dla modelu z różnicą: $U=E-RI$
**Pytanie (typ G).** $E=10$ V, $R=2$ kΩ, $I=1$ mA, niepewności względne po $1\%$, pomiary nieskorelowane. Oblicz $u(U)$.

**Rozwiązanie.** $u(E)=0{,}1$ V; $u(R)=20\ \Omega$; $u(I)=0{,}01$ mA.
Wkłady: $E$: $0{,}1$ V; $R$: $I\,u(R)=1\ \text{mA}\cdot20\ \Omega=0{,}02$ V; $I$: $R\,u(I)=2\ \text{k}\Omega\cdot0{,}01\ \text{mA}=0{,}02$ V.
$$u(U)=\sqrt{0{,}1^2+0{,}02^2+0{,}02^2}=0{,}1039\ \text{V}\approx0{,}104\ \text{V}$$
**Odpowiedź:** $\approx0{,}104$ V (klucz: 24Z_B_2, pyt. G). Gdyby ktoś zastosował różniczkę zupełną, dostałby $0{,}14$ V — i to jest dystraktor.
:::

::: przyklad Z18. Niepewność złożona dla $P=RI^2$
**Pytanie (typ G).** $R=2$ kΩ, $I=4$ mA, niepewności względne po $5\%$, nieskorelowane. Podaj $u_{\text{rel}}(P)$ i $u(P)$.

**Rozwiązanie.** Model $P=RI^2$: $\delta_P=\sqrt{\delta_R^2+(2\delta_I)^2}=\sqrt{5^2+10^2}=11{,}18\%$.
$P=2\ \text{k}\Omega\cdot(4\ \text{mA})^2=32$ mW → $u(P)=0{,}1118\cdot32=3{,}58\approx3{,}6$ mW.

**Odpowiedź:** $\delta_P\approx11{,}2\%$, $u(P)\approx3{,}6$ mW (klucz: 23Z_B_1, pyt. G).
:::

::: uwaga Dlaczego w kluczach bywają dwie różne odpowiedzi na to samo zadanie
Dla $U=E-RI$, $E=10$ V, $R=1$ kΩ, $I=5$ mA i $1\%$ na składnikach:
* metoda dla nieskorelowanych → $u(U)\approx0{,}12$ V (klucz 25Z_B_2),
* różniczka zupełna → $0{,}1+0{,}05+0{,}05=0{,}2$ V (klucz 20L_B_2).

Obie liczby są „prawidłowe” — zależą od przyjętej metody. Dlatego **czytaj, czy w treści jest słowo „nieskorelowane”**. Jeśli jest — pierwiastki z kwadratów; jeśli pytanie mówi wprost „metodą różniczki zupełnej” — suma modułów.
:::

---

## 11. Formułownik — wszystko w jednym miejscu

### 11.1 Obwody prądu stałego

| Wielkość / twierdzenie | Wzór |
|---|---|
| Prawo Ohma | $u=Ri$, $i=Gu$, $G=1/R$ |
| Moc | $p=ui=Ri^2=u^2/R$ |
| Szeregowo | $R=\sum R_k$ |
| Równolegle | $G=\sum G_k$, $R_1\|R_2=\frac{R_1R_2}{R_1+R_2}$ |
| Dzielnik napięcia | $U_2=E\frac{R_2}{R_1+R_2}$ |
| Dzielnik prądu | $I_1=J\frac{R_2}{R_1+R_2}$ |
| Gwiazda → trójkąt | $R_{AB}=\frac{R_AR_B+R_BR_C+R_CR_A}{R_C}$ |
| Trójkąt → gwiazda | $R_A=\frac{R_{AB}R_{CA}}{\sum R_\Delta}$ |
| Millman (2 węzły) | $U_{AB}=\frac{\sum(G_kE_k+J_k)}{\sum G_k}$ |
| Thévenin | $E_T=U_{\text{jałowe}}$, $R_T=\frac{U_{\text{jałowe}}}{I_{\text{zwarcia}}}$ |
| Norton | $J_N=I_{\text{zwarcia}}=E_T/R_T$ |
| Dopasowanie | $R=R_T$, $P_{\max}=\frac{E_T^2}{4R_T}=\frac{J_N^2R_T}{4}$ |
| Punkt pracy nieliniowego | $R_s=\frac{U}{I}$, $R_d=\frac{\mathrm{d}u}{\mathrm{d}i}$, prosta: $i=\frac{E_T-u}{R_T}$ |
| Tellegen | $\sum u_ki_k=0$ |

### 11.2 Metrologia

| Zagadnienie | Wzór |
|---|---|
| Błąd względny | $\delta=\frac{\Delta x}{x}$ |
| Analog: niepewność graniczna | $\Delta_g=\frac{k}{100}X_z$ |
| Analog: niepewność względna | $\delta_g=\frac{kX_z}{100X_m}$ |
| Cyfrowy | $\Delta_g=a\%X_m+b\%X_z$ |
| Graniczna → standardowa | $u=\Delta_g/\sqrt3$ (rozkład równomierny) |
| Rozszerzona | $U=k\,u_c\approx2u_c$ (95 %) |
| Złożona (nieskorelowane) | $u_c=\sqrt{\sum\left(\frac{\partial f}{\partial x_i}\right)^2u_i^2}$ |
| Złożona: iloczyn/iloraz | $\delta_c=\sqrt{\sum\delta_i^2}$ |
| Złożona: suma/różnica | $u_c=\sqrt{\sum u_i^2}$ |
| Różniczka zupełna | $\Delta y=\sum\left|\frac{\partial f}{\partial x_i}\right|\Delta x_i$ |
| Średnia i odchylenia | $\bar{x}$, $s=\sqrt{\frac{\sum(x_i-\bar x)^2}{n-1}}$, $u(\bar x)=\frac{s}{\sqrt n}$ |
| Metoda techniczna | $R=U/I$; $\delta\approx-R_x/R_V$ (ukł. a), $\delta\approx+R_A/R_x$ (ukł. b) |
| Granica wyboru układu | $R_x=\sqrt{R_AR_V}$ |
| Mostek Wheatstone'a | $R_x=R_0\frac{R_2}{R_1}$, $R_{x,\max}=R_{0,\max}\frac{R_2}{R_1}$ |
| Czas narastania oscyloskopu | $t_r\approx0{,}35/B$ |

### 11.3 Trzydzieści zdań-pułapek, na których traci się punkty

1. Moc **nie** podlega superpozycji — superponuj $u$ i $i$, moc licz na końcu.
2. Superpozycja jest niedozwolona w obwodach nieliniowych (dioda, żarówka, opór nieliniowy).
3. Zasada Tellegena obowiązuje w **każdym** obwodzie skupionym, także nieliniowym.
4. Twierdzenie Thévenina wymaga liniowości, ale **źródła sterowane zostają** przy liczeniu $R_T$.
5. Wyłączając źródło napięciowe robimy **zwarcie**, prądowe — **rozwarcie**.
6. Moc $P_{\max}=E_T^2/(4R_T)$ wydziela się w **obciążeniu**, przy $R=R_T$; sprawność wtedy $50\%$.
7. Kondensator w stanie ustalonym prądu stałego to **rozwarcie**, cewka — **zwarcie**.
8. Dwa idealne źródła napięciowe o różnych SEM **nie mogą** być równolegle.
9. Dwa idealne źródła prądowe o różnych $J$ **nie mogą** być szeregowo („układ sprzeczny”).
10. $R_s=U/I$ to opór **statyczny**; nachylenie stycznej to **dynamiczny** — nie mieszaj.
11. Odcinek pionowy charakterystyki → $R_d=\infty$; poziomy → $R_d=0$.
12. Opór w gałęzi z idealnym źródłem napięciowym **nie wpływa** na napięcie tego węzła.
13. Element szeregowy ze źródłem prądowym **nie zmienia** prądu, ale zmienia napięcie na źródle.
14. Szeregowo: w większym $R$ większa moc. Równolegle: w mniejszym $R$ większa moc.
15. Dzielnik napięcia obowiązuje **bez obciążenia**; z obciążeniem trzeba użyć $R_2\|R_o$.
16. Dwa elementy są równoległe, gdy łączą je **te same dwa węzły** (test, nie geometria rysunku).
17. Mostek Wheatstone'a to metoda **zerowa porównawcza**, nie kompensacyjna.
18. Równanie mostka: $R_1R_x=R_2R_0$ → $R_x=R_0R_2/R_1$ (uwaga na to, co jest w liczniku!).
19. Metoda techniczna $R=U/I$ to pomiar **pośredni złożony (pochodny)**.
20. Klasa przyrządu analogowego odnosi się do **zakresu**, nie do wskazania.
21. $\Delta_g$ analogowego **nie zależy** od wskazania; $\delta_g$ tak (maleje z $X_m$).
22. $\Delta_g$ cyfrowego rośnie **liniowo** z $X_m$ (od $b\%X_z$), a $\delta_g$ maleje hiperbolicznie do $a\%$.
23. Zmniejszenie zakresu zwykle zmniejsza niepewność — ale nie zawsze (człon $a\%X_m$ nie zależy od zakresu).
24. Niepewność podajemy z 1–2 cyframi znaczącymi, a wynik zaokrąglamy do jej rzędu.
25. „Na pewno obejmuje wartość prawdziwą” — **fałsz**; to „z przyjętym prawdopodobieństwem”.
26. Niepewność graniczna ≠ suma niepewności składowych; niepewność złożona zależy od **modelu pomiaru**.
27. Odchylenie standardowe pojedynczego pomiaru ma w mianowniku $n-1$, a średniej — dodatkowo $\sqrt n$.
28. Sprzężenie AC usuwa **składową stałą**; AC LINE to **źródło wyzwalania** (sieć 50 Hz), nie sprzężenie.
29. Oscyloskop analogowy **nie ma** pre-triggeru, zapisu i automatycznych pomiarów; rzadkie anomalie → DPO; najszersze pasmo → sampling (ale tylko sygnały powtarzalne).
30. Więcej bitów ADC to mniejsza kwantyzacja — **nie** większe pasmo i **nie** większy zakres.

---

## 12. Bank pytań z kluczy (2019–2026)

Poniżej wszystkie 252 pytania z 35 kluczy, pogrupowane według testów. Możesz filtrować po słowie kluczowym lub wybrać temat — każdy wiersz pokazuje też, w którym rozdziale kompendium znajdziesz potrzebną teorię.

<!--BANK-->

---

::: ciekawostka O tym kompendium
Treść powstała w całości z 35 kluczy PDF dołączonych do repozytorium (252 pytania, lata 2019–2026) oraz z klasycznej teorii obwodów i miernictwa. Rozdziały, ramki „Jak to jest pytane” i aneks z bankiem pytań są generowane automatycznie z tych samych danych źródłowych, więc liczby pytań i tematy zgadzają się z kluczami. Rysunki obwodów wykonano jako wektorowe SVG w konwencji IEC (prostokąt = rezystor), aby jak najbliżej odpowiadały rysunkom z arkuszy.
:::
