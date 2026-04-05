#05.09
def opprett_filen():
    fil = "test.in"
    with open(fil, "w") as f:
        for i in range(11):
            tall = str(i)
            f.write(tall + "\n")

def skriv_ut_foerste_linjer(filnavn, antall_linjer):
    with open(filnavn, "r") as f:
        for line in f:
            print(line.strip())
            antall_linjer -= 1
            if antall_linjer == 0:
                return

def skriv_ut_siste_linjer(filnavn, antall_linjer):
    filen = []
    with open(filnavn, "r") as f:
        for line in f:
            filen.append(line.strip())

    utfil = filen[-antall_linjer:]
    for linje in utfil:
        print(linje)


def main():
    opprett_filen()
    skriv_ut_foerste_linjer("test.in", 3)
    print()
    skriv_ut_siste_linjer("test.in", 3)

if __name__ == "__main__":
    main()
