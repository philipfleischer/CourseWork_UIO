# 04.04
def lokke_liste():
    aviser = ["Aftenposten", "VG", "Morgenbladet", "Dagbladet", "Klassekampen"]
    for e in aviser:
        print(e)

def lokke_mengde():
    partall = {10, 8, 6, 4, 2, 0}
    for t in partall:
        print(t)

def lokke_dict():
    kallenavn = {
        "Roger": "Roggis",
        "Magnus": "Kluten",
        "Stine": "Lappen",
        "Ingeborg": "Skruen",
    }
    for navn, kallenavn in kallenavn.items():
        print(navn)

def lokke_dict_values():
    kallenavn = {
        "Roger": "Roggis",
        "Magnus": "Kluten",
        "Stine": "Lappen",
        "Ingeborg": "Skruen",
    }
    for navn, kallenavn in kallenavn.items():
        print(kallenavn)

def main():
    lokke_liste()
    lokke_mengde()
    lokke_dict()
    lokke_dict_values()

if __name__ == "__main__":
    main()
