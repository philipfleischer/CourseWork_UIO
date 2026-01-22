"""
Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter og initialiserer
instansvariabler med disse. I tillegg skal konstruktøren opprette en instansvariabel hobbyer som en
tom liste . Skriv en metode leggTilHobby som tar imot en tekststreng og legger den til i
hobbyer-listen.
Skriv også en metode skrivHobbyer.
Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter
Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på metoden
skrivHobbyer.
"""
class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    def leggTilHobby(self):
        hobby = input("Skriv inn en hobby \n<")
        self._hobbyer.append(hobby)
        #print(self._hobbyer)
        return self._hobbyer

    def skrivHobbyer(self):
        #hobbyer = leggTilHobby([hobbyer])
        for hobby in self._hobbyer:
            print(hobby)

    def skrivUt(self):
        print(f"Hei {self._navn}, du er {self._alder} år gammel. Under er hobbyene dine:")
