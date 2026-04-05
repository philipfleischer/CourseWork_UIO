# 05.06
def skriv_dna_til_terminal():
    print("0---o")
    print(" 0-o ")
    print("  0")
    print(" o-0")
    print("o---0")


def skriv_dna_til_fil(filnavn):
    with open(filnavn, "a") as f:   # 'w' overskriver hvert kall, 'a' legger til på nytt under
        f.write("0---o\n")
        f.write(" 0-o \n")
        f.write("  0\n")
        f.write(" o-0\n")
        f.write("o---0\n")


def main():
    skriv_dna_til_terminal()
    skriv_dna_til_fil("dna.txt")
    skriv_dna_til_fil("dna.txt")
    skriv_dna_til_fil("dna.txt")

if __name__ == "__main__":
    main()
