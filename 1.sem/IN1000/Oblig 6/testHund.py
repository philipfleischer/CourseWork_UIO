#Importerer klassen Huns fra filen hund.py
from hund import Hund
def main():
    #Setter inn verdier for instansvariabelene i klassen
    hund1 = Hund(10, 20, 1)
    #bruker hund1 verdiene i prosedyrene i klassen
    print(hund1.spring())
    print(hund1.spis(50))
    print(hund1.get_vekt())

    print(hund1.spring())
    print(hund1.spis(100))
    print(hund1.get_vekt())
#Kaller på funksjonen main()
main()
