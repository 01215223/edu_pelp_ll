# Szybkie rozwiązywanie obwodów

## Omówienie zadań z kluczy PELP1 (Test 1, 2019–2026)

::: metoda Jak czytać ten dokument
Każdy rozdział to **jeden archetyp zadania**. Układ jest zawsze ten sam: najpierw *rozpoznanie* (po czym w 3 sekundy wiadomo, że to ten typ), potem *ścieżka* — lista działań do wykonania po kolei, a na końcu **zadania z prawdziwych kluczy**: wycinek oryginału (z pogrubioną odpowiedzią prawidłową), rachunek krok po kroku i lista pułapek, w które wpadają osoby liczące „po kolei, wszystko”.

Zadania opisane są sygnaturą `plik · litera`. Na przykład `25Z_A_1 · A` znaczy: klucz `PELP1_25Z_A_1_klucz.pdf`, pytanie A. Te same pliki leżą w katalogu głównym repozytorium, więc każde zadanie można otworzyć i sprawdzić w oryginale.

Wzory i rachunki są przepisane z kluczy — **każda liczba w tym dokumencie jest policzona od zera i zgadza się z odpowiedzią zaznaczoną w kluczu**. Tam, gdzie klucz dopuszcza dwie odpowiedzi (różniące się znakiem), jest to wyraźnie napisane.
:::

::: uwaga Skąd się wzięły te zadania
Materiał to 35 kluczy kolokwiów z lat 2019–2026 (252 pytania). Klucze mają tę cenną właściwość, że **każde pytanie ma więcej niż jedną odpowiedź prawidłową** (tak, jak pisze stopka klucza) — dzięki temu widać, które dystraktory powstały z typowych błędów rachunkowych, a nie z fantazji autora. To właśnie one są najlepszym materiałem do nauki szybkiego liczenia.
:::

## 1. Anatomia Testu 1: litera pytania mówi, jaka to metoda

Test 1 (obwody) ma od lat ten sam szkielet: 6–8 pytań, 9 punktów, 35 minut, jedna odpowiedź prawidłowa na pytanie. Co ważniejsze — **pytania pod tą samą literą są prawie zawsze tego samego typu**. Wystarczy spojrzeć na literę, żeby wiedzieć, jaką metodę wyciągnąć.

<!--LETTERMAP-->

::: klucz Co z tego wynika dla strategii
Nie czytaj testu od A do H. Zbierz najpierw punkty tam, gdzie metoda jest krótka i pewna — **A, E, F, C** to zwykle cztery punkty w kilkanaście minut. Dopiero potem bierz się za $G$ i $B$ (po 2 pkt, najwięcej liczenia i rysunku) oraz za $H$ (dioda/Thévenin).
:::

### 1.1 Budżet czasu: 35 minut na 9 punktów

| Pytanie | Pkt | Co robisz | Czas | Gdzie w dokumencie |
|---|---|---|---|---|
| A | 1 | opór zastępczy dwójnika ze źródłem sterowanym | 90 s | §3.1 |
| B | 1 | punkt pracy elementu nieliniowego (odczyt z wykresu) | 4 min | §3.10 |
| C | 1 | jakościowo: od czego zależy napięcie/prąd | 60 s | §3.2, §3.11 |
| D | 1 | napięcie $U$: dzielnik albo wzmacniacz operacyjny | 75 s | §3.9 |
| E | 1 | prądowe prawo Kirchhoffa — jeden węzeł | 60 s | §3.7 |
| F | 1 | metoda superpozycji — jedna składowa | 2 min | §3.8 |
| G | 2 | moc maksymalna / dopasowanie | 3 min | §3.5, §3.6 |
| H | 1 | dioda, Thévenin–Norton, dwójnik | 90 s | §3.3, §3.4 |

Razem około 14 minut rachunku — zostaje ponad 20 minut na czytanie rysunków i kontrolę. **Kto pisze test „od góry do dołu”, zwykle utyka na B albo G i traci punkty z E i F, które są najłatwiejsze.**

### 1.2 Kolejność rozwiązywania, która maksymalizuje punktację

1. **A** — 90 sekund, schemat zwykle prosty.
2. **E** — jedno równanie KCL, czasem odpowiedź to „układ jest sprzeczny”.
3. **F** — superpozycja: liczysz *jedną* składową, nie cały obwód.
4. **C** — pytanie jakościowe: nie licz, tylko rozstrzygnij, co znika.
5. **D**, **H** — dzielnik i dwójnik zastępczy.
6. **G** — moc maksymalna (2 pkt, trzy linijki rachunku).
7. **B** — na końcu: odczyt z wykresu wymaga spokoju.

## 2. Siedem nawyków, które dają dziesięć minut zapasu

::: zapamietaj 1. Policz tylko to, o co pytają
Pytanie „jaki jest wkład do prądu $I$ pochodzący od źródła $J_1$” **nie prosi o prąd $I$**, tylko o jedną składową. Pytanie „jaka jest SEM zastępczego źródła Thévenina” nie prosi ani o $R_T$, ani o prąd zwarciowy. Najczęstszy powód straty czasu na kolokwium: policzenie całego obwodu, gdy potrzebny był jeden ułamek.
:::

::: zapamietaj 2. Zwarcie i rozwarcie to dźwignia, nie „brzydki przypadek”
$E_T$ liczy się przy **rozwartych** zaciskach (bo wtedy w gałęzi wyjściowej nie płynie prąd i nie ma na niej spadku napięcia). $J_N$ liczy się przy **zwartych** zaciskach (bo wtedy napięcie na zaciskach wynosi zero i część źródeł sterowanych po prostu znika). Te dwa zdania rozwiązują większość zadań z liter C, F i H.
:::

