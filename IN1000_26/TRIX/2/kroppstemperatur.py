def kroppstemp():
    temp = float(input("Skriv inn kropp temp: "))
    if temp < 36.5:
        print("Du er kald")
    elif temp > 37.5:
        print("Du er varm")
    else:
        print("Du er hverken kald eller varm")

def main():
    kroppstemp()


if __name__ == "__main__":
    main()
