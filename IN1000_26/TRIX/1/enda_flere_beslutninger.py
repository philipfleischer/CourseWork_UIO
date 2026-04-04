#01.16
def beslutningera():
    # a)
    a, b = 6, 5
    if a+b > 11:
        print("IN1000")     # NEI

    # b)
    if 1 == 1 and 2 > 3:
        print("IN1000")     # NEI

    # c)
    if 1 < 2 or 2 < 1:
        print("IN1000")     # JA

    # d)
    if 3 < 2:
        print("IN1000")     # NEI
    elif 4 + 2 == 6:
        print("IN1000")     # JA
    else:
        print("ingenting")  # NEI

    #e)
    a, b = "b", 3
    if 1 == 2:
        if "a" == a:
            print("IN1000")     # NEI
        else:
            print("ingenting")  # NEI
    else:
        if 1 > 2 or  1 < 2:
            if b >= 3:
                print("IN1000")     # JA
            else:
                print("ingenting")  # NEI
        else:
            print("ingenting")  # NEI

def main():
    beslutningera()

if __name__ == "__main__":
    main()
