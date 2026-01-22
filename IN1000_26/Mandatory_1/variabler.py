# Skriver ut en enkel hilsen
print("Hei student!")

# Ber brukeren skrive inn navn
navn = input("Skriv inn navnet ditt: ")
print(f"Hei, {navn}")

# Ber brukeren skrive inn et nytt navn
nytt_navn = input("Skriv inn nytt navn: ")

# Slår sammen navnene uten mellomrom
sammen = navn + nytt_navn
print(f"Hei, {sammen}")

# Slår sammen navnene med " og " mellom
sammen = navn + " og " + nytt_navn
print(f"Hei, {sammen}")
