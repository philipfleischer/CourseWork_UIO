# 05.07
def format_text(text, filnavn, maks_ord):
    teller = 0
    with open(filnavn, "w") as f:
        ordene = text.split()
        for ord in ordene:
            if teller >= maks_ord:
                f.write("\n")
                teller = 0
            f.write(ord)
            f.write(" ")
            teller += 1


def main():
    format_text(
        "I denne oppgave skal du lage et program som tar inn en tekst og skriver den ut til en fil. I utdatafilen er det maksimalt antall ord som er tillatt per linje.",
        "maks_ord.txt",
        5,
    )

if __name__ == "__main__":
    main()
