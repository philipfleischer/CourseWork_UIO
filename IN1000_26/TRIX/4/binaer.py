#04.13
def binary():
    tall = int(input("Tast inn et tall: "))

    while tall != 0:
        print(tall%2)
        tall = tall//2

def main():
    binary()

if __name__ == "__main__":
    main()
