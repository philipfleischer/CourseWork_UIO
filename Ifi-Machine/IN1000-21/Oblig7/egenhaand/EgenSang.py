#Lager en klasse Sang
class Sang:
    #Lager konstruktøren med parameterne tittel og artist
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    #Funksjon som printer ut tittelen og artisten som er algt inn som argumenter
    def spill(self):
        print(f"Sangen '{self._tittel}' er skrevet av {self._artist}")

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
def main():
    sang1 = Sang("Ung og Dum", "Unge Ferrari")

    sang1.spill()
    print(sang1.sjekkArtist("Unge Ferrari"))
    print(sang1.sjekkTittel("Ung og Dum"))
    print(sang1.sjekkArtistOgTittel("Unge Ferrari", "Ung og Dum"))

main()

#Det eneste jeg mangler er den frivillige gule boksen.
