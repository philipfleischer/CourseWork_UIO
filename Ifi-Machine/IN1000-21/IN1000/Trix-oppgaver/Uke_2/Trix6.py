print("Hei og velkommen")
tall1 = input("Skriv inn et tall")
tall2 = input("Skriv inn et tall til")
tall3 = input("Skriv inn et siste tall")
print("Det største tallet er: ")
if tall1 <= tall2 and tall2 <= tall3:
    print(tall3)
    if tall3 == tall2 and tall3 == tall1:
            print("Det er 3 like av tallet")
    elif tall3 == tall2 or tall3 == tall1:
            print("Det er 2 like tall")

elif tall1 <= tall2 and tall2 >= tall3:
    print(tall2)
    if tall2 == tall3 and tall2 == tall1:
            print("Det er 3 like tall")
    elif tall2== tall3 or tall2 == tall1:
            print("Det er 2 like tall")
else:
    print(tall1)
    if tall1 == tall2 and tall1 == tall3:
            print("Det er 3 like tall")
    elif tall1 == tall2 or tall1 == tall3:
            print("Det er to like tall")
