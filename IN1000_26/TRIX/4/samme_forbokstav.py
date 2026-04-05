#04.17
def samme():
    personer = {}

    svar = "j"
    while svar == "j":
        navn = input("Navn: ")
        alder = int(input("Alder: "))
        personer[navn] = alder
        svar = input("Skriv 'j' for å legge til flere personer: ")

    bokstav = ""
    while len(bokstav) != 1:
        bokstav = str(input("Bokstav: "))

    for navn, alder in personer.items():
        forboks = navn[0]
        if forboks.lower() == bokstav.lower():
            print(f"Person: {navn} er {alder} år gammel.")

def main():
    samme()

if __name__ == "__main__":
    main()


# FASIT

personer = {}

inn = "j"
while inn == "j":
    navn = input("Oppgi navn: ")

    gyldigAlder = False
    while not gyldigAlder:
        alder = input("Oppgi alder: ")
        # Utfordring
        if alder.isdigit():
            gyldigAlder = True
            personer[navn] = int(alder)
        else:
            print("Ugyldig input!")

    inn = input("Skriv 'j' for å taste inn flere navn: ")

bokstav = input("Oppgi bokstav: ")
while len(bokstav) != 1:
    print("Ugyldig input!")
    bokstav = input("Oppgi en bokstav: ")

bokstav = bokstav.lower()

for key in personer:
    if key[0].lower() == bokstav:
        print(key, personer[key])