::: zapamietaj 3. Idealne źródło „zżera” opór
Idealne źródło **prądowe** włączone szeregowo w gałąź ustala prąd tej gałęzi — opory w tej gałęzi nie zmieniają już niczego (zadanie `19Z_A_1 · A`). Idealne źródło **napięciowe** włączone równolegle z czymś ustala napięcie — równoległy opór nie zmienia niczego. Zanim zaczniesz liczyć, sprawdź, czy w obwodzie nie ma takiego „dowódcy”.
:::

::: zapamietaj 4. Zerowanie źródeł w superpozycji — co dokładnie znika
$E \to 0$ to **zwarcie** (przewód). $J \to 0$ to **rozwarcie** (przerwa). Źródła sterowane **zostają** — nigdy ich nie wyłączaj. Po wyzerowaniu zwykle okazuje się, że dwa opory są równolegle, a trzeci jest zwarty i cały obwód sprowadza się do dzielnika prądu.
:::

::: zapamietaj 5. Kontrola granic i miana
Policz odpowiedź dla skrajnych wartości: $R \to 0$, $R \to \infty$, $g \to 0$, $J \to 0$. Wzór $1/(G - g)$ przy $g = 0$ musi dać $1/G$ (a nie $1/G$ razy dwa). Moc musi wyjść w mW przy kV i mA — sprawdzenie miana łapie większość pomyłek z przedrostkami.
:::

::: zapamietaj 6. Klucze są „ładne” — brzydki wynik to sygnał błędu
Autorzy kluczy dobierają liczby tak, żeby wynik był ułamkiem „szkolnym”: $3/10\ \text{mW}$, $1/(G-g)$, $3\ \text{mW}$, $9\ \text{mW}$, $6\ \text{V}$, $1 A$. Jeśli po dwóch minutach wychodzi $0,47\ \text{mW}$, a w odpowiedziach są $3/10$, $6/5$, $1$, $15/8$ — to nie „prawie pasuje”, to błąd. Wróć do rysunku.
:::

::: zapamietaj 7. Eliminacja: znak, rząd wielkości, monotoniczność
Zanim policzysz do końca, odsiej odpowiedzi, które są niemożliwe: ujemna rezystancja tam, gdzie nie ma źródła sterowanego; wynik większy od prądu źródła, choć obwód tylko dzieli prąd; napięcie większe od $E$. W kluczach dystraktory są budowane właśnie z takich „prawie-dobrych” wyników — eliminacja po znaku i rzędzie zostawia zwykle dwie kandydatki.
:::

## 3. Archetypy z zadaniami z kluczy

### 3.1 Opór zastępczy dwójnika ze źródłem sterowanym

**Rozpoznanie.** Pytanie „Opór zastępczy dwójnika AB wynosi:”, w środku romb (źródło sterowane) opisany jako $gu$, $\beta i$, $r i$ albo $3i$, obok zwykły opór. Odpowiedzi są wzorami z $R$, $G$, $g$, $\beta$, $r$.

**Ścieżka (60–90 s).** Nie zgaduj. Zrób dokładnie trzy rzeczy:

1. **Załóż napięcie** $u$ na zaciskach A–B (albo prąd $i$ wpływający do A).
2. **Zapisz prąd każdej gałęzi** tym napięciem: opór daje $G\cdot u$ (albo $u/R$), źródło sterowane daje $g\cdot u$, $\beta \cdot i$ itd. — z takim znakiem, jaki wynika z **grota strzałki w rombie**.
3. **Dodaj prądy** i podziel: $R_{AB} = u / i_{AB}$.

Dwa najczęstsze układy i ich wyniki:

| Układ | Prąd wypadkowy | $R_{AB}$ |
|---|---|---|
| opór $G$ i źródło $g\cdot u$, **oba wciągają prąd z A** | $i = (G + g)u$ | $1/(G + g)$ |
| opór $G$ i źródło $g\cdot u$, **źródło oddaje prąd do A** | $i = (G - g)u$ | $1/(G - g)$ |
| opór $R$ i źródło $\beta i$ **przeciwnie** do $i$ w $R$ | $i_{AB} = (1 - \beta )i$ | $R/(1 - \beta )$ |
| źródło $g\cdot u$ **szeregowo** z oporem | prąd gałęzi wymuszony: $gu$ | $1/g$ (opór nie wpływa) |

::: figura zadania/25Z_A_1_A.png | Klucz 25Z_A_1, pytanie A. Romb to źródło sterowane napięciem $u$; obok opór przewodności $G$. Odpowiedź prawidłowa: $1/(G - g)$.
:::

**Rachunek.** Napięcie na zaciskach to $u$. Przez opór płynie $G\cdot u$ w dół (z A do B). Grot strzałki w rombie skierowany jest **w górę**, czyli źródło $g\cdot u$ wstrzykuje prąd do węzła A — w oczach zacisków A–B jest to prąd *ujemny*. Prąd wypływający z A:

$$i_{AB} = G u - g u = (G - g)u \quad\Rightarrow\quad R_{AB} = \frac{u}{i_{AB}} = \frac{1}{G-g}$$

**Kontrola.** Dla $g = 0$ (źródło zniszczone) wzór daje $1/G$ — zgadza się z samym oporem. Odpowiedź $1/(G+g)$ to ta sama pomyłka, którą popełnia się, gdy nie patrzy się na grot strzałki.

::: figura zadania/24Z_A_1_A.png | Klucz 24Z_A_1, pytanie A. Romb $\beta i$ jest sterowany prądem $i$ płynącym przez opór $R$. Odpowiedź prawidłowa: $R/(1 - \beta )$.
:::

