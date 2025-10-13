#Importerer klassen Motorsykkel fra filen motorsykkel.py
from motorsykkel import Motorsykkel
def main():
    #Her setter jeg inn verdier for instansvariabelene som ble laget i klassen
    kjoretoy = Motorsykkel(90, "Honda", "kj 20968")
    #Under blir det lagt til en verdi til prosedyren kjor, i tillegg til at verdiene over blir implementert
    print(kjoretoy.kjor(1))
    #Under blir verdiene fra variabelen kjoretoy brukt i
    print(kjoretoy.hentKilometerStand())
    kjoretoy.skrivUt()

    kjoretoy2 = Motorsykkel(80, "Triumph", "PT 30402")
    print(kjoretoy2.kjor(1))
    print(kjoretoy2.hentKilometerStand())
    kjoretoy2.skrivUt()

    kjoretoy3 = Motorsykkel(60, "Harley Davidson", "TA 12345")
    print(kjoretoy3.kjor(10))
    print(kjoretoy3.hentKilometerStand())
    kjoretoy3.skrivUt()


main()
