# 04.12
def gronnsaks_forretning():
    beholdning = {}

    svar = ""
    while svar != "q":
        gronnsak = input("Oppgi grønnsak: ")
        pris = int(input("Oppgi pris: "))
        if not isinstance(pris, int):
            print("ERROR")
            return
        beholdning[gronnsak] = pris
        svar = input("Skriv 'q' for å avslutte eller trykke enter for å fortsette")

    for gronnsak, pris in beholdning.items():
        print(f"{gronnsak} : {pris} NOK")

def main():
    gronnsaks_forretning()

if __name__ == "__main__":
    main()
