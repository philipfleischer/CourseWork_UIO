from eksempel import fjern_alt, Spillkort

print()
print(" --- Hva er et objekt egentlig? ---")
print()
print("1) Objekter kan brukes passivt: En funksjon kan gjøre noe med et objekt.")
print("(Vi kaller funksjonen med objektet som argument)")
print()

listeobjekt = [1, 2, 3, 3, 2, 1]
print(listeobjekt) # Skriver ut objektet uten å endre på det

sortert_liste = sorted(listeobjekt) # returnerer et nytt listeobjekt uten å endre originalen
print(listeobjekt, sortert_liste)

fjern_alt(listeobjekt) # NOTE: denne funksjonen endrer objektets tilstand
print(listeobjekt)

print()
print("2) Objekter kan brukes aktivt: De har egne funksjoner (metoder) som lar objektene gjøre ting selv.")
print()

listeobjekt = [3,1,2] #Fyller pånytt
print(listeobjekt)

listeobjekt.sort()  # Lister ved hvordan de skal sortere innholdet sitt selv.
# NOTE: Her blir original-listen endret

print(listeobjekt)

print(listeobjekt.sort()) # denne metoden returnerer ingenting

print()
print("3) Objekter inneholder egne variabler (som vi kaller instansvariabler)")
print()

spillkortObjekt = Spillkort("hjerter", 2) # et hjemmelaget objekt
print(f"Å printe et hjemmelaget objekt gir i utgangspunktet: {spillkortObjekt}")

print()
print(f"Men vi kan printe instansvariabelen .type: {spillkortObjekt.type}")
print(f"og vi kan printe instansvariabelen .verdi: {spillkortObjekt.verdi}")

print()
print("4) Objekter har en bestemt type")
print()
print(f"listeobjektet har typen {type(listeobjekt)}")
print(f"spillkortobjekt har type {type(spillkortObjekt)}")
print()

"""
Hvordan ser vi forskjell på funksjoner og metoder?
- funksjon(objekt)
- objekt.metode()

Ikke bli forvirret av at metoder også kan ta inn ekstra argumenter!
- funksjon(objekt, annet_objekt)
- objekt.metode(annet_objekt)
- # "objekt" er her det aktive objektet som gjør noe.
- # "annet_objekt" er passivt argument til metoden.

Eksempel:
tall = HjemmelagetHeltall(10)
tall2 = HjemmelagetHeltall(20)
tall3 = tall.pluss(tall2)   # Samme som: tall3 = HjemmelagetHeltall(30).
"""


""" ------OUTPUT-------

--- Hva er et objekt egentlig? ---

1) Objekter kan brukes passivt: En funksjon kan gjøre noe med et objekt.
(Vi kaller funksjonen med objektet som argument)

[1, 2, 3, 3, 2, 1]
[1, 2, 3, 3, 2, 1] [1, 1, 2, 2, 3, 3]
[]

2) Objekter kan brukes aktivt: De har egne funksjoner (metoder) som lar objektene gjøre ting selv.

[3, 1, 2]
[1, 2, 3]
None

3) Objekter inneholder egne variabler (som vi kaller instansvariabler)

Å printe et hjemmelaget objekt gir i utgangspunktet: <eksempel.Spillkort object at 0x10b775be0>

Men vi kan printe instansvariabelen .type: hjerter
og vi kan printe instansvariabelen .verdi: 2

4) Objekter har en bestemt type

listeobjektet har typen <class 'list'>
spillkortobjekt har type <class 'eksempel.Spillkort'>

"""
