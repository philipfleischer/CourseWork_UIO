#Laget en dictionary under som består av nøkkelverdier og flyttall (tror nok ikke det er flyttall, men gjerne forklar hvordan jeg evt skulle gjort dette)
varer = {
"Melk": "14.90kr",
"Brød": "24.90kr",
"Yoghurt": "12.90kr",
"Pizza": "39.90kr"
}
print(varer)

#Under blir brukeren spurt om navn på vare og prisen
vare1 = input("Skriv inn en vare og prisen: \n< ")
#Under blir vare og pris splittet
fullstendig_vare1 = vare1.split(" ")
vare2 = input("Skriv inn en til vare og prisen: \n< ")
fullstendig_vare2 = vare2.split(" ")

#Under legger jeg inn nøkkelverdien og flyttallet til ordboken (varer)
varer[fullstendig_vare1[0]] = fullstendig_vare1[1]
varer[fullstendig_vare2[0]] = fullstendig_vare2[1]
#printer ut ordboken
print(varer)
