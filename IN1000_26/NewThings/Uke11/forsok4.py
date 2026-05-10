class Land:
    def __init__(self, navn, kommune_filnavn, fylkes_filnavn):
        self._navn = navn
        self._fylker = {}  # nøkkel: fylkesnummer, verdi: Fylke-objekt

        # Leser inn fylker først, fordi kommunene skal legges inn i riktig fylke.
        with open(fylkes_filnavn, "r", encoding="utf-8") as fylke_fil:
            for linje in fylke_fil:
                linje = linje.strip()
                if linje == "":
                    continue

                fylkes_nr, fylkes_navn = linje.split(",")
                self.legg_til_fylke(fylkes_nr, fylkes_navn)

        # Leser inn kommuner etterpå. De to første sifrene i kommunenummeret
        # brukes som fylkesnummer.
        with open(kommune_filnavn, "r", encoding="utf-8") as kommune_fil:
            for linje in kommune_fil:
                linje = linje.strip()
                if linje == "":
                    continue

                kommune_nr, kommune_navn = linje.split(",")
                fylkes_nr = kommune_nr[:2]

                fylke = self.hent_fylke(fylkes_nr)
                if fylke is not None:
                    fylke.legg_til_kommune(kommune_nr, kommune_navn)

    def hent_navn(self):
        return self._navn

    def legg_til_fylke(self, fylkesnr, fylkesnavn):
        if fylkesnr not in self._fylker:
            nytt_fylke = Fylke(fylkesnr, fylkesnavn, self)
            self._fylker[fylkesnr] = nytt_fylke
        else:
            print(f"Fylke nr. {fylkesnr} finnes allerede i {self._navn}")

    def hent_fylke(self, fylkesnr):
        if fylkesnr in self._fylker:
            return self._fylker[fylkesnr]

        print(f"{self._navn} har ikke noe fylke med nummer {fylkesnr}")
        return None

    def __iter__(self):
        # Gjør at vi kan skrive: for fylke in land:
        for fylkes_nr in self._fylker:
            yield self._fylker[fylkes_nr]

    def __len__(self):
        # Her betyr len(land): totalt antall kommuner i landet.
        antall_kommuner = 0
        for fylke in self:
            antall_kommuner += len(fylke)
        return antall_kommuner

    def __str__(self):
        utskrift = f"{self._navn} ({len(self._fylker)} fylker, {len(self)} kommuner)\n"

        for fylke in self:
            utskrift += str(fylke)

        return utskrift


class Fylke:
    def __init__(self, fylkes_nr, fylkes_navn, land):
        self._fylkes_nr = fylkes_nr
        self._fylkes_navn = fylkes_navn
        self._land = land
        self._kommuner = {}  # nøkkel: kommunenummer, verdi: Kommune-objekt

    def legg_til_kommune(self, kommunenr, kommunenavn):
        if kommunenr not in self._kommuner:
            ny_kommune = Kommune(kommunenr, kommunenavn, self)
            self._kommuner[kommunenr] = ny_kommune
        else:
            print(f"Kommune nr. {kommunenr} finnes allerede i {self._fylkes_navn}")

    def hent_navn(self):
        return self._fylkes_navn

    def hent_land(self):
        return self._land

    def __iter__(self):
        # Gjør at vi kan skrive: for kommune in fylke:
        for kommune_nr in self._kommuner:
            yield self._kommuner[kommune_nr]

    def __len__(self):
        return len(self._kommuner)

    def __str__(self):
        utskrift = f"    {self._fylkes_navn} ({len(self)} kommuner) (i {self._land.hent_navn()})\n"

        for kommune in self:
            utskrift += str(kommune)

        return utskrift


class Kommune:
    def __init__(self, kommune_nr, kommune_navn, fylke):
        self._kommune_nr = kommune_nr
        self._kommune_navn = kommune_navn
        self._fylke = fylke

    def __str__(self):
        fylkesnavn = self._fylke.hent_navn()
        landnavn = self._fylke.hent_land().hent_navn()
        return f"        {self._kommune_navn} (i {fylkesnavn} i {landnavn})\n"


norge = Land("Norge", "kommuner.csv", "fylker.csv")
print(norge)
