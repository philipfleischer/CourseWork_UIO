#kjør denne koden i Python - Tutor
from random import choice
class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._naboer = []

    def legg_til_nabo(self, nabo_stasjon):
        self._naboer.append(nabo_stasjon)

    def hent_navn(self):
        return self._navn

    def hent_tilfeldig_nabo(self):
        return choice(self._naboer)

def hovedprogram():
    stasjonsbok = {}

    for linje in open("ruter.txt"):
        biter = linje.strip().split()
        fra_navn = biter[0]
        til_navn = biter[1]
        if fra_navn not in stasjonsbok:
            stasjonsbok[fra_navn = Stasjon(fra_navn)
        if til_navn not in stasjonsbok:
            stasjonsbok[til_navn] = Stasjon(til_navn)
        fra_stasjon = stasjonsbok[fra_navn]
        til_stasjon = stasjonsbok[til_navn]

        fra_stasjon.legg_til_nabo(til_stasjon)
        til_stasjon.legg_til_nabo(fra_stasjon)


        start_navn = input("Hvilken stasjon vil du reise fra?")
        maal_navn = input("Hvilken stasjon vil du reise til?")
        start_stasjon = stasjonsbok[start_navn]
        maal_stasjon = stasjonsbok[maal_navn]

        her = start_stasjon
        while maal != maal_stasjon:
            her = her.hent_tilfeldig_nabo()
            print(her.hent_navn())
# ...
hovedprogram()
