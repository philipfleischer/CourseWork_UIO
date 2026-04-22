"""Oppgave 5A: Blokkerte oppdrag
I brettspillet Gloomhaven kan man spille mange forskjellige oppdrag som har hvert sitt nummer. Når du fullfører et oppdrag, kan dette blokkere andre oppdrag (slik at de ikke lenger kan spilles).

Dette representerer vi med en ordbok 'oppdrag' hvor nøklene er oppdragsnummer, og verdiene lister hvor:
- Element 0 viser om oppdraget er fullført (True) eller ikke (False).
- Element 1 er en liste over oppdrag som kan blokkere dette oppdraget hvis de fullføres.
Før noen av oppdragene er fullført vil denne ordboken se slik ut:

# oppdragsnummer: [fullført, blokkeres_av]
oppdrag = { 16: [False, []],
            24: [False, []],
            25: [False, []],
            33: [False, [42]],
            40: [False, [42]],
            41: [False, [42]],
            42: [False, [41]]}

Lag en funksjon er_blokkert(nummer, oppdrag) som tar inn følgende parametere:
- nummer: heltallsnummer på et oppdrag som vi skal sjekke om er blokkert.
- oppdrag: en ordbok på formatet vist i eksempelet over, men ikke nødvendigvis med de samme verdiene.

Funksjonen skal returnere True hvis oppdraget med nummer 'nummer' er blokkert av et annet oppdrag som er fullført, og False hvis ikke.
I denne deloppgaven kan du anta at 'nummer' alltid vil være en nøkkel som finnes i oppdrag.

Skriv ditt svar her:"""

# oppdragsnummer: [fullført, blokkeres_av]
oppdrag = { 16: [False, []],
            24: [False, []],
            25: [False, []],
            33: [False, [42]],
            40: [False, [42]],
            41: [False, [42]],
            42: [False, [41]]}


def er_blokkert(nummer, oppdrag):
    blokkeres_av = oppdrag[nummer][1]

    for oppdragsnr in blokkeres_av:
        if oppdrag[oppdragsnr][0]:
            return True

    return False


def main():
    blokk = er_blokkert(42, oppdrag)
    print(blokk)


if __name__ == "__main__":
    main()
