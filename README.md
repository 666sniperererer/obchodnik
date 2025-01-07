# obchodnik
Textová hra obchodník

Zadání pro mini-projekt.
Výstupem teamu je jeden kód.
Vždy jeden sdílí obrazovku a ostatní mu radí. 
Po cca 20 minutách se prostřídáte.

Základ:
Hra, kde máte peníze - 100 Kč.
Je možné chodit mezi lokacemi (Hradčany, Václavák, Holešovice)
Při přechodu do jiné lokace je přičte počet dnů.
Po 14-ti dnech hra končí
Vypíše se finální počet peněz.

Rozšíření 1:
V každé lokace je možné kupovat předměty:
Utopenec (50-100kč)
Med (100-200kč)
Láhev pálavy (200-500kč)

Ve všech lokacích mohu prodat a koupit tyto předměty v libovolném množství (mám inventář svých věcí).
V každé lokaci je cena jiná - pevně určená v programu
Nemůžu nakoupit víc předmětů než mám peněz.
Nemůžu prodat předměty, které nemám.

Rozšíření 2:
Každé místo má náhodně vygenerovanou cenu pro předměty.
Pokaždé, když k místu přijdu, tak se cena u všech předmětů změní o náhodnou hodnotu (-5 až +5).
Př. na začáku je cena Utopence na Hradčanech 60kč. Když přijdu na Hradčany poprvé, cena se zvedne o 2 kč -> 62kč. Když přijdu na Hradčany podruhé, cena se sníží o 5kč-> 57kč.

Rozšíření 3:
Máme limitovaný počet předmětů (2), které si můžeme koupit.
Je možné zajít do speciální lokace "Večerka", kde je možné si koupit kabát, který
nám rozšíří inventář o 2 předměty (cena je 150kč). 
Je možné si zde koupit batoh, který nám rozšíří inventář o 3 předměty (cena 400kč )

Rozšíření 4:
Na konci hry se program zeptá na jméno. Výsledek se jménem ze přípíše do souboru highscores.txt. Obsah souboru se vypíše do konzole.

Pozn. 
Úloha slouží k procvičení objektového programování - tzn: 
Předmět je třída - pamatujeme si min a max cenu. Pamatuje si aktuální cenu.
Lokace je třída - v lokacích jsou uložené přeměty
Osoba je třída - pamatujeme si počet předmětů, kolik máme peněz, jestli máme kabát...

Každá třída bude v jiném souboru - procvičíme importy.
