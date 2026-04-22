"""Oppgave 3B: Generér en gyldig kalender
Skriv om funksjonen 'lagKalender2023', slik at den bare lager gyldige datoobjekter. Dato-objektene skal komme i riktig (kronologisk) rekkefølge med 1. januar 2023 først og 31.desemeber 2023 til slutt. Du kan fortsatt bruke denne globale ordboken:

dageriMnd = { 1:31, 2:28, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

def lagKalender2023():
    kalender = []
    for dag in range(32):
        for mnd in range(13):
            kalender.appen(Dato(dag,mnd,2023))
    return kalender

Skriv funksjonen lagKalender2023 her:

Svar ->"""
from oppgave_3a import Dato

dageriMnd = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def lagKalender2023():
    kalender = []

    for mnd in range(1, 13):
        for dag in range(1, dageriMnd[mnd] + 1):
            kalender.append(Dato(dag, mnd, 2023))

    return kalender


lagKalender2023()
