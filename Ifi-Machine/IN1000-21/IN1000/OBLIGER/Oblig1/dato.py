#I de to linjene under, blir bruker bedt om å skrive inn to tallverdier, den første, dato, den andre, måned.
dag = int(input("Skriv inn en dagsdato: "))
maaned = int(input("Skriv inn en måned (1-12): "))
#Under laget jeg en liste med de forskjellige månedene
maaneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
#Under printer jeg dagen etterfulgt av et punktum og til slutt måneden, som brukeren valgte. Jeg satte maaned-1 siden indeksen starter på 0
print(dag, ".", maaneder[maaned-1])
#Dette er det samme konseptet som over
dag2 = int(input("Skriv inn en ekstra dagsdato: "))
maaned2 = int(input("Skriv inn en ekstra måned (1-12): "))

print(dag2, ".", maaneder[maaned2-1])
#Her laget jeg en if-test, de tre første if-ene gir riktig rekkefølge, den siste eli
if dag < dag2 and maaned == maaned2:
    print("Riktig rekkefølge")
elif dag == dag2 and maaned < maaned2:
    print("Riktig rekkefølge")
elif dag > dag2 and maaned < maaned2:
    print("Riktig rekkefølge")
elif dag < dag2 and maaned < maaned2:
    print("Riktig rekkefølge")
elif dag == dag2 and maaned == maaned2:
    print("Samme dato!")
else:
    print("Feil rekkefølge")
