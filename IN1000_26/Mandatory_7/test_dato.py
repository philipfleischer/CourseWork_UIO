from oblig7 import Dato


def main():
    dato = Dato("28.02.2026")

    print(dato.hent_år())

    if dato.dag_er_lik(15):
        print("Lønningsdag!")
    elif dato.dag_er_lik(1):
        print("Ny måned, nye muligheter")

    print(dato)
    dato.neste_dag()
    print(dato)

    ny_dato = input("Skriv inn ny dato (dd.mm.åååå) her: ")
    dato.endre_til(ny_dato)
    print(dato)


if __name__ == "__main__":
    main()
