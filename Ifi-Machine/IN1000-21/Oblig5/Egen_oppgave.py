"""
"""
skredderFil = open("skredder.txt", "r")
#Må hente inn tommerTilCM som er en annen funksjon.

def funk1(skredderFil):
    ordbok = {}
    for linjer in skredderFil:
        linjer = linjer.strip()
        kolonner = linjer.split(",")
        kroppsdel = kolonner[0]
        maal = kolonner[1]
        ordbok[kroppsdel] = maal


    print("Her er verdiene i tommer", ordbok)
    return ordbok


def funk2(skredderFil):
    ordbok = {}
    #verdier = ordbok[1]
    for linjer in skredderFil:
        linjer = linjer.strip()
        kolonner = linjer.split(",")
        kroppsdel = kolonner[0]
        tommer = float(kolonner[1])
        cm = 2.54 * tommer
        ordbok[kroppsdel] = cm
    #legg inn funksjonen her
    print("Her er verdiene i cm", ordbok)
    return ordbok
#funk1(skredderFil)
funk2(skredderFil)
