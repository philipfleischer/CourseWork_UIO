# Deloppgave 4D: Institutt
from oppgave_4a import Emne
from oppgave_4b import Studieprogram

class Institutt:

    def __init__(self, navn):
        self.navn = navn
        self._studieprogrammer = []
        self._emner = {}

    def legg_til(self, studieprogram):
        self._studieprogrammer.append(studieprogram)

        for emne in studieprogram:
            self._emner[emne.emnekode] = emne

    def __iter__(self):
        for studieprogram in self._studieprogrammer:
            yield studieprogram

    def __len__(self):
        return len(self._studieprogrammer)
