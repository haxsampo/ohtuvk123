

class Komentotehdas:
    def __init__(self):
        self.edeltava = 0
        self.komennot = {
            "summa": Summa(),
            "erotus": Erotus(),
            "nollaus": Nollaus(),
            "kumoa": Kumoa()
        }

class Summa:
    def _init_(self):
        pass
    
    def suorita(self, sovelluslogiikka, syote):
        sovelluslogiikka.plus(syote)

class Erotus:
    def _init_(self, sovelluslogiikka, syote):
        pass

    def suorita(self, sovelluslogiikka, syote):
        sovelluslogiikka.miinus(syote)

class Nollaus:
    def _init_(self, sovelluslogiikka, syote):
        pass

    def suorita(self, sovelluslogiikka, syote):
        sovelluslogiikka.nollaa()

class Kumoa():
    def _init_(self, sovelluslogiikka, syote):
        pass

    def suorita(self, sovelluslogiikka, syote):
        #sovelluslogiikka.plus(syote)
        pass