**Rachunek.** Prąd $i$ płynie przez $R$ w dół, więc $u_{AB} = R\cdot i$. Przez romb płynie $\beta \cdot i$ **w górę** (przeciwnie), zatem wypadkowy prąd wpływający do A to $i - \beta i = i(1 - \beta )$, a opór zastępczy

$$R_{AB} = \frac{u_{AB}}{i_{AB}} = \frac{R\,i}{i(1-\beta)} = \frac{R}{1-\beta}$$

**Kontrola.** $\beta = 0$ daje $R$ — dobrze. $\beta$ bliskie 1 daje opór ogromny, a $\beta > 1$ daje opór ujemny; to nie błąd, tak działa układ z aktywnym źródłem sterowanym.

::: figura zadania/23Z_A_1_A.png | Klucz 23Z_A_1, pytanie A. Tu romb $gu$ stoi **szeregowo** z oporem $R$. Odpowiedź prawidłowa: $1/g$.
:::

**Rachunek (najszybszy przypadek w całym teście).** Idealne źródło prądowe włączone szeregowo w gałąź **wymusza** prąd tej gałęzi: cokolwiek by nie było obok, przez całą gałąź płynie $gu$. Opór $R$ może tylko zmienić rozkład napięć, nie prąd. Zatem

$$R_{AB} = \frac{u}{i_{AB}} = \frac{u}{g\,u} = \frac{1}{g}$$

$R$ w ogóle nie wchodzi do wyniku — i to jest sedno zadania. Odpowiedź $R - 1/g$ bierze się z potraktowania źródła jak zwykłego oporu ujemnego; odpowiedź $R$ z pominięcia rombu.

::: pulapka Trzy pułapki tego archetypu
1. **Kierunek strzałki w rombie.** $1/(G-g)$ i $1/(G+g)$ różnią się tylko grotem. Zawsze najpierw ustal, czy źródło *dodaje* prąd do węzła A, czy go *zabiera*.
2. **„Opór szeregowy nie ma znaczenia”.** W układzie z $gu$ szeregowo odpowiedź $R$ jest dystraktorem; opór nie zmienia prądu wymuszonego.
3. **Zła kontrola:** dla $g = 0$ każdy poprawny wzór musi redukować się do zwykłego oporu. Jeśli nie redukuje się — wzór jest zły, bez liczenia dalej.
:::

### 3.2 Idealne źródło, które wymusza stan całej gałęzi

::: figura zadania/19Z_A_1_A.png | Klucz 19Z_A_1, pytanie A. W oczku są: źródło prądowe 1 A, opór 10 Ω, źródło 6 V i opór 2 Ω. Odpowiedź prawidłowa: „nie zmieni się”.
:::

**Rozpoznanie.** Pytanie o *wpływ* zmiany jednego elementu na napięcie innego; w obwodzie jest źródło prądowe i kilka oporów w jednym oczku.

**Ścieżka (30 s).** Sprawdź, czy źródło prądowe nie jest włączone **szeregowo** w jedyną drogę prądu. Jeśli tak — prąd w oczku jest już ustalony i żadna zmiana oporu go nie zmieni.

**Rachunek.** W oczku płynie 1 A (wymuszone przez źródło). Napięcie na oporze 10 Ω wynosi $U = 10\ \Omega \cdot 1\ \text{A} = 10\ \text{V}$ — i nie zależy od oporu 2 Ω ani od źródła 6 V (te dwa elementy tylko przesuwają poziom napięcia na źródle prądowym). Po zastąpieniu 2 Ω zwarciem nadal płynie 1 A, więc napięcie na 10 Ω **nie zmieni się**.

**Kontrola.** Gdyby odpowiedź brzmiała „zmniejszy się 1,2 raza”, musiałby istnieć dzielnik $12/10 = 1,2$ — i taki dystraktor w kluczu jest. To sygnał, że ktoś policzył stosunek oporów zamiast prądu.

::: zapamietaj Reguła do zapamiętania
W obwodzie jednym oczkiem ze źródłem prądowym **prąd jest dany**, a nie szukany. Pytania o „wpływ” rozwiązuje się wtedy bez ani jednego obliczenia.
:::

### 3.3 Thévenin: $E_T$ liczone przez rozwarcie

::: figura zadania/19Z_A_1_C.png | Klucz 19Z_A_1, pytanie C. Odpowiedź prawidłowa: 6 V.
:::

**Rozpoznanie.** „Jaka jest wartość siły elektromotorycznej źródła zastępczego Thévenina…”, „…napięcie stanu jałowego…”, zaciski narysowane jako dwa puste kółka.

**Ścieżka (45 s).**

1. **Rozewrzyj zaciski** (nic nie podłączaj).
2. Sprawdź, przez które gałęzie **nie płynie prąd** — na nich nie ma spadku napięcia, więc można je *przenieść* jako węzeł.
3. Policz napięcie między zaciskami (zwykle dzielnik).

**Rachunek.** Przez opór 12 Ω nie płynie prąd (wisi na rozwartych zaciskach), więc napięcie na nim wynosi 0 i $E_T$ jest równe napięciu na oporze 6 Ω. Źródło 10 V pracuje wtedy w dzielniku $4\ \text{\Omega}$ – $6\ \text{\Omega}$:

$$E_T = 10\ \text{V}\cdot\frac{6}{4+6} = 6\ \text{V}$$

**Kontrola.** Wartość musi być **mniejsza** od 10 V i większa od połowy (bo 6 Ω > 4 Ω). Odpowiedzi 8 V i 10 V odpadają od razu, bez liczenia. Odpowiedź 4 V to wynik dzielnika z zamienionymi oporami — klasyczny dystraktor.

