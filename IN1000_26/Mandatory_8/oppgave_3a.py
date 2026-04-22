"""Oppgave 3A: Fjerning av ugyldige datoer
- En venn av deg har sendt deg denne klassen som vedkommende har tenkt å legge til grunn for å lage en enkel kalender:

class Dato:
    def __init__(self, dd, mm, aaaa):
        self._dagnr = dd
        self._mnd = mm
        self._år = aaaa

    def dagnr(self):
        return self._dagnr
    def mnd(self):
        return self._mnd
    def år(self):
        return self._år

I tillegg har vennen din skrevet denne funksjonen som lager en kalender for året 2023 som ei liste av Dato-objekter:

def lagKalender2023():
    kalender = []
    for dag in range(32):
        for mnd in range(13):
            kalender.append(Dato(dag,mnd,2023))
    return kalender

Nå ber vennen din deg om å hjelpe til med å skrive en funksjon som fjerner dato-objekter som ikke finnes. Funksjonen tar inn ei liste med datoobjekter (som er det lagKalender2023 returnerer) og returnerer lista der de ugyldige datoene er fjernet. For å gjøre dette kan du legge til grunn at denne ordboken er tigjengelig i det globale skopet:

dageriMnd = { 1:31, 2:28, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

Skriv funksjonen fjernUgyldigeDatoer her:"""


class Dato:
    def __init__(self, dd, mm, aaaa):
        self._dagnr = dd
        self._mnd = mm
        self._år = aaaa

    def dagnr(self):
        return self._dagnr

    def mnd(self):
        return self._mnd

    def år(self):
        return self._år


def lagKalender2023():
    kalender = []
    for dag in range(32):
        for mnd in range(13):
            kalender.append(Dato(dag, mnd, 2023))
    return kalender


dageriMnd = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

def fjernUgyldigeDatoer(kalender):
    gyldige = []

    for dato in kalender:
        dag = dato.dagnr()
        mnd = dato.mnd()

        if mnd in dageriMnd and 1 <= dag <= dageriMnd[mnd]:
            gyldige.append(dato)

    return gyldige

fjernUgyldigeDatoer(lagKalender2023())
