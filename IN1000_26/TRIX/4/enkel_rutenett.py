#04.07
def rutenett():
    o_liste = []
    stjerneliste = []
    for i in range(5):
        o_liste.append("o")
        stjerneliste.append("*")

    rutenettListe = []
    rutenettListe.append(o_liste)
    rutenettListe.append(stjerneliste)
    rutenettListe.append(o_liste)

    print(rutenettListe[0])
    print(rutenettListe[1])
    print(rutenettListe[2])

    for element in rutenettListe:
        print(element)

def main():
    rutenett()

if __name__ == "__main__":
    main()
