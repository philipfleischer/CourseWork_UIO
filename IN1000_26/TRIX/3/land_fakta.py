# 03.04
def ordboeker_land():
    cap_bok = {"Norge": "Oslo", "Nederland": "Amsterdam", "Spania": "Madrid"}
    lan_bok = {"Norge": "norsk", "Nederland": "nederlandsk", "Spania": "spansk"}
    pop_bok = {"Norge": 5391369, "Nederland": 17282163, "Spania": 46733038}

    land = input("Skriv inn land: ")
    if land not in cap_bok:
        print("Error")
        return
    print(cap_bok[land])
    print(lan_bok[land])
    print(pop_bok[land])

def nested_land():
    landFakta = {
        "Norge": {"hovedstad": "Oslo", "spraak": "norsk", "innbyggere": 5391369},
        "Nederland": {"hovedstad": "Amsterdam", "spraak": "nederlandsk", "innbyggere": 17282163},
        "Spania": {"hovedstad": "Madrid", "spraak": "spansk", "innbyggere": 46733038}
    }

    land = input("Skriv land: ")
    if land in landFakta:
        print(f"Hovedstaden til {land} er {landFakta[land]["hovedstad"]}")
        print(f"I {land} snakker folk {landFakta[land]["spraak"]}")
        print(f"{land} har {landFakta[land]["innbyggere"]} innbyggere")
    else:
        print("ERROR")


def main():
    ordboeker_land()
    nested_land()

if __name__ == "__main__":
    main()
