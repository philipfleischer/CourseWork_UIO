"""
Oppgave 5: Egen oppgave (LISTER OG ORDØKER)

Lag et program som hjelper en arrangør å holde oversikt over allergier ved påmelding.

Programmet skal:
1) Spørre brukeren hvor mange deltakere som skal registreres (heltall).
2) For hver deltaker:
    - Spør om navn
    - Spør om allergier, skrevet som en kommaseparert liste (f.eks: "nøtter, melk") Hvis deltakeren ikke har allergier, kan brukeren skrive "ingen".
3) Lagring:
    - Bruk en ordbok (dictionary) der nøkkel er navnet (string), og verdien er en liste med allergier (liste med strings).
4) Til slutt skal programmet skrive ut:
    - En oversikt over alle deltakere og deres allergier
    - En samlet oversikt over hvilke allergier som forekommer totalt (unike allergier)
    - Hvor mange deltakere som har hver allergi
"""


def allergier():
    ordb = {}

    while True:
        try:
            deltakere = int(input("Hvor mange deltakere: "))
            break
        except ValueError:
            print("Du må skrive inn et heltall.")

    for i in range(deltakere):
        navn = input("Skriv inn navn på deltaker: ")
        allergier = (
            input(
                "Skriv inn allergier til deltaker eller skriv 'ingen'. (skill dem med komma: egg, melk): \n"
            )
            .strip()
            .lower()
        )
        if allergier == "ingen" or allergier == "":
            ordb[navn] = []
        else:
            ordb[navn] = [aller.strip() for aller in allergier.split(",")]

    print("\n--- Oversikt per deltaker ---")
    for deltaker, allergier in ordb.items():
        if allergier:
            print(f"{deltaker} har allergier: {', '.join(allergier)}")
        else:
            print(f"{deltaker} har ingen allergier")

    # Unike allergier og ant forekomster
    unike = set()
    teller = {}

    for allergilisten in ordb.values():
        for allergi in allergilisten:
            unike.add(allergi)
            teller[allergi] = teller.get(allergi, 0) + 1

    print("\n--- Samlet oversikt ---")
    if not unike:
        print("Ingen allergier registrert.")
    else:
        print("Unike allergier:")
        for allergi in unike:
            print(f"- {allergi}")

        print("\nAntall deltakere per allergi:")
        for allergi, antall in teller.items():
            print(f"- {allergi}: {antall}")


def main():
    allergier()


if __name__ == "__main__":
    main()
