# 03.14
def rgber():
    koder = input("Skriv inn RGB kode: ")
    deler = koder.split(" ")
    print(f"Typen til split på str er: {type(deler)} !!")
    if len(deler) != 3:
        print("ERROR, too few args")
        return

    r = int(deler[0])
    g = int(deler[1])
    b = int(deler[2])

    if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
        print("Error, out of 0-255")
        return

    print("ALT OK!")


def main():
    rgber()

if __name__ == "__main__":
    main()
