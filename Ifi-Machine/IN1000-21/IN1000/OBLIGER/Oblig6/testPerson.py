"""
Lag deretter et testprogram for klassen Person der du lar brukeren skrive inn navn og alder,
og oppretter et Person-objekt med informasjonen du får. Deretter skal brukeren ved hjelp av en
løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal
informasjon om brukeren skrives ut.
"""
#Importerer klassen Person fra filen person.py
from person import Person
#Deklarerer funksjonen main()
def main():
    navn = input("Skriv inn navnet ditt \n< ")
    alder = int(input("Skriv inn alderen din \n< "))

    #her oppretter jeg et objekt som henter argumenter fra input over og legger inn i konstruktøren
    person1 = Person(navn, alder)

    avgjoerelse = ""
    while avgjoerelse != "stopp":
        #Her utføres en handling som bruker opplysningene i person1 i prosedyren leggTilHobby()
        person1.leggTilHobby()
        avgjoerelse = input("Fortsette? (stopp=stopp) \n< ")

    person1.skrivUt()
    person1.skrivHobbyer()

main()
