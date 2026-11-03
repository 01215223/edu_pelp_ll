# Obwody po ludzku

Ten dokument to **studenckie, możliwie sugestywne objaśnienie** zestawu
slajdów z pliku **„Wykład - slajdy.pdf”** (PELP1, Instytut Systemów
Elektronicznych PW, dr inż. Ł. Maślikowski). Plik ma 68 stron i składa się
z czterech wykładów:

| Wykład | Temat | Strony w połączonym pliku | Numeracja na slajdach |
|---|---|---:|---:|
| W1 | Modele elementów | 1–17 | 1/17 … 17/17 |
| W2 | Prawa i zasady obwodowe | 18–33 | 1/16 … 16/16 |
| W3 | Elementy zastępcze | 34–51 | 1/18 … 18/18 |
| W4 | Elementy nieliniowe · wzmacniacz operacyjny · moc | 52–68 | 1/17 … 17/17 |

Zasada tego opracowania jest odwrotna niż na slajdach. Slajd podaje
definicję i wzór. Tutaj najpierw pada pytanie **„co ja mam sobie
wyobrazić?”**, potem dopiero wzór, a na końcu zawsze **przykład policzony
do końca na liczbach**. Formalny, dokładniejszy komentarz do tych samych
wykładów jest w katalogu `wyklady/` tego repozytorium; ten tekst ma być
tym, co czyta się **przed** nim — albo zamiast niego, gdy czasu jest mało.

Odsyłacze wyglądają tak: `[plik s. 29 = W2/s. 12]` — pierwsza liczba to
strona połączonego PDF-u, druga to numer widoczny w stopce slajdu.
Kompletny spis slajd → sekcja jest w §6.3.

## Jak czytać, żeby coś z tego zostało

* **Pierwsze czytanie** — tylko tekst zwykły i ramki **„Po ludzku”**.
  Wzory możesz omijać; chodzi o obraz w głowie.
* **Drugie czytanie** — ramki **Przykład**, z kartką. Każdy przykład
  przelicz samodzielnie, zanim spojrzysz na wynik. Liczby są celowo
  „okrągłe”, więc jeśli wychodzi Ci $4{,}17382$, to znaczy, że coś poszło
  nie tak wcześniej — i to jest przydatna informacja.
* **Przed kolokwium** — §5 (wybór metody) i §6 (ściąga z pułapkami).

::: ciekawostka Jedno zdanie, które streszcza całe cztery wykłady
**Obwód to układ równań.** Każdy element mówi jedną prawdę o swoim
napięciu i prądzie („ja jestem oporem: $u = Ri$”, „ja jestem źródłem:
$u = 9$ V i koniec dyskusji”), a prawa Kirchhoffa mówią, jak te prawdy
muszą zgadzać się między sąsiadami. Wszystkie „metody” z wykładów
(superpozycja, Thévenin, dzielniki…) to tylko sprytne sposoby, żeby tych
równań było mniej albo żeby były prostsze. Jeśli zapamiętasz tylko to —
i tak jesteś do przodu.
:::

## 0. Zanim zaczniesz: jeden obraz na cały przedmiot

### 0.1 Analogia wodna — dobra na start, zła jako religia

Najsugestywniejszy obraz prądu wymyślono dawno: **obwód elektryczny działa
jak zamknięta instalacja wodna**.

::: figura figury/analogia.svg | Analogia wodna. Pompa pcha wodę przez zwężkę, źródło „pcha” ładunki przez opór. Przepływ jest wszędzie w pętli taki sam — dokładnie jak prąd w pojedynczym oczku.
:::

| Woda | Prąd elektryczny | Oznaczenie |
|---|---|---|
| pompa (daje ciśnienie) | źródło napięciowe | $E$ |
| ciśnienie / różnica wysokości | napięcie | $u$ [V] |
| przepływ (litry na sekundę) | natężenie prądu | $i$ [A] |
| zwężka, odcinek cienkiej rurki | opór | $R$ [Ω] |
| zbiornik z elastyczną membraną | kondensator | $C$ |
| ciężkie koło łopatkowe (bezwładność) | cewka | $L$ |

Trzy rzeczy, które ta analogia oddaje **świetnie**:

1. **Prąd się nie „zużywa”.** Ile wody wypływa z pompy, tyle do niej wraca.
   Żarówka nie „spala prądu” — prąd za żarówką jest taki sam jak przed nią.
   Zużywa się **energia**, nie prąd. To podstawa I prawa Kirchhoffa.
2. **Napięcie jest różnicą.** Nie istnieje „napięcie w punkcie” — jak nie
   istnieje „wysokość jednego końca deski”. Mówimy o różnicy ciśnień,
   różnicy wysokości, różnicy potencjałów między dwoma punktami.
3. **Opór to zwężka.** Ta sama różnica ciśnień na szerszej rurce daje
   większy przepływ niż na węższej — dokładnie tak działa $i = u/R$.

::: pulapka Gdzie analogia wodna kłamie
Woda wycieknie z przeciętej rury; ładunek nie „wylewa się” z przeciętego
przewodu. Woda w rurze porusza się mniej więcej tak szybko, jak sygnał
o zmianie ciśnienia; elektron w drucie wędruje ślamazarnie (rzędu
milimetra na sekundę), a „wiadomość”, że obwód zamknięto, biegnie przez
przewodnik prawie z prędkością światła. Wreszcie: w wodzie nie ma
odpowiednika pola magnetycznego. Używaj analogii do prądu, napięcia
i oporu — i odstaw ją, gdy zaczyna przeszkadzać.
:::

### 0.2 Potencjał to wysokość terenu, masa to „poziom zero”

Każdy węzeł obwodu ma **potencjał** — wyobraź go sobie jako wysokość
w terenie. Napięcie między dwoma węzłami to różnica wysokości. Jednemu
węzłowi wolno **umownie** przypisać 0 V: to *masa* (ziemia), tak jak na
mapie „0 m n.p.m.”. Zmiana wyboru masy zmienia wszystkie potencjały,
ale **żadnego napięcia i prądu** — tak jak mierzenie wzrostu od podłogi
parteru albo od poziomu morza nie zmienia różnicy wzrostu dwóch osób.

Dzięki temu zamiast za każdym razem mówić o napięciu między dwoma
węzłami, najczęściej pytamy po prostu: **jaki jest potencjał węzła A?**
Na rysunku z §0.3 masa jest węzłem B, więc potencjał A to po prostu
napięcie na środkowym oporze.

### 0.3 Obwód, który przejdzie przez cały dokument

Większość metod pokażę na **jednym** obwodzie (nazwijmy go obwodem
z dwiema bateriami), i powiem wynik z góry — po to, żeby potem było
widać, że każda metoda daje **ten sam wynik**, bo musi.

::: figura figury/hero.svg | Obwód z dwiema bateriami: bateria 9 V z lewej i 6 V z prawej karmią — przez własne opory 2 Ω — wspólny węzeł A, z którego prąd wraca oporem 2 Ω do masy B. Strzałki czerwone to *założone* kierunki prądów.
:::

Obraz, który warto mieć: dwie pompy o różnym ciśnieniu pchają wodę do
wspólnej rury; część wody uchodzi rurą środkową. Silniejsza pompa
(9 V) wniesie więcej; słabsza (6 V) wniesie mniej, ale wcale nie
„zostanie cofnięta” — jej prąd będzie mały, bo węzeł A ustali się
*poniżej* 6 V.

Odpowiedź (udowodnimy ją w §2.5, potem jeszcze trzy razy):

$$
U_A = 5\ \mathrm{V},\qquad I_1 = 2\ \mathrm{A},\qquad I_2 = 2{,}5\ \mathrm{A},\qquad I_3 = 0{,}5\ \mathrm{A}
$$

Zauważ od razu rymowankę węzła A: dopływa $2 + 0{,}5$ ampera, odpływa
$2{,}5$ ampera. Zgoda prądów to nie magia — to test, który powinieneś
robić po każdym zadaniu.

::: zapamietaj Po ludzku — trzy pytania przed każdym zadaniem
1. **Czy w obwodzie jest coś nieliniowego** (dioda, opis graficzny,
   „opór nieliniowy”)? Jeśli nie — masz do dyspozycji wszystkie skróty.
2. **Czy szukam wszystkiego, czy tylko jednej liczby?** Jedna liczba —
   szukaj skrótu (dzielnik, Thévenin). Wszystko — pisz Kirchhoffa.
3. **Czy chodzi o moc?** Jeśli tak, najpierw policz prądy i napięcia;
   supermocy superpozycji tu nie ma (§2.10 pokazuje, dlaczego).
:::

## 1. Wykład 1 — z czego składa się świat obwodów

`[plik s. 1–17]`

### 1.1 Od równań Maxwella do klocków z kabelkami

`[plik s. 3–4 = W1/s. 3–4]` Wykład pokazuje równania Maxwella, po czym
mówi: „są dość skomplikowane” — i to jest jeden z najważniejszych
momentów przedmiotu, bo cała teoria obwodów opiera się na świadomym
uproszczeniu.

::: def Po ludzku — element skupiony
Prawdziwy rezystor trochę się grzeje, trochę jest niezamierzoną cewką,
trochę kondensatorem. Teoria obwodów każe nam udawać, że każda
właściwość mieszka osobno w swoim **klocku z wyprowadzeniami**.
O klocku wiemy tylko jedno: **jaką zależność między napięciem a prądem na
jego zaciskach deklaruje jego równanie**. Co kryje się w jego środku, nie ma
znaczenia. Obwód to wtedy rysunek: klocki i idealne (zerowy opór!) przewody.
:::

Po co takie udawanie? Bo pole elektromagnetyczne w „normalnych”
układach zachowuje się *jakby* zmiany były natychmiastowe w całej
płycie — pole jest **quasi-stacjonarne**. Test jest prosty: długość fali
przy 50 Hz to 6000 km, więc dla każdego urządzenia przy gniazdku —
natychmiastowość to świetne przybliżenie. Przy Wi-Fi 2,4 GHz długość
fali to kilkanaście centymetrów i ta sama płytka staje się „długa” —
wtedy potrzebna jest linia i stałe rozłożone, a klocki przestają
wystarczać. Cały PELP1 żyje w świecie, gdzie udawanie wolno.

### 1.2 Dwie wielkości i jedna umowa o strzałkach

`[plik s. 5–6 = W1/s. 5–6]` Mamy tylko cztery litery, a praktycznie dwie:

* $i$ **[A]** — prąd, czyli „ile ładunku przepływa na sekundę”,
* $u$ **[V]** — napięcie, czyli różnica potencjałów („wysokości”),
* $q$ **[C]** — ładunek (dla kondensatora), $\psi$ **[Wb]** — strumień
  skojarzony (dla cewki); wrócą na jeden slajd.

Mała litera ($u$) znaczy „wartość, która *może* zmieniać się w czasie”;
wielka ($U$, $I$) znaczy „w tym problemie stała”. To czysta kurtuazja
zapisu, a nie dwa rodzaje fizyki.

::: zapamietaj Po ludzku — strzałka to zakład, minus to przegrana, z której nic nie wynika
Strzałka napięcia wskazuje punkt, który **zakładasz**, że ma wyższy
potencjał. Strzałka prądu wskazuje kierunek, w którym **zakładasz**, że
płyną umowne ładunki dodatnie. Możesz te kierunki wybrać dowolnie.
Jeśli wyliczona wartość wyjdzie ujemna, to nie błąd — to obwód mówi
„płynę odwrotnie, niż narysowałeś”. **Błędem jest zmienianie strzałki
w połowie zadania albo używanie wzoru dla innej pary strzałek.**
:::

::: przyklad Przykład 1.1 — minus, który mówi prawdę
Na oporze $R = 5\ \Omega$ narysowano strzałki prądu i napięcia **w tę
samą stronę** (zgodnie), a prąd wynosi $i = 2\ \mathrm{A}$.

Dla strzałek zgodnych wzór Ohma ma minus (zobacz §1.5 i §2.4):

$$
u = -Ri = -5 \cdot 2 = -10\ \mathrm{V}
$$

Tłumaczenie: punkt, w który celuje strzałka napięcia, jest *naprawdę*
o 10 V **niższy**. Moc *pobierana* (dla tej pary strzałek $p = -ui$):

$$
p = -ui = -(-10)\cdot 2 = 20\ \mathrm{W} > 0
$$

Opór grzeje się mocą 20 W — zgodnie z fizyką. Test na całe życie:
**moc pobierana przez opór musi wyjść dodatnia**. Jeśli wyszła ujemna,
źle zestawiłeś znaki, a nie odkryłeś perpetuum mobile.
:::

