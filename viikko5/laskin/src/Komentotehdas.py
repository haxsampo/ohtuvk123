#from functools import partial

class Komentotehdas:
    def __init__(self):
        self.edeltavaFunc = None
        self.edeltavaArvo = 0

        self.komennot = {
            "summa": Summa(),
            "erotus": Erotus(),
            "nollaus": Nollaus(),
            "kumoa": Kumoa()
        }

    def getEdeltavaFunc(self):
        return self.edeltavaFunc
        

class Summa:
    def __init__(self):
        pass

    def suorita(self, arvo, _sovellus,_komentotehdas,komento):
        if(komento=="kumoa"):           
            self.kumoa(arvo, _sovellus,_komentotehdas,komento)
        else:
            _komentotehdas.edeltavaFunc = "summa"
            _komentotehdas.edeltava = _sovellus.tulos
            _sovellus.plus(arvo)
    
    def kumoa(self, arvo, _sovellus,_komentotehdas,komento):
        _sovellus.aseta_arvo(_komentotehdas.edeltava)


class Erotus:
    def __init__(self):
        pass

    def suorita(self, arvo, _sovellus,_komentotehdas,komento):
        if(komento=="kumoa"):
            self.kumoa(arvo, _sovellus,_komentotehdas,komento)
        else:
            _komentotehdas.edeltavaFunc = "erotus"
            _komentotehdas.edeltava = _sovellus.tulos
            _sovellus.miinus(arvo)
    
    def kumoa(self, arvo, _sovellus,_komentotehdas,komento):
        _sovellus.aseta_arvo(_komentotehdas.edeltava)

class Nollaus:
    def __init__(self):
        pass

    def suorita(self, arvo, _sovellus,_komentotehdas,komento):
        if(komento=="kumoa"):
            self.kumoa(arvo, _sovellus,_komentotehdas,komento)
        else:
            _komentotehdas.edeltavaFunc = "nollaus"
            _komentotehdas.edeltava = _sovellus.tulos
            _sovellus.nollaa()
    
    def kumoa(self, arvo, _sovellus,_komentotehdas,komento):
        _sovellus.aseta_arvo(_komentotehdas.edeltava)

class Kumoa():
    def __init__(self):
        #palauta edellinen olento
        pass

    def suorita(self, arvo, _sovellus,_komentotehdas,komento):
        olento = _komentotehdas.komennot[_komentotehdas.getEdeltavaFunc()]
        olento.suorita(arvo, _sovellus,_komentotehdas,komento)
