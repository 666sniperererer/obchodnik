class Lokace:
    def __init__(self, nazev, predmet1, predmet2, predmet3):
        self.nazev = nazev
        self.predmet1 = predmet1
        self.predmet2 = predmet2
        self.predmet3 = predmet3

    def __str__(self):
        return self.nazev
