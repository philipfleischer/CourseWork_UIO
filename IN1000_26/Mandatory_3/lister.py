"""
Dette programmet demonstrerer bruk av lister i Python.
Først opprettes en liste med tall, hvor det legges til et nytt tall,
og programmet skriver ut utvalgte elementer samt beregner summen og produktet.
Deretter kombineres tallene med disse resultatene i en ny liste.
Til slutt ber programmet brukeren om navn, lagrer dem i en liste,
og sjekker om et bestemt navn finnes i listen.
"""


def lister():
    # Del 1
    tall = [1, 2, 3]
    tall.append(4)
    print(f"Første elem i listen: {tall[0]}. Tredje elem i listen: {tall[2]}")

    # Del 2
    summen = sum(tall)
    prod = 1

    for t in tall:
        prod *= t

    ny_liste = [summen, prod]
    alt_liste = []
    for t in tall:
        alt_liste.append(t)

    for e in ny_liste:
        alt_liste.append(e)

    print(alt_liste)

    # Del 3
    tom_liste = []
    for _ in range(3):
        tom_liste.append(input("Skriv inn navn: "))

    print(tom_liste)

    if "Philip" in tom_liste:
        print("Du husket meg!")
    else:
        print("Glemte du meg?")


def main():
    lister()


if __name__ == "__main__":
    main()
