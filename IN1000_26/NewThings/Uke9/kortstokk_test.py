# from kortstokk import Spillkort, Kortstokk
from kortstokk import Kortstokk

kortstokken = Kortstokk() #Lager kortstokk som innehodler mange kort

kortstokken.stokk() # Stokker alle kortene i kortstokken

# Nytt i uke 9
print()
for kort in kortstokken:
    print(kort)

øverste_kort = kortstokken.trekk() # Popper det øverste korten i bunken

print()
print(f"Øverste kort har symbol {øverste_kort.symbol} og verdi {øverste_kort.verdi}!")
print(øverste_kort)
print()

print()
for kort in kortstokken:
    print(kort)
