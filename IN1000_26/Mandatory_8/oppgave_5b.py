"""Deloppgave 5B: Opplåste oppdrag
I tillegg til blokkering, kreves det ofte at andre oppdrag er fullført for at et oppdrag skal låses opp og kunne spilles.

For å representere dette utvider vi ordboken 'oppdrag' fra forrige deloppgave, slik at nøklene fortsatt er oppdragsnummer, og verdiene lister hvor:
- Element 0 viser om oppdraget er fulltført (True) eller ikke (False).
- Element 1 er en liste over oppdrag som kan blokkere dette oppdraget hvis de fullføres.
- Element 2 er listen over oppdrag som alle må fullføres for å låse opp dette oppdraget.

Før noen av oppdragene er fullført, vil denne ordboken se slik ut:

# oppdragsnummer: [fullført, blokkeres_av, låses_opp_av]
oppdrag = { 16: [False, [], []],
            24: [False, [], [16]],
            25: [False, [], [16]],
            33: [False, [42], [25]],
            40: [False, [42], [24, 33]],
            41: [False, [42], [40]],
            42: [False, [41], [24]]}

Lag en funksjon kan_spilles(nummer, oppdrag) som tar inn følgende parametre:
- nummer: heltallsnummer på et oppdrag som vi skal sjekke om kan spilles
- oppdrag: en ordbok på formatet vist i eksempelet over, men ikke nødvendigvis med de samme verdiene
Funksjonen skal returnere False hvis oppdraget ikke kan spilles, det vil si hvis minst en av følgende stemmer:
- dette oppdragsnummeret finnes ikke i ordboken
- oppdraget er blokkert, det vil si at er_blokkert(nummer, oppdrag) returnerer True
(du kan anta at denne funksjonen virker selv om du ikke fikk til forrige deloppgave)
- man har ikke fullført alle oppdragene som dette oppdraget låses opp av
Hvis oppdraget derimot kan spilles, skal funksjonen returnere True.
Skriv ditt svar her"""

# oppdragsnummer: [fullført, blokkeres_av, låses_opp_av]
oppdrag = {
    16: [False, [], []],
    24: [False, [], [16]],
    25: [False, [], [16]],
    33: [False, [42], [25]],
    40: [False, [42], [24, 33]],
    41: [False, [42], [40]],
    42: [False, [41], [24]],
}


def er_blokkert(nummer, oppdrag):
    blokkeres_av = oppdrag[nummer][1]

    for oppdragsnr in blokkeres_av:
        if oppdrag[oppdragsnr][0]:
            return True

    return False


def kan_spilles(nummer, oppdrag):
    if nummer not in oppdrag:
        return False

    if er_blokkert(nummer, oppdrag):
        return False

    laases_opp_av = oppdrag[nummer][2]

    for oppdragsnr in laases_opp_av:
        if not oppdrag[oppdragsnr][0]:
            return False

    return True

def main():
    print(kan_spilles(16, oppdrag))  # True
    print(kan_spilles(24, oppdrag))  # False

if __name__ == "__main__":
    main()
