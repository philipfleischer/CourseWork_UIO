"""Oppgaveteksten til denne quizen:
Du skal i denne oppgaven lage en quiz. Start med å gi en varm velkomst.
Deretter spørre om navn og hvor enkel quizen vil bli i en skala fra 1-10 i
samme input-felt.
Hvis svaret på skalaen er fra 6-10, skal en ting skje, samme fra 4-0 og Hvis
det er 5, så skal det stå, "kjedelig tall".
Deretter skal det komme tre spørsmål, vanskelighetsgraden skal stige for brukeren.
Spørsmål 1 skal spørre hvor mange måneder det er i et semester, med if-test.
Spørsmål 2 skal spørre hvilke aldersgrenser det er på filmer, med if-test.
Spørsmål tre skal spørre hvor enkelt neste spørsmål skal være på en skala fra 1-10
Til slutt skal poeng bli telt opp for hver riktig og/eller feil oppgaver og det skal komme en slutt-melding"""


print("Hei og velkommen til en god quiz!")
navn_ambisjon = input("Hva heter du og hvor godt tror du dette vil gå fra 1-10? \n< ")
navnOgAmbisjon = navn_ambisjon.split(maxsplit=1)
if int(navnOgAmbisjon[1]) >= 6:
    print(f''"Hei", navnOgAmbisjon[0] + ". Jasså", navnOgAmbisjon[1], "er rimelig ambisiøst")
if int(navnOgAmbisjon[1]) == 5:
    print(f''"Hei", navnOgAmbisjon[0] + ". Jasså", navnOgAmbisjon[1], "er et rimelig kjedelig tall")
if int(navnOgAmbisjon[1]) <= 4:
    print(f''"Hei", navnOgAmbisjon[0] + ". Jasså", navnOgAmbisjon[1], "er et tegn på at dette kommer til å bli vanskelig", navnOgAmbisjon[0])

poeng = 0
sporsmaal1 = int(input("Hvor mange måneder er et semester (Svar i heltall)? \n<"))
if sporsmaal1 == 6:
    print("Helt riktig")
    poeng +=1
    print("poeng: ",poeng)
else:
    print("Feil svar")
    poeng -= 1
    print("poeng: ",poeng)
#trim funksjon
sporsmaal2 = input("Hvilke aldersgrenser er det på filmer? svar f.eks: 10,12,14 \n< ")
delt = sporsmaal2.split(",")
print(delt)
if delt[0] == "12" and delt[1] == "16" and delt[2] == "18":
    print("Helt riktig")
    poeng += 1
    print("poeng: ",poeng)
else:
    print("Feil svar")
    poeng -= 1
    print("poeng: ",poeng)

sporsmaal3 = int(input("Ut ifra nivået som har vært til nå, vil neste spørsmål være over/under 5 (svar i heltall)? \n< "))
if sporsmaal3 < 5:
    print("Helt riktig. Quizen er over")
    poeng += 1
    print("poeng: ",poeng)
elif sporsmaal3 == 5:
    print("Tja, litt kjedelig svar. Quizen er over")
    print("poeng: ",poeng)
else:
    print("Feil svar. Quizen er over")
    poeng -= 1
    print("poeng: ",poeng)

if poeng == 3:
    print("Antall poeng er ",poeng, ". Du har fått alt rikitg!!")
elif poeng == 2 or poeng == 1:
    print("Antall poeng er ",poeng, ". Det kan lønne seg å prøve på nytt:)")
else:
    print("Dette gikk ikke så bra du fikk:",poeng,"poeng. Prøv på nytt.")
