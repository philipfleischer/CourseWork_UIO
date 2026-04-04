#02.22
# Forklar i hvilken rekkefølge de forskjellige linjene utføres når vi kjører programmet

def prosedyre_a():                              # 14
    navn = input("Navn: ")                      # 15
    print("Hei,", navn)                         # 16

def prosedyre_b():                              # 9
    alder = int(input("Alder: "))               # 10
    print("Om ti år er din alder", alder)       # 11

def start():                                    # 2
    a = 5                                       # 3
    b = 5                                       # 4

    if a > b:                                   # 5
        b = 10
    elif b > a:                                 # 6
        prosedyre_a()
    else:                                       # 7
        prosedyre_b()                           # 8

    print(a + b)                                # 12

start()                                         # 1
prosedyre_a()                                   # 13
