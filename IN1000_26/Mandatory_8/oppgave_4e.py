#Deloppgave 4E: Utvidelse Emne

class Emne:

    def __init__(self, emnekode, navn, hoest, vaar):
        self.emnekode = emnekode
        self.navn = navn
        self.hoest = hoest
        self.vaar = vaar
        self._eier = None

    def legg_til_eier(self, institutt):
        self._eier = institutt

    def __str__(self):
        if self.hoest and self.vaar:
            sem = "høst og vår"
        elif self.hoest:
            sem = "høst"
        elif self.vaar:
            sem = "vår"

        if not self._eier:
            return f"{self.emnekode}: {self.navn} ({sem})"
        else:
            return f"{self.emnekode}: {self.navn} ({sem}) - eies av {self._eier.navn}"
