# ======================================================
# Oppgave 5: Egen oppgave – Beslutninger (if / elif / else)
#
# Oppgavetekst:
# Lag et enkelt quiz-program som stiller brukeren tre spørsmål.
# Hvert spørsmål har ett korrekt svar.
#
# Programmet skal:
# 1. Spørre brukeren om svar på tre spørsmål
# 2. Sjekke om hvert svar er korrekt ved hjelp av if / elif / else
# 3. Gi tilbakemelding på hvert svar (riktig / feil)
# 4. Til slutt skrive ut hvor mange riktige svar brukeren fikk
#
# Krav:
# - Bruk if / elif / else
# - Bruk input() for å hente svar fra brukeren
# - Programmet skal fungere selv om brukeren skriver store eller små bokstaver
#
# ======================================================


def quiz():
    poeng = 0

    spm1 = input("Hvor gammel er en født i år 2000?: ")
    if int(spm1) == 26:
        poeng += 1

    spm2 = input("Er jorden flat?: ")
    if spm2.strip().lower() == "nei":
        poeng += 1
    elif spm2.strip().lower() == "":
        print("Bedre svar enn ja!")
    else:
        poeng -= 1
        print("Nei, nei nei! Minus poeng her")

    spm3 = input("Hva heter hovedstaden i Norge?: ")
    if spm3.strip().lower() == "oslo":
        poeng += 1

    print(f"Total poengsum: {poeng}\n")


def main():
    quiz()


if __name__ == "__main__":
    main()
