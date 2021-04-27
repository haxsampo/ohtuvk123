from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka
from Komentotehdas import Komentotehdas


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")
    komentotehdas = Komentotehdas()

    kayttoliittyma = Kayttoliittyma(sovellus, window, komentotehdas)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
