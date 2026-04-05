#05.11
def sorter_etter_karakater(filnavn):
    kar = {}
    with open(filnavn, "r") as f:
        for line in f:
            navn, karakter = line.strip().split(",")
            if karakter in kar:
                kar[karakter].append(navn)
            else:
                kar[karakter] = [navn]  # Må lagre dette som en liste her
    return kar

def skriv_ut_sortert(bok):
    OPPGAVE B

def main():
    bok = sorter_etter_karakater("karakter.csv")
    skriv_ut_sortert(bok)

if __name__ == "__main__":
    main()
