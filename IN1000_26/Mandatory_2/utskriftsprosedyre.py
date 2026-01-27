# Dette programmet ber brukeren om å skrive inn navn og hvor de kommer fra,
# og skriver deretter ut en hilsen. Funksjonen kjøres tre ganger slik at
# programmet kan ta imot og skrive ut informasjon fra tre forskjellige brukere.


def in_out():
    navn = input("Skriv inn navn: ")
    fra = input("Hvor kommer du fra? ")
    print(f"Hei, {navn}! Du er fra {fra}\n")


def main():
    in_out()
    in_out()
    in_out()


if __name__ == "__main__":
    main()
