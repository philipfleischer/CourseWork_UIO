#Lager en funksjon, gjør dette 5 ganger: adiisjon, subtraksjon, divisjon, tommerTilCm og skrivBeregninger
def addisjon(tall1, tall2):
    return tall1 + tall2
#printer og legger til to parametere i funksjonen, dette skjer på samme måte som nevnt over
print(addisjon(2,3))



def subtraksjon(tall1, tall2):
    return tall1 - tall2

#Under tester jeg funksjonene med assert
assert subtraksjon(4,3) > 0
assert subtraksjon(-3,-3) == 0
assert subtraksjon(-2,10) < 0

def divisjon(tall1, tall2):
    return tall1 // tall2

assert divisjon(72,3) > 0
assert divisjon(-0,-2) == 0
assert divisjon(2,-3) < 0

#Bruker assert for antallTommer for å være sikker på at antallTommer er større enn 0
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    tommer = antallTommer * 2.54
    print("Resultat: ", tommer, "\n")


tommerTilCm(10)

def skrivBeregninger():
    print("Utregninger:")
    tall1 = int(input("Skriv inn tall1: "))
    tall2 = int(input("Skriv inn tall2: "))

    #setter tall1 og tall2 til flyttall
    tall1 = float(tall1)
    tall2 = float(tall2)
    print("\n")
    print("Resultat av summering: ", addisjon(tall1, tall2))
    print("Resultat av subtraksjon: ", subtraksjon(tall1, tall2))
    print("Resultat av divisjon: ", divisjon(tall1, tall2), "\n")
    print("Konvertering fra tommer til cm:")
    tall_tommer = int(input("Skriv inn et tall: "))
    tall_tommer = float(tall_tommer)
    print(tommerTilCm(tall_tommer))
skrivBeregninger()


#jeg får opp none helt nederst av en eller annen grunn
