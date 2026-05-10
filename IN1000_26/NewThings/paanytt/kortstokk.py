from random import shuffle

class Spillkort:
    def __init__(self, symbol, verdi):
        self._symbol = symbol
        self._verdi = verdi
        self.får_verdi_senere = None

    def hent_symbol(self):
        return self._symbol

    def hent_verdi(self):
        return self._verdi

    def __str__(self):
        return f"Symbol: {self._symbol} - Verdi: {self._verdi}"


class Kortstokk:
    def __init__(self):
        self._kort = []
        for symbol in ["hjerter", "kløver", "spar", "ruter"]:
            for verdi in range(2, 10):
                nytt_kort = Spillkort(symbol, verdi)
                self._kort.append(nytt_kort)

    def stokk(self):
        shuffle(self._kort)

    def trekk(self):
        overste = self._kort.pop()
        return overste

    def __iter__(self):
        for kort in self._kort:
            yield kort



def main():
    kortstokken = Kortstokk()
    kortstokken.stokk()
    overste_kort = kortstokken.trekk()
    print()
    print(f"Øverste kort har symbol {overste_kort.hent_symbol()} og verdi {overste_kort.hent_verdi()}")
    print()

    print()
    print("-----UKE9-----")
    for kort in kortstokken:
        print(kort)

if __name__ == "__main__":
    main()
