#03.05
def tjeneste():
    ord = input("Skriv ord: ")
    print(ord.upper())
    print(f"Ant ord i listen: {len(ord)}")
    foerste = ord[0]
    print(f"Første bokstav i {ord} er {foerste}")
    ant_boks_i_ord = ord.count(foerste)
    print(f"Bokstaven forekommer {ant_boks_i_ord} ganger i {ord}")

def main():
    tjeneste()

if __name__ == "__main__":
    main()
