"""I denne oppgaven skal du lage et program som lar deg holde styr på,
legge til og skrive ut venners bursdager"""

"""kan splitte der det er "." for så å finne ut hvilken key i dictet jeg skal legge
det i. Kanskje sortere for måned også. Jeg ble ikke ferdig med denne oppgaven,
prøvde å gjøre den så raskt som mulig. Vet at man kunne gjort mye av det under
med langt mindre kode.
"""

print("Hei og velkommen til en bursdagsliste-oppsett! \n")

tomBursdagsDict = {}

teller = 0
bursdagsBarn = input("Skriv inn bursdagsbarnet: \n< ")
bursdagsDato = input("Skriv inn en bursdagsdato: \n< ")
while teller < bursdagsDato:
    teller+=1
    bursdagsDato = int(input("Skriv inn en bursdagsdato (01.01.2000): \n< "))
    BD_split = bursdagsDato.split(".")
    if bursdagsdato[teller] == "01":
        tomBursdagsDict["Januar"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "02":
        tomBursdagsDict["Februar"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "03":
        tomBursdagsDict["Mars"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "04":
        tomBursdagsDict["April"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "05":
        tomBursdagsDict["Mai"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "06":
        tomBursdagsDict["Juni"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "07":
        tomBursdagsDict["Juli"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "08":
        tomBursdagsDict["August"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "09":
        tomBursdagsDict["September"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "10":
        tomBursdagsDict["Oktober"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "11":
        tomBursdagsDict["November"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    elif bursdagsdato[teller] == "12":
        tomBursdagsDict["Desember"].append(bursdagsDato)
        print("yooo", tomBursdagsDict)
    else:
        break




""""Januar" : , "Februar" : , "Mars" : , "April" : , "Mai" : ,
"Juni" : , "Juli" : , "August" : , "September" : , "November" : , "Desember" : """