::: metoda Jeśli pytają też o $R_T$ (albo o $J_N$)
$R_T$ = opór widziany z zacisków po **wyzerowaniu źródeł niezależnych** (napięciowe → zwarcie, prądowe → rozwarcie) i **zostawieniu** źródeł sterowanych. W tym obwodzie: $R_T = 4\,\Omega \parallel 6\,\Omega + 12\,\Omega = 2{,}4 + 12 = 14{,}4\ \Omega$, a $J_N = E_T/R_T = 6/14{,}4 = 0{,}42\ \text{A}$. Para $(E_T, R_T)$ i para $(J_N, R_T)$ to to samo źródło w dwóch kostiumach.
:::

### 3.4 Norton: $J_N$ liczone przez zwarcie

To najczęściej punktowane zadanie z liter F i H, a zarazem miejsce, w którym najłatwiej stracić czas — jeśli liczy się cały obwód, zamiast zwarciu się przyjrzeć.

::: figura zadania/24Z_A_1_H.png | Klucz 24Z_A_1, pytanie H. Odpowiedź prawidłowa: 1 mA.
:::

**Ścieżka (40 s).**

1. **Zewrzyj zaciski A–B** (rysunek: kreska między A i B).
2. Popatrz, **które wielkości sterujące** źródłami sterowanymi są teraz równe zeru.
3. Policz prąd płynący przez to zwarcie.

**Rachunek.** Opór 2 kΩ wisi bezpośrednio między A i B, więc po zwarciu panuje na nim napięcie $u = 0$. Źródło sterowane $g\cdot u$ daje wtedy $g\cdot 0 = 0$ — **znika z obwodu**, niezależnie od tego, ile wynosi $g = 2\ \text{mS}$. Zostaje samo źródło 1 mA, którego prąd nie ma innej drogi niż przez zwarcie:

$$J_N = 1\ \text{mA}$$

**Kontrola.** Wartość $g = 2\ \text{mS}$ jest w zadaniu po to, żeby skusić do liczenia $g\cdot u$. Ale skoro $u = 0$, to nie ma czego mnożyć. Odpowiedzi $2\ \text{mA}$ i $-2\ \text{mA}$ to wynik policzenia $g\cdot u$ przy $u$ wziętym z *osobno* rozwiązanego obwodu — najczęstsza pomyłka.

::: figura zadania/25Z_A_1_H.png | Klucz 25Z_A_1, pytanie H. Tym razem w rombie jest źródło sterowane napięciem $r\cdot i$, a $i$ to prąd oporu $R_2$. Odpowiedź prawidłowa: $J$.
:::

**Rachunek.** Zwarcie A–B bocznikuje $R_2$, więc prąd $i$ płynący przez $R_2$ **wynosi zero**. Źródło $r\cdot i$ daje $r\cdot 0 = 0\ \text{V}$ — czyli w obwodzie zwarciowym zachowuje się jak **kawałek przewodu**. To przewód łączy węzeł lewy z zaciskiem A, więc zwarcie obejmuje także $R_1$: cały prąd $J$ płynie przez zwarcie.

$$J_N = J$$

**Kontrola i pułapka.** Odpowiedź $J/(1 + r/R_1)$ (jest w kluczu jako dystraktor) powstaje z założenia, że przez romb płynie prąd zwarcia — a przecież jest on sterowany prądem $i$ gałęzi, którą zwarcie **zeruje**. To jest cała trudność tego zadania: *nie* „policz obwód”, tylko „zobacz, co zwarcie wyłącza”.

::: figura zadania/21L_A_1_F.png | Klucz 21L_A_1, pytanie F. W rombie źródło $3i$ sterowane prądem oporu 2 kΩ. Odpowiedź prawidłowa: −1 mA i 1 mA (klucz dopuszcza oba znaki).
:::

**Rachunek.** Zwarcie A–B zeruje napięcie na oporze 2 kΩ, więc $i = 0$, więc źródło $3i$ daje 0. Prąd zwarcia to po prostu prąd źródła 1 mA — z dokładnością do zwrotu. Klucz zaznacza **obie** odpowiedzi, $-1\ \text{mA}$ i $1\ \text{mA}$, bo zwrot zależy od umowy: jeśli $J_N$ wypływa z A, to $+1\ \text{mA}$, jeśli wpływa — $-1\ \text{mA}$. Na teście wybierasz ten znak, który jest w Twojej wersji.

::: zapamietaj Reguła dla całej rodziny F/H
**Zwarcie → napięcia sterujące = 0. Rozwarcie → prądy gałęzi wiszących = 0.** W obu przypadkach źródło sterowane „gaśnie” i obwód robi się trywialny. Zanim napiszesz pierwsze równanie, zadaj sobie pytanie: *co to zwarcie (rozwarcie) wyłącza?*
:::

### 3.5 Dopasowanie: moc maksymalna w oporze $R$

::: figura zadania/25Z_A_1_G.png | Klucz 25Z_A_1, pytanie G (2 pkt). Odpowiedź prawidłowa: 3/10 mW.
:::

**Rozpoznanie.** „Wartość oporu $R$ została dobrana tak, aby wydzielała się w nim maksymalna możliwa moc. Moc ta wynosi:”. W obwodzie jest jedno źródło i dwa opory, a $R$ wisi na zaciskach.

**Ścieżka (2 min).**

1. Odetnij $R$ i policz **$E_T$** (napięcie rozwarcia) oraz **$R_T$** (opór widziany z zacisków).
2. Warunek dopasowania: $R = R_T$.
3. Moc: $P_{max} = E_T^2/(4 R_T)$.

