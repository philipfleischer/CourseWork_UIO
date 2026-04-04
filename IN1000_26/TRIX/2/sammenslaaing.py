# 02.05
def sammenslaaingen():
    # a)
    a, b = 10, "hei!"
    # c = a+b   # c vil gi feilmelding TypeError, siden en Int og Str ikke kan konkateneres eller summeres
    c = str(a)+b
    print(c)

    # b)
    x, y = "10", "hei"
    print(x + y)    # Dette går fint: 10hei

    # c)
    i, j = 10, "12"
    # print(i + j)  # Dette gir feil, TypeError som i oppgave a.
    print(i+int(j))

def main():
    sammenslaaingen()


if __name__ == "__main__":
    main()
