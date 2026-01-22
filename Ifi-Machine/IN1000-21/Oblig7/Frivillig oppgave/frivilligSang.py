class Sang:

    def __init__(self, tittel, artist):
        self._artist = artist
        self._tittel = tittel

    def __str__(self):
        


    def spill(self):
        print(f"Sangen '{self._tittel}' er skrevet av {self._artist}")


    def sjekkArtist(self, artist):
            if artist.lower() == self._artist.lower():
                return True
            else:
                return False


    def sjekkTittel(self, tittel):
            if tittel.lower() == self._tittel.lower():
                return True
            else:
                return False


    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) == True and self.sjekkTittel(tittel) == True:
            return True
        else:
            return False


def main():
    sang1 = Sang("Ung og Dum", "Unge Ferrari")

    sang1.spill()
    print(sang1.sjekkArtist("Unge Ferrari"))
    print(sang1.sjekkTittel("Ung og Dum"))
    print(sang1.sjekkArtistOgTittel("Unge Ferrari", "Ung og Dum"))

main()