### 1.3 Cztery pytania, które można zadać każdemu elementowi

`[plik s. 7–8 = W1/s. 7–8]` Klasyfikacja ze slajdów brzmi urzędowo, ale
to tak naprawdę cztery praktyczne pytania:

| Pytanie | Odpowiedzi | Po co mi to wiedzieć |
|---|---|---|
| Ile ma wyprowadzeń? | 2 — **dwójnik**; 4 — czwórnik | dwójnik opisuje jedna para $u, i$ |
| Czy jego parametry zmieniają się w czasie? | nie — **stacjonarny** | $R$, $C$, $L$ mogę traktować jak liczby |
| Czy równanie jest liniowe? | tak / **nieliniowy** | metody-skróty działają tylko w świecie liniowym |
| Czy potrafi oddać energię z siebie? | tak — **aktywny**; nie — **pasywny** | rezystor sam nie może generować energii — test wyniku |

Każdemu typowi odpowiada *typ* równania: elementy rezystancyjne wiążą
$u$ z $i$ w tej samej chwili (krzywa na wykresie $u$–$i$), pojemnościowe
wiążą $u$ z $q$, indukcyjne — $i$ z $\psi$. Na kolokwium z W1–W4
pracujemy niemal wyłącznie na **elementach rezystancyjnych
przy prądzie stałym**: jego cała osobowość to jedna krzywa.

::: pulapka „Bezźródłowy” to nie to samo co „pasywny”
Element **bezźródłowy** to taki, który *może* spoczywać w punkcie
$u = 0$, $i = 0$ (krzywa przechodzi przez początek układu) — nawet jeśli
w środku ma źródła *sterowane*. Taki dwójnik może mimo to oddawać moc
w innych punktach pracy (czyli być aktywny). Zdanie „w środku są tylko
źródła sterowane, więc dwójnik jest bezźródłowy” jest prawdziwe;
wniosek „więc jest pasywny jak rezystor” — już nie (zobacz §3.4).
:::

### 1.4 Źródła idealne, czyli dwóch uparciuchów

`[plik s. 9–10 = W1/s. 9–10]`

::: def Po ludzku — idealne źródło napięciowe
Uparty strażnik napięcia. Mówi: „między moimi zaciskami będzie **dokładnie**
$E$ woltów. Jaki prąd przeze mnie popłynie — nie obchodzi mnie, dostosuję
się”. Charakterystyka $u = E$ to **pionowa linia** na wykresie $u$–$i$:
napięcie stałe, prąd dowolny (rysunek niżej).
:::

::: def Po ludzku — idealne źródło prądowe
Bliźniak o odwrotnej fiksacji: „przeze mnie popłynie **dokładnie** $J$
amperów. Jakie napięcie pojawi się na moich zaciskach — dostosuję się”.
Na wykresie $u$–$i$ to **pozioma linia** $i = J$.
:::

Konwencja: dla źródeł prąd i napięcie strzałkuje się **zgodnie**,
bo wtedy iloczyn $E \cdot i$ (lub $J \cdot u$) jest mocą *oddawaną*
przez źródło do obwodu — dodatnią wtedy, gdy źródło faktycznie
„popracowuje”.

::: pulapka Dwaj uparciuchy nie dogadają się nigdy
* Nie wolno **zwierać** idealnego źródła napięciowego ani łączyć
  równolegle dwóch o różnych wartościach: zwarcie każe widzieć $u = 0$,
  źródło każe $u = E$ — sprzeczność (albo nieskończony prąd).
* Nie wolno **rozwierać** idealnego źródła prądowego ani łączyć
  szeregowo dwóch o różnych wartościach: rozwarcie każe $i = 0$,
  źródło każe $i = J$ — znowu sprzeczność.

Gdy w zadaniu wychodzi Ci taka konfiguracja, znaczy to zwykle, że
poprzedni krok rachunków poszedł w las.
:::

### 1.5 Opór, prawo Ohma oraz dwa skrajne przypadki

`[plik s. 11–13 = W1/s. 11–13]` Opór to klocek, który zamienia energię
elektryczną w ciepło. Jego charakterystyka zawsze przechodzi przez
zero (bez napięcia nie ma prądu) i leży w ćwiartkach, w których
pobrana moc jest dodatnia. **Opór liniowy** ma charakterystykę prostą —
to właśnie prawo Ohma:

$$
u = Ri, \qquad i = Gu, \qquad G = \frac{1}{R}
$$

gdzie $R$ [Ω] to opór (rezystancja), a $G$ [S] — przewodność
(konduktancja). Kluczowa uwaga z gwiazdką: **ten zapis obowiązuje, gdy
strzałka napięcia jest przeciwna do strzałki prądu** (napięcie „mierzy
spadek” w stronę, w którą prąd płynie, a strzałka napięcia celuje
w wyższy potencjał — czyli wstecz). Dla strzałek zgodnych wpisz minus:
$u = -Ri$ (przykład 1.1).

Dwa skrajne opory wystarczą na połowę zadań:

* **zwarcie**: $R \to 0$, zawsze $u = 0$, a prąd — „jaki obwód zechce”.
  Innymi słowy: to samo co idealne źródło napięciowe o $E = 0$.
* **rozwarcie**: $R \to \infty$, zawsze $i = 0$, a napięcie — „jakie
  wyjdzie”. Czyli: idealne źródło prądowe o $J = 0$.

Zapamiętaj też „sztuczki z pamięcią przeciwną”: wyłączone źródło
napięciowe *staje się zwarciem* ($E \to 0$), a wyłączone prądowe —
**rozwarciem** ($J \to 0$). Ta zamiana przewinie się przez
superpozycję (§2.10) i Thévenina (§3.6).

::: figura figury/charakterystyki.svg | Cztery charaktery na jednym obrazku. Zwróć uwagę, że tylko opór (i skłonność źródła rzeczywistego) łączą napięcie z prądem „uczciwą” zależnością — uparciuchy programują jedną wielkość i ignorują drugą.
:::

### 1.6 Kondensator i cewka: dwa rodzaje pamięci

`[plik s. 14 = W1/s. 14]` Te dwa elementy pojawiają się na jednym slajdzie,
głównie dla porządku — w zadaniach W1–W4 grają role epizodyczne, i
zawsze przez tę samą furtkę: **jak wyglądają dla prądu stałego**.

* **Kondensator** ($i = C\, du/dt$, energia $\frac{1}{2}CU^2$): zbiornik
  z membraną — przechowuje ładunek i „nie przepuszcza” ustalonego prądu.
  Dla prądu stałego w stanie ustalonym jest **rozwarciem**.
* **Cewka** ($u = L\, di/dt$, energia $\frac{1}{2}LI^2$): koło zamachowe
  dla prądu — przechowuje energię w polu magnetycznym i w stanie
  ustalonym nie stawia napięciu oporu. Dla prądu stałego jest **zwarciem**.

::: przyklad Przykład 1.2 — ile energii „siedzi” w elemencie
Kondensator $C = 100\ \mu\mathrm{F}$ naładowano do napięcia $U = 10\ \mathrm{V}$:

$$
w_C = \frac{1}{2} C U^2 = \frac{1}{2} \cdot 100 \cdot 10^{-6} \cdot 100 = 5 \cdot 10^{-3}\ \mathrm{J} = 5\ \mathrm{mJ}
$$

Cewka $L = 50\ \mathrm{mH}$, przez którą płynie ustalony prąd $I = 2\ \mathrm{A}$:

$$
w_L = \frac{1}{2} L I^2 = \frac{1}{2} \cdot 0{,}05 \cdot 4 = 0{,}1\ \mathrm{J}
$$

To właśnie ta energia sprawia, że element *pasywny* potrafi przez chwilę
**oddać** moc: oddaje tylko to, co wcześniej zgromadził (jak naładowany
zbiornik albo rozkręcone koło).
:::

### 1.7 Źródło rzeczywiste, czyli bateria, która się męczy

`[plik s. 15–16 = W1/s. 15–16]` Prawdziwa bateria nie jest uparciuchem:
im większy prąd z niej czerpiesz, tym mniejsze napięcie daje.
Model mówi dokładnie to:

$$
u = E - R_w i \qquad\qquad i = J - G_w u
$$

czyli modelowo: idealne źródło napięciowe i **szeregowy** opór $R_w$
(a w wersji prądowej: idealne źródło prądowe i **równoległa**
przewodność $G_w$). Opór wewnętrzny
jest jak cienki wężyk między pompą a kranem — przy dużym przepływie
„zjada” ciśnienie.

::: przyklad Przykład 1.3 — bateria 9 V z oporem wewnętrznym 1 Ω
Baterię $E = 9\ \mathrm{V}$, $R_w = 1\ \Omega$ obciążamy oporem
$R_0 = 8\ \Omega$. Prąd w oczku: $I = 9/(1 + 8) = 1\ \mathrm{A}$.
Napięcie na zaciskach (czyli na obciążeniu): $U = R_0 I = 8\ \mathrm{V}$ —
jeden wolt „zginął” w baterii. Moc w obciążeniu: $P = UI = 8\ \mathrm{W}$;
w ciepło w baterii idzie $R_w I^2 = 1\ \mathrm{W}$; źródło idealne w
środku oddaje $EI = 9\ \mathrm{W}$. Bilans: $9 = 8 + 1$ — znowu się zgadza.

Obciąż tę samą baterię oporem $1\ \Omega$: $I = 4{,}5\ \mathrm{A}$, napięcie na
zaciskach siada do $4{,}5\ \mathrm{V}$ — połowy. Taka jest natura $R_w$.
Ten model wróci jako kulminacja dwóch rozdziałów: obwód Thévenina
(§3.6) *jest* źródłem rzeczywistym.
:::

### 1.8 Źródła sterowane: słuchają tu, działają tam

`[plik s. 17 = W1/s. 17]` Ostatni slajd W1 wprowadza element, który nie ma
dwóch, lecz **cztery** zaciski: jedną parą „nasłuchuje” (mierzy napięcie
lub prąd gdzieś w obwodzie), a drugą parą zachowuje się jak źródło
idealne, którego wartość jest proporcjonalna do tego nasłuchu.
To model tranzystora i wzmacniacza w teorii obwodów.

| Sterujące → wymuszane | Równanie wyjścia | Jednostka stałej | Wejście wygląda jak |
|---|---|---|---|
| napięcie → napięcie | $u_2 = k u_1$ | V/V (bez wymiaru) | rozwarcie ($i_1 = 0$) |
| napięcie → prąd | $i_2 = g u_1$ | A/V = S | rozwarcie ($i_1 = 0$) |
| prąd → napięcie | $u_2 = r i_1$ | V/A = Ω | zwarcie ($u_1 = 0$) |
| prąd → prąd | $i_2 = \beta i_1$ | A/A (bez wymiaru) | zwarcie ($u_1 = 0$) |

::: metoda Rytuał jednostek, który ratuje zadania
Zanim wstawisz współczynnik sterowania do równania, sprawdź, czy **jednostki
się domykają**: $r$ ma omy, więc $r i_1$ daje wolty — pasuje do źródła
napięciowego; $g$ ma siemensy, więc $g u_1$ daje ampery. Jeśli jednostka
wyniku nie pasuje do rodzaju źródła na rysunku, pomyliłeś typ źródła
albo wielkość sterującą. Dwie sekundy, a wyłapuje połowę pomyłek.
:::

Wejście sterujące nie pobiera ani prądu (gdy słucha napięcia), ani nie
bierze napięcia (gdy słucha prądu) — to idealizacja „samego nasłuchu”.
Kluczowa zasada, która przewinie się wszędzie: źródła sterowanego
**nigdy się nie wyłącza** (§2.10, §3.6) i nie wolno go „tracić” przy
przekształceniach obwódu (§3.1).

::: przyklad Przykład 1.4 — dwa sterowania na jednej liczbie
Gdzieś w obwodzie występuje napięcie $u_1 = 2\ \mathrm{V}$.
Źródło napięciowe sterowane napięciem o $k = 3$ wystawi więc
$u_2 = k u_1 = 6\ \mathrm{V}$ — niezależnie od tego, jaki prąd zechce przez nie
popłynąć (to nadal uparciuch napięciowy!). Źródło prądowe sterowane tym
samym napięciem o $g = 0{,}5\ \mathrm{S}$ wystawi $i_2 = g u_1 = 1\ \mathrm{A}$ —
niezależnie od napięcia na jego zaciskach. Zmieni się $u_1$ — zmienią
się oba, posłusznie i natychmiast.
:::

