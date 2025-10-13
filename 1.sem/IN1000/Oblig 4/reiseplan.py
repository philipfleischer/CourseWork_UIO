steder = []
klesplagg = []
avreiseDatoer = []
antall = 5
for i in range(5):
    sted = input("Legg til sted: \n< ")
    steder.append(sted)
    plagg = input("Legg til klesplagg: \n< ")
    klesplagg.append(plagg)
    dato = input("Legg til avreisedato: \n< ")
    avreiseDatoer.append(dato)
    continue

print(steder, klesplagg, avreiseDatoer)

reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreiseDatoer)

for i in reiseplan:
    print("Under ser du 3 lister:\n", i)

liste_indeks1 = int(input("hvilken av listene ønsker du å gå inn i? (skriv ett tall mellom 0-2) \n< "))
liste_indeks2 = int(input("hvilken av elementene ønsker du å gå inn i? (skriv ett tall mellom 0-4)\n< "))

if liste_indeks1 == 0 or liste_indeks1 == 1 or liste_indeks1 == 2:
    print("Du har valgt denne listen:", reiseplan[liste_indeks1])
    if liste_indeks2 == 0 or liste_indeks2 == 1 or liste_indeks2 == 2 or liste_indeks2 == 3 or liste_indeks2 == 4:
        print("Du har valgt dette elementet: ", reiseplan[liste_indeks1][liste_indeks2])
else:
    print("Ugyldig input")
