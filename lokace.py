class Lokace:
    def __init__(self, nazev, predmety):
        self.nazev = nazev
        #self.predmet1 = predmet1
        #self.predmet2 = predmet2
        #self.predmet3 = predmet3
        self.predmety = predmety

    def __str__(self):
        return self.nazev
