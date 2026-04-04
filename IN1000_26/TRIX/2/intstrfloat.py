#02.02
def hvatype():
    # a)
    print(type(3))      # int

    # b)
    print(type("3"))    # str

    # c)
    print(type(5.0 + 3.5))  # float

    # d)
    print(float("4" + ".8") / 2)    # float 2.4

    # e)
    print("3" + "5")        # str 35

    # f)
    print("3"*3)            # str 333

    # g)
    print(type(3*"A"))      # str

    # h)
    print(type(int("3")))   # int

    # i)
    #print(3 + "3")      # TypeError

    # j)
    print(float(3))     # 3.0

    # k)
    print("1.50" == "1.5")  # False

    # l)
    print(float("1.50") == float("1.5"))    # True

def main():
    hvatype()


if __name__ == "__main__":
    main()
