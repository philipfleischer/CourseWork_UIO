def meny():
    # Definerer tilgjengelige retter og tilbehør
    salat = "Salat"
    biff = "Biff"
    torsk = "Torsk"

    tilbehor1 = "Gulrotter"
    tilbehor2 = "Bernaise"

    hovedrett = ""
    tilb = ""

    # Skriver ut menyen
    print(
        f"Meny:\n1. {salat}\n2. {biff}\n3. {torsk}\n- Tilbehor:\n   - {tilbehor1}\n   - {tilbehor2}\n"
    )

    def bestill_hovedrett():
        # Ber brukeren velge hovedrett helt til gyldig input er gitt
        while True:
            hovedrett = input(
                "Velg en hovedrett (skriv inn 1=salat 2=biff 3=torsk):\n-> "
            ).strip()

            try:
                hovedrett = int(hovedrett)
            except ValueError:
                print("Ugyldig input, proev igjen\n")
                continue

            if hovedrett == 1:
                return salat
            elif hovedrett == 2:
                return biff
            elif hovedrett == 3:
                return torsk
            else:
                print("Ugyldig nummer, proev igjen\n")

    def bestill_tilbehoer():
        # Ber brukeren velge tilbehør helt til gyldig input er gitt
        while True:
            tilb = input(
                "Skriv inn oensket tilbehoer (skriv inn 1=gulrot 2=bernaise):\n-> "
            ).strip()

            try:
                tilb = int(tilb)
            except ValueError:
                print("Ugyldig input, proev igjen.\n")
            if tilb == 1:
                return tilbehor1
            elif tilb == 2:
                return tilbehor2
            else:
                print("Ugyldig input, proev igjen\n")

    # Henter brukerens valg
    hovedrett = bestill_hovedrett()
    tilb = bestill_tilbehoer()

    # Gir tilbakemelding basert på valgene
    if (hovedrett == torsk or hovedrett == biff) and tilb == tilbehor2:
        print("Du spiser ikke nok grønnsaker!")
    elif hovedrett == salat and tilb == tilbehor1:
        print("Du har valgt et vegetarmaaltid")
    elif (hovedrett == salat and tilb != tilbehor1) or (
        hovedrett != salat and tilb == tilbehor1
    ):
        print(f"Du har valgt {hovedrett} med {tilb}")


if __name__ == "__main__":
    meny()
