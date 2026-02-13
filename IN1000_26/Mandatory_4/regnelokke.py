def funk():
    # Del 1
    tall = 1
    samling = []
    while tall != 0:
        tall = int(input("Tall: "))
        # Del 2
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
