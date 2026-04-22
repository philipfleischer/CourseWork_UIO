"""Oppgave 2D: Funksjon med hjemmelaget objekt
Skriv funksjonen 'obliger_godkjent' som skal beregne akkurat det samme som funksjonen godkjent i oppgave 2B. Eneste forskjellen er at parameteren til funksjonen nå er et studentobjekt av klassen Student. Merk at funksjonen skal skrives i det globale skopet og at de dermed ikke har tilgang til instansvariabelen self._obliger.

Svar ->"""


class Student:
    def __init__(self, obliger):
        # parameteren obliger er ei liste med poeng (heltall)
        # variabler som starter med _ er utilgjengelig utenfor klassen
        self._obliger = obliger

    def antall_obliger(self):
        return len(self._obliger)

    def oblig(self, nr):
        return self._obliger[nr - 1]


def obliger_godkjent(student):
    if student.antall_obliger() != 8:
        return False

    sum_foerste_seks = 0
    for nr in range(1, 7):
        sum_foerste_seks += student.oblig(nr)

    if sum_foerste_seks >= 19 and student.oblig(7) > 0 and student.oblig(8) > 0:
        return True
    else:
        return False
