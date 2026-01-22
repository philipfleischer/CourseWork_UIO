telefonbok = { "Arne": 22334455, "Lisa": 95959595, "Jonas": 97959795, "Peder": 12345678 }

navn = input("Skriv inn et navn: ")
if navn in telefonbok:
    nummer = telefonbok[navn]
    print("Telefonnummeret til", navn, "er", nummer)
else:
    nummer = input("Hva er telefonnummeret til " + navn + "?")
    nummer = int(nummer)
    telefonbok[navn] = nummer
