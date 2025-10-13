#her importerer jeg klassen Sang fra filen sang.py
from sang import Sang
#Lager en klasse kalt Spilleliste
class Spilleliste:
    #Lager konstruktøren, som tar inn et listenavn som parameter.
    def __init__(self, listenavn):
        #Lagt inn en tom liste som instansvariabel, trenger ikke å ha som parameter over.
        self._sanger = []
        self._navn = listenavn

    #Metoden lesFraFil tar inn parameteret musikk
    def lesFraFil(self, musikk):
        #musikk er altså en fil som skal bli ført inn i funksjonen og bli lest (r=read)
        musikk = open(musikk, "r")
        #iterer gjennom filen
        for linje in musikk:
            #I filen som blir tatt utgangspunkt i så blir tittel og artist skilt med et semikolon
            alleData = linje.strip().split(";")
            #Her setter jeg altså til et Sang-objekt som tar inn to parametere som det skal, nemlig artist og tittel
            tittel_artist = Sang(alleData[1], alleData[0])
            #Her kalles leggTilSang metoden som skal gjøre noe med dette objektet
            self.leggTilSang(tittel_artist)

    #metoden leggTilSang tar inn ett parameter, f.eks. tittel_artist
    def leggTilSang(self, sang):
        #objektet blir kjørt gjennom string metoden i Sang-klassen
        #Hvis den nye stringen ikke finnes fra før av i listen så blir den lagt til i listen. Finnes den derimot kommer en feilmelding
        if sang.__str__() not in self._sanger:
            self._sanger.append(sang)
        else:
            print("Sangen finnes allerede i spillelisten")

    #Funksjonen fjernSang tar inn ett parameter
    def fjernSang(self, sang):
        #Hvis sangen som blir satt inn som parameter finnes i instansvariabelen/listen, så brukes kommandoen remove, som fjerner sangen
        if sang in self._sanger:
            self._sanger.remove(sang)
        else:
            #hvis den ikke finnes i listen, så kommer det opp en feilmelding
            print("sangen finnes ikke i spillelisten")

    #Funksjonen spillSang tar inn ett parameter
    def spillSang(self, sang):
        #parameteret blir kjørt gjennom string-metoden i Sang-klassen og printet ut
        print(sang.__str__())

    #funksjonen spillAlle, iterer gjennom listen og printer hver linje til terminalen.
    def spillAlle(self):
        for linje in self._sanger:
            print(linje)

    #metoden finnSang tar inn ett parameter "tittel"
    def finnSang(self, tittel):
        #iterer gjennom listen
        for i in self._sanger:
            #hvis linjen "i" i listen av sjekkTittel metoden av parameterert tittel == True, betyr det at sangen finnes i listen og blir returnert
            if i.sjekkTittel(tittel) == True:
                return i

    #Metoden nySang tar inn to parameter
    def nySang(self, artist, tittel):
        #Iterer gjennom listen
        for i in self._sanger:
            #Hvis linjen "i" i metoden sjekkArtistOgTittel == True, betyr det at den finnes i listen og den blir returnert
            if i.sjekkArtistOgTittel(artist, tittel) == True:
                return i
        return None

    #metoden hentArtistUtvalg tar inn ett parameter
    def hentArtistUtvalg(self, artistnavn):
        #Lager en tom liste
        liste = []
        #Iterer gjennom listen self._sanger
        for i in self._sanger:
            #Hvis linjen "i" gjennom sjekkArtist metoden med parameteret som blir gitt == True, så skal linjen bli lagt til den tomme listen
            if i.sjekkArtist(artistnavn) == True:
                liste.append(i)
        #Returnerer listen, slik at den kan bli akssesert i hovedprogrammet
        return liste
