"""
Du skal hente ut forskjellige mål fra en txt fil og legge navnet på målet inn i
en ordbok som nøkkelverdier og selve målene som verdier. Funnksjonen skal ta inn
filen som et parameteter, og til slutt returnere ordboken.
Etter dette skal du lage en funksjon som konverterer målene fra filen, som
nå er skrevet som tommer om til cm.
Kall på funksjonen igjen.
"""
skredderFil = open("skredder.txt", "r")
#Må hente inn tommerTilCM som er en annen funksjon.

def funk1(skredderFil):
    ordbok = {}
    for linjer in skredderFil:
        linjer = linjer.strip()
        kolonner = linjer.split(" ")
        kroppsdel = kolonner[0]
        maal = kolonner[1]
        maal_float = float(maal)
        ordbok[kroppsdel] = maal_float
    print("Målene i ordboken er i tommer: \n", ordbok)
    return ordbok


ordbok = funk1(skredderFil)
#Her legger jeg inn en funksjon fra: regnefunksjoner.py
def tommerTilCm(ordbok):
    antallTommer = list(ordbok.values())
    liste = []
    teller = 0
    while teller < len(antallTommer):
        #cm = float(antallTommer[i]) * 2.54
        tommer = antallTommer[teller] * 2.54
        liste.append(tommer)
        teller+=1
    print("Her er verdiene fra ordboken over i cm:", liste)

tommerTilCm(ordbok)
