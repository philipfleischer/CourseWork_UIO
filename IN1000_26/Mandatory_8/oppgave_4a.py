# Deloppgave 4A: Emne


class Emne:

    def __init__(self, emnekode, navn, hoest, vaar):
        self.emnekode = emnekode
        self.navn = navn
        self.hoest = hoest
        self.vaar = vaar

    def __str__(self):
        if self.hoest and self.vaar:
            sem = "høst og vår"
        elif self.hoest:
            sem = "høst"
        elif self.vaar:
            sem = "vår"

        return f"{self.emnekode}: {self.navn} ({sem})"
