class Osoba:
    def __init__(self, predmety, penezenka, lokace, kabat):
        self.predmety = predmety
        self.penezenka = penezenka
        self.kabat = kabat
        self.lokace = lokace

    def uprav_penezenku(self, o_kolik):
        self.penezenka += o_kolik

    def nasad_kabat(self):
        self.kabat = 1

    def nakup_predmet(self, predmet):
        pass

    def prodej_predmet(self, predmet):
        pass

    def presun(self, nova_lokace):
        self.lokace = nova_lokace


