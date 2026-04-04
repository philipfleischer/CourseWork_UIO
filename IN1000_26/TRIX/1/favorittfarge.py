#01.11
def sjekkFarge():
    farge = input("Skriv inn fav farge: ")

    if farge.lower() == "gul":
        print(f"SITRON ER {farge}")
    elif farge.lower() == "oransje":
        print(f"APPELSIN ER {farge}")
    elif farge.lower() == "grønn":
        print(f"EPLE ER {farge}")

def main():
    sjekkFarge()

if __name__ == "__main__":
    main()
