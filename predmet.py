import random


class Predmet:
    def __init__(self, nazev, min_cena, max_cena):
        self.nazev = nazev
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.akt_cena = random.randint(min_cena,max_cena)

    def __str__(self):
        return self.nazev

    def upravcenu(self):
        self.akt_cena += random.randint(-5,5)