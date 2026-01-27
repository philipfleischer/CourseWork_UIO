def in_out():
    navn = input("Skriv inn navn: ")
    fra = input("Hvor kommer du fra? ")
    print(f"Hei, {navn}! Du er fra {fra}\n")


def main():
    in_out()
    in_out()
    in_out()


if __name__ == "__main__":
    main()
