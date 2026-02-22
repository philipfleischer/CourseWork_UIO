def ant_bokstaver(ord):
    return len(ord)

def ant_ord(tekst):
    ordbok = {}
    ord_liste = tekst.strip().split()
    tot_ord = len(ord_liste)
    for i in range(len(ord_liste)):
        if ord_liste[i] in ordbok:
            ordbok[ord_liste[i]] += 1
        else:
            ordbok[ord_liste[i]] = 1

    return ordbok, tot_ord

def main():
    # ord = input("Skriv inn ord: ")
    # print(f"Antall bokstaver i {ord} er: {ant_bokstaver(ord)}")

    # tekst = input("SKriv inn en tekst: ")
    # print(f"Ord og antall forekomster i {tekst} = {ant_ord(tekst)}")

    tekst = input(">>>Skriv inn en setning:\n>>>").strip().lower()
    ordbok, tot_ord = ant_ord(tekst)
    print(f">>>Det er {tot_ord} ord i setningen din.")
    for ord, ant in ordbok.items():
        print(f">>>Ordet '{ord}' forekommer {ant} ganger, og har {ant_bokstaver(ord)} bokstaver")

if __name__ == "__main__":
    main()
