liste = [1, 10, 12]
liste2 = input("Skriv inn 4 navn til listen: \n<")
ferdig_liste2 = liste2.split(" ")
listeNavn = []
listeNavn.extend(ferdig_liste2)

if "Philip" in ferdig_liste2:
    print("Du husket meg!")
else:
    print("Du glemte meg")

sum = int(liste[0]+liste[1]+liste[2])
produkt =  int(liste[0]*liste[1]*liste[2])
sumOgProdukt = []
sumOgProdukt.append(sum)
sumOgProdukt.append(produkt)
print(sumOgProdukt)

fellesListe = []
fellesListe.append(liste)
fellesListe.append(sumOgProdukt)
print(fellesListe)

fellesListe.remove(sumOgProdukt)
print(fellesListe)
