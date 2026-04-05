#05.05
def les_poeng(filnavn):
    poeng = {}
    with open(filnavn, "r") as f:
        for line in f:
            deler = line.strip().split(":")
            navn = deler[0]
            poenger = deler[1].split(",")
            tot = 0
            for poengs in poenger:
                tot += int(poengs)
            poeng[navn] = tot
    return poeng


def main():
    bok = les_poeng("poeng.txt")
    print(bok)

if __name__ == "__main__":
    main()
