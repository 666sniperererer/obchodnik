class Menu:
    def __init__(self, polozky_menu):
        self.polozky_menu = polozky_menu

    def vykresli_menu(self):
        print("--------------------------")
        for polozka in self.polozky_menu.items():
            print(f"{polozka[0]} - {polozka[1]}")

    def vyber_polozku(self):
        vyber = input("Co vybereš? ")


testmenu = Menu({1:"První položka",2:"Druhá položka",3:"Třetí položka"})

testmenu.vykresli_menu()

testmenu.vyber_polozku()
