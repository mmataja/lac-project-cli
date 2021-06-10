Seminarski rad – zadatak i vrednovanje
Koristeći programski jezik Python potrebno je implementirati cjeloviti program s mogućnošću
izvođenja različitih obrada, uključujući fork-exec tehniku, postupanje po primitku signala i usklađivanje
višedretvenoga rada. Program izvodi određenu obradu ovisno o tome koju je stavku glavnoga izbornika
korisnik odabrao, a izvodi se sve dok korisnik eksplicitno ne prekine njegovo izvođenje odgovarajućom
naredbom.

U nastavku dokumenta opisane su osnovne i posebne funkcionalnosti programa koji treba osmisliti i
izvesti, kao i način vrednovanja rada.
Osnovne funkcionalnosti
U ovom je odjeljku dan opis osnovnih zahtjeva koje program mora zadovoljavati.
1. Pri pokretanju programa, na zaslon se ispisuje općenita pozdravna poruka, trenutni datum i
vrijeme oblika Sat*Minute*Sekunde DanUtjednu Dan+Mjesec+Godina, verzija
interpretora programskog jezika Python koja se koristi te naziv operacijskoga sustava koji se
koristi i korisničko ime korisnika trenutno prijavljenog za rad sa sustavom.
2. Program zatim korisniku nudi glavni izbornik oblika (samostalno dopuniti izgled izbornika)
1 – Kratki opis ili naziv 1. funkcionalnosti
2 – Kratki opis ili naziv 2. funkcionalnosti
3 – Kratki opis ili naziv 3. funkcionalnosti
4 – Kratki opis ili naziv 4. funkcionalnosti
5 – Kratki opis ili naziv 5. funkcionalnosti
6 – Kratki opis ili naziv 6. funkcionalnosti
exit ili logout – Završetak izvođenja programa
koji je jednak za sve korisnike te čeka na unos odgovarajuće opcije.
3. Program od korisnika traži unos jedne od opcija ponuđenih u glavnome izborniku. Ako je
unesena ispravna opcija, ona se izvršava (na način kako je opisano u poglavlju „Posebne
funkcionalnosti“).
a. Potrebno je implementirati prepoznavanje pogrešno unesene opcije
i. Pogreške tipa 17 ili exti (nepostojeći el. izbornika)
b. Ako korisnik pritisne tipku Enter umjesto unosa stavke izbornika, ništa se ne događa,
a na zaslon se ponovo ispisuje poruka o potrebnom unosu. Pritisak Entera umjesto
očekivanog unosa korisnika u bilo kojem dijelu programa treba pokrenuti ponovni
prikaz poruke u unosu, sve dok korisnik ne unese očekivanu vrijednost.
4. Nakon završetka izvođenja određene funkcionalnosti programa, korisniku se ponovo nudi
glavni izbornik (bez pozdravne poruke iz točke 1). Postupak se ponavlja do unosa naredbe
kraj ili izlaz (potrebno implementirati obje mogućnosti), kada program završava s
izvođenjem.
5. Program mora biti oblikovan na način da radi na bilo kojem računalu tj. platformi, neovisno o
nazivu kućnog direktorija korisnika, korisničkom imenu i sličnim podatcima. (Napomena: To,
primjerice, znači da adresa kućnog direktorija ne smije biti „hard code-ana“ već očitana iz
odgovarajućih izvora.)
1Odjel za informatiku, Sveučilište u Rijeci
Sveučilišni preddiplomski studij informatike
Operacijski sustavi (2020./2021.)
Posebne funkcionalnosti
U ovom je odjeljku dan opis konkretnih obrada koje program mora izvršiti odabirom određene stavke
izbornika.
-------------------------------------------------------------------------------------------------------
1. Stavka izbornika 1 – od korisnika se traži unos određene naredbe koju je moguće pokrenuti u
sučelju naredbenog retka. Ako korisnik ne unese naredbu u roku od 16 sekundi, korisniku se
prikazuje poruka da je vrijeme za unos završilo i ponovo se prikazuje glavni izbornik programa.
Naredbena se linija, osim naredbe, može sastojati i od 0 ili više parametara (grupiranih iz
jednog znaka minusa ili nabrojanih odvojeno, npr. -al ili -a -l), od jednog ili više
argumenata ili njihove kombinacije. Ispravnost unosa naredbe nije potrebno provjeravati.
Program zatim pokreće novi proces koji će izvesti unesenu naredbu s danim parametrima i
argumentima. Naredba koja se može izvesti treba rezultat svoga djelovanja prikazati korisniku
na zaslonu, pa završiti svoje izvođenje na uredan način (npr., proces ne smije postati zombi),
pri čemu proces roditelj ispisuje poruku o korektnoj izvršenosti. U slučaju da korisnik pokreće
naredbu cal bez argumenata, kalendar se obvezno mora prikazati u formatu namijenjenom
Ujedinjenom Kraljevstvu (engleski jezik, prvo prikazana nedjelja kao početni dan).

