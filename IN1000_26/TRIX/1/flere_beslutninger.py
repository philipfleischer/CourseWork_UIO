#01.13
def beslutninger():
    # a)
    a = 6
    if 6 == a:
        print("IN1000") # Skrives UT!

    # b)
    a = 5
    b = 6
    if a > b:
        print("IN1000") # Skrives IKKE UT!

    # c)
    a = 5 + 2
    b = 6
    if a <= b:
        print("IN1000") # Skrives IKKE UT!

    # d)
    a = 6
    b = a
    if a >= b:
        print("IN1000") # Skrives UT!

    # e)
    a = 6+1
    if a == a:
        print("ingenting")  # Skrives UT!
    else:
        print("IN1000") #Skrives IKKE UT!

def main():
    beslutninger()

if __name__ == "__main__":
    main()