::: klucz Sprawdź się W1 (30 sekund na pytanie)
1. Strzałka napięcia na elemencie pokazuje punkt, który *zakładam*, że ma
   niższy potencjał. — **fałsz**, strzałka napięcia celuje w wyższy.
2. Zwarcie to graniczny przypadek źródła prądowego $J = 0$. — **fałsz**,
   to $E = 0$; źródło $J = 0$ to rozwarcie.
3. Cewka w stanie ustalonym prądu stałego jest zwarciem. — **prawda**.
4. Idealne źródło prądowe może mieć napięcie 0 V i nadal wymuszać prąd.
   — **prawda** (i wtedy oddaje moc zerową).
:::

## 2. Wykład 2 — zasady ruchu w obwodzie

`[plik s. 18–33]`

### 2.1 Słownik rysunku: gałąź, węzeł, oczko

`[plik s. 20 = W2/s. 3]` Schemat da się czytać jak mapę.

* **Gałąź** — jeden dwójnik (lub wrota) wraz z jego dwiema końcówkami;
  płynie przez niego *jeden* prąd.
* **Węzeł** — miejsce, gdzie styka się kilka gałęzi; **cały węzeł ma jeden
  potencjał**, łącznie z idealnymi przewodami, które go tworzą. Uwaga:
  węzeł „rozlewa się” po przewodach i po zwarciu — dwa rogi rysunku
  połączone samym przewodem to *ten sam* węzeł.
* **Obwód (droga zamknięta)** — spacer po gałęziach wracający do
  startu; **oczko** — najmniejszy taki spacer, „okienko” schematu,
  w środku którego nie ma żadnej gałęzi.

W obwodzie z dwiema bateriami (§0.3) węzły są tylko dwa: A (cała górna
szyna) i B (cała dolna szyna, masa). Elementów jest pięć, ale tylko trzy prądy
między szynami trzeba oznaczyć osobno; oczek są **dwa**.

### 2.2 I prawo Kirchhoffa: węzeł jak rondo

`[plik s. 21 = W2/s. 4]`

::: def Po ludzku — prawo prądów (PPK)
Prąd nie może gromadzić się ani znikać w węźle. **Ile wpływie, tyle
wypłynie — w każdej chwili.** Węzeł jest jak rondo bez parkingów:
żaden samochód nie kończy na nim podróży.
:::

$$
\sum i = 0
$$

gdzie prądy wpływające zapisujemy ze znakiem $+$, wypływające z $-$ (albo
odwrotnie — byle konsekwentnie). Prawo działa dla *dowolnego* zamkniętego
obszaru, nie tylko dla pojedynczego węzła.

::: przyklad Przykład 2.1 — brakujący prąd w węźle
Do węzła wpływają 2 A i 3 A, wypływa jedną gałęzią 1 A. Ile wypływa
czwartą? Z PPK: $2 + 3 - 1 - I = 0$, czyli $I = 4\ \mathrm{A}$ wypływające.
Gdyby rachunkowo wyszło $I = -4$, oznaczałoby to wpływ 4 A. Żadnej
rewolucji — strzałka była zakładem (§0.3).
:::

### 2.3 II prawo Kirchhoffa: spacer, po którym wracasz do tej samej wysokości

`[plik s. 22 = W2/s. 5]`

::: def Po ludzku — prawo napięć (NPK)
Idziesz zamkniętą trasą po obwodzie i sumujesz napięcia (z $+$, gdy
strzałka napięcia zgadza się z kierunkiem twojego marszu, z $-$, gdy
jest przeciwna). Po powrocie do startu musiała wyjść **dokładnie zerowa
suma** — bo wróciłeś do tej samej „wysokości”. Bateria to winda
podnosząca cię o $E$; opory to schody, którymi schodzisz o $RI$.
:::

$$
\sum u = 0
$$

::: przyklad Przykład 2.2 — kontrola oczek obwodu z dwiema bateriami
Znamy już wynik z §0.3: $U_A = 5$ V, $I_1 = 2$ A, $I_2 = 2{,}5$ A,
$I_3 = 0{,}5$ A. Sprawdźmy go prawem napięć:

* oczko lewe: winda 9 V ma dać spadki $R_1 I_1 + R_2 I_2 = 2\cdot2 + 2\cdot2{,}5
  = 4 + 5 = 9\ \mathrm{V}$ — zgadza się;
* oczko prawe: winda 6 V: $R_3 I_3 + R_2 I_2 = 1 + 5 = 6\ \mathrm{V}$ — zgadza się;
* oczko zewnętrzne: $-9 + R_1 I_1 - R_3 I_3 + 6 = -9 + 4 - 1 + 6 = 0$.

Dwie baterie „ciągną” w tym samym oczku w przeciwne strony; różnica 3 V
rozkłada się jako 4 V i 1 V — ze znakami wszystko się bilansuje.
Taką kontrolę rób na końcu **każdego** zadania: kosztuje 15 sekund.
:::

### 2.4 Znaki biorą się tylko ze strzałek (jedyna tabelka, którą trzeba znać)

`[plik s. 23 = W2/s. 6]` Cała „trudność znaków” w teorii obwodów mieści się
w dwóch wierszach:

| Element | Równanie zapisane dla strzałek… | Konwencja ze slajdów to |
|---|---|---|
| opór (bierny) | **przeciwnych**: $u = Ri$, moc pobierana $p = ui$ | dla zgodnych: $u = -Ri$, $p = -ui$ |
| źródło (czynny) | **zgodnych**: $u = E$ albo $i = J$, moc oddawana $p_o = Ei$ lub $Ju$ | dla przeciwnych: minus |

Skąd logika? Prąd w oporze płynie od wyższego potencjału do niższego,
czyli *przeciwnie* do strzałki napięcia, która celuje w punkt wyższy;
stąd przy naturalnym przepływie ich strzałki są przeciwne. Źródło
wypycha prąd ku swemu wyższemu potencjałowi, więc dla niego naturalna
jest para strzałek zgodnych.

### 2.5 Przepis na cały obwód (Kirchhoff bez skrótów) — i pierwszy rachunek

`[plik s. 24–26 = W2/s. 7–9]` Algorytm ze slajdów:

1. zastrzałkuj prądy i napięcia (dowolnie, ale na zawsze);
2. wpisz $N - 1$ równań prądowych ($N$ = liczba węzłów; ostatnie równanie
   węzła byłoby konsekwencją pozostałych, więc się nie liczy);
3. wpisz $M$ równań napięciowych ($M$ = liczba oczek);
4. dopisz równania elementów i rozwiąż.

Prawie zawsze szybszy odpowiednik tego przepisu to **jedno równanie na
potencjały węzłów**: dla węzła o potencjale $V$ prąd, który wypływa do
sąsiada przez opór, to $(V - V_2)/R$ ($V_2$ — potencjał sąsiada),
i dla każdego węzła zapisujemy jedno PPK.
Obwód z dwiema bateriami ma właściwie *jeden* nieznany potencjał, $U_A$,
więc idzie to tak:

::: przyklad Przykład 2.3 — obwód z dwiema bateriami liczony „na serio”
Strzałkowania jak na rysunku z §0.3: $I_1$ i $I_3$ **dopływają** do A w
górę swoich gałęzi, $I_2$ **odpływa** w dół. Wyrażamy każdy prąd przez
$U_A$ (masa = B):

* lewa gałąź: od B jedziemy windą 9 V i tracimy $R_1 I_1$ na oporze,
  więc $U_A = 9 - 2 I_1$, czyli $I_1 = \dfrac{9 - U_A}{2}$;
* gałąź środkowa to czysty opór: $I_2 = \dfrac{U_A}{2}$;
* prawa: $I_3 = \dfrac{6 - U_A}{2}$.

Prawo prądów dla węzła A („co dopłynęło, odpłynęło”): $I_1 + I_3 = I_2$.

$$
\frac{9 - U_A}{2} + \frac{6 - U_A}{2} = \frac{U_A}{2}
\quad\Longrightarrow\quad 15 - 2U_A = U_A
\quad\Longrightarrow\quad U_A = 5\ \mathrm{V}
$$

Prądy: $I_1 = (9-5)/2 = 2\ \mathrm{A}$, $I_2 = 5/2 = 2{,}5\ \mathrm{A}$,
$I_3 = (6-5)/2 = 0{,}5\ \mathrm{A}$ — wszystkie dodatnie, więc trafiliśmy
ze strzałkami; PPK: $2 + 0{,}5 = 2{,}5$ ✔.

Zauważ komentarz fizyczny: słabsza bateria dalej dostarcza prąd
($0{,}5$ A *do przodu*), bo węzeł ustalił się na 5 V — niżej niż jej
6 V. Gdyby $U_A$ przekroczyło 6 V, ta bateria byłaby ładowana.
:::

::: uwaga Po co w tym przepisie rezygnuje się z części równań
Slajd `[plik s. 26 = W2/s. 9]` mówi: gdy przy węźle stoi **idealne źródło
napięciowe**, jego prąd jest niewiadomą, o którą nikt zwykle nie pyta —
więc równanie prądowe takiego węzła można pominąć (sąsiednie węzły
„zlewa się” w tzw. superwęzeł). Dwojaki obraz: gdy dwa oczka dzielą
**idealne źródło prądowe**, jego napięcie jest niewygodną niewiadomą —
pisze się jedno równanie „superoczka” omijające to źródło. Zasada:
**nie jesteś pewien — pisz wszystko; ochota na skróty przyjdzie sama**.
:::

### 2.6 Szeregowo i równolegle: test nie polega na wyglądzie

`[plik s. 27–28 = W2/s. 10–11]`

::: zapamietaj Po ludzku — jeden test zamiast definicji
* **Szeregowo** ⇔ przez oba elementy płynie *ten sam* prąd. Wyznacznik:
  w węźle między nimi nie siedzi **żaden inny** element (woda nie ma
  dokąd uciec).
* **Równolegle** ⇔ na obu panuje *to samo* napięcie. Wyznacznik: oba
  elementy łączą **tę samą parę** węzłów (mają wspólne końce).

„Obok siebie na rysunku” nie znaczy równolegle; „jeden pod drugim” nie
znaczy szeregowo. Zapytaj o prąd i o napięcie — wygląd to sprawa
rysownika.
:::

Są też połączenia, które nie są ani jednym, ani drugim — trójkąt (Δ) i
gwiazda (Y) z trzech dwójników (§3.3) oraz mostek. Rozpoznanie tego
faktu w pierwszych 5 sekundach zadania oszczędza 5 minut zafiksowania
się na złym wzorze.

### 2.7 Dzielniki: najczęstszy skrót na kolokwium

`[plik s. 29–30 = W2/s. 12–13]`

::: figura figury/dzielniki.svg | Dwie „skale”: w szeregu napięcie dzieli się jak opory, w równoległości prąd dzieli się jak przewodności. W obu wzorach na dole jest *suma*, różnica jest w liczniku.
:::

::: wzor Dzielniki (formy, w których najtrudniej się pomylić)
Napięciowy (dwa opory szeregowo, napięcie całkowite $U$; pytasz o napięcie
na oporze dolnym $R_2$): $U_2 = U \cdot \dfrac{R_2}{R_1 + R_2}$.

Prądowy (dwa opory równolegle, prąd całkowity $I$; pytasz o prąd gałęzi
$R_1$): $I_1 = I \cdot \dfrac{G_1}{G_1 + G_2} = I \cdot \dfrac{R_2}{R_1 + R_2}$.
:::

::: zapamietaj Hasło, które nosi się na kolokwium
*Dzielnik napięcia pyta: „na którym oporze siedzisz?” — i stawia ten opór
na górze ułamka. Dzielnik prądu robi odwrotnie, bo prąd idzie chętniej
tam, gdzie opór mniejszy: na górze ląduje opór **tej drugiej** gałęzi.*
Jeśli wynik prądowego wyszedł większy dla większego oporu, zamieniłeś
licznik.
:::

::: przyklad Przykład 2.4 — oba dzielniki w minutę
**Napięciowy:** $U = 12\ \mathrm{V}$, $R_1 = 3\ \mathrm{k\Omega}$ (górny),
$R_2 = 9\ \mathrm{k\Omega}$ (dolny). $U_2 = 12 \cdot 9/12 = 9\ \mathrm{V}$ — a przy
okazji prąd szeregu to $12\ \mathrm{V} / 12\ \mathrm{k\Omega} = 1\ \mathrm{mA}$.