**Rachunek dla tego zadania.** $R_T = 3\,\text{k}\Omega \parallel 2\,\text{k}\Omega = 1{,}2\ \text{k}\Omega$. Napięcie rozwarcia to napięcie na oporze 2 kΩ w dzielniku z 3 kΩ:

$$E_T = 3\ \text{V}\cdot\frac{2}{3+2} = 1{,}2\ \text{V},\qquad P_{max} = \frac{(1{,}2)^2}{4\cdot 1200} = \frac{1{,}44}{4800}\ \text{W} = 0{,}3\ \text{mW} = \tfrac{3}{10}\ \text{mW}$$

::: wzor Wzór skrócony, który oszczędza pół minuty
Dla najczęstszego układu: źródło $E$, opór szeregowy $R_s$ i opór równoległy $R_p$ **na zaciskach** (tak jak wyżej: $R_s = 3\ \text{k\Omega}$, $R_p = 2\ \text{k\Omega}$):

$$P_{max} = \frac{E^2\,R_p}{4\,R_s\,(R_s + R_p)}$$

Wystarczy podstawić bez liczenia $E_T$ i $R_T$ osobno. Sprawdzenie: $9 \cdot 2000 / (4 \cdot 3000 \cdot 5000) = 0{,}3\ \text{mW}$.
:::

::: figura zadania/21L_A_1_H.png | Klucz 21L_A_1, pytanie H (2 pkt). Tu $E = 4\ \text{V}$, $R_s = 1\ \text{k\Omega}$, $R_p = 3\ \text{k\Omega}$. Odpowiedź prawidłowa: 3 mW.
:::

**Rachunek.** Ze wzoru skróconego:

$$P_{max} = \frac{4^2\cdot 3000}{4\cdot 1000\cdot 4000} = \frac{48\,000}{16\,000\,000}\ \text{W} = 3\ \text{mW}$$

albo klasycznie: $E_T = 4\cdot 3/4 = 3\ \text{V}$, $R_T = 1\ \text{k\Omega} \parallel 3\ \text{k\Omega} = 0,75\ \text{k\Omega}$, $P = 9/(4\cdot 750) = 3\ \text{mW}$.

**Kontrola.** Moc maksymalna musi być **mniejsza** od mocy, jaką źródło daje przy zwarciu ($E^2/R_s$), i większa od zera. Tu $E^2/R_s = 16\ \text{mW}$, więc 3 mW jest w dobrym przedziale. Dystraktory $12\ \text{mW}$, $16\ \text{mW}$ to moce „przy zwarciu” — nieosiągalne dla odbiornika.

### 3.6 Moc dysponowana — to ta sama liczba

::: figura zadania/24Z_A_1_G.png | Klucz 24Z_A_1, pytanie G (2 pkt). Odpowiedź prawidłowa: 9 mW.
:::

**Rozpoznanie.** „Moc dysponowana źródła na lewo od zacisków AB wynosi:”.

**Definicja w jednym zdaniu.** Moc dysponowana to **największa moc, jaką dwójnik może oddać odbiornikowi** — czyli dokładnie $P_{max}$ z poprzedniego rozdziału. Nie trzeba nic nowego liczyć, tylko $E_T$ i $R_T$.

**Rachunek.** Źródło prądowe 4 mA i opór 3 kΩ tworzą źródło rzeczywiste: $E_T = J\cdot R_1 = 4\ \text{mA}\cdot 3\ \text{k}\Omega = 12\ \text{V}$, $R_T = 3\ \text{k}\Omega + 1\ \text{k}\Omega = 4\ \text{k}\Omega$ (opór 1 kΩ jest **szeregowo** z zaciskami).

$$P_{dysp} = \frac{E_T^2}{4R_T} = \frac{144}{4\cdot 4000}\ \text{W} = 9\ \text{mW}$$

**Kontrola.** $E_T = 12\ \text{V}$ jest większe od napięcia samego źródła? Nie ma „samego napięcia” — źródło jest prądowe, więc 12 V jest w porządku. Dystraktor $12\ \text{mW}$ to $E_T^2/R_T$ (moc przy zwarciu), $36\ \text{mW}$ to $E_T^2/R_w$ — oba to moce nieosiągalne, bo przy zwarciu odbiornik ma 0 Ω, a nie $R_T$.

::: zapamietaj Trzy moce, które łatwo pomylić
| Wielkość | Wzór | Kiedy występuje |
|---|---|---|
| moc przy zwarciu | $E_T^2/R_T$ | odbiornik $R = 0$ |
| **moc dysponowana = maksymalna** | $E_T^2/(4R_T)$ | odbiornik $R = R_T$ |
| moc źródła rzeczywistego zasilającego $R$ | $E_T^2 R/(R_T+R)^2$ | dowolne $R$ |

W zadaniach „dobierz $R$, by moc była maksymalna” **zawsze** chodzi o środkowy wiersz.
:::

### 3.7 Prądowe prawo Kirchhoffa: jeden węzeł i jedna kreska

::: figura zadania/24Z_A_1_E.png | Klucz 24Z_A_1, pytanie E. Odpowiedź prawidłowa: 1 A.
:::

**Ścieżka (30 s).**

1. Wybierz **jeden** węzeł — ten, w którym spotykają się wszystkie opisane prądy.
2. Strzałka **do** węzła = plus, **od** węzła = minus.
3. Suma = 0.

**Rachunek.** Dla prawego węzła: wchodzi 2 A (od dołu) i $I$, wychodzi 3 A (do góry, w lewo). Zatem

$$2 + I = 3 \quad\Rightarrow\quad I = 1\ \text{A}$$

