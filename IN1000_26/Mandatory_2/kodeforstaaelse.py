"""
Svar til spm 1 og 2:
- Programmet vil kjøre dersom bruker skriver inn et heltall.
- Hvis brukeren ikke gjør det, så får vi en ValueError.
- Hvis heltallet er mindre enn 10 så blir print skrevet og programemt blir avsluttet.
- Hvis heltallet er større enn 10 så avsluttes programmet.
- En feil vi får uansett er konkateneringen av print linjen, siden vi ikke kan printe int + str.

"""

a = input("Tast inn et heltall!")
b = int(a)
if b < 10:
    print(b + "Hei!")
