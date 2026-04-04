def spør_om_is():
    kuler = int(input("Hvor mange kuler: "))
    kPris = 30
    print(f"Prisen for {kuler} kuler is er {kPris * kuler} kr.")

def spør_om_pizza():
    pris = 100
    typ_P = input("Type pizza: ")
    if typ_P.lower() == "ost":
        pris = 80
    print(f"Pizzaen {typ_P} koster {pris} kr.")

def ta_bestilling():
    hva = input("Hva vil du ha: ")
    if hva.lower() == "is":
        spør_om_is()
    elif hva.lower() == "pizza":
        spør_om_pizza()
    else:
        print("Må være pizza eller is")

def main():
    ta_bestilling()

if __name__ == "__main__":
    main()
