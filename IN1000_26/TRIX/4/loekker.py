# 04.01
def for_loekke():
    for i in range(11):
        print(i)

def while_loekke():
    count = 0
    while count < 11:
        print(count)
        count+=1

def for_loekke_liste():
    liste = ["Sauer", "er", "myke", "dyr."]
    for dyr in liste:
        print(dyr)

def while_loekke_liste():
    liste = ["Sauer", "er", "myke", "dyr."]
    indeks = 0

    while indeks < len(liste):
        print(liste[indeks])
        indeks+=1

def main():
    for_loekke()
    while_loekke()
    for_loekke_liste()
    while_loekke_liste()

if __name__ == "__main__":
    main()
