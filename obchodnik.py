from numpy.ma.extras import median

from lokace import Lokace
from osoba import Osoba
from predmet import Predmet
global aktualni_den
aktualni_den = 1

global max_predmetu
max_predmetu = 2

global mas_kabat
mas_kabat = 0

global mas_batoh
mas_batoh = 0

hradcany = Lokace("Hradčany",
                  Predmet("Utopenec", 50, 100),
                  Predmet("Med", 100, 200),
                  Predmet("Láhev pálavy", 200,500))
vaclavak = Lokace("Václavák",
                  Predmet("Utopenec", 50, 100),
                  Predmet("Med", 100, 200),
                  Predmet("Láhev pálavy", 200,500))
holesovice = Lokace("Holešovice",
                    Predmet("Utopenec", 50, 100),
                    Predmet("Med", 100, 200),
                    Predmet("Láhev pálavy", 200,500))
vecerka = Lokace("Večerka", "nic", "nic", "nic")

obchodnik = Osoba("Honza", [], 100, hradcany, 0)

#hlavní cyklus
cinnost = 0

while cinnost != 99:
    print(f"Nyní jsi v lokaci: {obchodnik.lokace}")
    print(f"V peněžence máš {obchodnik.penezenka} Kč")
    print(f"Aktuální den: {aktualni_den}")
    if obchodnik.lokace != vecerka:
        print(f"Utopenec zde stojí: {obchodnik.lokace.predmet1.akt_cena} Kč")
    if obchodnik.lokace != vecerka:
        print(f"Med zde stojí: {obchodnik.lokace.predmet2.akt_cena} Kč")
    if obchodnik.lokace != vecerka:
        print(f"Láhev pálavy zde stojí: {obchodnik.lokace.predmet3.akt_cena} Kč")
    print(f"U sebe máš: {obchodnik.predmety}")
    print(f"Počet předmětů je: {len(obchodnik.predmety)}/{max_predmetu}")
    cinnost = int(input(f"Co chceš dělat? \n"
        f" 1 - Přesun \n"
        f" 2 - Nákup \n"
        f" 3 - Prodej \n"))

    if cinnost == 1: #přesun na jinou lokaci, aktuální den +1

        nova_lokace = int(input("Zadej číslo nové lokace: \n"
              "1 - Hradčany \n"
              "2 - Václavák \n"
              "3 - Holešovice \n"
              "4 - Večerka \n"))

        if nova_lokace == 1:
            obchodnik.presun(hradcany)
            print(f"Přesunul jsi se na {nova_lokace}")
            aktualni_den += 1
            obchodnik.lokace.predmet1.upravcenu()
            obchodnik.lokace.predmet2.upravcenu()
            obchodnik.lokace.predmet3.upravcenu()

        if nova_lokace == 2:
            obchodnik.presun(vaclavak)
            print(f"Přesunul jsi se na {nova_lokace}")
            aktualni_den += 1
            obchodnik.lokace.predmet1.upravcenu()
            obchodnik.lokace.predmet2.upravcenu()
            obchodnik.lokace.predmet3.upravcenu()

        if nova_lokace == 3:
            obchodnik.presun(holesovice)
            print(f"Přesunul jsi se na {nova_lokace}")
            aktualni_den += 1
            obchodnik.lokace.predmet1.upravcenu()
            obchodnik.lokace.predmet2.upravcenu()
            obchodnik.lokace.predmet3.upravcenu()

        if nova_lokace == 4:
            obchodnik.presun(vecerka)
            print(f"Přesunul jsi se do Večerky.")
            aktualni_den += 1
            koupit_inv = int(input("Co chceš dělat? \n"
                                   "1 - Koupit Kabát za 150,- (+2 INV) \n"
                                   "2 - Koupit Batoh za 400,- (+3 INV) \n"
                                   "3 - Nedělat nic.\n "))
            if koupit_inv == 1:
                if obchodnik.penezenka >= 150 and mas_kabat == 0:
                    print("Koupil jsi kabát za 150, můžeš nosit +2 předměty")
                    max_predmetu += 2
                    mas_kabat = 1
                else:
                    print("Nelze, nemáš dost peněz, nebo už kabát máš!")

            if koupit_inv == 2:
                if obchodnik.penezenka >= 400 and mas_batoh == 0:
                    print("Koupil jsi batoh za 400, můžeš nosit +3 předměty")
                    max_predmetu += 3
                    mas_batoh = 0
                else:
                    print("Nelze, nemáš dost peněz, nebo už batoh máš!")

        elif nova_lokace > 4:
            print(f"Chybná lokace! Lokace {nova_lokace} neexistuje!")

    if cinnost == 2: #nákup
        if max_predmetu == len(obchodnik.predmety):
            print("Nemůžeš nakupovat, není místo v inventáři.")
        else:
            co_koupit = int(input(f"Co chceš koupit? Máš v peněžence {obchodnik.penezenka} Kč \n"
                              f"1 - Utopenec za {obchodnik.lokace.predmet1.akt_cena}\n"
                              f"2 - Med za {obchodnik.lokace.predmet2.akt_cena} \n"
                              f"3 - Láhev pálavy za {obchodnik.lokace.predmet3.akt_cena}\n"))

            if co_koupit == 1:
                if obchodnik.penezenka >= obchodnik.lokace.predmet1.akt_cena:
                    obchodnik.predmety.append("Utopenec")
                    print(f"Nakoupil jsi 1 Utopenec za {obchodnik.lokace.predmet1.akt_cena}")
                    obchodnik.penezenka -= obchodnik.lokace.predmet1.akt_cena
                else:
                    print(f"Na to nemáš!")

            if co_koupit == 2:
                if obchodnik.penezenka >= obchodnik.lokace.predmet2.akt_cena:
                    obchodnik.predmety.append("Med")
                    print(f"Nakoupil jsi 1 Med za {obchodnik.lokace.predmet2.akt_cena}")
                    obchodnik.penezenka -= obchodnik.lokace.predmet2.akt_cena
                else:
                    print(f"Na to nemáš!")

            if co_koupit == 3:
                if obchodnik.penezenka >= obchodnik.lokace.predmet3.akt_cena:
                    obchodnik.predmety.append("Med")
                    print(f"Nakoupil jsi 1 Med za {obchodnik.lokace.predmet3.akt_cena}")
                    obchodnik.penezenka -= obchodnik.lokace.predmet3.akt_cena
                else:
                    print(f"Na to nemáš!")


    if cinnost == 3: #prodej
        co_prodat = int(input(f"Co chceš prodat? U sebe máš {obchodnik.predmety} \n"
                          f"1 - Utopenec za {obchodnik.lokace.predmet1.akt_cena}\n"
                          f"2 - Med za {obchodnik.lokace.predmet2.akt_cena} \n"
                          f"3 - Láhev pálavy za {obchodnik.lokace.predmet3.akt_cena}\n"))

        if co_prodat == 1:
            obchodnik.predmety.remove("Utopenec")
            obchodnik.penezenka += obchodnik.lokace.predmet1.akt_cena
        if co_prodat == 2:
            obchodnik.predmety.remove("Med")
            obchodnik.penezenka += obchodnik.lokace.predmet2.akt_cena
        if co_prodat == 3:
            obchodnik.predmety.remove("Láhev pálavy")
            obchodnik.penezenka += obchodnik.lokace.predmet3.akt_cena

    if cinnost == 99: #ukončení hry uživatelem
        print("Ukončil jsi hru!")
        with open("./highscores.txt", "a", encoding="utf-8") as file:
            file.write(f"{obchodnik.nazev} vydělal celkem {obchodnik.penezenka}\n")


    if aktualni_den >= 14: #konec hry, spočítej a zapiš do highscore
        print(f"Konec hry! Tvůj konečný obsah peněženky je: {obchodnik.penezenka} Kč")
        with open("./highscores.txt", "a", encoding="utf-8") as file:
            file.write(f"{obchodnik.nazev} vydělal celkem {obchodnik.penezenka}\n")

with open("./highscores.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")