**Prądowy:** źródło wciska $I = 6\ \mathrm{A}$ w parę $R_1 = 2\ \Omega$,
$R_2 = 4\ \Omega$. $I_1 = 6 \cdot 4/6 = 4\ \mathrm{A}$ — większa część idzie
mniejszym oporem, $I_2 = 2\ \mathrm{A}$. Kontrola: wspólne napięcie
$U = I_1 R_1 = 8\ \mathrm{V} = I_2 R_2$ ✔.
:::

::: pulapka Dzielnik umiera, gdy go obciążysz
Wzór dzielnika napięciowego opisuje wyjście **nieobciążone**. Podepnij do
przykładu 2.4 odbiornik $R_L = 9\ \mathrm{k\Omega}$ równolegle do $R_2$:
dolny opór zastępczy to $9 \parallel 9 = 4{,}5\ \mathrm{k\Omega}$, i napięcie
spada do $12 \cdot 4{,}5/(3 + 4{,}5) = 7{,}2\ \mathrm{V}$, a nie zostaje 9 V.
Każde „tu podajemy coś dalej” w treści zadania usuwa darmowość dzielnika.
:::

### 2.8 Zasada kompensacji: gałąź da się podmienić baterią o tym samym napięciu

`[plik s. 31 = W2/s. 14]`

::: def Po ludzku — kompensacja
W gotowym, rozwiązanym obwodzie gałąź, na której panuje napięcie $u$,
można zastąpić idealnym źródłem napięciowym $E = u$ (albo — idąc od
strony prądu — gałąź z prądem $i$ źródłem prądowym $J = i$), a **żaden
prąd i żadne napięcie w reszcie obwodu się nie ruszy**. Reszta świata
widzi gałąź tylko przez jej $u$ oraz $i$; jeśli klon daje to samo,
świat się nie orientuje.
:::

Z tego wynikają dwie darmowe operacje:

* **punkty o równym potencjale można zewrzeć** (zwarcie to $E = 0$
  o napięciu dokładnie równym ich różnicy potencjałów: 0);
* **gałąź bezprądową można rozewrzeć** (rozwarcie to $J = 0$ — tyle, ile
  już tam pływa).

Obie operacje zobaczysz żywcem w §3.3 (mostek zrównoważony) i §4.5.

::: przyklad Przykład 2.5 — środek obwodu-dwóch-baterii jako bateria
W punkcie pracy z §2.5 na środkowym oporze $R_2$ panuje na stałe 5 V.
Podmieńmy ten opór źródłem $E = 5\ \mathrm{V}$ (+ na górze). Obwody
pozostałych gałęzi nie zauważą zmiany: $I_1 = (9-5)/2 = 2\ \mathrm{A}$,
$I_3 = (6-5)/2 = 0{,}5\ \mathrm{A}$, jak było. A co z prądem „nowej baterii”?
Z PPK dopłynie do niej $2{,}5\ \mathrm{A}$ — w kierunku *odwrotnym* do jej
strzałki oddawania, więc ta „bateria” pochłania $5 \cdot 2{,}5 = 12{,}5\ \mathrm{W}$,
czyli dokładnie tyle, ile wcześniej grzał opór. Podmianka klonuje
zachowanie, nie funkcję.
:::

### 2.9 Zasada ruchliwości źródeł: winda, którą można przesadzić

`[plik s. 32 = W2/s. 15]`

::: def Po ludzku — ruchliwość źródła napięciowego
Wstaw do **wszystkich** gałęzi schodzących się w jednym węźle identyczne
źródło napięciowe, zwrócone tak samo względem węzła. Żaden prąd się nie
zmieni. Dlaczego? Każde oczko przechodzące przez ten węzeł zawiera
*parę* tych źródeł, które podczas spaceru wchodzą ze przeciwnymi
znakami — jedna winda
jedzie w górę, druga dokładnie tyle samo w dół; bilans napięć oczek, a
więc i prądy, zostają te same. Zmieniają się tylko potencjały
(„poziom startu wszystkich wind”).
:::

Praktyczna korzyść jest graficzna: źródło napięciowe siedzące „w złej
gałęzi” (np. samo między węzłami, bez oporu w szeregu) można
„przeprowadzić przez węzeł” do innych gałęzi, aż wyląduje tam, gdzie
pozwala policzyć opór zastępczy albo napięcie. Wersja lustrzana tyczy
źródeł prądowych wstawianych równolegle do gałęzi jednego oczka —
one nie zmieniają napięć. Na poziomie PELP1 to narzędzie rysunkowe:
nie liczy się nim, lecz **przekształca** rysunek, żeby powstałe
równania dały się policzyć.

### 2.10 Zasada superpozycji: włączaj baterie po jednej

`[plik s. 33 = W2/s. 16]`

W świecie **liniowym** skutki się nie mieszają — dokładnie jak fale na
wodzie, które przechodzą przez siebie. Każde źródło niezależne wnosi
własny, proporcjonalny wkład w każdy prąd i napięcie, a wynik jest
sumą. Przepis:

1. zostaw jedno źródło niezależne; pozostałe **wyłącz**
   ($E \to$ zwarcie, $J \to$ rozwarcie — §1.5);
2. policz szukaną wielkość w tym podukładzie (dzielniki najczęściej);
3. powtórz dla każdego źródła i **dodaj** wyniki (ze znakami strzałki!).

::: pulapka Dwa zakazy superpozycji (oba ważne)
* **Źródeł sterowanych się nie wyłącza** — one nie są pobudzeniem, tylko
  własnością obwodu; zostają w każdym podukładzie.
* **Mocy się nie superponuje**: $P = RI^2$ nie jest liniowe w $I$, więc
  suma mocy z podukładów *nie* jest mocą w oryginale. Moc liczysz na
  samym końcu z całkowitych prądów i napięć.
:::

::: figura figury/superpozycja.svg | Superpozycja obwodu z dwiema bateriami. Wyłączenie źródła napięciowego = zwarcie; w ten sposób do pracy wraca albo sama bateria 9 V, albo sama 6 V.
:::

::: przyklad Przykład 2.6 — superpozycją otrzymujemy te same 5 V
Cel: $U_A$ w obwodzie z §0.3, ale tym razem w dwóch podukładach.

Podukład z samą baterią 9 V (bateria 6 V zwarta): węzeł A widzi
$R_2 \parallel R_3 = 2 \parallel 2 = 1\ \Omega$ w szeregu z $R_1 = 2\ \Omega$,
więc dzielnik daje $U_A' = 9 \cdot \dfrac{1}{2 + 1} = 3\ \mathrm{V}$.

Podukład z samą baterią 6 V (bateria 9 V zwarta): dokładnie odwrotny
rysunek, $U_A'' = 6 \cdot \dfrac{1}{2+1} = 2\ \mathrm{V}$.

Suma: $U_A = 3 + 2 = 5\ \mathrm{V}$ — tak jak w przykładzie 2.3. Przy okazji
widzimy, kto ile wnosi: 9-woltowa bateria „daje” węzłowi 3 V,
6-woltowa — 2 V.

A teraz pułapka z mocami: podukładowo prąd $R_2$ to $I_2' = 1{,}5$ A
i $I_2'' = 1$ A, moce $4{,}5\ \mathrm{W}$ i $2\ \mathrm{W}$; suma to $6{,}5\ \mathrm{W}$ — **błędnie,
bo prawdziwa moc to $2{,}5^2 \cdot 2 = 12{,}5\ \mathrm{W}$**. Kwadratu sumy nie
wolno zamieniać na sumę kwadratów.
:::

::: klucz Sprawdź się W2
1. Dwa elementy stoją obok siebie na rysunku, więc są równoległe. —
   **fałsz**, liczy się wspólna para węzłów, nie wygląd.
2. W superpozycji źródło sterowane też wyłączamy jak niezależne. —
   **fałsz**, sterowane zostaje zawsze.
3. Punkty o tym samym potencjale wolno połączyć przewodem bez zmiany
   jakiegokolwiek prądu. — **prawda** (kompensacja dla $E = 0$).
4. Prąd gałęzi dzielnika prądowego jest odwrotnie proporcjonalny
   do własnego oporu. — **prawda** (stąd „ten drugi” w liczniku).
:::

## 3. Wykład 3 — sztuka upraszczania: czarne skrzynki

`[plik s. 34–51]`

Cały wykład jest jedną myślą, powtarzaną na kilku poziomach:

::: zapamietaj Po ludzku — gra w czarną skrzynkę
Innych nie obchodzi, z czego zrobiony jest mój dwójnik. Widzą wyłącznie
to, co umiesz zmierzyć na jego zaciskach: zależność $u$ od $i$.
**Jeśli znajdę prostszy dwójnik o identycznej zależności zaciskowej,
można je zamienić** — i zewnątrz nikt nie zauważy różnicy.
:::

### 3.1 Reguły bezpieczeństwa podmieniania

`[plik s. 36–39 = W3/s. 3–6]` Cena zamiany jest znana i trzeba ją znać:

* W **środku** zastępczego dwójnika panują już inne prądy i napięcia —
  wewnątrz nie wolno potem „pytać” o prąd tego czy innego oporu pierwotnego
  ani o moc, jaką dostaje. Zamiana trzyma w ryzach tylko zaciski $u$, $i$
  (oraz ich iloczyn, bilanse mocy **z punktu widzenia zacisków**).
* Zamianę robi się **między dwoma węzłami, które po zamianie nadal
  istnieją**. Węzły wewnątrz skrzynki są tymczasowo żegnane.
* **Nie wolno zgubić szukanej wielkości.** Jeśli pytanie brzmi „prąd
  przez $R_3$”, nie chowaj $R_3$ w skrzynce na zawsze — wolno to tylko
  na chwilę, jeśli później wrócisz do oryginału przez kompensację (§4.5).
* Zamiana obejmująca **wielkość sterującą źródłem sterowanym** jest
  legalna tylko wtedy, gdy objęła też samo źródło. Chowanie „uszu”
  źródła przy pozostawieniu go na zewnątrz skrzynki jest błędem.

### 3.2 Opór zastępczy: przyłóż, zmierz, podziel

`[plik s. 40–41 = W3/s. 7–8]` Dla *bezźródłowej* (krzywa przez zero, §1.3)
czarnej skrzynki cała charakterystyka jest prostą przez początek, więc
wystarczy jedna liczba $R_Z$. Definicja praktyczna:

::: wzor Opór zastępczy
$R_Z = \dfrac{u_x}{i_x}$, gdzie $u_x$ to napięcie **zewnętrznego**, próbnego
źródła przyłożonego do zacisków, a $i_x$ — prąd, jaki to źródło wymusi.
Odwrotność: $G_Z = 1/R_Z$.
:::

Gdy skrzynka składa się tylko z oporów liniowych, nie trzeba nic
„próbować”: zwijasz ją od najbardziej wewnętrznych połączeń:

| Połączenie | Opór zastępczy | Zapamiętać po ludzku |
|---|---|---|
| szereg | $R_Z = \sum R_n$ | zwężki jedna za drugą — zawsze trudniej |
| równolegle | $G_Z = \sum G_n$, dla dwóch: $R_Z = \dfrac{R_1 R_2}{R_1 + R_2}$ | dokładasz kolejne rury — zawsze łatwiej |
| dwa równe równolegle | $R_Z = R/2$ | połowa, używane stale |
| $n$ równych równolegle | $R_Z = R/n$ | jak powyżej |

::: przyklad Przykład 3.1 — zwijanie od środka
Między węzłami A–B stoi: gałąź 4 Ω oraz równoległa z nią gałąź o dwóch
oporach po 2 Ω w szeregu. Gałąź szeregowa to $2 + 2 = 4\ \Omega$. Mamy więc
$4 \parallel 4 = \dfrac{4 \cdot 4}{4 + 4} = 2\ \Omega$ — opór zastępczy to
$R_Z = 2\ \Omega$. Kontrola prądem przy $U = 10\ \mathrm{V}$: każda gałąź bierze
$10/4 = 2{,}5\ \mathrm{A}$, razem 5 A, a $10\ \mathrm{V} / 2\ \Omega = 5\ \mathrm{A}$ — zgadza się.

Strategia w prawdziwych zadaniach: bierzesz **najbardziej zagłębioną**
grupę (tę najdalej od zacisków) i zamieniasz ją w jedną liczbę; rysunek
przerysowujesz mniejszy. Działa jak zwijanie parasola.
:::

### 3.3 Ani szereg, ani równolegle: gwiazda, trójkąt i mostek

`[plik s. 42 = W3/s. 9]` Czasem trzy dwójniki tworzą **gwiazdę** (wspólny
środek, trzy promienie) albo **trójkąt** (każdy z trzech oporów łączy
inną parę zacisków x, y, z). Żadna para nie jest ani szeregowa, ani równoległa —
stąd potrzeba wymiany całej trójki naraz.

