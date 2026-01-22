#Lager en klasse Sang
class Sang:
    #Lager konstruktøren med parameterne tittel og artist
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    def __str__(self):
        linje = [str(self._tittel), str(self._artist)]
        return linje

    #Funksjon som printer ut tittelen og artisten som er algt inn som argumenter
    def spill(self):
        print(f"Spiller '{self._tittel}' skrevet av '{self._artist}'")

    #Metode som finner ut om artisten som blir lagt inn som argument er lik innstansvariabelen
    def sjekkArtist(self, artist):
            if artist.lower() == self._artist.lower():
                return True
            else:
                return False

    #Metoden er lik den over, men tittel istedenfor artist
    def sjekkTittel(self, tittel):
            if tittel.lower() == self._tittel.lower():
                return True
            else:
                return False

    #Metode som har samme funksjon som funksjonen og metoden over.
    #Forskjellen er at her så må både artisten og tittelen være riktig
    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) == True and self.sjekkTittel(tittel) == True:
            return True
        else:
            return False

#Laget en funksjon main som setter inn verdier og gir instruksjoner ved hjelp av klassen
#Denne må du fjerne!!!!!!!!!!!!!!!!!!!!!!
def main():
    sang1 = Sang("Ung og Dum", "Unge Ferrari")

    sang1.spill()
    print(sang1.sjekkArtist("Unge Ferrari"))
    print(sang1.sjekkTittel("Ung og Dum"))
    print(sang1.sjekkArtistOgTittel("Unge Ferrari", "Ung og Dum"))

main()
