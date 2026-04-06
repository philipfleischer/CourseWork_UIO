class Dato:
    def __init__(self, ddmmåååå: str):
        self.endre_til(ddmmåååå)

    def hent_dag(self):
        return self.dag

    def hent_maaned(self):
        return self.maaned

    def hent_år(self):
        return self.aar

    def dag_er_lik(self, dag_nr):
        return self.dag == dag_nr

    def er_skuddaar(self):
        return (self.aar % 4 == 0 and self.aar % 100 != 0) or (self.aar % 400 == 0)

    def dager_i_maaned(self):
        if self.maaned in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.maaned in [4, 6, 9, 11]:
            return 30
        elif self.maaned == 2:
            return 29 if self.er_skuddaar() else 28

    def neste_dag(self):
        self.dag += 1

        if self.dag > self.dager_i_maaned():
            self.dag = 1
            self.maaned += 1

            if self.maaned > 12:
                self.maaned = 1
                self.aar += 1

        self.dato = f"{self.dag}.{self.maaned}.{self.aar}"

    def endre_til(self, ddmmåååå):
        self.dato = str(ddmmåååå)
        deler = self.dato.split(".")
        self.dag = int(deler[0])
        self.maaned = int(deler[1])
        self.aar = int(deler[2])

    def __str__(self):
        return self.dato


class Lag:
    def __init__(self, navn: str, elo: int, mål: float):
        self.navn = navn
        self.elo = elo
        self.mål = mål

    def __str__(self):
        return self.navn


class Kamp:
    def __init__(self, hjemme: Lag, borte: Lag):
        self.hjemme = hjemme
        self.borte = borte
        self.hmål = None
        self.bmål = None

    def simuler(self):
        self.hmål = random.randint(0, 9)
        self.bmål = random.randint(0, 9)

    def __str__(self):
        if self.hmål is None or self.bmål is None:
            return f"{self.hjemme} - {self.borte}"
        return f"{self.hjemme} - {self.borte} {self.hmål} - {self.bmål}"


class Runde:
    def __init__(self, sesong):
        self.sesong = sesong
        self._kamper = []

    def legg_til(self, hjemmelag_navn, bortelag_navn):
        hjemmelag = self.sesong._lag[hjemmelag_navn]
        bortelag = self.sesong._lag[bortelag_navn]
        kamp = Kamp(hjemmelag, bortelag)
        self._kamper.append(kamp)

    def __iter__(self):
        return iter(self._kamper)


class Sesong:
    def __init__(self):
        self._lag = {}
        self._runder = {}

    def les_lag_fra_fil(self, filnavn):
        with open(filnavn, "r", encoding="utf-8") as fil:
            for linje in fil:
                linje = linje.strip()
                if linje == "":
                    continue
                navn, elo, mål = linje.split(", ")
                self._lag[navn] = Lag(navn, int(elo), float(mål))

    def runde(self, nummer):
        if nummer not in self._runder:
            self._runder[nummer] = Runde(self)
        return self._runder[nummer]
