# Oppgave 3 (løkker og lister):
# 1) Lager en liste [0..9] med while-løkke
# 2) Lager samme liste med for-løkke
# 3) Svarer på teori om forskjellen på while vs for, og hvorfor for-løkke "har en samling"
# 5) Lager en liste med tall som øker med 3 til og med 20
# 6) Skriver ut tallene i listen
# 7) Skriver ut indeksene i listen
# 8) Endrer listen slik at alle tall ganges med 10
# 9) Skriver ut listen etter endring

# Teori (punkt 3 og 4)
# 3) Forskjellen på hvordan man tenker:
# - While-løkke: man må selv styre når løkken skal stoppe. Man lager ofte en teller, oppdaterer den i løkken, og bruker en betingelse (f.eks. teller < 10).
# - For-løkke: man vet hvor mange ganger man vil ha gjentakelse, og lar Python "gå gjennom" en samling (f.eks: range(10)). Da slipper man å håndtere stopping manuelt.
# 4) En for-løkke forutsetter at man allerede har en samling:
# a) Samlingen finnes i uttrykket etter "in". For eksempel: for i in range(10): Her lager range(10) en "samling/sekvens" av verdier som for-løkken itererer over.
# b) Elementene i denne samlingen er tallene 0 til 9 (altså list(range(10)) == [0,1,2,3,4,5,6,7,8,9]). Samlingen man lager selv (listen) får ofte de samme tallene, men forskjellen er:
# - range(10) er "kilden" løkken itererer over
# - listen er resultatet man fyller opp med append()


def del1():
    # 1) While-løkker er gode når vi vil ha kontroll underveis og kan stoppe på en gitt betingelse
    samling = []
    teller = 0
    while teller < 10:
        samling.append(teller)
        teller += 1
    return samling


def del2():
    # 2) For-løkker er gode når vi vet antall gjentagelser
    samling = []
    for i in range(10):
        samling.append(i)
    return samling


def del5():
    samling = []
    teller = 0
    while teller <= 20:
        samling.append(teller)
        teller += 3
    return samling


def print_del6(samling):
    # 69 Skriver ut tallene én etter én
    for i in samling:
        print(i)


# Teori (punkt 7 og 8)
# 7) Når vi skal skrive ut indeksene:
#    for i in range(len(samling)):
#    fordi vi trenger posisjonene 0..len-1, ikke selve tallene i listen.
#
# Kunne noen samlingsvalg skapt problemer?
# Ja: Hvis man prøver "for i in samling: print(samling[i])" så antar man at tallene i listen kan brukes som indekser. Det går ofte galt (f.eks. hvis listen har tall 0,3,6...), eller hvis tallene er større enn lengden på listen.
#
# 8) Når vi skal endre innholdet (gange alle med 10), må vi endre på indeksene:
#    for i in range(len(samling)): samling[i] *= 10


def print_del7(samling):
    # 7) Skriver ut indeksene
    for i in range(len(samling)):
        print(i)


def endre_del8(samling):
    for i in range(len(samling)):
        samling[i] *= 10


def main():
    samling1 = del1()
    samling2 = del2()

    print("Del 1 (while):", samling1)
    print("Del 2 (for):", samling2)

    samling3 = del5()
    print("\nDel 5 liste:", samling3)

    print("\nDel 6 (skriv tall):")
    print_del6(samling3)

    print("\nDel 7 (skriv indekser):")
    print_del7(samling3)

    endre_del8(samling3)
    print("\nDel 9 (etter *=10):", samling3)


if __name__ == "__main__":
    main()
