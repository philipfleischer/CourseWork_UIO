from kortstokk import Spillkort, Kortstokk

kortstokken = Kortstokk()
kortstokken.stokk()

øverste_kort = kortstokken.trekk()

print(f"Øverste kort har symbol {øverste_kort.symbol} og verdi {øverste_kort.verdi}")
