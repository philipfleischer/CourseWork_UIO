tom_liste = []

i=0
tall = int(input("Skriv inn et heltall: \n< "))
while i < tall:
    tall = int(input("Skriv inn et heltall: \n< "))
    if tall != 0:
        tom_liste.append(tall)
        continue
    else:
        break

for tall in tom_liste:
    print(tall)

minSum = 0
for tall in tom_liste:
    minSum += tall
    print("Her er", minSum)

minst = tom_liste[0]
for e in tom_liste:
    if e < minst:
        minst = e
print("Minste verdi:",minst)

storst = tom_liste[0]
for e in tom_liste:
    if e > storst:
        storst = e
print("største verdi:", storst)
