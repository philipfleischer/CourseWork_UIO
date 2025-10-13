
def adder(tall1, tall2):
    sum = tall1 + tall2
    return sum

tall1 = int(input("Tall nummer 1: "))
tall2 = int(input("Tall nummer 2: "))

sum = adder(tall1, tall2)
adder(tall1, tall2)
print("sum =", sum)
adder(tall1, tall2)


"""
def tellForekomst(minTekst, minBokstav):
    teller = 0
    while teller < minTekst.count(minBokstav):
        teller += 1
        if teller == minTekst.count(minBokstav):
            print("Antall forekomster av", minBokstav, "er", teller, "i minText")
        else:
            continue
min_Tekst = open('minTekst.txt', unpack = True)
minTekst = min_Tekst.readlines()
print(minTekst)
minBokstav = input("Skriv inn en bokstav: \n< ")
tellForekomst(minTekst, minBokstav)
"""

with open('minTekst.txt', 'r') as minTekst:
    minBokstav = input("Skriv inn en bokstav: \n< ")
    print(minTekst.readlines())
    teller = 0
    while teller < minTekst.readlines().count(minBokstav):
        teller+=1
        if teller == minTekst.readlines().count(minBokstav):
            print("JAAAAA")
        else:
            print("NEEEEI")
