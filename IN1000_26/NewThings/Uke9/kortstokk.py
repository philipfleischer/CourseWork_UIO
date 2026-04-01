from random import shuffle

class Spillkort:
    def __init__(self, symbol: str, verdi: int):
        self.symbol = symbol
        self.verdi = verdi
        self.kortstokk = None

    # "Magisk" metode som kalles hver gang objektet gjøres om til en str. For eksempel print(...). eller str(objekt).
    def __str__(self):
        utskrift = self.symbol + " " + str(self.verdi)
        if self.kortstokk is not None:
            utskrift += f" (i en kortstokk på adresse {id(self.kortstokk)})"
        return utskrift


class Kortstokk:
    def __init__(self):
        self._kort: list = []
        for symbol in ["herter", "kløver", "spar", "ruter"]:
            for verdi in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
                nytt_kort = Spillkort(symbol, verdi)
                nytt_kort.kortstokk = self  # Hvorfor = self?
                self._kort.append(nytt_kort)

    # "Magisk" metode som kalles hver gang for-løkke trenger ny verdi fra objektet
    # Se kommentarer nederst
    # Denne blir kalt når man for-løkker på objektet:
        # for x in objekt
    def __iter__(self):
        for kort in self._kort:
            yield kort

    def stokk(self):
        shuffle(self._kort)

    def trekk(self):
        øverste_kort = self._kort.pop(0)
        øverste_kort.kortstokk = None
        return øverste_kort


"""
Return og Yield

return:
- Kjøres bare én gang.
- Alt funksjonen skal returnere må med der.
- Avslutter funksjonen etterpå - ingen flere kodelinjer fra funksjonen kjøres.

yield:
- Kjøres flere ganger.
- Kan returnere én og én ting av gangen (f.eks. hver gang løkke trenger å gå videre).
- Pauser funksjonen i stedet for å avslutte den.
Funksjonen fortsetter den den slapp neste gang vi trenger en returverdi fra den.
- def __iter__ MÅ inneholde yield, ellers vil feilmelding komme.

__eq__:
- Man sjekker om to objekter er like: Objekt1 == objekt2

Bruker vi objekt == None, kaller vi __eq__ metoden til klassen.
For å være sikre på at et objekt virkelig er None-objekt, så må vi bruke dette: "object is None", vi bruker altså "is" ordet, som orverstyrer __eq__ metoden.
Kan også bruke "isinstance(objekt, int)" for å sjekke om objektet er en integer verdi, True/False.
"""
