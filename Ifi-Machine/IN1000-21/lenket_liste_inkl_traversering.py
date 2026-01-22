#kjør denne koden i Python - Tutor
class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._nabo = None

    def sett_nabo(self, nabo_stasjon):
        self._nabo = nabo_stasjon

    def hent_nabo(self):
        assert self._nabo is not None
        return self._nabo

    def hent_navn(self):
        return self._navn
        
def hovedprogram():
    trikkestall = Stasjon("trikkestall")
    forrige = trikkestall
    for stasjonsnavn in open("trase.txt"):
        denne = Stasjon(stasjonsnavn.strip())
        forrige.sett_nabo(denne)
        forrige = denne

        maal = input("Hvilken stasjon vil du reise til?")
        her = trikkestall
        while maal != her.hent_navn():
            her = her.hent_nabo()
            print(her.hent_navn())

hovedprogram()