Uwaga na kierunki: strzałka „3 A” jest narysowana **w lewo**, czyli prąd *wychodzi* z prawego węzła; strzałka „1 A” dotyczy lewego węzła i jest w tym zadaniu informacją zbędną. Cała trudność to nie rachunek, a odczytanie grotów.

::: figura zadania/23Z_A_1_E.png | Klucz 23Z_A_1, pytanie E. Odpowiedź prawidłowa: „układ jest sprzeczny”.
:::

**Rachunek (i lekcja).** 1 A i 2 A są **wymuszone** i oba wchodzą do tego samego węzła — a węzeł nie ma żadnego innego wyjścia (oba „końce” są zwarte tym samym przewodem, w którym płynie $I$). Bilans nie może się zamknąć:

$$1 + 2 \neq 0$$

Taki układ **nie istnieje fizycznie** — i to jest prawidłowa odpowiedź. Kontrola zajmuje 5 sekund i jest pewnym punktem: jeśli suma prądów wymuszonych w węźle nie może dać zera, żadna liczba nie jest poprawna.

::: pulapka Kiedy odpowiedź brzmi „sprzeczny” / „za mało danych”
Klucze mają takie odpowiedzi w kilku miejscach i nie są to żarty. Warunki, po których je poznasz:

* prądy wymuszone przez źródła **nie bilansują się** w węźle lub w oczku ($1 + 2 = 0$? nie),
* dwa idealne źródła napięciowe o **różnych** SEM połączone równolegle,
* dwa idealne źródła prądowe o **różnych** prądach połączone szeregowo.

Najpierw sprawdź bilans, dopiero potem licz.
:::

### 3.8 Superpozycja: jedna składowa, nie cały obwód

::: figura zadania/23Z_A_1_F.png | Klucz 23Z_A_1, pytanie F. Odpowiedź prawidłowa: $-J_1 R_1/(R_1+R_2)$.
:::

**Rozpoznanie.** „W metodzie superpozycji składowa prądu $I$ pochodząca od źródła $J_1$ wynosi:”. W obwodzie są dwa źródła niezależne i co najmniej jedno sterowane.

**Ścieżka (90 s).**

1. **Zostaw tylko $J_1$**: $E \to \text{zwarcie}$, $J_2 \to ro \text{zwarcie}$, $J_1 \to \text{bez zmian}$.
2. Zauważ, co się stało: zwarcie $E$ przyłącza prawy koniec $R_2$ do szyny dolnej, więc $R_1$ i $R_2$ stoją **równolegle**.
3. Policz **dzielnik prądu**: $I = J_1 \cdot R_1/(R_1 + R_2)$.
4. Ustal znak z grotów.

**Rachunek.** Źródło $J_1$ ma strzałkę **w dół**, czyli wypycha prąd do szyny dolnej i zasysa go z węzła górnego. Prąd wraca do węzła przez $R_1$ i $R_2$, więc przez $R_2$ płynie **w lewo** (od prawego końca do węzła). Natomiast $I$ jest zaznaczone **w dół**, w gałęzi źródła $E$ — czyli prąd wpływający do tego węzła od strony $R_2$ jest dla $I$ ujemny:

$$I^{(J_1)} = -J_1\,\frac{R_1}{R_1+R_2}$$

**Kontrola.** Dla $R_1 \gg R_2$ wynik dąży do $-J_1$ (prawie cały prąd idzie przez $R_2$) — zgadza się z intuicją. Dystraktor $-J_1 R_2/(R_1+R_2)$ to dzielnik z zamienionymi oporami: **w dzielniku prądu w liczniku stoi opór *drugiej* gałęzi**.

::: metoda Dzielnik prądu — jedna linijka, którą warto wykuć
Prąd gałęzi $R_1$ przy źródle $J$ zasilającym równoległe $R_1 \parallel R_2$:

$$I_1 = J\,\frac{R_2}{R_1+R_2}$$

W liczniku jest opór **drugiej** gałęzi. (W dzielniku napięcia jest odwrotnie: $U_2 = E R_2/(R_1+R_2)$ — w liczniku opór **tej** gałęzi, na której mierzymy napięcie.)
:::

### 3.9 Wzmacniacz operacyjny: cała litera D w dwóch krokach

::: figura zadania/25Z_A_1_D.png | Klucz 25Z_A_1, pytanie D. Wtórnik napięciowy: źródło $E$ na wejściu $+$, opór $R_1$ w pętli sprzężenia zwrotnego. Odpowiedź prawidłowa: $E$.
:::

**Rozpoznanie.** Trójkąt ze znakami $+$ i $-$, w pętli opór $R_1$, na wyjściu dzielnik z $R_2$, na wejściu $+$ źródło $E$. Odpowiedzi są iloczynami typu $E(1 + R_1/R_2)$ i $E(1 + R_2/R_1)$.

**Ścieżka (45 s).** Dwa kroki, zawsze te same:

1. **Wzmacniacz jest idealny**: $u_+ = u_-$ (nic się nie „wzmacnia” w sensie napięcia wejściowego — ono tylko wyrównuje wejścia).
2. **Do wejść nie wpływa prąd**: przez $R_1$ i $R_2$ płynie tylko prąd wyjścia, więc w pętli z samym $R_1$ nie ma spadku napięcia.

**Rachunek.** $u_+ = E$ (źródło $E$ wprost na wejściu $+$). Opór $R_1$ łączy wyjście z wejściem $-$ i nie płynie przez niego prąd, więc $u_- = U$. Z $u_+ = u_-$ dostajemy od razu

$$U = E$$

$R_1$ i $R_2$ nie zmieniają wyniku — $R_2$ obciąża wyjście, ale idealny wzmacniacz daje sobie z tym radę. **To jest całe zadanie**: odpowiedzi $E(1 + R_1/R_2)$ i $E(1 + R_2/R_1)$ to wzory na wzmocnienie nieodwracające, czyli odpowiedź na *inne* pytanie.

