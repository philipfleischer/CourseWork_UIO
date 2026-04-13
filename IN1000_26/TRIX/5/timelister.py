# 05.15
"""
05.15 Timelister

I denne oppgave skal du lage et system for å holde styr på timelister. Dette er en utfordrende oppgave som omhandler fillesing, filskriving, og ordbøker.

Vi har flere timeliste filer som ser slik ut:

Den første linjen i filen er en overskrift som inneholder navn
Resten av filen er 5 linjer som inneholder antall arbeidstimer for hver dag i arbeidsuken.

timeliste1.txt:

Louise,Sven,Kaja,Anna
8,6,7,6
8,6,7,7
4,6,0,0
8,6,4,0
8,6,0,0

timeliste2.txt:

Anna,Odd,Paal
0,4,8
0,4,8
6,5,8
8,5,8
6,5,0

a) Skriv en funksjon som leser inn en timelistefil og returnerer resultatet som en ordbok.
Funksjonen skal returnere følgende gitt fil 1:
{'Louise': [8, 8, 4, 8, 8], 'Sven': [6, 6, 6, 6, 6], 'Kaja': [7, 7, 0, 4, 0], 'Anna': [6, 7, 0, 0, 0]}

b) Skriv en funksjon som slår sammen to timelisteordbøker. Hvis et navn vises i begge ordbøkene, bør tidsoppføringene summeres sammen.

Resultatet skal se slik ut:
{'Louise': [8, 8, 4, 8, 8], 'Sven': [6, 6, 6, 6, 6], 'Kaja': [7, 7, 0, 4, 0], 'Anna': [6, 7, 6, 8, 6], 'Odd': [4, 4, 5, 5, 5], 'Paal': [8, 8, 8, 8, 0]}

c) Skriv en prosedyre som tar en timelisteordbok og skriver den til en fil på den samme formaten som de andre filene. Den skal ha to parametre: en timelisteordbok og et utdatafilnavn. Bruk denne prosedyren til å skrive den kombinerte timelisteordbok en fil.
"""
# 05.15


def les_timeliste(filnavn):
    fil = open(filnavn, "r")

    navneListe = fil.readline().strip().split(",")
    time_ordbok = {}

    for navn in navneListe:
        time_ordbok[navn] = []

    for linje in fil:
        timeliste = linje.strip().split(",")
        for i in range(len(navneListe)):
            navn = navneListe[i]
            tim = int(timeliste[i])
            time_ordbok[navn].append(tim)

    fil.close()
    return time_ordbok


def slaa_sammen(ordbok1, ordbok2):
    ny_ordbok = {}

    for noekkel in ordbok1:
        ny_ordbok[noekkel] = ordbok1[noekkel][:]

    for noekkel in ordbok2:
        if noekkel in ny_ordbok:
            for i in range(5):
                ny_ordbok[noekkel][i] += ordbok2[noekkel][i]
        else:
            ny_ordbok[noekkel] = ordbok2[noekkel][:]

    return ny_ordbok


def skriv_timeliste_til_fil(timeliste_bok, utfil):
    fil = open(utfil, "w")

    navneListe = list(timeliste_bok.keys())
    fil.write(",".join(navneListe) + "\n")

    for i in range(5):
        linje = []
        for navn in navneListe:
            linje.append(str(timeliste_bok[navn][i]))
        fil.write(",".join(linje) + "\n")

    fil.close()


def main():
    bok1 = les_timeliste("timeliste1.txt")
    bok2 = les_timeliste("timeliste2.txt")
    merged_time = slaa_sammen(bok1, bok2)
    skriv_timeliste_til_fil(merged_time, "timelisteUt.txt")


if __name__ == "__main__":
    main()
