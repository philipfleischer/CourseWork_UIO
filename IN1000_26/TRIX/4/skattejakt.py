# 04.16

def skattejakten():
    kart = skattekartet()
    print(kart)
    skriv_ut_skattekart(kart)
    skattekart, x, y = gyldige_koordinater(kart)
    skattekart[x][y] = "X"
    skriv_ut_skattekart(skattekart)
    linjeskiftern()
    finn_skatten(skattekart)


def skattekartet():
    skattekart = [] # n lister med n elementer
    n = 5   #Størrelsen

    # Lag n antall rader (lister)
    for i in range(n):
        rad = []

        # Fyll listene med bokstaven "O"
        # n antall ruter per rad
        for e in range(len(skattekart)):
            rad.append("O")

        # Legg til hver rad ("O"-liste) i skattekart-listen
        skattekart.append(rad)
    return skattekart

def gyldige_koordinater(kart):
    gyldig = False
    while not gyldig:
        try:
            koord = input("Skriv inn koordinater (som dette: 1,2): ")
            koordinater = koord.split(",")
            x = int(koordinater[0])
            y = int(koordinater[1])
            if kart[x][y] is not None:
                gyldig = True
                return kart, x, y
        except (IndexError, ValueError):
            continue


def skriv_ut_skattekart(kart):
    for rad in kart:
        # Konverterer en liste til en streng
        # med mellomrom mellom elementene
        print(" ".join(rad))

def linjeskiftern():
    for i in range(15):
        print()

def finn_skatten(skattekart):
    visningskart = skattekartet()
    teller = 0

    while teller < 3:
        print("Gjett hvor skatten er.")
        _, x, y = gyldige_koordinater(skattekart)
        if skattekart[x][y] == "X":
            print("Du fant skatten!")
            return
        visningskart[x][y] = "#"
        skriv_ut_skattekart(visningskart)

        teller += 1
    print("Du fant ikke skatten! Den var her: ")
    skriv_ut_skattekart(skattekart)


def main():
    skattejakten()

if __name__ == "__main__":
    main()
