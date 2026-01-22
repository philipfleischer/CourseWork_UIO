class EspressoMaskin:
    #Konstruktør
    def __init__(self, maxKapasitet):
        self._max = maxKapasitet
        self._vannMengde = 1000
    # Lag espresso dersom det er nok vann
    def lagEspresso(self):
        if self._vannMengde >= 40:
            self._vannMengde -= 40
            print("Vær så god her har du en espresso!")
        else:
            print("ikke no vann")

    # Lag lungo dersom det er nok vann
    def lagLungo(self):
        if self._vannMengde >= 110:
            self._vannMengde -= 110
            print("Værsågod, her har du en lungo")
        else:
            print("FEEEEil")
    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyllVann(self, ml):
        if ml <= self._max - self._vannMengde:
            self._vannMengde += ml
            print("vannmengden er nå", self._vannMengde)
        else:
            print("For mye vann, overload")
    # Les av tilgjengelig vann i ml
    def hentVannmengde(self):
        return self._vannMengde

print(EspressoMaskin.lagEspresso())
print(EspressoMaskin.lagLungo())

print(EspressoMaskin.fyllVann(1000))
print(EspressoMaskin.fyllVann(10))

print(EspressoMaskin.hentVannmengde())
