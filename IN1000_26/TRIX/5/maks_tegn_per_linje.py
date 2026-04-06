#05.13
def tegner(tekst, utfil, maks_tegn):
    with open(utfil, "w") as f:
        ordene = tekst.strip().split()
        teller = 0
        for ord in ordene:
            if teller + len(ord) > maks_tegn:
                f.write("\n")
                teller = len(ord) + 1
            else:
                teller += len(ord) + 1
            f.write(ord)
            f.write(" ")


def main():
    tegner("I denne oppgave skal du lage et program som tar inn en tekst og skriver den ut til en fil. I utdatafilen er det maksimalt antall tegn som er tillatt per linje.", "test.out", 21)

if __name__ == "__main__":
    main()
