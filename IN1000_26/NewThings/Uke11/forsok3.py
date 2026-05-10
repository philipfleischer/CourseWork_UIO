from kommuner_fylker import kommuner, fylker


class Land:
    def __init__(self, navn, kommuner, fylker):
        self.navn = navn
        self.fylker = {}

        for kommunenr in kommuner:
            kommunenavn = kommuner[kommunenr]
            fylkesnr = kommunenr[0:2]
            fylkesnavn = fylker[fylkesnr]

            self.legg_til_fylke(
                fylkesnr, fylkesnavn
            )  # legger bare til fylke hvis det ikke fins fra før
            fylke = self.hent_fylke(fylkesnr)
            fylke.legg_til_kommune(kommunenr, kommunenavn)

    def legg_til_fylke(self, fylkesnr, fylkesnavn):
        if fylkesnr not in self.fylker:
            nytt_fylke = Fylke(fylkesnr, fylkesnavn)
            self.fylker[fylkesnr] = nytt_fylke
        else:
            print(f"Fylke nr. {fylkesnr} finnes allerede i {self.navn}")

    def hent_fylke(self, fylkesnr):
        if fylkesnr in self.fylker:
            return self.fylker[fylkesnr]
        else:
            print(f"{self.navn} har ikke noe fylke med nummer {fylkesnr}")
            return None

    def __str__(self):
        utskrift = f"{self.navn} ({len(self.fylker)} fylker, {len(self)} kommuner)\n"

        for fylkesnr in self.fylker:
            fylke = self.fylker[fylkesnr]
            utskrift += f"{fylke}"

        return utskrift

    # NOTE: Antall kommuner, ikke antall fylker
    def __len__(self):
        antall_kommuner = 0

        for fylkesnr in self.fylker:
            fylke = self.fylker[fylkesnr]
            antall_kommuner += len(fylke.kommuner)

        return antall_kommuner


class Fylke:
    def __init__(self, fylkesnr, fylkesnavn):
        self.nummer = fylkesnr
        self.navn = fylkesnavn
        self._kommuner = {}

    def legg_til_kommune(self, kommunenr, kommunenavn):
        if kommunenr not in self._kommuner:
            ny_kommune = Kommune(kommunenr, kommunenavn)
            self._kommuner[kommunenr] = ny_kommune
        else:
            print(f"Kommune nr. {kommunenr} finnes allerede i {self.navn}")

    def __str__(self):
        utskrift = f"    {self.navn} ({len(self._kommuner)} kommuner)\n"

        for kommunenr in self._kommuner:
            kommune = self._kommuner[kommunenr]
            utskrift += f"{kommune}"

        return utskrift


class Kommune:
    def __init__(self, kommunenr, kommunenavn):
        self.nummer = kommunenr
        self.navn = kommunenavn

    def __str__(self):
        return f"\t{self.navn}\n"


norge = Land("Norge", kommuner, fylker)
print(norge)
