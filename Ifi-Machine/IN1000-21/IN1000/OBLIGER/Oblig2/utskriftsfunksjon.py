#Bruker "def" for å lage en funksjon, i dette tilfellet spor
def spor():
    navn = input("Skriv inn navnet ditt: /n>")
    bosted = input("Skriv inn hvor du bor: /n>")
    print("Hei",navn+ "! Du kommer fra ", bosted)

"""Under starter vi den tidligere lagde funksjonen, oppgaven ba om at
spørsmålene skulle stilles 3 ganger, derav 3 "spor()" """
spor()
spor()
spor()
