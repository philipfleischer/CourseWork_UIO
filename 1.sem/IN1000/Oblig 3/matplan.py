print("Under er alle beboerne: \n<")
person_mat = {
"Anne": ["Frokost: Boller", "Lunsj: Brød", "Middag: Pasta"],
"Per": ["Frokost: Brød", "Lunsj: Boller", "Middag: Pizza"],
"Berit": ["Frokost: Hallumi", "Lunsj: Brød", "Middag: Pasta"],
"Geir": ["Frokost: Pizza", "Lunsj: Boller", "Middag: Pasta"]
}
#Her har jeg laget en prosedyre kalt kallbeboerne() bruker en for-løkke for å finne og skrive ut nøkkelverdiene
def kallbeboerne():
    for key in person_mat:
        print(key)
    beboer = input("Skriv inn en av beboerne over: \n<")

    if beboer in person_mat:
        print(beboer, "er registrert. Dette er favorittmåltidene:")
        print(person_mat[beboer])
    else:
        print(beboer, "er ikke registrert")

kallbeboerne()

"""
a)
Jeg ville brukt en liste siden det kun er en type elementer som blir implementert.
b)
Jeg ville brukt en ordbok siden det er to typer elementer som blir implementert.
Der brukernavnet er nøkkelverdien og poengene er innholdsverdiene.
c)
Jeg ville også her bare brukt en liste, siden du får ut personen,
selv om to stykker deler samme fornavn. Deler de samme fornavn mellomnavn og etternavn,
som er usannsynelig, kunne man også ha brukt mengde, for å finne ut hvor mange
ganger det tilfellet forekommer.
d)
Her ville jeg ha brukt en ordbok for å holde styr på hvem som har allergi,
hvilken allergi de har og hvilke typer mat de kan og ikke kan spise.
I tillegg ville jeg brukt mengde for å vite hvor mange som ikke kan spise
de forskjellige rettene og dermed ikke lage for mye eller for lite mat.
"""
