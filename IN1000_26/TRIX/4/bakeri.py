# 04.xx
def bakeriet():
    bakeri = {}
    bakeri["Croissant"] = 25
    bakeri["Grovbroed"] = 40
    bakeri["Kneippbroed"] = 20
    bakeri["Rosinbolle"] = 20
    bakeri["Baguette"] = 10
    skriv_ut_bakeri(bakeri)
    print("Croissant koster nå 10 NOK mer!")
    bakeri["Croissant"] += 10
    skriv_ut_bakeri(bakeri)

def skriv_ut_bakeri(bakeri):
    print()
    for vare, pris in bakeri.items():
        print(f"Varen {vare} koster {pris} NOK.")
    print()


def main():
    bakeriet()

if __name__ == "__main__":
    main()
