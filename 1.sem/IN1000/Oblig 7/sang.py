#Lager en klasse Sang
class Sang:
    #Lager konstruktøren med parameterne tittel og artist
    def __init__(self, artist, tittel):
        self._tittel = tittel
        self._artist = artist
        
    #Her lager jeg en metode som bruker den innebygde metoden __str__, hver gang et Sang-objekt blir kalt så blir det kjørt gjennom denne
    def __str__(self):
        return f'Spiller {self._tittel} av {self._artist}'

    #Funksjonen printer ut f-stringen i metoden over
    def spill(self):
        print(self.__str__())

    #Lager en metode som sjekker artisten som er gitt
    def sjekkArtist(self, navn):
        #Splitter navnet siden en kan ha flere navn
        liste = navn.split()
        #iterer gjennom listen jeg laget
        for ord in liste:
            #Hvis elementet en er i (ord) finnes i self._artist så blir True returnert, hvis den ikke er lik i noen av iterasjonene så: False
            if ord in self._artist.split():
                return True
        else:
            return False


    #Metoden sjekker om en gitt tittel finnes fra før av
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False

    #I denne metoden blir to parametere tatt med og begge må være True for at True skal bli returnert. Ellers False
    def sjekkArtistOgTittel(self, artist, tittel):
        #Her bruker jeg også self."metodenavn" for å kalle på en annen metode i en metode.
        if self.sjekkArtist(artist) == True and self.sjekkTittel(tittel) == True:
            return True
        else:
            return False
