# 04.03
def minst_stoerst():
    tallListe = [6, -4, 7, -2, 8, -3, 9, -11]

    # Finn minste
    minst = tallListe[0]
    for tall in tallListe:
        if tall < minst:
            minst = tall
    print(f"Minste med for: {minst}")
    minste = min(tallListe)
    print(f"Minste med min(): {minste}")

    # Finn største
    storst = tallListe[0]
    for tall in tallListe:
        if tall > storst:
            storst = tall
    print(f"Største med for: {storst}")
    storste = max(tallListe)
    print(f"Største med max(): {storste}")



def main():
    minst_stoerst()

if __name__ == "__main__":
    main()
