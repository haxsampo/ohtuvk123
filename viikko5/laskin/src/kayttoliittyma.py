from tkinter import ttk, constants, StringVar
import Komentotehdas

class Kayttoliittyma:
    def __init__(self, sovellus, root, komentotehdas):
        self._sovellus = sovellus
        self._root = root
        self._komentotehdas = komentotehdas

        #self._komennot = {
        #    Komento.SUMMA: Summa(self._sovellus, self._syote_kentta.get()),
        #    Komento.EROTUS: Erotus(self._sovellus, self._syote_kentta.get()),
        #    Komento.NOLLAUS: Nollaus(self._sovellus, self._syote_kentta.get()),
        #    Komento.KUMOA: Kumoa(self._sovellus, self._syote_kentta.get())
        #}

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento("summa")
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento("erotus")
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento("nollaus")
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento("kumoa")
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        arvo = 0
        #siirrä arvotsekki vaikka inittiin tms
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        komento_olio = self._komentotehdas.komennot[komento]
        komento_olio.suorita(self._sovellus, arvo)

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)


