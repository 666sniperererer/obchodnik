class Osoba:
    def __init__(self, predmety, penezenka, kabat):
        self.predmety = predmety
        self.penezenka = penezenka
        self.kabat = 0

    def uprav_penezenku(self, o_kolik):
        self.penezenka += o_kolik

    def nasad_kabat(self):
        self.kabat = 1

    def nakup_predmet(self, predmet):
        pass

