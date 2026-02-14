# Oppgave 4: Egen oppgave — Løkker og samlinger
#
# Oppgavetekst:
# Lag et lite "bursdagsregister" som lar brukeren holde styr på venners bursdager. Programmet skal bruke både løkker og en samling (ordbok/dictionary).
#
# 1) Bruk en dictionary der nøkkel er navn (string) og verdi er bursdag (string på format "DD.MM").
# 2) Programmet skal kjøre i en løkke og vise en meny helt til brukeren velger å avslutte.
# 3) Menyen skal ha disse valgene:
#    (1) Legg til/oppdater bursdag
#    (2) Søk etter bursdag (skriv inn navn og få bursdagen tilbake)
#    (3) Skriv ut alle bursdager sortert alfabetisk etter navn
#    (4) Slett en bursdag
#    (5) Avslutt
# 4) Programmet skal håndtere ugyldige valg (f.eks. hvis brukeren skriver "9" eller tekst).
# 5) Når man legger til bursdag, skal programmet sjekke at formatet er "DD.MM".


def legg_til(ob: dict, navn: str, dato: str) -> bool:
    dato = dato.strip()

    if len(dato) != 5 or dato[2] != ".":
        return False

    dag, maaned = dato.split(".", 1)

    if not (dag.isdigit() and maaned.isdigit()):
        return False

    ob[navn] = dato
    return True


def get_dato(ob: dict, navn: str) -> None:
    if navn not in ob:
        print("Person finnes ikke i databasen")
        return

    print(f"{navn}: {ob[navn]}")


def alph(ob: dict) -> None:
    if not ob:
        return

    alf_samling = list(ob.keys())
    alf_samling.sort()
    print_alf(ob, alf_samling)


def print_alf(ob: dict, samling: list) -> None:
    for navn in samling:
        print(f"Navn: {navn}. Fodselsdato: {ob[navn]}")


def slett(ob, navn):
    if navn in ob:
        del ob[navn]
        print(f"Sletet {navn} fra databasen")
    else:
        print("Person ikke i databasen")


def meny(ob: dict) -> None:
    while True:
        valg = input(
            "\nMeny:\n- (1) Legg til/oppdater bursdag\n- (2) Søk etter bursdag (skriv inn navn og få bursdagen tilbake)\n- (3) Skriv ut alle bursdager sortert alfabetisk etter navn\n- (4) Slett en bursdag\n- (5) Avslutt\n-> "
        ).strip()

        if valg == "1":
            navn = input("Skriv navn: ").strip()
            dato = input("Skriv fodselsdato: ").strip()
            ok = legg_til(ob, navn, dato)
            if ok:
                print("Lagret")
            else:
                print("Ugyldig dato. Bruk DD.MM, f.eks: 27.01")

        elif valg == "2":
            navn = input("Skriv navn: ").strip()
            get_dato(ob, navn)

        elif valg == "3":
            alph(ob)

        elif valg == "4":
            navn = input("Skriv navn: ").strip()
            slett(ob, navn)

        elif valg == "5":
            print("Avslutter")
            break

        else:
            print("Ugyldig input, må være mellom 1-5")

    return


def main():
    ob = {}
    navn1 = "Karl"
    dato1 = "27.01"

    legg_til(ob, navn1, dato1)

    meny(ob)


if __name__ == "__main__":
    main()
