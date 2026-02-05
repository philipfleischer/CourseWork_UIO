"""
Dette programmet beregner billettpris basert på brukerens alder.
Programmet spør brukeren om alder og validerer at input er et gyldig heltall.
Avhengig av alderen plasseres brukeren i én av tre priskategorier:
barnebillett, standardbillett eller seniorbillett.
Til slutt skrives riktig billettpris ut til brukeren.
"""


def bilettpris():
    barneBilett = 20
    standardBilett = 50
    seniorBilett = 35

    while True:
        try:
            alder = int(input("Skriv inn din alder: "))
        except ValueError:
            print("Ugyldig input. Vennligst skriv et heltall.")
            continue

        if alder < 0:
            print("alder kan ikek være negativ.")
            continue

        if alder < 15:
            print(
                f"Du er {alder} år gammel og skal kjøpe Barne Bilett til: {barneBilett}kr"
            )
        elif alder < 70:
            print(
                f"Du er {alder} år gammel og skal kjøpe Standard Bilett til: {standardBilett}kr"
            )
        else:
            print(
                f"Du er {alder} år gammel og skal kjøpe Senior Bilett til: {seniorBilett}kr"
            )
        break


def main():
    bilettpris()


if __name__ == "__main__":
    main()
