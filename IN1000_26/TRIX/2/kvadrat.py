#02.14
# Forklar i hvilken rekkefølge de forskjellige linjene utføres når vi kjører programmet.

def kvadrat():
    tall = input("Tall: ")                      # 5, 11
    tall = int(tall)                            # 6, 12

    print(tall, "*", tall, "=", tall * tall)    # 7, 13

def main():
    a = True                                    # 1
    b = False                                   # 2

    if a:                                       # 3
        kvadrat()                               # 4

    if b:                                       # 8
        kvadrat()

    print("En gang til:")                       # 9
    kvadrat()                                   # 10