::: figura figury/gwiazda.svg | Gwiazda–trójkąt w wersji symetrycznej: trójkąt trzech oporów 9 Ω widzi świat dokładnie tak jak gwiazda trzech oporów 3 Ω. Punktów wspólnych mają tylko zaciski x, y, z.
:::

::: wzor Przekształcenie Y–Δ (na rysunku: $R_x$ to ramię przy zacisku $x$)
$\Delta \to Y$: $R_x = \dfrac{R_{xy}\, R_{zx}}{R_{xy} + R_{yz} + R_{zx}}$ —
mnemotechnik: *iloczyn tych dwóch, które dotykają x, dzielony przez sumę
wszystkich trzech oporów trójkąta*.

$Y \to \Delta$: $R_{xy} = \dfrac{R_x R_y + R_y R_z + R_z R_x}{R_z}$ —
*ta sama suma iloczynów dla wszystkich, dzielnik — ramię „naprzeciw”*.

Wersja symetryczna, występująca w połowie zadań: $R_{\Delta} = 3 R_Y$.
:::

Dlaczego to działa? Wystarczy, że opór widziany między każdą z trzech
par zacisków (trzeci zacisk wolny) jest ten sam w obu figurach — trzy
równania, trzy niewiadome.

::: metoda Zanim sięgniesz po Y–Δ, wykonaj test mostka
W najpopularniejszym kandydacie do tej zamiany (mostek: dwa dzielniki między tymi
samymi węzłami, poprzeczka między ich środkami) wzory Y–Δ zwykle nie są
potrzebne. Policz najpierw oba potencjały środkowe dzielnikami:
jeśli **równe** — prąd poprzeczki jest zerowy, poprzeczkę można **usunąć**
(kompensacja!) i wszystko staje się nagle szeregowo-równoległe.
:::

::: przyklad Przykład 3.2 — mostek, który okazał się prostszy niż wygląda
Między A i B dwa dzielniki: lewy $2\ \Omega$ (góra) + $4\ \Omega$ (dół), prawy
$3\ \Omega$ (góra) + $6\ \Omega$ (dół); poprzeczka C–D ma $5\ \Omega$.
Potencjały względem B (przy całkowitym $U$): $V_C = U \cdot 4/6$,
$V_D = U \cdot 6/9$ — oba równe $\frac{2}{3}U$. Mostek jest **zrównoważony**,
prąd poprzeczki zerowy, usuwamy ją: $R_Z = (2+4) \parallel (3+6)
= 6 \parallel 9 = 3{,}6\ \Omega$. Opór 5 Ω mógł zostać wstawiony do treści zadania
jako podpucha — w tym stanie nie robi nic.
:::

### 3.4 Dwójnik ze źródłem sterowanym: udaje opór, którego w nim nie ma

`[plik s. 43 = W3/s. 10]` Skrzynka posiadająca same opory i źródła
**sterowane** jest nadal bezźródłowa (§1.3) — więc ma opór zastępczy.
Ale zwijanie po omacku się nie uda, bo źródło sterowane może prąd
w skrzynce *wzmocnić* lub *cofnąć*. Właściwy rytuał: podłącz źródło
próbne $u_x$, nazwij prąd zaciskowy $i_x$, zapisz Kirchhoffa i wylicz
iloraz.

::: przyklad Przykład 3.3 — opór 3-omowy „rośnie” do 9 omów
W dwójniku napięcie próbne $u_x$ wymusza prąd $i_x$ płynący przez opór
$R = 3\ \Omega$ i szeregowe źródło sterowane o napięciu $u_d = 2 u_R$,
gdzie $u_R$ jest napięciem na tym oporze (strzałki tak, że napięcia
się dodają). NPK w pętli próbnej:

$$
u_x = u_R + u_d = u_R + 2u_R = 3u_R = 3 \cdot (3 i_x) = 9 i_x
\qquad\Longrightarrow\qquad R_Z = \frac{u_x}{i_x} = 9\ \Omega
$$

Zaciski „czują” 9 Ω, choć jedyny fizyczny rezystor w środku ma 3 Ω:
sterowane źródło dokłada napięcie tak, by udawać większy opór.
Odwróć zwrot sterowania, a może wyjść opór **ujemny** — skrzynka
zaciskowo oddaje moc. Dlatego twór bezźródłowy ≠ pasywny (§1.3) i
dlatego nie wolno liczyć $R_Z$ samymi wzorami szeregowo-równoległymi,
gdy w środku czai się „romb”.
:::

### 3.5 Łączenie i zamiana źródeł

`[plik s. 44–46 = W3/s. 11–13]` Trzy legalne zagrywki, wszystkie będące zastosowaniem
gry w czarną skrzynkę do źródeł:

1. **Źródła napięciowe szeregowo się dodają** (ze znakiem zwrotu),
   **prądowe równolegle się dodają**: dwie windy jedna na drugiej; dwie
   pompy wpinające się w ten sam węzeł.
2. **Coś równolegle do idealnego źródła napięciowego można z zacisków
   wyrzucić** — skrzynka wygląda nadal jak to samo źródło (napięcie
   wymusza ono); analogicznie coś **szeregowo z idealnym źródłem
   prądowym** znika z charakterystyki.

::: pulapka „Można wyrzucić” ≠ „nie istnieje”
Ta zamiana trzyma tylko zaciski. Jeśli pytanie dotyczy prądu przez ten
„wyrzucony” element albo jego mocy, element oczywiście działa —
policzysz go osobno ze znanego napięcia (przy $E$) lub prądu (przy $J$).
:::

3. **Źródło rzeczywiste napięciowe ↔ rzeczywiste prądowe**: te same
   liczby, tylko „narysowane odwrotnie”:

::: wzor Zamiana źródeł rzeczywistych
Z $E$ szeregowe z $R_w$ robi się $J = E / R_w$ równoległe z $G_w = 1/R_w$.
I odwrotnie: $E = J R_w$, przy $R_w = 1/G_w$.
:::

::: przyklad Przykład 3.4 — ta sama czarna skrzynia w dwóch przebraniach
Źródło: $E = 12\ \mathrm{V}$, $R_w = 3\ \Omega$. Wersja prądowa: $J = 12/3 = 4\ \mathrm{A}$
równolegle do $3\ \Omega$. Sprawdźmy na obciążeniu $R_0 = 6\ \Omega$:

* wersja napięciowa: $I = 12/(3 + 6) = 1{,}33\ \mathrm{A}$, napięcie na obciążeniu
  $U = 8\ \mathrm{V}$;
* wersja prądowa: prąd 4 A dzieli się na $3\ \Omega$ i $6\ \Omega$; obciążenie
  dostaje $4 \cdot \dfrac{3}{3 + 6} = 1{,}33\ \mathrm{A}$ (dzielnik prądowy: „ten
  drugi” na górze) — ten sam rezultat, $U = 8\ \mathrm{V}$ ✔.

Zamianę warto robić, gdy druga postać ułatwia zwinięcie oporów
z sąsiadami. Wewnętrzne moce jednak się różnią: w wersji napięciowej
$R_w$ grzeje się prądem 1,33 A; w prądowej po równoległym oporze
płynie $4 - 1{,}33 = 2{,}67\ \mathrm{A}$. Znowu: skrzynka to tylko charakterystyka zaciskowa.
:::

### 3.6 Twierdzenie Thévenina: dowolna plątanina to jedna bateria z oporem

`[plik s. 47, s. 50–51 = W3/s. 14, s. 17–18]` Kulminacja wykładu i najbardziej
użyteczne twierdzenie na kolokwium.

::: def Po ludzku — Thévenin
Weź **dowolny liniowy** dwójnik (poza czystym źródłem prądowym): baterie,
opory, źródła sterowane — co chcesz. Z punktu widzenia dwóch zacisków
A–B zachowa się on **zawsze** jak jedno źródło rzeczywiste: idealna
bateria $E_T$ w szeregu z jednym oporem $R_W$. Żadna plątanina nie
potrafi z zacisków zachowywać się bardziej skomplikowanie.
:::

Przepis kucharski (trzy kroki, każdy na osobnym rysunku):

1. **$E_T$**: odczep obciążenie, zostaw A–B **rozwarte** i policz napięcie
   między nimi. (Skoro rozwarte — prąd wyjścia jest zerowy, rachunek
   zwykle prosty.)
2. **$R_W$**: wyłącz źródła **niezależne** w dwójniku ($E \to$ zwarcie,
   $J \to$ rozwarcie), sterowane zostaw. Policz opór zastępczy od strony
   A–B: zwijaniem (§3.2), a gdy są źródła sterowane — źródłem próbnym
   (§3.4).
3. **Z powrotem załóż obciążenie** do modelu: $E_T$, $R_W$, odbiornik w
   jednym prostym oczku.

::: figura figury/thevenin.svg | Dwójnik obwodu z dwiema bateriami po odjęciu gałęzi środkowej. Potrafi na zaciskach A–B zachowywać się równie dobrze jak pojedyncza bateria 7,5 V z oporem 1 Ω.
:::

::: przyklad Przykład 3.5 — te same 5 V otrzymane Théveninem
Odrywamy $R_2$ jako „obciążenie”. Reszta (dwie gałęzie z bateriami)
to nasz dwójnik A–B.

**Krok 1, $E_T$.** Zaciski rozwarte; jedyna droga prądu to pętla
zewnętrzna przez obie baterie: $I = \dfrac{9 - 6}{2 + 2} = 0{,}75\ \mathrm{A}$.
Potencjał A: $E_T = 9 - R_1 I = 9 - 1{,}5 = 7{,}5\ \mathrm{V}$ (sprawdź drugą
stroną: $6 + R_3 I = 7{,}5\ \mathrm{V}$ ✔).

**Krok 2, $R_W$.** Obie baterie wyłączamy w zwarcia. Od strony A–B widać
$R_1 \parallel R_3 = 2 \parallel 2 = 1\ \Omega$.

**Krok 3.** Zakładamy $R_2 = 2\ \Omega$ do baterii zastępczej:
$I_2 = \dfrac{7{,}5}{1 + 2} = 2{,}5\ \mathrm{A}$, $U_A = 2 \cdot 2{,}5 = 5\ \mathrm{V}$ —
znany wynik (§2.5), czwarty raz ten sam.
:::

### 3.7 Norton: ten sam bohater w przebraniu prądowym

`[plik s. 48–49 = W3/s. 15–16]` Norton mówi to samo co Thévenin, tylko
modelem jest źródło prądowe rzeczywiste: $J_N$ (prąd między **zwartymi**
zaciskami A–B) równolegle z $G_W = 1/R_W$.

::: wzor Trójca i reguła „dwie z trzech”
$$
E_T = J_N R_W, \qquad J_N = \frac{E_T}{R_W}, \qquad
R_W = \frac{E_T}{J_N}
$$

Wystarczy policzyć **dwie** liczby wprost z obwodu pierwotnego;
trzecia wynika gratis. Wybieraj te, których rachunek wygląda krócej:
opór **szeregowy** przy zaciskach skłania do liczenia $E_T$
(przy rozwarciu nie bierze prądu); opór **równoległy** między
zaciskami — licz $J_N$ (przy zwarciu nie bierze napięcia); wiele źródeł
niezależnych — $R_W$ (wyłączenie wszystkiego bardzo upraszcza rysunek).
:::

::: przyklad Przykład 3.6 — Norton dla naszego dwójnika
Zwarcie A–B (w przykładzie 3.5): lewa bateria daje do zwarcia
$9/2 = 4{,}5\ \mathrm{A}$, prawa $6/2 = 3\ \mathrm{A}$, razem $J_N = 7{,}5\ \mathrm{A}$
w dół. Kontrola wzorów: $R_W = E_T / J_N = 7{,}5 / 7{,}5 = 1\ \Omega$ ✔.
Zauważ „pułapkę kierunku”: $E_T$ i $J_N$ muszą być strzałkowane
**przeciwnie** (w sensie zacisków), aby ich iloraz wyszedł dodatnim
$R_W$. Znak nie „zgaduje się” — wyniknie z rysunków kroków 1 i (tu) 1'.
:::

::: uwaga Uwaga praktyczna
Do $E_T$, $J_N$ i $R_W$ używamy **trzech różnych rysunków** (rozwarcie,
zwarcie, źródła wyłączone). Prądy i napięcia o tych samych nazwach
($i_1$…) mają na nich inne wartości. Łączenie liczb z różnych rysunków
bez powrotu do modelu Thévenina/Nortona jest najczęstszym generatorem błędnych
odpowiedzi.
:::

