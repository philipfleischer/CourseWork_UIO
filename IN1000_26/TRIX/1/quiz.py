#01.14
def lagetQuiz():
    poeng = 0
    spm1 = input("Cap Norge: ")
    if spm1 != "Oslo":
        print("Beklager, svaret var Oslo")
        poeng-=1
    else:
        print("Helt rett! +1 poeng")
        poeng+=1

    spm2 = input("Cap Sverige: ")
    if spm2 == "Stockholm":
        print("Helt korrekt!")
        poeng+=1
    else:
        print("Beklager, svaret var Stockholm")
        poeng -= 1
    print(f"Du fikk {poeng} poeng!")

def main():
    lagetQuiz()

if __name__ == "__main__":
    main()
