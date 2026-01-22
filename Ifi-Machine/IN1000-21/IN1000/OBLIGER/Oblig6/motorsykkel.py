#Lager en klasse som jeg kaller Motorsykkel
class Motorsykkel:
    #Definerer konstruktøren med tre instansvariabler
    def __init__(self, km, merke, regNr):
        self._avstand = km
        self._merke = merke
        self._regNr = regNr

    #Definerer en prosedyre som også tar parameteret km fra testMotorsykkel.py sin input verdi
    def kjor(self, km):
        self._avstand += km
        return self._avstand

    #Siden jeg ikke skulle legge inn noen kilometerstand, blir den totale verdien lik som den innlagte tidligere
    def hentKilometerStand(self):
        return self._avstand
    #Her skriver jeg ut merket, registreringsummeret og km standen som bruker velger i test programmet.
    def skrivUt(self):
        print(f"Merke:{self._merke}\nRegistreringsnummer:{self._regNr}\nKilometerstand:{self._avstand}")
        #Kunne returnert verdiene slik som under, visste ikke helt hva som var best
        #return self._merke, self._regNr, self._avstand