2. Stavka izbornika 2 – od korisnika se traži unos apsolutne ili relativne adrese 1 direktorija koji
treba obrisati u stablu direktorija. Program provjerava je li adresa točna (npr. unesena je samo
jedna adresa), postoji li objekt koji je potrebno brisati te može li ga se obrisati. U slučaju da je
uneseno više adresa ili u slučaju da adresa ne postoji, o tome treba obavijestiti korisnika. Ako
postoji, ali nije ga moguće obrisati (jer ima poddirektorije), o tome treba obavijestiti korisnika.
Ako postoji i može ga se obrisati, na zaslon je potrebno ispisati adresu direktorija koji je
nadređen objektu koji se briše te identifikator grupe njegova vlasnika, obrisati zadani objekt,
te na kraju ispisati sadržaj direktorija koji je nadređen objektu koji se briše kako bi se vidjelo
da zadani objekt više ne postoji.

3. Stavka izbornika 3 – omogućava korisniku unos broja signala koji će se poslati trenutnome
procesu (interpretoru naredbi). Trenutni proces ignorira sve procese čiji su brojevi u rasponu
od 1 do 8 a rezultiraju prekidanjem procesa u izvođenju i stvaranjem core datoteke. Sve ostale
signale program obrađuje kako je zadano. Ako je broj signala veći od 31, javlja se poruka o
pogrešnom unosu i upit za unos se ponavlja sve dok se ne unese korektna vrijednost. Za
zaprimljeni signal broj 14 ili 15, program na zaslon ispisuje poruku o zaprimljenom signalu i
njegovu rednu broju, zapisuje PPID i PID procesa, te trenutno stanje stoga u datoteku
stog1.txt koja se stvara u kućnom direktoriju, obavještava korisnika porukom o tome što
je napravio, pa nastavlja uobičajeno izvođenje (prikaz glavnoga izbornika).

4. Stavka izbornika 4 – u tri procesne dretve, u kojima su radni intervali proračuna raspoređeni
po vašoj želji, računa se zbroj svih neprostih brojeva iz intervala [0,1660000] koji se na
koncu proračuna i ispisuje na zaslon. Osim toga, svi neprosti brojevi iz intervala trebaju se
zapisati u listu naziva lista_brojeva čiji se sadržaj ispisuje na kraju proračuna. Pri
implementaciji je potrebno koristiti odgovarajući mehanizam za vremensko usklađivanje
višedretvenoga rada (samostalno procijeniti i odabrati koji mehanizam, temeljem vrste
problema koji se treba riješiti).

5. Stavka izbornika 5 – korisniku se omogućava unos cjelobrojne vrijednosti n veće od 2 450 000
(potrebno napraviti provjeru unosa n i ponuditi ponovni unos ako je vrijednost manja od
tražene). Pokreću se dvije procesne dretve: prva dretva radi listu neparnih brojeva zadanog
intervala [0,n], a druga upisuje listu dobivenih brojeva umanjenih za ¼ pojedinog broja
(elementa liste) u tekstnu datoteku umanjenje.txt, i to nakon što je lista u potpunosti
izrađena (dretva koja ju izrađuje identificira se vl. nazivom koji joj je dodijelio sustav te
prikazuje poruku o dovršenosti). Pri implementaciji je potrebno koristiti odgovarajući
mehanizam za vremensko usklađivanje višedretvenoga rada (samostalno procijeniti i odabrati
koji mehanizam, temeljem vrste problema koji se treba riješiti).

6. Stavka izbornika 6 – korisniku se omogućava unos pozitivne cjelobrojne vrijednosti, ne manje
od 10 ni veće od 177 000 (potrebno napraviti provjeru unosa i ponuditi ponovni unos ako je
vrijednost ne odgovara intervalu). Program od broja 55550550550550550550 oduzima
kvadrate brojeva u rasponu od 1 do unesene vrijednosti koristeći četiri dretve (vrijednosti
intervala proračuna rasporediti jednoliko po dretvama). Za svaku je dretvu potrebno
proračunati koliko se dugo vremenski izvodila, a po završetku proračuna svaka dretva na zaslon
ispisuje trajanje svoga izvođenja. Također, samo glavna dretva ispisuje na zaslon konačan
rezultat oduzimanja. Pri implementaciji je potrebno koristiti odgovarajući mehanizam za
vremensko usklađivanje višedretvenoga rada (samostalno procijeniti i odabrati koji
mehanizam, temeljem vrste problema koji se treba riješiti).
