#Lager en klasse som jeg kaller Hund
class Hund:
    #Definerer konstruktøren med tre instansvariabler
    def __init__(self, alder, vekt, metthet):
        self._alder = alder
        self._vekt = vekt
        self._metthet = metthet

    def get_alder(self):
        return self._alder

    def get_vekt(self):
        return self._vekt

    def spring(self):
        self._metthet -= 1
        return self._metthet

    def spis(self, heltall):
#Her er self._metthet + parameteret heltall som er hentet fra brukerinput annerledes enn self._metthet i prosedyren over
        self._metthet += heltall
        if self._metthet > 7:
            self._metthet += 1
        return self._metthet
