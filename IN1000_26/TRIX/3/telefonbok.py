#03.07
def telebok():
    telefonbok = {}
    telefonbok["Arne"] = 23415124
    telefonbok["Lisa"] = 53424325
    telefonbok["Jonas"] = 34567899
    telefonbok["Peder"] = 92357896

    navn = input("Skriv inn navn: ")
    if navn in telefonbok:
        print(telefonbok[navn])
    else:
        nr = int(input(f"Skriv inn {navn} sitt nummer: "))
        telefonbok[navn] = nr

    print(telefonbok)


def main():
    telebok()

if __name__ == "__main__":
    main()
