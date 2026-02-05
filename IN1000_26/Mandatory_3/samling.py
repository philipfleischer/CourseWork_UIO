"""
Dette programmet bruker en ordbok (dictionary) for å lagre butikkvarer og tilhørende priser.
Programmet starter med forhåndsdefinerte varer og skriver disse ut.
Deretter får brukeren legge til nye varer med tilhørende priser i samlingen.
Til slutt kan brukeren velge en vare og få prisen skrevet ut.
Ordbok er valgt fordi den knytter hver vare (nøkkel) direkte til en pris (verdi).
"""


def samling():
    # Del 1
    matPriser = {"melk": 14.90, "brød": 24.90, "yoghurt": 12.90, "pizza": 39.90}

    # Valgte å bruke en dictionary/ordbok, siden det er den enkleste måten å samle matvarer som nøkler og prisen som verdier

    for vare, pris in matPriser.items():
        print(vare, "- koster:", pris, "kr")

    # Del 2
    vare1 = input("Skriv inn vare: ")
    pris1 = input(f"Skriv inn pris til {vare1}: ")
    matPriser[vare1] = pris1

    vare2 = input("Skriv inn vare: ")
    pris2 = input(f"Skriv inn pris {vare2}: ")
    matPriser[vare2] = pris2

    for vare, pris in matPriser.items():
        print(vare, "- koster:", pris, "kr")

    vareUt = input("Hvilken vare ønsker du?: ")
    if vareUt in matPriser:
        print(f"{vareUt} - koster {matPriser[vareUt]} kr")
    else:
        print("Varen finnes ikke")


def main():
    samling()


if __name__ == "__main__":
    main()
