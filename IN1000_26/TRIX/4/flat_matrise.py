# 04.09
def matr_flater():
    eksempel_matrise = [[0, 1, 2], [3, 2, 1], [1, 1, 0]]
    for liste in eksempel_matrise:
        print(liste)

    ny_tom = []
    for liste in eksempel_matrise:
        for element in liste:
            print(element)
            ny_tom.append(element)

    print(ny_tom)

    eksempel_3d_matrise = [[[0, 1, 2], [3, 2, 1]], [[1, 1, 0], [4, 2, 3], [2, 1, 0]]]

    nyere = []
    for lister in eksempel_3d_matrise:
        for liste in lister:
            for element in liste:
                nyere.append(element)

    print(nyere)

def main():
    matr_flater()

if __name__ == "__main__":
    main()
