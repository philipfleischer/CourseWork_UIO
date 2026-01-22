from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def leggTilSang(self, nySang):
        #nySang skal appendes til self._sanger
        for nySang in self._sanger:
            if nySang is not self._sanger:
                self._sanger.append(nySang)
            else:
                print("Sangen finnes allerede i listen.")

    def fjernSang(self, sang):
        #Skal jeg fjerne siste sang, altså bruke pop eller noe annet

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
    
