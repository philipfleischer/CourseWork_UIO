class Bil:
    def __init__(self, eier):
        self._eier = eier

    def print_eier(self):
        print(self._eier)

bil1 = Bil("Magnar")
bil2 = Bil("Hildur")
bil2.print_eier()
