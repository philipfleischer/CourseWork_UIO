def toolcase1(tall1, tall2):
    print("\nVelg beregning:")
    print("1) Addisjon")
    print("2) Subtraksjon")
    print("3) Divisjon")

    valg = input("Ditt valg (1-3): ").strip()

    if valg == "1":
        adder = addisjon(tall1, tall2)
        print(f"Resultat av summering: {adder}\n")
        assert isinstance(adder, int), "Adder is not int, error"

    elif valg == "2":
        subber = subtraksjon(tall1, tall2)
        print(f"Resultat av subtraksjon: {subber}\n")
        assert isinstance(subber, int), "Subber is not int, error"

    elif valg == "3":
        divver = divisjon(tall1, tall2)
        if divver is not None:
            print(f"Resultat av divisjon: {divver}\n")

    else:
        print("Ugyldig valg.\n")


def addisjon(tall1, tall2):
    return tall1 + tall2

def subtraksjon(tall1, tall2):
    return tall1 - tall2

def divisjon(tall1, tall2):
    try:
        return tall1 / tall2
    except ZeroDivisionError:
        print("Error, cant divide by zero!")
        return None


def toolcase2(tommer):
    tommer_cm = 2.54
    if tommer < 0:
        print("Not valid")
        return

    cm = tommer * tommer_cm
    print(f"Resultat: {cm}")
    return

def skriv_beregninger():
    try:
        print("Velg verktøy:")
        print("1) Utregninger (add/sub/div)")
        print("2) Konvertering fra tommer til cm")

        valg = input("Ditt valg (1-2): ").strip()

        print("Utregninger:")

        if valg == "1":
            tall1 = int(input("Skriv inn tall 1: "))
            tall2 = int(input("Skriv inn tall 2: "))
            toolcase1(tall1, tall2)

        elif valg == "2":
            print("Konvertering fra tommer til cm:")
            tall3 = int(input("Skriv inn tall: "))
            toolcase2(tall3)

    except ValueError:
        print("Needs to be a numeric value")
        return

def main():
    skriv_beregninger()


if __name__ == "__main__":
    main()
