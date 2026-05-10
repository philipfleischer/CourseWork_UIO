from kommuner_fylker import kommuner, fylker


class Land:
    def __init__(self, navn):
        self._navn = navn
        self._fylker = {}

    def legg_til_fylker(self, fylkes_nr, fylkes_navn):
        if fylkes_nr not in self._fylker:
            nytt_fylke = Fylke(fylkes_nr, fylkes_navn)
            self._fylker[fylkes_nr] = nytt_fylke
        else:
            print(f"Fylket {fylkes_navn} finnes allerede i {self._navn}")

    def hent_fylke(self, fylkes_nr):
        if fylkes_nr in self._fylker:
            return self._fylker[fylkes_nr]
        else:
            print(f"{self._navn} har ikke noe fylke med nummer {fylkes_nr}")
            return None

    def __str__(self):
        return f"{self._navn} ({len(self._fylker)} fylker)"

    def __iter__(self):
        for fylke in self._fylker:
            yield fylke


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
        return f"   {self._fylkes_navn} ({len(self._kommuner)})"


class Kommune:
    def __init__(self, kommune_nr, kommune_navn):
        self._kommune_nr = kommune_nr
        self._kommune_navn = kommune_navn

    def __str__(self):
        return f"\t{self._kommune_navn}"
