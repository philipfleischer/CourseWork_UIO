# Dette programmet konverterer temperaturer mellom Fahrenheit og Celsius.
# Først bes brukeren om å skrive inn en temperatur i Fahrenheit og skriver
# ut tilsvarende verdi i Celsius. Deretter kan brukeren skrive inn en vilkårlig
# temperatur og velge enhet (C eller F), og programmet konverterer temperaturen
# til den andre enheten. Programmet inneholder også sjekk for ugyldig input slik
# at brukeren må skrive inn gyldige tall og riktige enheter.


def fahr_til_cel(fahr: float) -> float:
    return (fahr - 32) * 5 / 9


def cel_til_fahr(cel: float) -> float:
    return (cel / 5) * 9 + 32


def temp_checker(inp: str) -> float:
    while True:
        try:
            return float(input(inp))
        except ValueError:
            print("Ugyldig tall, prøv igjen")


def type_checker(inp: str) -> str:
    while True:
        enhet = input(inp).strip().upper()
        if str(enhet) in ("C", "F"):
            return str(enhet)
        print("Ugyldig enhet, bruk C eller F.")


def del_1():
    fahrenheit = temp_checker("Skriv inn temp i Fahrenheit: ")
    print(f"Fahrenheit: {fahrenheit}. Celsius: {fahr_til_cel(fahrenheit):.2f}")


def del_2():
    temperatur = temp_checker("Skriv inn en temperatur: ")
    enhet = type_checker("Skriv inn temp enhet: C/F -> ")

    if enhet == "F":
        print(f"{temperatur} F = {fahr_til_cel(temperatur):.2f} C")
    else:
        print(f"{temperatur} C = {cel_til_fahr(temperatur):.2f} F")


def main():
    del_1()
    del_2()


if __name__ == "__main__":
    main()
