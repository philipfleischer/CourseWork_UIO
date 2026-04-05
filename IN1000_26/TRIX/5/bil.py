#05.05
def les_bil(filnavn):
    resultatet = {}
    with open(filnavn, "r") as f:
        for line in f:
            deler = line.strip().split(":")
            kategori = deler[0]
            verdi = deler[1]
            resultatet[kategori] = verdi
        f.close()
    return resultatet

def skriv_res(bok):
    for kat, ver in bok.items():
        print(f"Kategorien: {kat} har verdien: {ver}")


def main():
    res = les_bil("bil.txt")
    skriv_res(res)

if __name__ == "__main__":
    main()
