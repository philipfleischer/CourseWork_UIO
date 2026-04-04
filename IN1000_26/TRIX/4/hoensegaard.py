# 04.15
def simuler_natt(ant_levende):
    kommer_rev = input("Kommer reven?\n>")
    if kommer_rev.lower() == "nei":
        return
    sover_bonde = input("Sover bonden?\n>")
    if sover_bonde.lower() == "ja":
        ant_levende -= 3
        if ant_levende < 0:
            print("Det bor nå 0 høner på gården.")
        else:
            print(f"Det bor nå {ant_levende} høner på gården.")
    else:
        print(f"Det bor {ant_levende} høner på gården. Bonden selger ett reveskinn, og tjener 190kr.")
    return ant_levende


def main():
    ant_levende = int(input("Hvor mange høner bor på gården?\n> "))
    while ant_levende > 0:
        ant_levende = simuler_natt(ant_levende)

if __name__ == "__main__":
    main()
