# Deloppgave 4B: Studieprogram


class Studieprogram:

    def __init__(self, navn):
        self.navn = navn
        self._data = {}

    def legg_til(self, emne):
        if emne.emnekode not in self._data.keys():
            self._data[emne.emnekode] = emne
            return
        else:
            print(f"{emne.emnekode} finnes fra før!")

    @property
    def emne_ordbok(self):
        return self._data

    def __iter__(self):
        for emne in self._data.values():
            yield emne

    def __len__(self):
        return len(self._data)
