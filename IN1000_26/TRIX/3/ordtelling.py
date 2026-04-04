# 03.02
def ordslister():
    ordliste = [
        "I","dag","er","jeg","så","lykkelig","så","lykkelig","så","lykkelig","det",
        "hele","endte","dejligt","jeg","synger","og","er","glad","Ja","alting","endte",
        "lykkeligt","så","lykkeligt","så","lykkeligt","i","dag","er","jeg",
        "så","lykkelig","som","dagen","den","er","lang",
    ]
    print(f"Lengden av ordliste: {len(ordliste)} --!!!")

    ordmengde = set(ordliste)
    print(f"Antall unike ord i ordliste: {len(ordmengde)}")

    ordBok = {"lykkelig": 0, "så": 0, "dag": 0}
    antLykke = 0
    antSaa = 0
    antDag = 0
    for ord in ordliste:
        if ord == "lykkelig":
            antLykke += 1
            ordBok["lykkelig"] = antLykke
        elif ord == "så":
            antSaa += 1
            ordBok["så"] = antSaa
        elif ord == "dag":
            antDag += 1
            ordBok["dag"] = antDag
    print(f"lykkelig: {antLykke} ganger, så: {antSaa} ganger, dag: {antDag} ganger.")

    for ord, ant in ordBok.items():
        print(f"Ordet {ord} forekommer {ant} ganger i ordboken!")

    boklisten = list(ordBok)        # Her får vi en liste med nøkler
    bokmengden = set(ordBok)        # Her får vi en mengde med nøkler

    print("\nOrdbok liste:")
    print(boklisten)
    print("\nOrdbok mengde:")
    print(bokmengden)


    #Bedre måte å legge inn antall forekomster:
    frekvens = {}
    frekvens["lykkelig"] = ordliste.count("lykkelig")
    frekvens["så"] = ordliste.count("så")
    frekvens["dag"] = ordliste.count("dag")

    print(frekvens)

def main():
    ordslister()

if __name__ == "__main__":
    main()
