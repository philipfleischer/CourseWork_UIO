def adder(tall1, tall2):
    return tall1 + tall2


def min_forekomst(min_tekst, min_bokstav):

    count = min_tekst.count(min_bokstav)

    print(f"Antall forekomster av {min_bokstav} i {min_tekst} = {count}")


def main():
    sum = adder(1, 2)
    print(f"Sum av to tall er: {sum}\n")

    tekst = input("Skriv inn en streng: ")
    bokstav = input("Skriv inn en bokstav: ")
    min_forekomst(tekst, bokstav)

if __name__ == "__main__":
    main()
