# Dette er versjonen vi fikk, som ikke skal endres:
class Dato:
    def __init__(self, ddmmåååå):
        pass

    def hent_år(self):
        return 2026

    def dag_er_lik(self, dag_nr):
        return True

    def neste_dag(self):
        print(f"Gikk til neste dag!")

    def endre_til(self, ddmmåååå):
        print(f"Endret datoen til {ddmmåååå}!")


class Lag:
    pass


class Kamp:
    def simuler(self):
        print("Spilte kampen mellom hjemmelaget og bortelaget!")


class Runde:
    def __iter__(self):
        for _ in range(8):
            yield Kamp()

    def legg_til(self, hjemmelag_navn, bortelag_navn):
        print(f"La til {hjemmelag_navn} - {bortelag_navn} i Runde-objektet!")


class Sesong:
    def les_lag_fra_fil(self, filnavn):
        print(f"Leste lag fra filen {filnavn}!")

    def runde(self, nummer):
        return Runde()
