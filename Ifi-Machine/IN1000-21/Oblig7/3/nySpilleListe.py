from nysang import Sang
musikk = open("nyMusikk.txt", "r")

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, musikk):
        for linje in musikk:
            alleData = linje.strip().split(";")
            print(alleData)

            #listen = [self._sanger.append(alleData[0]) for alleData in range(alleData)]
            #self._sanger.append(alleData[0])

#Jeg må løse legg denne ikke fakk med den over
    def leggTilSang(self, nySang):
        #nySang skal appendes til self._sanger
        #Det er linjen under som ikke er riktig
        for nySang in self._sanger:
            print("hei")
            if nySang not in self._sanger:
                self._sanger.append(nySang)
                print(self._sanger)
            else:
                return False



    def fjernSang(self, sang):
        for sang in self._sanger:
            if sang is self._sanger:
                return self._sanger.remove(sang)
            else:
                return "Finnes ikke i listen"

        """for sang in self._sanger:
        Må bruke samme metode som over,
        for å finne ut om sangen finnes
        gjør den det så skal den fjernes,
        hvis ikke, så feilmelding.

        Bruk f.eks. self._sanger.remove(sang)
        """

    def spillSang(self, sang):
        funk = self.spill(self)
        if sang == self._tittel:
            return funk
        else:
            print("Noe gikk galt her ass")

    def spillAlle(self):
        for sanger in self._sanger:
            print(sanger)

    def finnSang(self, tittel):
        if tittel in self._tittel:
            print(tittel)
        else:
            return None

    def hentArtistUtvalg(self, artist):
        for self._tittel in artist:
            print(self._tittel)

def hoved():
    spilleliste1 = Spilleliste("halla")

    print(spilleliste1.fjernSang("Ung og Dum"))
    spilleliste1.lesFraFil(musikk)
    print(spilleliste1.leggTilSang("Piker og Vin"))
    print(spilleliste1.leggTilSang("Money"))
    print(spilleliste1.leggTilSang("Money"))

    spilleliste1.spillAlle()
hoved()
