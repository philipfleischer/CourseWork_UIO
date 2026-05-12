class Person:
    def __init__(self, alder):
        self._alder1 = 0
        alder2 = alder  # merk at ikke self

    def sett_alder1(self, alder):
        self._alder1 = alder

    def sett_alder3(self, alder):
        alder3 = alder  # merk at ikke self

    def hent_alder1(self):
        return self._alder1

    def hent_alder2(self):
        return alder2  # merk at ikke self

    def hent_alder3(self):
        return alder3  # merk at ikke self


p1 = Person(10)
p2 = Person(20)
print(p1.hent_alder2())
