import math

print()
print("--- Roller variabler kan ha i programmet ---")
print()
print("1) Holder styr på sant/usant Boolean")
if 3 < 2:
    tre_er_mindre_enn_to = True # boolsk variabel (bool)
else:
    tre_er_mindre_enn_to = False

print()
# print("Tre er mindre enn to:", tre_er_mindre_enn_to)
print(f"Tre er mindre enn to: {tre_er_mindre_enn_to}")

print()
print("2) Konstant verdi (som ikke endres når den er definert)")
print()
PI = math.pi # pi i store PI betyr ikke endre
print(f"Forholdet mellom diameter og omkrets av en sirkel er lik: {PI}")

print("3) Ukjent verdi som brukeren skriver inn")
print()

tekst = input("Skriv inn et heltall: ")
diameter = int(tekst)

print()

print("4) Resultat av en utregning som kan lagres til senere bruk")
print()
omkrets = PI*diameter
print(f"Hvis diameter av en sirkel er {diameter} så er omkretsen lik {omkrets}")
print()

print("5) En samling (liste, ordbok, ...) av mange verdier")
print()
terningsider = [1, 2, 3, 4, 5, 6]
print(terningsider)
print()

print("6) Løkkevariabel som går gjennom verdiene i en samling en etter en")
print()

for terningside in terningsider:
    print(f"En side av terningen er {terningside}")

print()
print("7) Parameter (hovedprogram --> funksjon)")
print()

def hallo(navn):    # navn er en parameter
    print(f"hallo, {navn}, godt å se deg!")

hallo("Kaptein Rosk")   # "Kaptein Rosk" er et argument

print()
print("8) Returverdi (hovedprogram <-- funksjon)")
print()

def lykketall():
    tall = int(input("Skriv inn lykketall: "))
    return tall

res = lykketall()
print(f"{res}? Ikke verst!")
print()

# Det finnes mange flere roller en variabel kan ha også-

"""
Hva Skal Vi Med FUNKSJONER?
- Hensikten er å gjøre programmer mer oversiktlige og lettere å skrive og lese for mennesker.
- Funksjoner er et verktøy til å redusre kompleksitet.
- Vi kan bruke funskjoner uten å tenke på hvordan de virker innvendig.
- print-funksjonen i Python er egentlig 100 linjer skrevet i C (et annet programmeringsspråk), men det har ikke vi trengt å tenke på - det viktigste for oss er å bruke den riktig.
- HVA funksjoner gjør og HVORDAN DEN BRUKES RIKTIG er viktgi når vi bruker en funksjon.
- HVORDAN funksjonen gør det den gjør er bare viktig når vi lager / endrer funksjonen.

Hva Skal Vi Med Objekter?
- Hensikten er å gjøre programmer mer oversiktlige og lettere å skrive og lese for menensker (akkurat som med funskjoner).
- Også objekter er et verktøy til å redusere kompleksitet.
- Vi kan bruke objekter uten å tenke på hvordan de virker innvendig.
- Litt som at vi kan bruke en bil uten at vi trenger å kunnne bygge eller reparere en bil.
- Hva objektet gjør og hvordan det brukes riktig er viktig når vi bruker et objekt.
- Hvordan objektet gjør det det gjør er bare viktig når vi lager / endrer oppskriften på hvordan denne typen objekt skal lages.
"""


""" ---------OUTPUT-------------

--- Roller variabler kan ha i programmet ---

1) Holder styr på sant/usant Boolean

Tre er mindre enn to: False

2) Konstant verdi (som ikke endres når den er definert)

Forholdet mellom diameter og omkrets av en sirkel er lik: 3.141592653589793
3) Ukjent verdi som brukeren skriver inn

Skriv inn et heltall: 2

4) Resultat av en utregning som kan lagres til senere bruk

Hvis diameter av en sirkel er 2 så er omkretsen lik 6.283185307179586

5) En samling (liste, ordbok, ...) av mange verdier

[1, 2, 3, 4, 5, 6]

6) Løkkevariabel som går gjennom verdiene i en samling en etter en

En side av terningen er 1
En side av terningen er 2
En side av terningen er 3
En side av terningen er 4
En side av terningen er 5
En side av terningen er 6

7) Parameter (hovedprogram --> funksjon)

hallo, Kaptein Rosk, godt å se deg!

8) Returverdi (hovedprogram <-- funksjon)

Skriv inn lykketall: 13
13? Ikke verst!

"""
