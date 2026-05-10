from kommuner_fylker import kommuner, fylker


class Land:
    def __init__(self, navn, kommuner, fylker):
        self._navn = navn
        self._fylker = {}
        self._populer_fylker()

    def _populer_fylker(self):
        for kommune_nr in kommuner:
            kommune_navn = kommuner[kommune_nr]
            fylkes_nr = kommune_nr[0:2]
            fylkes_navn = fylker[fylkes_nr]

            self.legg_til_fylker(fylkes_nr, fylkes_navn)
            fylke = self.hent_fylke(fylkes_nr)
            fylke.legg_til_kommune(kommune_nr, kommune_navn)

    def legg_til_fylker(self, fylkes_nr, fylkes_navn):
        if fylkes_nr not in self._fylker:
            nytt_fylke = Fylke(fylkes_nr, fylkes_navn)
            self._fylker[fylkes_nr] = nytt_fylke
        #else:
            #print(f"Fylket {fylkes_navn} finnes allerede i {self._navn}")

    def hent_fylke(self, fylkes_nr):
        if fylkes_nr in self._fylker:
            return self._fylker[fylkes_nr]
        else:
            print(f"{self._navn} har ikke noe fylke med nummer {fylkes_nr}")
            return None

    def __str__(self):
        utskrift = f"{self._navn} ({len(self)} fylker)\n"

        for fylkes_nr in self._fylker:
            fylke = self._fylker[fylkes_nr]
            utskrift += f"{fylke}"

        return utskrift

    def __iter__(self):
        for fylke in self._fylker:
            yield fylke

    def __len__(self):
        antall_kommuner = 0

        for fylke_nr in self._fylker:
            fylke = self._fylker[fylke_nr]
            antall_kommuner = len(fylke._kommuner)

        return antall_kommuner


class Fylke:
    def __init__(self, fylkes_nr, fylkes_navn):
        self._fylkes_nr = fylkes_nr
        self._fylkes_navn = fylkes_navn
        self._kommuner = {}

    def legg_til_kommune(self, kommune_nr, kommune_navn):
        if kommune_nr not in self._kommuner:
            ny_kommune = Kommune(kommune_nr, kommune_navn)
            self._kommuner[kommune_nr] = ny_kommune
        else:
            print(f"Kommune nr. {kommune_nr} finnes allerede i {self._fylkes_navn}")

    def __str__(self):
        # utskrift = f"   {self._fylkes_navn} ({len(self._kommuner)} kommuner)\n"
        utskrift = f"   {self._fylkes_navn} ({len(self._kommuner)} kommuner)\n"

        for kommune_nr in self._kommuner:
            kommune = self._kommuner[kommune_nr]
            utskrift += f"{kommune}"

        return utskrift


class Kommune:
    def __init__(self, kommune_nr, kommune_navn):
        self._kommune_nr = kommune_nr
        self._kommune_navn = kommune_navn

    def __str__(self):
        return f"\t{self._kommune_navn}\n"


norge = Land("Norge", kommuner, fylker)
print(norge)
