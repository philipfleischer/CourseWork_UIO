#Lager den første listen med 3 tall
liste = [1, 10, 12]
#legger til (append) tallet 100 bakerst i listen
liste.append(100)
#printer elementene som har fått indeksnummer 0 og 2 (altså element 1 og 3)
print(liste[0], liste[2])
#lager en ny tom liste
listeNavn = []
#ber om 4 navn, som blir lagt inn i en liste
listeVar = input("Skriv inn 4 navn til listen: \n<")
#lager enda en liste der navnene blir splittet der mellomrom forekommer
ferdig_listeVar = listeVar.split(" ")
#Legger denne listen inn i den tomme listen over
listeNavn.extend(ferdig_listeVar)
print(liste)
#Mye mulig jeg har misforstått oppgaveteksten, men jeg synes dette så unødvendig mye ut

#Her er det en if-setning som sjekker om mitt fornavn er husket eller glemt
if "Philip" in ferdig_liste2:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Under blir den første listen sine elementer gjort om til integer og addert
sum = int(liste[0]+liste[1]+liste[2])
#Under blir den første listen sine elementer gjort om til integer og multiplisert
produkt =  int(liste[0]*liste[1]*liste[2])
#Lager en tom liste som skal inneholde sum og produkt
sumOgProdukt = []
#Under legger jeg først til sum, så legger jeg produkt etter
sumOgProdukt.append(sum)
sumOgProdukt.append(produkt)
print(sumOgProdukt)

#Lager enda en tom liste
fellesListe = []
#Under legger jeg til den første listen
fellesListe.append(liste)
#Under legger jeg til listen som inneholder summen og produktet
fellesListe.append(sumOgProdukt)
print(fellesListe)
"""Under har jeg fjernet den ene listen som inneholdt to elementer.
Jeg kunne også ha brukt pop, men da måtte jeg ha kjørt det to ganger.
Eller så kunne jeg ha brukt en loop"""
fellesListe.remove(sumOgProdukt)
print(fellesListe)
