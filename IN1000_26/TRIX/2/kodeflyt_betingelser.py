#02.11
# Skriv kjørerekkefølgen til linjene i følgende tre scenarioer:
# a) Hvis brukeren taster inn 50
# b) Hvis brukeren taster inn 80
# c) Hvis brukeren taster inn 21

def flyten():
    pris = 50
    tekst = input("Skriv inn alder: ")
    alder = int(tekst)

    if alder < 12 or alder > 67:
        print("Du må betale", pris*0.5, "kr")   # Bruker taster 80 her
    else:
        print("Du må betale", pris, "kr")   # Bruker taster 21 og 50 her

    print("Ha en fin dag!")

def main():
    flyten()

if __name__ == "__main__":
    main()