::: klucz Sprawdź się W3
1. Po zamianie dwójnika na źródło Thévenina moc wydzielana wewnątrz jest
   ta sama. — **fałsz**, ta sama jest tylko moc zaciskowa; wnętrze jest inne.
2. Opór równoległy do idealnego źródła napięciowego nie wpływa na napięcie
   zaciskowe dwójnika. — **prawda**, ale jego własny prąd oczywiście
   płynie.
3. Przy liczeniu $R_W$ źródła sterowane wyłączamy tak jak niezależne. —
   **fałsz**, sterowane zostają; w razie nich liczymy $u_x/i_x$.
4. Dysponując dwiema bateriami w skrzynce, otrzymam charakterystykę
   bardziej złożoną niż źródło rzeczywiste. — **fałsz**, Thévenin: nie da się.
:::

## 4. Wykład 4 — świat nieliniowy, wzmacniacz i rachunek mocy

`[plik s. 52–68]`

### 4.1 Wzmacniacz operacyjny: perfekcjonista, który nie toleruje różnicy

`[plik s. 54–55 = W4/s. 3–4]`

::: def Po ludzku — wzmacniacz operacyjny (WO)
Wyobraź sobie źródło napięciowe sterowane napięciem wejściowym
($u_+ - u_-$) z **absurdalnie wielkim** współczynnikiem ($k \to \infty$).
W otwartej pętli najmniejsza różnica potencjałów wejść przerzuca jego
wyjście na jeden z krańców — wzmocnienie takie jest bezużyteczne samo
w sobie. Zamknięcie **ujemnego sprzężenia zwrotnego** (część wyjścia
prowadzona na wejście minus) zmienia potwór w zwierzę domowe: układ tak
reguluje, by różnica $u_+ - u_-$ zanikła. W granicy $k \to \infty$:
:::

::: wzor Dwa równania idealnego WO w ujemnym sprzężeniu
$u_+ = u_-$ (wejścia „siadają” na tym samym potencjale) oraz
$i_+ = i_- = 0$ (wejścia nie pobierają prądu). Wyjście zrobi
wszystko, co potrzeba, by ten stan utrzymać.
:::

Obraz: regulator temperatury. Wejście $+$ to zadana temperatura,
$u_-$ — termometr w pokoju ogrzewanym przez wyjście-grzejnik. Układ
grzeje tak długo, aż zrówna termometr z żądaniem — i wtedy utrzymuje
tyle, ile trzeba. Zapomnij o $k$: po prostu „skleił się” warunek równych
potencjałów przy zerowych prądach wejść.

::: figura figury/wo.svg | Wzmacniacz odwracający. Węzeł „minus” nazywa się wirtualną masą: trzyma potencjał masy, ale prąd do masy przez niego nie płynie (bo wejścia WO nie pobierają prądu).
:::

::: przyklad Przykład 4.1 — wzmacniacz odwracający z liczbami
$R_1 = 1\ \mathrm{k\Omega}$, $R_f = 4\ \mathrm{k\Omega}$, na wejście podano
$u_{we} = 1{,}5\ \mathrm{V}$. Wejście $+$ jest na masie (0 V), więc węzeł
$u_-$ również trzyma 0 V (wirtualna masa). Na $R_1$ panuje całe
$1{,}5\ \mathrm{V}$, więc płynie przez niego $I = 1{,}5\ \mathrm{V} /
1\ \mathrm{k\Omega} = 1{,}5\ \mathrm{mA}$. Ten prąd nie ma dokąd iść poza
gałęzią sprzężenia ($i_- = 0$), więc cały idzie przez $R_f$, powodując
spadek $1{,}5\ \mathrm{mA} \cdot 4\ \mathrm{k\Omega} = 6\ \mathrm{V}$. Skoro węzeł
minus siedzi na 0 V, wyjście musi usiąść na $-6\ \mathrm{V}$:

$$
u_{wy} = -\frac{R_f}{R_1} u_{we} = -4 \cdot 1{,}5 = -6\ \mathrm{V}
$$

To samo rozumowanie dla wersji nieodwracającej daje $1 + R_f/R_1$ —
wzmocnienie przynajmniej 1 i zawsze dodatnie.
:::

::: pulapka Wirtualna masa to nie zwarcie
$u_- = 0\ \mathrm{V}$ wolno Ci przyjąć przy liczeniu **napięć i prądów sąsiednich
oporów**, ale rysowanie przewodu z $u_-$ do masy zepsułoby obwód. WO utrzymuje
wartość napięcia tego węzła, dopasowując swoje wyjście; prawdziwy
przewód zwarłby węzeł na sztywno i przejął prąd, który w rzeczywistości
płynie przez $R_f$.
:::

### 4.2 Opór nieliniowy: „ile wynosi R?” przestaje mieć jedną odpowiedź

`[plik s. 56 = W4/s. 5]` Z liniowością żegnamy się, gdy
charakterystyka jest wygięta. W konkretnym punkcie pracy $Q = (U_0, I_0)$ można
policzyć **dwie** różne „rezystancje”:

::: wzor Opór statyczny i dynamiczny
**Statyczny** („wielkie liczby”) $R_s = \dfrac{U_0}{I_0}$ —
stosunek współrzędnych punktu. Na wykresie $i(u)$ odpowiada mu
**sieczna** z początku układu do Q (jej nachylenie $di/du$ to $G_s$).

**Dynamiczny** („małe ruchy”) $R_d = \left(\dfrac{du}{di}\right)_Q$ —
lokalna odwrotność nachylenia **stycznej** do charakterystyki w Q
(nachylenie $di/du$ tej stycznej to $G_d$).

Dla oporu liniowego $R_s = R_d = R$ (sieczna i styczna to ta sama prosta).
:::

Sugestia: $R_s$ odpowiada prędkości średniej z całej podróży;
$R_d$ — wskazaniu prędkościomierza w tej chwili. Odległość możesz
liczyć przez średnią; hamowanie opiszesz chwilową. W obwodach:
napięcie i prąd punktu pracy biorą się z $R_s$-rzeczywistości, a
zachowanie dla *małych* zmian wokół Q (np. sygnał nałożony na prąd
stały) opisuje $R_d$.

### 4.3 Dioda idealna: zawór, który zgadujesz i sprawdzasz

`[plik s. 57 = W4/s. 6]`

::: figura figury/dioda.svg | Idealna dioda jest tylko w połowie elementem: przy próbie skierowania prądu pod prąd jest rozwarciem, przy przepływie do przodu zwarciem o zerowym napięciu.
:::

::: metoda Metoda dwustanowa (jeden przepis na zawsze)
1. **Zgadnij stan diody** na oko: obwód „chce” pchnąć prąd w kierunku
   strzałki diody czy przeciwnie?
2. Zamień diodę hipotezą: przewidywanie = **przewodzi** → zwarcie
   ($u_D = 0$), przewidywanie = **blokuje** → rozwarcie ($i_D = 0$).
3. Policz resztę obwodu (jest liniowa!) i **sprawdź znak**:
   przewidywanie przewodzenia wymaga $i_D > 0$, blokowania — $u_D < 0$.
4. Znak przeciwny? Hipoteza odchodzi do kosza, zamień stan i powtórz.
   Dla jednej idealnej diody jeden z dwóch stanów zawsze przejdzie test.
:::

::: przyklad Przykład 4.2 — zgadnij, sprawdź
Obwód z rysynku: $E = 5\ \mathrm{V}$, $R = 1\ \mathrm{k\Omega}$, dioda skierowana
w dół (kierunek przewodzenia zgadza się z prądem obwodu).
**Hipoteza „przewodzi”**: zwarcie zamiast diody, więc $i = 5\ \mathrm{V} /
1\ \mathrm{k\Omega} = 5\ \mathrm{mA} > 0$ — co się zgadza z kierunkiem przewodzenia.
Przeszło.

Teraz odwróć baterię ($E = -5\ \mathrm{V}$). Hipoteza „przewodzi” daje
$i = -5\ \mathrm{mA}$: prąd płynie pod strzałkę diody — niemożliwe.
**Hipoteza „blokuje”**: rozwarcie, prąd 0; całe napięcie baterii odkłada
się na otwartej diodzie o znaku $u_D = -5\ \mathrm{V} < 0$ — zgodnie z hipotezą.
Przeszło za drugim razem.
:::

### 4.4 Składanie charakterystyk: rysunkowe „dodawanie elementów”

`[plik s. 58–59 = W4/s. 7–8]` Dwa nieliniowe (lub mieszane) dwójniki
obejmujesz jednym zastępczym, dodając ich wykresy — ale **co wolno
dodać, dyktuje połączenie**:

| Połączenie | Wspólne dla obu | Dodajemy graficznie |
|---|---|---|
| równoległe | napięcie $u$ | **prądy** przy każdym ustalonym $u$ (poruszasz się „pionowo”) |
| szeregowe | prąd $i$ | **napięcia** przy każdym ustalonym $i$ (poruszasz się „poziomo”) |

::: przyklad Przykład 4.3 — składanie w jednym punkcie
Obok siebie opór liniowy $2\ \Omega$ i element nieliniowy z §4.5
o charakterystyce $i = u^2/8$. W punkcie $u = 4$ V: opór bierze
$4/2 = 2\ \mathrm{A}$, element nieliniowy $16/8 = 2\ \mathrm{A}$; połączone
**równolegle** biorą razem 4 A — punkt (4, 4) leży na charakterystyce
zastępczej. Połącz je **szeregowo** i przepuść 2 A: na oporze siadają
4 V, na nieliniowym — 4 V (bo przy 2 A ma on dokładnie 4 V); razem 8 V,
punkt (8, 2). Na papierze robisz to ołówkiem, wykres po wykresie.
:::

### 4.5 Jeden element nieliniowy w obwodzie: prosta oporu to miejsce rokowań

`[plik s. 60–62 = W4/s. 9–11]` Gdy nieliniowy jest tylko jeden element,
nie walczymy z całym obwodem równaniami, bo wykresów nie da się
podstawić do układu liniowego. Robi się podział władzy:

::: metoda Przepis na układ z jednym elementem nieliniowym
1. Oddziel element nieliniowy od reszty zaciskami A–B.
2. Reszta jest liniowa — zamień ją na źródło Thévenina ($E_T$, $R_W$).
3. Źródło rzeczywiste nanieś na wykres elementu: jego charakterystyka
   $i = \dfrac{E_T}{R_W} - \dfrac{u}{R_W}$ to prosta opadająca,
   zwana **prostą oporu** (obciążenia). Punkt przecięcia z
   charakterystyką elementu to punkt pracy Q.
4. Gdy potrzebne są wielkości **wewnątrz** oryginalnej części liniowej,
   wróć do niej, podmieniając element nieliniowy wg kompensacji na
   źródło $E = U_0$ (albo $J = I_0$) z punktu Q (§2.8).
:::

Sugestywny obraz: charakterystyka elementu to lista propozycji
(„przy 4 V wezmę 2 A”); prosta oporu to lista tego, co umie dostarczyć
źródło („przy 4 V oddam dokładnie 2 A”). Punkt przecięcia to jedyny
warunek, na który zgadzają się obie strony negocjacji.

::: figura figury/prosta.svg | Punkt pracy elementu $i = u^2/8$ karmionego źródłem Thévenina $E_T = 8$ V, $R_W = 2\ \Omega$. Prosta oporu łączy (8 V, 0 A) z (0 V, 4 A); przecięcie Q odczytujesz w miejscu, gdzie krzywa elementu ją przecina.
:::

::: przyklad Przykład 4.4 — negocjacje na liczbach
Źródło: $E_T = 8\ \mathrm{V}$, $R_W = 2\ \Omega$; element: $i = u^2/8$
($u$ [V], $i$ [A]). Prostą oporu nanosisz dwoma „kotwicami”: rozwarcie
($i = 0$) daje $u = E_T = 8$ V; zwarcie ($u = 0$) daje
$i = E_T/R_W = 4$ A. Algebraicznie: $i = (8 - u)/2$, więc w Q:

$$
\frac{u^2}{8} = \frac{8 - u}{2}
\quad\Longrightarrow\quad u^2 + 4u - 32 = 0
\quad\Longrightarrow\quad u = 4\ \mathrm{V}
$$

(drugi pierwiastek $u = -8\ \mathrm{V}$ odrzucamy jako niezgodny z wykresem
i kierunkiem prądu). Prąd w punkcie Q wynosi $i = 16/8 = 2\ \mathrm{A}$. W tym punkcie: $R_s = U_0/I_0 = 4/2 = 2\ \Omega$,
$R_d$ liczymy z pochodnej $di/du = u/4$, w Q to 1 S, więc
$R_d = 1\ \Omega$. **Ten sam element i dwa różne „opory”** (§4.2) — wszystko
zgadza się z sieczną i styczną na rysynku.
:::

