class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

#FUNKER!!!
    def lesFraFil(self, musikk):
        musikk = open(musikk, "r")
        for linje in musikk:
            alleData = linje.strip().split(";")
            self._sanger.append(alleData)


#FUNKER!!!
    def leggTilSang(self, sang):
        if sang.__str__() not in self._sanger:
            self._sanger.append(sang.__str__())
        else:
            print("Sangen finnes allerede i spillelisten")

    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang)
        else:
            print("sangen finnes ikke i spillelisten")

#FUNKER!!!
    def spillSang(self, sang):
        print(sang.__str__())
        #sang.spill()

#FUNKER!!!
    def spillAlle(self):
        for linje in self._sanger:
            print(linje)
#FUNKER!!!!!
    def finnSang(self, tittel):
        i=0
        while i < len(self._sanger):
            if tittel == self._sanger[i][0]:
                return self._sanger[i]
            i+=1
        else:
            return None

#Kan splitte opp etter mellomrom i artistnavn og _sanger
    def hentArtistUtvalg(self, artistnavn):
        i=0
        while i < len(self._sanger):
            if artistnavn == self._sanger[i][1]:
                #queenListe.append(self._sanger[i])
                yield self._sanger[i]
                
            i+=1
        else:
            print("artistnavnet finnes ikke i listen")
