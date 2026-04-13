"""
I denne oppgaven skal du manipulere og jobbe med lister.

a) Skriv en funksjon vanlig_konkat() som konkatenerer to lister. Gitt to lister (to argumenter): ["a", "b", "c"] og [1, 2, 3], skal funksjonen returnerer ["a", "b", "c", 1, 2, 3].

b) Skriv funksjonen annenhver_konkat() som fletter to lister samme
n. Gitt ["a", "b", "c"] og [1, 2, 3] som argumenter så skal funksjonen returnere listen ["a", 1, "b", 2, "c", 3]. Du kan anta at gitt listene er av samme lengde.

c) Skriv en funksjon tall_til_liste() som returnerer en liste med siffer gitt et tall. Dvs. tallet 895 skal returnere [8, 9, 5].
Du kan konvertere tallet til en annen datatype og så dele det opp.
"""

# 05.17
def vanlig_konkat(list1, list2):
    ny_liste = list1 + list2
    return ny_liste

def annenhver_konkat(list1, list2):
    liste = []
    lengde = len(list1)
    for i in range(lengde):
        liste.append(list1[i])
        liste.append(list2[i])
    return liste

def tall_til_liste(tall):
    sifre = []
    for siffer in str(tall):
        tallet = int(siffer)
        sifre.append(tallet)
    return sifre

def main():
    l1 = ["a", "b", "c"]
    l2 = [1, 2, 3]
    ny_liste = vanlig_konkat(l1, l2)
    print(ny_liste)

    nyere = annenhver_konkat(l1, l2)
    print(nyere)

    tall = tall_til_liste(895)
    print(tall)

if __name__ == "__main__":
    main()
