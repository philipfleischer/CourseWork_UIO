from random import shuffle

class Spillkort:
    def __init__(self, symbol: str, verdi: int):
        # Når disse instansvariablene er definert her (med verdier),
        # så kan de brukes senere: et_spillkort.verdi (f.eks.)
        self.symbol = symbol
        self.verdi = verdi
        # NOTE: Kan også definrere instansvariabler som får verdi senere
        # (enten direkte i programmet: objekt.får_verdi_senere = 2
        # eller via en annen metode som kalles senere: objekt.få_en_verdi())
        # self.får_en_verdi_senere = None

class Kortstokk:
    # Denne metoden kalles en konstruktør
    # Den kalles automatisk når objektet er laget og
    # gjør alt som skal gjøres med et nylaget objekt
    def __init__(self):
        # NOTE: Denne instansvariabelen brukes aldri direkte og er ikke en del av grensesnittet.
        # _ først i navnet forteller oss at denne er til internt bruk!
        self._kort: list = []
        for symbol in ["herter", "kløver", "spar", "ruter"]:
            for verdi in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
                nytt_kort = Spillkort(symbol, verdi)
                self._kort.append(nytt_kort)

    def stokk(self):
        # Nå blir rekkefølgen i listen endret tilfeldig
        shuffle(self._kort)

    def trekk(self):
        # pop-metoden finner elementet på denne indeksen (her: 0)
        # fjerner det elementet fra listen
        # og returnerer det så det kan i en variabel
        øverste_kort = self._kort.pop(0)
        return øverste_kort
