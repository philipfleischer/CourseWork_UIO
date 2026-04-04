# 04.08
def while_inputs1():
    tall = int(input("Tall1: "))
    teller = 0
    while tall >= teller:
        print(teller)
        teller+=1


def while_inputs2():
    svar = ""
    while svar != "slutt":
        print("Hei!")
        svar = input("Skriv inn noe: ")


def while_inputs3():
    tall = 1
    while tall < 10:
        tall = int(input("Skriv inn tall: "))


def main():
    while_inputs1()
    while_inputs2()
    while_inputs3()

if __name__ == "__main__":
    main()
