# 03.10
def matrisen():
    liste_noestet = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(liste_noestet[0][0]) # skriver ut 1
    print(liste_noestet[1][2]) # skriver ut 6
    print(liste_noestet[2][1]) # skriver ut 8

    sum_1_kol = sum(liste_noestet[0])
    print(f"Summen av 1. kolonne: {sum_1_kol}")

    print(
        f"Summen av det første elementet i hver liste: {liste_noestet[0][0] + liste_noestet[1][0] + liste_noestet[2][0]}"
    )

def main():
    matrisen()

if __name__ == "__main__":
    main()

""" OUTPUT:

1
6
8
Summen av 1. kolonne: 6
Summen av det første elementet i hver liste: 12

"""
