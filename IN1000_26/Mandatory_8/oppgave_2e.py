"""Oppgave 2E: Metode
Skriv metoden 'obliger_godkjent' som skal beregne akkurat det samme som funksjonen 'obliger_godkjent' i forrige oppgave. Eneste forskjell er at metoden skal være med i grensesnittet til klassen Student. Du trenger bare å skrive selve metoden, ikke resten av klassen.

Skriv metoden 'obliger_godkjent' her:
Svar->"""


def obliger_godkjent(self):
    sum_foerste_seks = 0
    for nr in range(1, 7):
        sum_foerste_seks += self.oblig(nr)

    return sum_foerste_seks >= 19 and self.oblig(7) > 0 and self.oblig(8) > 0