::: zapamietaj Kiedy $E(1 + R_1/R_2)$ jest naprawdę poprawne
Gdy źródło $E$ stoi na **wejściu $-$** przez dzielnik, a wejście $+$ jest uziemione (układ odwracający) — wtedy $U = -E R_1/R_2$. Gdy $E$ jest na wejściu $+$, a $R_1$/$R_2$ tworzą dzielnik **w pętli sprzężenia** — wtedy $U = E(1 + R_1/R_2)$. Rozróżnienie zajmuje 5 sekund: **popatrz, do którego wejścia dochodzi źródło, a które jest uziemione.**
:::

### 3.10 Punkt pracy elementu nieliniowego: dwa opory z jednego wykresu

To najczęstsze pytanie całego Testu 1 (15 z 17 pytań z literą B w bazie). Zawsze o to samo: z charakterystyki $i(u)$ odczytać **opór statyczny** i **dynamiczny** w punkcie pracy.

::: figura zadania/25Z_A_1_B.png | Klucz 25Z_A_1, pytanie B. Element zasilony z idealnego źródła prądowego 3 mA. Odpowiedź prawidłowa: $R_s = 1{,}33$ kΩ, $R_d = 0{,}5$ kΩ.
:::

**Ścieżka (90 s).**

1. **Znajdź punkt pracy.** Idealne źródło prądowe **wymusza prąd**, więc szukasz na wykresie $i = 3\ \text{mA}$ — tam, gdzie krzywa przecina tę poziomą linię.
2. **Opór statyczny** to sieczna **od początku układu**: $R_s = u/i$ w tym punkcie.
3. **Opór dynamiczny** to **styczne nachylenie** w tym punkcie: $R_d = \Delta u/\Delta i$.

**Rachunek (sprawdzenie odpowiedzi).** W punkcie pracy $i = 3\ \text{mA}$ i $u = 4\ \text{V}$:

$$R_s = \frac{u}{i} = \frac{4\ \text{V}}{3\ \text{mA}} = 1{,}33\ \text{k}\Omega$$

Styczna w tym punkcie podnosi się o $0{,}5$ V na każde $1$ mA, czyli

$$R_d = \frac{\Delta u}{\Delta i} = 0{,}5\ \text{k}\Omega$$

**Kontrola.** Dla charakterystyki **wypukłej** (prąd rośnie szybciej niż liniowo — właśnie tak wygląda ten wykres) zawsze $R_d < R_s$. Jeśli w Twoim wyniku $R_d > R_s$, to znak, że zamieniłeś wielkości — a dystraktor „$R_s = 1{,}33$ kΩ, $R_d = 2$ kΩ” jest w kluczu dokładnie po to, żeby to sprawdzić.

::: pulapka Trzy pułapki odczytu z wykresu
1. **Źródło napięciowe vs prądowe.** Źródło napięciowe $E$ → szukasz punktu na pionowej linii $u = E$. Źródło prądowe $J$ → na poziomej $i = J$. Pomylenie tych dwóch daje zupełnie inny punkt.
2. **Jednostki osi.** Oś $i$ w mA, oś $u$ w V — wtedy $u/i$ wychodzi w **kΩ**, nie w Ω. To najczęstszy błąd rachunkowy w tym zadaniu.
3. **Styczna ≠ sieczna z sąsiedniego punktu.** $R_d$ bierz z nachylenia *w punkcie pracy*; jeśli krzywa jest mocno zakrzywiona, policz styczną z dwóch najbliższych punktów siatki.
:::

### 3.11 Pytania jakościowe (litera C): nie licz, rozstrzygaj

W pytaniach typu „W przedstawionym układzie o niezerowych wartościach elementów napięcie $U$ na źródle prądowym: 1. zależy od $E$, 2. nie zależy od $J_1$, …” nie ma nic do policzenia — jest do **rozstrzygnięcia**. Trzy reguły wystarczają:

* **Idealne źródło napięciowe** wymusza napięcie między swoimi zaciskami — wszystko, co jest z nim **równolegle**, nie wpływa na to napięcie.
* **Idealne źródło prądowe** wymusza prąd swojej gałęzi — wszystkie opory **szeregowo** z nim nie zmieniają prądu, zmieniają tylko rozkład napięć (i to one decydują o napięciu *na źródle*).
* Napięcie **na źródle prądowym** jest tym, co „zostaje” po odjęciu spadków na wszystkich oporach w pętli — dlatego zależy od **wszystkich** elementów w tej pętli, także od oporów, które dla prądu są obojętne.

::: metoda Test w 15 sekund
Zadaj sobie jedno pytanie: *„gdybym zmienił ten opór, czy zmieniłby się prąd wymuszony / napięcie wymuszone?”*. Jeśli nie — element jest obojętny i odpowiedź „nie zależy od…” jest prawdziwa. Jeśli tak — odwrotnie.
:::

### 3.12 Rozpoznawanie połączeń: dwa węzły i nic więcej

::: figura zadania/25Z_A_1_F.png | Klucz 25Z_A_1, pytanie F. Odpowiedź prawidłowa: „(1 i 2) oraz (3 i 5)”.
:::

**Rozpoznanie.** Pytanie „Połączenie równoległe występuje między parami elementów:”, schemat z pięcioma oporami i numerami, odpowiedzi w stylu „(1 i 2) oraz (3 i 5)”.

