# Lager brukernavn fra fullt navn, bygger e-postadresse med valgt suffix, og tilbyr en enkel meny der brukeren kan lagre og skrive ut e-poster.

def lag_brukernavn(navn):
    deler = navn.split()
    if len(deler) < 2:
        fornavn = deler[0] if deler else ""
        return fornavn.lower()

    fornavn = deler[0]
    etternavn = deler[-1]
    brukernavn = fornavn + etternavn[:1]
    return brukernavn.lower()

def lag_epost(brukernavn, suffix):
    return f"{brukernavn}@{suffix}"

def skriv_ut_eposter(ordbok):
    for navn, suffix in ordbok.items():
        brukernavn = lag_brukernavn(navn)
        print(lag_epost(brukernavn, suffix))

def interaktivt_prog():
    ordbok = {}
    svar = "Fortsett"
    while True:
        print("\nMeny\n")
        print("1) Tilføje nytt navn og e-post suffix")
        print("2) Skrive ut alle e-postaddresser")
        print("3) Avslutte? Skriv '3'")
        svar = input("Oppgi svar (1-3): ").strip()

        if svar == "1":
            navn = input("Skriv inn fullt navn: ").strip()
            suffix = input("Skriv inn e-post suffix: ").strip()
            ordbok[navn] = suffix

        elif svar == "2":
            if ordbok:
                skriv_ut_eposter(ordbok)
            else:
                print("Ingen elementer i ordbok enda, legg til flere")

        elif svar == "3":
            break

    return

def main():
    interaktivt_prog()


if __name__ == "__main__":
    main()
