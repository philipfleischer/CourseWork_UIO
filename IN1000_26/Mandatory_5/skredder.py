"""Skriv et beregningsprogram for skreddere med en funksjon som
leser inn en fil (som du lager selv og leverer sammen med de andre filene) der hver linje
beskriver et navn på et mål og selve målet i tommer. Formatet vil se slik ut:
Skulderbredde 4
Halsvidde 3.2
Livvidde 10
La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og
returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av
funksjonen tommer_til_cm som du skrev tidligere for å skrive ut målene i centimeter."""

def skredder(filnavn):
    ordbok = {}
    with open(filnavn, 'r') as fil:
        for linje in fil:
            deler = linje.split()
            type_maal = deler[0]
            maal = deler[1]
            ordbok[type_maal] = maal
    return ordbok


def alle_tommer_til_cm(ordbok):
    tommer_cm = 2.54
    for navn, maal in ordbok.items():
        try:
            if float(maal) < 0:
                print("Tommer må være positivt heltall")
                return

            cm = float(maal) * tommer_cm
            print(f"{navn} {cm}")
        except ValueError:
            print(f"{maal} -> Needs to be numeric value")


def main():
    file = "skredder_maal.csv"
    ordbok = skredder(file)
    alle_tommer_til_cm(ordbok)

if __name__ == "__main__":
    main()
