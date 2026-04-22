"""Oppgave 3C: Kalendere for flere år
I et år er det 365 dager, bortsett fra i skuddår som har 29. februar (29.2) i tillegg. Så et skuddår har 366 dager. Skriv en funksjon som returnerer ei ordbok med kalendere for årene fra og med 2023 til og med 2041. En kalender er en liste med dato-objekter. I tillegg til ordboken dageriMnd har du en global liste over skuddår i perioden:

skuddår = [2024, 2028, 2032, 2036, 2040]
dageriMnd = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

Ordaboken som returneres skal ha årstallet som nøkkel, og innholdsverdien skal være kalenderen (liste av datoobjekter) for det året.

Skriv funksjonen lagKalender2023_2040 her:

Svar ->"""
from oppgave_3a import Dato

skuddår = [2024, 2028, 2032, 2036, 2040]
dageriMnd = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }


def lagKalender2023_2040():
    kalendere = {}

    for aar in range(2023, 2042):
        kalender = []

        for mnd in range(1, 13):
            antall_dager = dageriMnd[mnd]

            if mnd == 2 and aar in skuddår:
                antall_dager = 29

            for dag in range(1, antall_dager + 1):
                kalender.append(Dato(dag, mnd, aar))

        kalendere[aar] = kalender

    return kalendere


def main():
    antall_aar = 2040 - 2023
    kalender = []
    for i in range(antall_aar + 1):
        kalender = lagKalender2023_2040()

    print(kalender)


if __name__ == "__main__":
    main()

lagKalender2023_2040()
