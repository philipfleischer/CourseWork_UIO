print("Hei og velkommen til en enkel matte test!")
sporsmaal1 = int(input("Hva er 9+11?"))
if sporsmaal1 == 20:
    print("Riktig")

    sporsmaal2 = int(input("Hva er 10-20"))
    if sporsmaal2 == -10:
        print("Riktig")

        sporsmaal3 = int(input("Hva er 10*10?"))
        if sporsmaal3 == 100:
            print("Riktig")

            sporsmaal4 = int(input("Hva er 10/10?"))
            if sporsmaal4 == 1:
                print("Riktig")
                print("Du vant spillet!")
else:
    print("Du tapte spillet")