::: uwaga Metoda rzutowania przebiegu
Slajd `[plik s. 62 = W4/s. 11]` pokazuje odmianę graficzną dla źródła
zmieniającego się w czasie: dla każdej chwili prostą oporu przesuwa
względem charakterystyki i zbiera rzuty w przebieg $i(t)$. Intencja
jest ta sama — przecięcie listy propozycji elementu z możliwością
źródła — tylko powtarzana dla każdej chwili: mamy do czynienia z
sekwencją statycznych rokowań, wykonywaną na jednym wykresie.
:::

### 4.6 Moc: kto płaci rachunek (i dowód, że rachunek się zeruje)

`[plik s. 63–65 = W4/s. 12–14]`

::: wzor Moc pobierana i oddawana
Dla strzałek **przeciwnych** moc **pobierana** przez element: $p = ui$.
Moc **oddawana**: $p_o = -ui$. Dla odwrotnego układu strzałek znaki się
zamieniają. Wynik ujemny nie jest porażką: oznacza, że element realizuje
przeciwny kierunek przekazu, niż deklaruje nazwa $p$.
:::

* **Opór**: zawsze spożywa, $p = Ri^2 = Gu^2 = u^2/R \ge 0$. Jest elementem stratnym: raz zamienionej
  w ciepło energii nie da się w nim odzyskać.
* **Źródło idealne napięciowe** oddaje $p_o = Ei$, prądowe $p_o = Ju$ —
  ale ta moc **może wyjść ujemna**, np. bateria trakcyjna w trybie
  ładowania: przyjmuje, a nie oddaje.
* **Zasada Tellegena**: suma algebraiczna mocy chwilowych pobranych
  przez wszystkie elementy jest w każdej chwili zerowa. To bilans
  księgowy całego obwodu i **świetna kontrola rachunków**.

::: przyklad Przykład 4.5 — rachunek mocy obwodu z dwiema bateriami
Dane: $U_A = 5$ V, $I_1 = 2$ A, $I_2 = 2{,}5$ A, $I_3 = 0{,}5$ A (przykład 2.3).

| Element | Skrót | Moc |
|---|---|---:|
| bateria E1 | oddaje $9 \cdot 2$ | 18 W |
| bateria E2 | oddaje $6 \cdot 0{,}5$ | 3 W |
| $R_1$ | pobiera $2 \cdot 2^2$ | 8 W |
| $R_2$ | pobiera $2 \cdot 2{,}5^2$ | 12,5 W |
| $R_3$ | pobiera $2 \cdot 0{,}5^2$ | 0,5 W |

Suma oddanych: 21 W — suma pobranych: 21 W ✔. Dopiero taka tabela
mówi całą prawdę energetyczną: większość płaci bateria 9 V, a gałąź
baterii 6 V dokłada skromne 3 W (bo prąd w niej ledwo płynie).
:::

### 4.7 Dopasowanie energetyczne: szczyt pomiędzy „za mało” i „za dużo”

`[plik s. 66–68 = W4/s. 15–17]` Źródło rzeczywiste ($E_T$, $R_W$) zasila
odbiornik $R_0$. Moc odbiornika $P(R_0) = I^2 R_0$ ma kształt pagórka:

* $R_0 \to 0$: prąd ogromny, ale $U_0 \to 0$, więc $P = U_0 I \to 0$
  (cała moc grzeje źródło);
* $R_0 \to \infty$: napięcie prawie $E_T$, ale $I \to 0$, więc $P \to 0$
  (odbiornik „ogląda” napięcie nie płacąc).

W środku jest maksimum — rachunek daje:

$$
R_0 = R_W, \qquad P_{\mathrm{dysp}} = \frac{E_T^2}{4 R_W} = \frac{J_N^2}{4 G_W}
$$

$P_{\mathrm{dysp}}$ nazywa się **mocą dysponowaną** źródła: tyle źródło potrafi
oddać najlepiej dbającemu odbiornikowi. Po ludzku: równy opór
odbiornika i „wewnętrznego wężyka” dzieli napięcie na pół — jedna
połowa się marnuje.

::: figura figury/dopasowanie.svg | Moc w obciążeniu dla źródła Thévenina z przykładu 3.5. Ta sama moc (9 W) pojawia się dla dwóch różnych oporów, raz „drogą napięciową”, raz „prądową” — pagórek jest stromy z jednej strony i łagodny z drugiej.
:::

::: przyklad Przykład 4.6 — dopasowanie na źródle 7,5 V / 1 Ω
Bierzemy źródło z przykładu 3.5 ($E_T = 7{,}5\ \mathrm{V}$, $R_W = 1\ \Omega$) i
podłączamy różne obciążenia $R_0$. Prąd to $7{,}5 / (1 + R_0)$:

| $R_0$ [Ω] | $I$ [A] | $P = I^2 R_0$ [W] | Komentarz |
|---:|---:|---:|---|
| 0,25 | 6 | 9 | prąd duży, napięcie na nim małe |
| 1 | 3,75 | 14,06 | **szczyt: $R_0 = R_W$** |
| 2 | 2,5 | 12,5 | nasz $R_2$ z obwodu §0.3 |
| 4 | 1,5 | 9 | prąd za mały |

Moc maksymalna zgadza się ze wzorem: $P_{\mathrm{dysp}} = 7{,}5^2 / 4 =
14{,}06\ \mathrm{W}$. Sprawność w punkcie dopasowania: odbiornik dostaje
połowę mocy źródła idealnego (drugą połowę marnuje $R_W$), czyli 50%.
:::

::: ciekawostka Po co więc to dopasowanie, skoro marnuje pół?
Bo pytanie jest różne w dwóch światach. W sieci energetycznej chodzi
o *sprawność* — projektuje się $R_W \ll R_0$, żeby moc gubiła się
tylko symbolicznie. Dopasowanie maksymalizuje **moc po stronie
odbiornika przy źródle o danym oporze wewnętrznym** — ważne, gdy sygnał
jest słabiutki (antena, tor pomiarowy), a połowę mikroenergii i tak
trzeba oddać, żeby chociaż tę drugą połowę dało się *zauważyć*.
:::

::: klucz Sprawdź się W4
1. W WO z ujemnym sprzężeniem wejścia mają równe potencjały, więc płynie
   między nimi prąd zwarcia. — **fałsz**, $i_+ = i_- = 0$.
2. Dla oporu liniowego $R_s = R_d$. — **prawda**.
3. Dioda idealna przy napięciu wstecznym zachowuje się jak zwarcie.
   — **fałsz**, jak rozwarcie.
4. Przy dopasowaniu sprawność przekazu energii ze źródła rzeczywistego
   to 100%. — **fałsz**, 50%.
5. Moc pobierana przez opór liniowy może czasem wyjść ujemna, gdy prąd
   płynie „pod prąd”. — **fałsz**: $Ri^2$ jest niezależne od kierunku.
:::

## 5. Warsztat: jak wybrać metodę, zamiast zgadywać

### 5.1 Drzewo decyzyjne w 30 sekund

| Sytuacja | Pierwszy ruch | Dlaczego |
|---|---|---|
| Szukam wszystkich prądów i napięć | równanie węzłowe / komplet Kirchhoffa (§2.5) | jeden rachunek daje wszystko |
| Szukam jednej wielkości przy kilku źródłach niezależnych | superpozycja (§2.10) albo Thévenin (§3.6) | reszty obwodu nie trzeba znać |
| Dwa opory szeregowo / równolegle | dzielniki (§2.7) | wynik bez układania równań |
| Pytanie o rezystancję z zacisków bez źródeł niezależnych | zwijanie, a przy sterowanych — $u_x / i_x$ (§3.4) | jest tylko jedna liczba do znalezienia |
| Interesuje mnie tylko jedna gałąź / obciążenie | odczep ją: część liniowa → Thévenin, gałąź → obciążenie (§4.5) | duży obwód zamieniasz na jeden prosty rysunek |
| ANI szereg ANI równolegle | najpierw test równowagi mostka (§3.3), potem Y–Δ | test trwa chwilę, a często usuwa cały problem |
| W obwodzie jest dioda (nie wiem, czy przewodzi) | metoda dwustanowa (§4.3) | po hipotezie obwód jest liniowy |
| Element nieliniowy / wykres charakterystyki | Thévenin części liniowej + prosta oporu (§4.5) | wykresu nie da się wstawić do równań |
| Moc / maksymalna moc | najpierw prądy i napięcia, potem $p = ui$ / dopasowanie (§4.7) | moc nie jest liniowa |
| Kontrola po rozwiązaniu | PPK węzłów, NPK oczek, bilans Tellegena (§4.6) | każda z tych kontroli jest prawie darmowa |

### 5.2 Ten sam wynik (5 V) na cztery sposoby — jaki stąd morał

| Sposób | Gdzie w dokumencie | Kluczowe przejście |
|---|---|---|
| równanie węzłowe | przykład 2.3 | $(9 - U_A) + (6 - U_A) = U_A$ |
| superpozycja | przykład 2.6 | $U_A' = 3$, $U_A'' = 2$, suma 5 V |
| Thévenin + obciążenie | przykład 3.5 | $I_2 = 7{,}5/(1 + 2) = 2{,}5$ A, $U_A = 5$ V |
| kompensacja jako kontrola | przykład 2.5 | bateria 5 V w miejsce $R_2$ odtwarza te same prądy |

Jeśli dwie z tych dróg przynoszą **różne** liczby — jedna jest błędna
i wiesz to bez klucza odpowiedzi. Nabranie nawyku liczenia krytycznego
wyniku dwoma metodami to najtańsze ubezpieczenie w całym przedmiocie.

### 5.3 Zadania do policzenia (odpowiedzi za nimi)

**(T1)** Na oporze $R = 10\ \Omega$ strzałki prądu i napięcia ustawiono
zgodnie, a rachunek daje $i = -0{,}3\ \mathrm{A}$. Wylicz $u$ i moc pobraną.

**(T2)** Dzielnik $U = 20\ \mathrm{V}$, $R_1 = 4\ \mathrm{k\Omega}$ (góra),
$R_2 = 16\ \mathrm{k\Omega}$ (dół). Podaj napięcie wyjściowe bez obciążenia i po
podpięciu $R_L = 16\ \mathrm{k\Omega}$ równolegle do $R_2$.

**(T3)** W obwodzie z §0.3 baterię $E_2$ zastąpiono zwarciem
(opór $R_3$ został). Policz nowe $U_A$ i prądy gałęzi.

**(T4)** Sieć: bateria 12 V w szeregu z oporem $2\ \Omega$ zasila węzeł A;
opór $6\ \Omega$ łączy A z masą B. Dla zacisków A–B policz $E_T$ i $R_W$,
a po podpięciu obciążenia $4{,}5\ \Omega$ — jego prąd, napięcie i moc.

**(T5)** Dioda z rysunku §4.3, ale osadzona odwrotnie (anodą w dół),
$E = 5\ \mathrm{V}$, $R = 1\ \mathrm{k\Omega}$. Podaj stan, prąd i napięcie na diodzie.

**(T6)** Źródło rzeczywiste $E_T = 20\ \mathrm{V}$, $R_W = 5\ \Omega$. Jak dobrać
obciążenie do maksymalnej mocy i ile ona wyniesie? Jaką część
otrzymuje odbiornik przy okazji?

::: klucz Odpowiedzi do zadań treningowych
**T1.** $u = -Ri = -10 \cdot (-0{,}3) = 3\ \mathrm{V}$; $p = -ui = 0{,}9\ \mathrm{W}$ pobrane.
Znak minus prądu znaczy przepływ odwrotny do strzałki, a opór jak
zwykle pochłania moc.

**T2.** Bez obciążenia: $U_{wy} = 20 \cdot 16/20 = 16\ \mathrm{V}$. Z obciążeniem:
dół staje się $16 \parallel 16 = 8\ \mathrm{k\Omega}$,
$U_{wy} = 20 \cdot 8/12 = 13{,}33\ \mathrm{V}$ — dzielnik „ugina się” pod
obciążeniem (§2.7).

**T3.** Z równania węzłowego: $(9 - U_A)/2 = U_A/2 + U_A/2$, czyli $U_A = 3\ \mathrm{V}$ —
to dokładnie składowa $U_A'$ z superpozycji w przykładzie 2.6,
jak powinno być. $I_1 = 3\ \mathrm{A}$, $I_2 = 1{,}5\ \mathrm{A}$, prąd w $R_3$ w dół: $1{,}5\ \mathrm{A}$.

