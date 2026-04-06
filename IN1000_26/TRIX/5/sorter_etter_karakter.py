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
    for karakterer in sorted(bok.keys()):
        print(f"{karakterer}: {bok[karakterer]}")

def hent_vanligste_karakter(bok):
    vanligste = 0
    retur = ""
    for karakter, navn in bok.items():
        if len(navn) > vanligste:
            vanligste = len(navn)
            retur = karakter

    return retur

def main():
    bok = sorter_etter_karakater("karakter.csv")
    skriv_ut_sortert(bok)
    print(hent_vanligste_karakter(bok))

if __name__ == "__main__":
    main()
