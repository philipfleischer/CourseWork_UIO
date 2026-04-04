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
        return f"Navn: {self.navn}. Elo: {self.elo}. Antall mål: {self.mål}"


class Kamp:
    def __init__(self, hjemme: str, borte: str):
        self.hjemmelag = hjemme
        self.bortelag = borte

    def simuler(self):
        print(f"Spilte kampen mellom {self.hjemmelag[0]} og {self.bortelag[0]} : {self.hjemmelag[2]} - {self.bortelag[2]}")



class Runde:
    def __init__(self, sesong: str):
        self.sesong = sesong
        self._kamper = []

    def __iter__(self):
        for _ in range(8):
            yield Kamp()

    def legg_til(self, hjemmelag_navn, bortelag_navn):
        #print(f"La til {hjemmelag_navn} - {bortelag_navn} i Runde-objektet!")
        pass


class Sesong:
    def __init__(self):
        self._lagliste = []

    def les_lag_fra_fil(self, filnavn):
        with open(filnavn, "r", encoding="utf-8") as f:
            data = f.read().split(",")
            lagnavn = data[0]
            elo = data[1]
            mål = data[2]
            lag = Lag(lagnavn, elo, mål)
            self._lagliste.append(lag)


    def runde(self, nummer):
        return Runde(nummer)
