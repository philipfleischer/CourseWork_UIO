#Under lager jeg en prosedyre som jeg kaller bilettpris1
def billettpris1():
    #Lager en variabel som heter alder, bruker int for å få alderen i en integer verdi istedenfor string
    alder = int(input("Skriv inn din alder: \n<"))
    #Satt bliettprisen foreløpig til 0
    billettpris = 0
    #lager en if-sjekk, hvis brukeren er 17 eller yngre blir det en barnebilett
    if alder <= 17:
        billettpris = 30
        print("En barnebillett på",billettpris,"kr")
    #Eller hvis brukeren er over 17, men yngre enn 63, blir det en vanlig bilett
    elif alder > 17 and alder < 63:
            billettpris = 50
            print("En billett på",billettpris,"kr")
    #Eller hvis brukeren er over 63, så blir det en pensjonistbillett
    else:
        billettpris = 35
        print("En pensjonistbillett på",billettpris,"kr")
#her kjører jeg prosedyren
billettpris1()
