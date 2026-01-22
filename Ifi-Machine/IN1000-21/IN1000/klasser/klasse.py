class Fly:
    def __init__(self, antallSeter, antallDoerer, antallMotorer, produsent, modellNummer, kmStand):
        self._antallSeter = antallSeter
        self._antallDoerer = antallDoerer
        self._antallMotorer = antallMotorer
        self._produsent = produsent
        self._modellNummer = modellNummer
        self._kmStand = kmStand

    def flyr(self, tall):
        self._kmStand += tall

    def printInfo(self):
        print(f"{self._produsent}\n{self._modellNummer}\n{self._kmStand}")
