"""
Dette programmet bruker en ordbok til å lagre beboere og deres daglige måltider.
Hver beboer er knyttet til en liste som inneholder frokost, lunsj og middag.
Programmet skriver først ut navnene på alle registrerte beboere.
Deretter kan brukeren velge en beboer og få skrevet ut matplanen.
Hvis beboeren ikke finnes, gis det en feilmelding til brukeren.
"""


def matplan():
    # Del 1
    maaltidsPlan = {
        "Vigdis": ["brød", "egg", "pølser"],
        "Terje": ["knekkebrød", "yoghurt", "kjøttkaker"],
    }

    for beboer, _ in maaltidsPlan.items():
        print(beboer)

    while True:
        navn = input("Skriv inn navn til en beboer: ")
        if navn in maaltidsPlan:
            print(f"Matplanen til {navn} er: {maaltidsPlan[navn]}")
            break
        else:
            print("Beboer er ikke registrert.")


def main():
    matplan()


if __name__ == "__main__":
    main()


"""
Teoretisk spørsmål svar:
1. Ville brukt en mengde/set for alle brukernavn på IN1000 studenter, siden det er samme datatype og alle skal være unike.
2. Ville brukt en dictionary/ordbok for å knytte brukernavn og antall stp i key-value pairs, siden dette er naturlig og gir raskt oppslag og oversikt.
3. Ville brukt en liste for alle navn til lottovinnere, siden vi bare vil ha oversikt over dem.
4. Ville brukt en dictionary/ordbok for gjesters navn og deres allergier, siden det gir god oversikt, lett å legge inn unike verdier til hver nøkkel og det er raskt å slå opp.
"""
