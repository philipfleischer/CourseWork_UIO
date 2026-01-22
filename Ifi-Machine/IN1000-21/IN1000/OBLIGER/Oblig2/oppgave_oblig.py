#Først definerer vi print_prosa() #1
def print_prosa():
    print("Melding til alle gaardeiere:")
    print("Antall dyr paa gaarden: ")
#Her definerer vi antall_dyr #2
antall_dyr = 4
#Her kjører vi funksjonen #3
print_prosa()
#Her printer vi antall_dyr = 4 #4
print(antall_dyr)
#Her blir antall nye dyr spurt om, gjort om til int og lagret i variabelen antall_nye_dyr #5
antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden: "))
#her blir alle dyr på gården lagt sammen i variabelen antall_dyr#6
antall_dyr = antall_dyr + antall_nye_dyr
#Her kjører vi funksjonen på nytt #7
print_prosa()
#her printes hvor antall_dyr #8
print(antall_dyr)
#Her går vi gjennom den første if-sjekken #9
if antall_dyr > 12:
    print("Det er mer enn ett dusin dyr paa gaarden!")
#Her går vi gjennom den andre if-sjekken # 10
elif antall_dyr == 12:
#Printer ut svaret siden antall_dyr == 12 #11
    print("Det er ett dusin dyr paa gaarden!")
else:
    print("Det er mindre enn ett dusin dyr paa gaarden!")
