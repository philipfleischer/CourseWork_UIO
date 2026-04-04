# 03.13
def flaggerfarger(flaggOrdbok):
    flaggOrdbok["uruguay"] = ["blått", "hvitt", "gult"]

    for land, farger in flaggOrdbok.items():
        print(land)
        print(f"----{farger}")


def land_til_farge(flaggOrdbok):
    landet = input("Land: ")
    if landet.lower() not in flaggOrdbok:
        print("ERROR")
        return
    fargene = []
    for land, farger in flaggOrdbok.items():
        if land == landet:
            fargene = farger

    for farger in fargene:
        print(farger)

    farg = input("Skriv farge: ")
    if farg in fargene:
        print("Fargen forekommer i landets flagg")
    else:
        print("Fargen forekommer IKKE i landets flagg")


def main():
    flaggOrdbok = {
        "norge": ["rødt", "hvitt", "blått"],
        "sverige": ["blått", "gult"],
        "danmark": ["rødt", "hvitt"],
        "finland": ["hvitt", "blått"],
        "japan": ["rødt", "hvitt"],
        "gabon": ["grønt", "gult", "blått"],
        "storbritannia": ["rødt", "blått", "hvitt"],
        "chile": ["blått", "hvitt", "rødt"],
    }
    flaggerfarger(flaggOrdbok)
    land_til_farge(flaggOrdbok)

if __name__ == "__main__":
    main()
