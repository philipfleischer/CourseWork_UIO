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


    def leggTilSang(self, sang):
        if sang not in self._sanger:
            self._sanger.append(sang)
        else:
            print("Sangen finnes allerede i spillelisten")

    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang)
        else:
            print("sangen finnes ikke i spillelisten")

#FUNKER!!!
    def spillSang(self, sang):
        print(sang)

#FUNKER!!!
    def spillAlle(self):
        print(self._sanger)
