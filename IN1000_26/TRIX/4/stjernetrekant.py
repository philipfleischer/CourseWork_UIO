#04.05
def stjernerne():
    stjerner = ""
    teller = 0

    while teller < 9:
        stjerner += "*"
        teller += 1
        print(stjerner)

def main():
    stjernerne()


if __name__ == "__main__":
    main()
