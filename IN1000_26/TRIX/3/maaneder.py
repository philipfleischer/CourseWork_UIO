# 03.03
def maaned():
    mListe = [
        "Januar","Februar","Mars","April","Mai","Juni",
        "Juli","August","September","Oktober","November","Desember",
    ]
    mini = int(input("Skriv inn måned nummer: "))
    if mini < 0 or mini > 12:
        print("ERROR")
        return
    print(mListe[mini-1])

def main():
    maaned()

if __name__ == "__main__":
    main()
