def reise_info():
    navn = input("Skriv inn destinasjon: ")
    klear = input("Skriv inn klær: ")
    dato = input("Skriv inn avreisedato: ")

    return navn, klear, dato


def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value[0]} and {value[1]}")


def hent_info(dictionary):
    print("Oversikt:\n")
    print_dict(dictionary)

    navn = input("Skriv destinasjon du ønsker informasjon om: ")
    if navn not in dictionary:
        print(f"{navn} er ikke registrert, prøv igjen.")
        return hent_info(dictionary)

    oenske = input("Skriv hva du ønsker å se av klær/dato: ").strip().lower()
    if oenske != "klær" and oenske != "dato":
        print(f"{oenske} er ikke gyldig, prøv igjen.")
        return hent_info(dictionary)

    res = 0
    if oenske == "dato":
        res = 1

    print(f"{navn}: {dictionary[navn][res]}")


def endre_reise(dictionary):
    endre = input("Vil du endre reisen? (ja/nei): ").strip().lower()
    if endre != "ja" and endre != "nei":
        print(f"{endre} er ikke gyldig, Må være ja eller nei. Prøv igjen.")
        return endre_reise(dictionary)
    if endre == "nei":
        return

    navn = input("Skriv reise du vil endre: ")
    if navn not in dictionary:
        print(f"{navn} er ikke gyldig, prøv igjen.")
        return endre_reise(dictionary)

    attributt = (
        input(
            f"Vil du endre {navn} reisen din sitt klær eller dato info? (Skriv klær eller dato): "
        )
        .strip()
        .lower()
    )

    if attributt not in ("klær", "dato"):
        print(f"{attributt} er ikke gyldig, prøv igjen.")
        return endre_reise(dictionary)

    klaer_old, dato_old = dictionary[navn]

    if attributt == "klær":
        klaer_ny = input("Skriv inn klær: ")
        dictionary[navn] = (klaer_ny, dato_old)
    dato_ny = input("Skriv inn dato: ")
    dictionary[navn] = (klaer_old, dato_ny)

    print("Oversikt:")
    print_dict(dictionary)


def main():
    dest_dict = {}
    for _ in range(2):
        navn, klear, dato = reise_info()
        dest_dict[navn] = klear, dato

    print_dict(dest_dict)
    hent_info(dest_dict)

    endre_reise(dest_dict)


if __name__ == "__main__":
    main()