**Ścieżka (30 s).** Dwa opory są **równoległe** wtedy i tylko wtedy, gdy są przyłączone do **dokładnie tej samej pary węzłów**. Nie „wyglądają podobnie”, nie „są obok siebie” — muszą mieć wspólny początek i wspólny koniec. Praktyczny trik: **zamaluj jeden węzeł** (wszystko, co połączone przewodem bez elementu) i sprawdź, które opory dotykają obu zamalowanych obszarów.

**Rachunek.** Opory 1 i 2 wiszą między tym samym górnym węzłem a tym samym węzłem środkowym — para (1, 2). Opory 3 i 5 wiszą między lewym i prawym węzłem szyny dolnej, połączonej z górą przez idealne przewody — para (3, 5). Opór 4 stoi między węzłem środkowym a szyną dolną, więc jest **szeregowo** względem równoległej pary — nie tworzy pary równoległej z żadnym pojedynczym oporem.

::: pulapka Pułapka „wygląda na szereg”
Dwa opory narysowane jeden za drugim bywają równoległe, jeśli przewód między nimi nie prowadzi nigdzie indziej — a wtedy są to **te same dwa węzły**. Zanim odpowiesz, prześledź przewody do końca, a nie tylko do najbliższego zakrętu.
:::

## 4. Kontrola wyniku w pięć sekund

Zanim wpiszesz odpowiedź do tabelki, przejdź tę listę. Kosztuje 5 sekund, wyłapuje większość błędów.

| Pytanie kontrolne | Przykład z tego dokumentu |
|---|---|
| Czy wynik ma sens przy $g = 0$ / $\beta = 0$ / $J = 0$? | $1/(G-g) \to 1/G$ ✔ |
| Czy znak jest zgodny z grotami? | superpozycja: $-J_1R_1/(R_1+R_2)$ |
| Czy moc jest mniejsza od $E^2/R_s$? | 3 mW < 16 mW ✔ |
| Czy $E_T$ jest mniejsze od $E$ w dzielniku? | 6 V < 10 V ✔ |
| Czy prąd zwarcia nie jest większy od prądu źródła, gdy nie ma wzmocnienia? | $J_N = 1\ \text{mA}$ ✔ |
| Czy jednostka się zgadza (mA·kΩ = V)? | $4\ \text{mA} \cdot 3\ \text{k\Omega} = 12\ \text{V}$ ✔ |
| Czy wynik jest „ładny”? | $3/10\ \text{mW}$, $3\ \text{mW}$, $9\ \text{mW}$, $6\ \text{V}$ ✔ |

::: uwaga Sześć najczęstszych dystraktorów w kluczach
1. **Zamienione opory w dzielniku** ($4\ \text{V}$ zamiast $6\ \text{V}$, $-J_1R_2/\ldots$ zamiast $-J_1R_1/\ldots$).
2. **Zły znak źródła sterowanego** ($1/(G+g)$ zamiast $1/(G-g)$).
3. **Policzenie wielkości sterującej po zwarciu** ($J/(1+r/R_1)$ zamiast $J$).
4. **Moc przy zwarciu zamiast mocy dopasowania** ($E^2/R_T$ zamiast $E^2/(4R_T)$).
5. **Zignorowanie idealnego źródła** (traktowanie źródła prądowego jak oporu — $R - 1/g$).
6. **„Prawie zaokrąglone”** odpowiedzi w zadaniach pomiarowych (tam opisane w kompendium, §6.4).
:::

## 5. Ściąga: widzę → robię → wynik

| Widzę w treści | Robię | Wynik |
|---|---|---|
| romb <b>g·u</b> równolegle z oporem przewodności <b>G</b> | wpisuję prąd wypadkowy (G ± g)·u | 1/(G ± g) |
| romb <b>β·i</b> równolegle z oporem <b>R</b> | prąd wypadkowy (1 ± β)·i | R/(1 ± β) |
| romb szeregowo z oporem | prąd wymuszony przez źródło | 1/g |
| „SEM źródła zastępczego Thévenina” | rozwieram zaciski, liczę dzielnik | E<sub>T</sub> = E·R<sub>p</sub>/(R<sub>s</sub> + R<sub>p</sub>) |
| „wydajność prądowa źródła Nortona” | zwieram zaciski, wyłączam to, co zeruje sterowanie | J<sub>N</sub> = prąd zwarcia |
| „moc maksymalna” / „moc dysponowana” | R = R<sub>T</sub>, potem P = E<sub>T</sub>²/(4R<sub>T</sub>) | P<sub>max</sub> |
| „rozkład prądów w węźle” | KCL: strzałki do węzła +, od węzła − | ΣI = 0 |
| „składowa od źródła J<sub>1</sub>” | zeruję E (zwarcie) i J<sub>2</sub> (rozwarcie) | dzielnik prądu |
| „napięcie U na wyjściu wzmacniacza” | u<sub>+</sub> = u<sub>−</sub>, brak prądu wejść | zwykle U = E albo U = E(1 + R<sub>1</sub>/R<sub>2</sub>) |
| „opór statyczny / dynamiczny” | punkt pracy, potem sieczna i styczna | R<sub>s</sub> = u/i, R<sub>d</sub> = Δu/Δi |

<!--ANNEX-->

::: ciekawostka Gdzie szukać teorii
Ten dokument jest **praktyczny**: metody, rachunki, pułapki. Pełne wyprowadzenia, definicje i rozdziały teoretyczne (§1–§12, w tym 18 rozwiązanych zadań i aneks z mapowaniem wszystkich 252 pytań) są w kompendium: `kompendium/index.html` oraz `kompendium/kompendium.pdf`. Najlepszy tryb pracy: najpierw ten dokument (jak liczyć), potem kompendium (dlaczego tak), a na końcu własne testy na czas.
:::
