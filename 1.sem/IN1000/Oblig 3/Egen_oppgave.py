"""Du skal lage et program som spør navnet til brukeren.
Deretter skal det bli spurt om en allergi brukeren har.
Lag en ordbok der nøkkelordet er allergien og forskjellige matretter som kan og ikke kan spises kommer etter.
Lag deretter en prosedyre der allergien skal bli kjørt gjennom ordboken, hint - for-loop.
I prosedyren skal det bli brukt en if-setning.
Hvis allergien er i ordboken skal det bli skrevet ut, hvis den ikke er det skal det komme en feilmelding.
Nå skal du kjøre prosedyren.
Til slutt skal brukeren få en quiz om den allergien som ble valgt"""


navn = input("Skriv inn fornavn og etternavn: \n< ")
print("Hei", navn)
allergi = input("Skriv inn hvilken allergi du har (gluten-, sitrusallergi eller laktoseintollerant) \n< ")

spiselige_allergier = {
"glutenallergi" : [{"Brokkoli", "Tomatsuppe", "Kjøttgryte"}, {"Pizza", "Brød", "Lefse"}],
"sitrusallergi" : [{"Pizza", "Taco", "Pasta"}, {"Sitron", "Appelsin", "Lime"}],
"laktoseintollerant" : [{"Hallumi", "Kjeks", "Knekkebrød"}, {"Melk", "Youghurt", "ost"}]
}

def svarAllergi1():
    for key in spiselige_allergier:
        if key == allergi:
            print("Ut ifra hvilken allergi du har kan du f.eks. spise:", spiselige_allergier[allergi][0])
            print("Mat som du ikke kan spise her er:", spiselige_allergier[allergi][1])
            break
        else:
            print("Noe gikk galt")

svarAllergi1()

poeng = 0
if allergi == "glutenallergi":
    sporsmaal1 = input("Hva er gluten? \n< ")
    x = sporsmaal1.lower()
    if x == "protein" or sporsmaal1 == "et protein":
        print("Riktig")
        poeng+=1
    else:
        print("Feil")
        poeng-=1
    sporsmaal2 = input("Hvilken sykdom gjør gluten problematisk \n< ")
    y = sporsmaal2.lower()
    if y == "cøliaki":
        print("riktig")
        poeng+=1
    else:
        print("Feil")
        poeng-=1
    sporsmaal3 = input("Er en allergisk reaksjon farlig? \n< ")
    z = sporsmaal3.lower()
    if z == "nei":
        print("Riktig")
        poeng+=1
        print("Du fikk", poeng, "poeng!")
    else:
        print("Feil")
        poeng-=1
        print("Du fikk", poeng, "poeng!")
elif allergi == "sitrusallergi":
    sporsmaal1 = input("Er sitrusallergi vanlig? \n< ")
    x = sporsmaal1.lower()
    if x == "nei":
        print("Riktig")
        poeng+=1
    else:
        print("Feil")
        poeng-=1
    sporsmaal2 = input("Hvorfor reagerer man på dette? \n< ")
    y = sporsmaal2.lower()
    if y == "protein" or sporsmaal2 == "proteinet":
        print("Riktig")
        poeng+=1
    else:
        print("feil")
        poeng-=1
    sporsmaal3 = input("Hva er den enkleste forebyggingen en kan gjøre? \n< ")
    z = sporsmaal3.lower()
    if z == "slutte" or sporsmaal3 == "stoppe":
        print("Riktig")
        poeng+=1
        print("Du fikk", poeng, "poeng!")
    else:
        print("Feil")
        poeng-=1
        print("Du fikk ", poeng, "poeng:(")
elif allergi == "laktoseintollerant":
    sporsmaal1 = input("Er det å være laktoseintollerant vanlig? \n< ")
    x = sporsmaal1.lower()
    if x == "nei":
        print("Riktig")
        poeng+=1
    else:
        print("Feil")
        poeng-=1
    sporsmaal2 = input("Hvorfor reagerer man på dette? \n< ")
    y = sporsmaal2.lower()
    if y == "karbohydrat" or sporsmaal2 == "karbohydratet" or sporsmaal2 == "melkesukker":
        print("Riktig")
        poeng+=1
    else:
        print("feil")
        poeng-=1
    sporsmaal3 = input("Hva er den enkleste forebyggingen en kan gjøre? \n< ")
    z = sporsmaal3.lower()
    if z == "slutte" or sporsmaal3 == "stoppe":
        print("Riktig")
        poeng+=1
        print("Du fikk ", poeng, "poeng!")
    else:
        print("Feil")
        poeng-=1
        print("Du fikk ", poeng, "poeng:(")
else:
    print("Noe galt har skjedd")
