# Programmet leser inn heltall fra brukeren helt til brukeren skriver 0. Tallene lagres i en liste. Etterpå skriver programmet ut alle tallene, regner ut summen uten sum(), og finner minste og største tall uten min()/max(). Dette trener på while-løkke (ukjent antall input) og for-løkke (gå gjennom samling).


def funk():
    # Del 1
    tall = 1
    samling = []
    while tall != 0:
        tall = int(input("Tall: "))
        # Del 2
        if tall != 0:
            samling.append(tall)

    # Del 3
    for t in samling:
        print(t)

    # Del 4
    summ = 0
    for t in samling:
        summ += t
    print("Summen:", summ)

    # Del 5
    minst = 0
    storst = 0
    for t in samling:
        if t < minst:
            minst = t
        if t > storst:
            storst = t

    print("min:", minst, " max:", storst)


def main():
    funk()


if __name__ == "__main__":
    main()
