"""Oppgave 2B: Funksjon
Skriv en prosedyre 'godkjent' som sjekker om en student kan fremstille seg til eksamen i IN1000. Maks. poeng for obligene i IN1000 representerer vi i denne lista: [3,5,5,5,5,6,1,1]. Maks poeng er 3 for oblig 1, 5 for oblig2, osv. På de første 6 obligene kan poengene variere fra 0 til maks, men for å få godkjent de første seks må summen være minst 19 (maks sum er 29). På de to siste gis 1 for godkjent og 0 for ikke godkjent. For at det obligatoriske arbeidet skal være godkjent må summen av poengene på oblig 1-6 være minst 19, og oblig 7 og 8 må begge ha 1 poeng. 'godkjent' tar poenglista som eneste parameter og returnerer True hvis poengkravet for å gå opp til eksamen er oppfylt, False ellers."""


def godkjent(poengliste):
    sum_foerste_seks = sum(poengliste[0:6])

    if sum_foerste_seks >= 19 and poengliste[6] > 0 and poengliste[7] > 0:
        return True
    else:
        return False


def main():
    poengliste = [3, 5, 5, 5, 5, 6, 1, 1]
    ta_eksamen = godkjent(poengliste)
    print(ta_eksamen)


if __name__ == "__main__":
    main()
