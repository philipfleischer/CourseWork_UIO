"""
SortertRekke-klasse:
- Lages med en liste elementer som vi antar er heltall (ikke unike nødvendigvis).
- Når vi går gjennom et SortertRekke-objekt men en for-løkke, får
    vi alle elementene (med riktig antall repetisjoner), men sortert.
- To SortertRekke-objekter være like hvis de inneholder de samme tallene (men uavhengig av antall).
- len(...) av en SortertRekke skal være antal UNIKE tall
"""

class SortertRekke:
    def __init__(self, liste):
        self._liste = liste
        self._antall = {}
        self._nokler = []
        for element in liste:
            if element not in self._antall:
                self._antall[element] = 0
                self._nokler.append(element)
            self._antall[element] += 1

        # Sorterer nøklene i stigende rekkefølge
        self._nokler.sort()

    def __len__(self):
        return len(self._nokler)

    def __iter__(self):
        for nokkel in self._nokler:
            antall = self._antall[nokkel]
            for i in range(antall):
                yield nokkel

    def __eq__(self, other):
        return self._nokler == other._nokler


sr = SortertRekke([1, 1, 2, 1, 1]) # len(sr) == 2
sr2 = SortertRekke([2, 1])  # len(sr2) == 2
sr3 = SortertRekke([2, 1, 0])  # len(sr3) == 3

print(len(sr))
print(len(sr2))
print(len(sr3))
print()

for tall in sr:
    print(tall)  # 1 -> 1 -> 1 -> 1 -> 2
print()
print(sr == sr2) #True
print(sr == sr3) #False
