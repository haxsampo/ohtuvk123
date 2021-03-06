KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.kapasiteetti_kasvatuskoko_tsek(kapasiteetti, kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = self.kapasiteetti_kasvatuskoko_tsek(kasvatuskoko, kapasiteetti, OLETUSKASVATUS)
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kapasiteetti_kasvatuskoko_tsek(self, arvo, kapasiteetti, ifnone):
        if arvo is None:
            return ifnone
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            return kapasiteetti

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True           
        return False



    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm += 1
            return True
        else:
            pass

        if not self.kuuluu(n):
            self.lisaa_n_ei_kuulu(n)
            return True

        return False

    def lisaa_n_ei_kuulu(self,n):
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        if self.alkioiden_lkm % len(self.ljono) == 0:
            taulukko_old = self.ljono
            self.kopioi_taulukko(self.ljono, taulukko_old)
            self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(taulukko_old, self.ljono)      

    def poista(self, n):
        nIndeksi = self.indeksin_etsinta(n)
        if nIndeksi != -1:
            self.listan_lyhentaminen(nIndeksi)
            return True

        return False

    def indeksin_etsinta(self, n):
        nIndeksi = -1
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                nIndeksi = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[i] = 0
                break
        return nIndeksi

    def listan_lyhentaminen(self, i):
        apu = 0
        for j in range(i, self.alkioiden_lkm - 1):
            apu = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu

        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