**T4.** $E_T = 12 \cdot 6/8 = 9\ \mathrm{V}$; $R_W = 2 \parallel 6 = 1{,}5\ \Omega$.
Z obciążeniem: $I = 9 / 6 = 1{,}5\ \mathrm{A}$, $U = 6{,}75\ \mathrm{V}$,
$P = 10{,}125\ \mathrm{W}$.

**T5.** Hipoteza „przewodzi” wymusza prąd skierowany pod strzałkę
diody — sprzeczność. Dioda **blokuje**: $i = 0$, a napięcie anoda–katoda
wynosi $u_D = -5\ \mathrm{V}$ (zwrot wsteczny). Obwodem nie może popłynąć prąd — wynik „nic się nie
dzieje” jest tu właściwą i elegancką odpowiedzią.

**T6.** $R_0 = R_W = 5\ \Omega$; $P_{\mathrm{dysp}} = 20^2/(4 \cdot 5) = 20\ \mathrm{W}$
(prąd dopasowania $2\ \mathrm{A}$, napięcie obciążenia 10 V). Połowa mocy
źródła idealnego — sprawność 50%.
:::

## 6. Ściąga

### 6.1 Formułownik czterech wykładów

| Temat | Wzór | Uwaga praktyczna |
|---|---|---|
| prawo Ohma | $u = Ri$, $i = Gu$, $G = 1/R$ | strzałki przeciwne; dla zgodnych minus |
| źródło rzeczywiste napięciowe | $u = E - R_w i$ | $i$ — prąd oddawany przez źródło |
| źródło rzeczywiste prądowe | $i = J - G_w u$ | lustro poprzedniego |
| kondensator | $i = C \dfrac{du}{dt}$, $w = \dfrac{1}{2} C U^2$ | w stanie ustalonym prądu stałego: rozwarcie |
| cewka | $u = L \dfrac{di}{dt}$, $w = \dfrac{1}{2} L I^2$ | w stanie ustalonym: zwarcie |
| PPK, NPK | $\sum i = 0$ (węzeł), $\sum u = 0$ (oczko) | znaki ze strzałek / kierunku obiegu |
| dzielnik napięciowy | $U_2 = U \dfrac{R_2}{R_1 + R_2}$ | „swój na górze” |
| dzielnik prądowy | $I_1 = I \dfrac{R_2}{R_1 + R_2} = I \dfrac{G_1}{G_1 + G_2}$ | „ten drugi na górze” |
| opory szeregowo | $R_Z = \sum R_n$ | |
| opory równolegle | $G_Z = \sum G_n$; dwa: $R_Z = \dfrac{R_1 R_2}{R_1 + R_2}$ | |
| opór zastępczy | $R_Z = \dfrac{u_x}{i_x}$ | źródło próbne; konieczne przy sterowanych |
| Y→Δ | $R_{xy} = \dfrac{R_x R_y + R_y R_z + R_z R_x}{R_z}$ | symetrycznie: $R_\Delta = 3 R_Y$ |
| Δ→Y | $R_x = \dfrac{R_{xy} R_{zx}}{\sum R_\Delta}$ | |
| źródła rzeczywiste | $J = E / R_w$, $E = J R_w$, $G_w = 1/R_w$ | zamiana Thévenin ↔ Norton |
| Thévenin/Norton | $E_T = J_N R_W$ | dwie z trzech wystarczą (§3.7) |
| moc pobierana | $p = ui$ (strzałki przeciwne) | opór: $p = R i^2 = u^2/R$ |
| Tellegen | $\sum p = 0$ | kontrola rachunków |
| dopasowanie | $R_0 = R_W$, $P_{\mathrm{dysp}} = \dfrac{E_T^2}{4 R_W}$ | sprawność w dopasowaniu 50% |
| statyczny/dynamiczny | $R_s = U_0/I_0$, $R_d = \left(\dfrac{du}{di}\right)_Q$ | sieczna vs styczna |
| WO odwracający | $u_{wy} = -\dfrac{R_f}{R_1} u_{we}$ | węzeł minus = wirtualna masa |
| WO nieodwracający | $u_{wy} = \left(1 + \dfrac{R_f}{R_1}\right) u_{we}$ | wzmocnienie $\ge 1$ |

### 6.2 Piętnaście zdań-pułapek

1. **„Po wyłączeniu źródła prądowego zamieniam je w zwarcie.”** Fałsz:
   rozwarcie.
2. **„Element równoległy do idealnego źródła napięciowego mogę zawsze
   pominąć.”** Półprawda: tylko przy pytaniach o zaciski; o jego prąd
   albo moc pytać nadal wolno.
3. **„Superpozycja działa też dla mocy.”** Fałsz: $RI^2$ nie jest liniowe.
4. **„W superpozycji sterowane źródła zostawiam.”** Prawda — to kluczowe.
5. **„Opór ujemny dwójnika jest niemożliwy.”** Fałsz: w środku może siedzieć
   sterowane źródło (§3.4).
6. **„Jeżeli punkty mają równy potencjał, to połączenie przewodnikiem nic
   nie zmieni.”** Prawda — kompensacja przy $E = 0$.
7. **„Poprzeczka mostka zrównoważonego bierze maksymalny prąd.”**
   Fałsz: zerowy, właśnie.
8. **„Diodę idealną w stanie przewodzenia opisuje prąd wyznaczony przez
   jej opór.”** Fałsz: jest zwarciem, prąd dyktuje reszta obwodu.
9. **„Wirtualną masę można zastąpić przewodem do masy.”** Fałsz.
10. **„Dzielnik napięciowy działa nadal tak samo pod obciążeniem.”**
    Fałsz (§2.7).
11. **„Źródła w oczku skumulowały napięcie — coś jest nie tak z zadaniem.”**
    Fałsz; sumować trzeba ze zwrotami, a spadki na oporach wchodzą do bilansu (§2.3).
12. **„Charakterystyka elementu liniowego przechodzi przez (0,0).”**
    Fałsz jako zdanie ogólne: przez początek układu przechodzą
    charakterystyki elementów bezźródłowych; idealne źródło niezależne
    bezźródłowe nie jest, choć należy do obwodu liniowego.
13. **„W obwodzie z elementem nieliniowym mogę użyć Thévenina do całości.”**
    Fałsz — tylko do części liniowej po odłączeniu elementu nieliniowego.
14. **„Dopasowanie to najlepszy sposób przekazywania energii w ogóle.”**
    Fałsz — maksymalizuje moc, nie sprawność (50%).
15. **„Minus w wyniku oznacza błąd.”** Fałsz — oznacza kierunek odwrotny
    do strzałki (§1.2).

### 6.3 Indeks: slajd połączonego PDF-u → sekcja tego dokumentu

**Wykład 1 — modele elementów** (strony pliku 1–17):

| Strona pliku | Treść slajdu | Tutaj |
|---:|---|---|
| 1 | Strona tytułowa W1 | §1 |
| 2 | Spis treści W1 | §1 |
| 3 | Równania Maxwella | §1.1 |
| 4 | Teoria obwodów, element skupiony | §1.1 |
| 5 | Podstawowe wielkości | §1.2 |
| 6 | Konwencja oznaczeń | §1.2 |
| 7 | Klasyfikacja elementów | §1.3 |
| 8 | Równania elementów | §1.3 |
| 9 | Idealne źródło napięciowe | §1.4 |
| 10 | Idealne źródło prądowe | §1.4 |
| 11 | Opór (ogólny) | §1.5 |
| 12 | Opór liniowy, prawo Ohma | §1.5 |
| 13 | Zwarcie i rozwarcie | §1.5 |
| 14 | Pojemność i indukcyjność | §1.6 |
| 15 | Rzeczywiste źródło napięciowe | §1.7 |
| 16 | Rzeczywiste źródło prądowe | §1.7 |
| 17 | Źródła sterowane | §1.8 |

**Wykład 2 — prawa i zasady obwodowe** (strony pliku 18–33):

| Strona pliku | Treść slajdu | Tutaj |
|---:|---|---|
| 18 | Strona tytułowa W2 | §2 |
| 19 | Spis treści W2 | §2 |
| 20 | Układ elektryczny: gałąź, węzeł, oczko | §2.1 |
| 21 | I prawo Kirchhoffa | §2.2 |
| 22 | II prawo Kirchhoffa | §2.3 |
| 23 | Równania elementów a strzałkowanie | §2.4 |
| 24 | Wyznaczanie wszystkich prądów i napięć | §2.5 |
| 25 | Przykład na wykładzie | §2.5 |
| 26 | Wyznaczanie wybranej wielkości | §2.5 |
| 27 | Połączenia szeregowe i równoległe | §2.6 |
| 28 | Połączenia Δ i Y | §2.6, §3.3 |
| 29 | Dzielnik napięciowy | §2.7 |
| 30 | Dzielnik prądowy | §2.7 |
| 31 | Zasada kompensacji | §2.8 |
| 32 | Zasada ruchliwości źródeł | §2.9 |
| 33 | Zasada superpozycji | §2.10 |

**Wykład 3 — elementy zastępcze** (strony pliku 34–51):

| Strona pliku | Treść slajdu | Tutaj |
|---:|---|---|
| 34 | Strona tytułowa W3 | §3 |
| 35 | Spis treści W3 | §3 |
| 36 | Rezystancyjny element zastępczy | §3, §3.1 |
| 37 | Następstwa stosowania zamiany | §3.1 |
| 38 | Reguły zamiany (węzły, szukana wielkość) | §3.1 |
| 39 | Reguły zamiany (wielkość sterująca) | §3.1, §3.4 |
| 40 | Opór zastępczy: definicja | §3.2 |
| 41 | Połączenia szeregowe i równoległe oporów | §3.2 |
| 42 | Przekształcenie Y–Δ | §3.3 |
| 43 | Opór zastępczy ze źródłem sterowanym | §3.4 |
| 44 | Łączenie źródeł idealnych tego samego rodzaju | §3.5 |
| 45 | Łączenie źródeł idealnych z elementami | §3.5 |
| 46 | Zamiana źródeł rzeczywistych | §3.5 |
| 47 | Twierdzenie Thévenina | §3.6 |
| 48 | Twierdzenie Nortona | §3.7 |
| 49 | Uwagi praktyczne (dwie z trzech) | §3.7 |
| 50 | Wyznaczanie $E_T$ i $J_N$ z definicji | §3.6, §3.7 |
| 51 | Wyznaczanie $R_W$ z definicji | §3.6 |

**Wykład 4 — elementy nieliniowe, wzmacniacz operacyjny, moc**
(strony pliku 52–68):

| Strona pliku | Treść slajdu | Tutaj |
|---:|---|---|
| 52 | Strona tytułowa W4 | §4 |
| 53 | Spis treści W4 | §4 |
| 54 | WO — otwarta pętla | §4.1 |
| 55 | WO — zamknięta pętla sprzężenia | §4.1 |
| 56 | Opór nieliniowy, $R_s$, $R_d$ | §4.2 |
| 57 | Dioda idealna | §4.3 |
| 58 | Składanie charakterystyk — równolegle | §4.4 |
| 59 | Składanie charakterystyk — szeregowo | §4.4 |
| 60 | Układ z jednym elementem nieliniowym | §4.5 |
| 61 | Metoda prostej oporu | §4.5 |
| 62 | Metoda rzutowania przebiegu | §4.5 |
| 63 | Moc chwilowa | §4.6 |
| 64 | Moc w oporze i źródłach | §4.6 |
| 65 | Zasada Tellegena | §4.6 |
| 66 | Dopasowanie energetyczne — problem | §4.7 |
| 67 | Warunek dopasowania | §4.7 |
| 68 | Moc dysponowana | §4.7 |

### 6.4 Co dalej w tym repozytorium

* **Formalna wersja tego samego materiału** z pełniejszymi wywodami,
  superwęzłami i klasycznymi ćwiczeniami: `wyklady/wyklady.pdf`.
* **Cała teoria z prawdziwymi pytaniami z kolokwiów**: `teoria/teoria.pdf`.
* **Tempo liczenia na czas** i schematy archetypów zadań:
  `szybkie/szybkie.pdf`.
* **Kompendium zawierające też metrologię** (Test 2):
  `kompendium/kompendium.pdf`.

Powodzenia na kolokwium. Licz powoli, sprawdzaj bilansem — i pamiętaj,
że minus w wyniku to obwód korygujący twoją strzałkę, a nie wyrok.
