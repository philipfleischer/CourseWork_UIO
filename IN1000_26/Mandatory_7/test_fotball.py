from oblig7 import Sesong


def main():
    sesong = Sesong()
    sesong.les_lag_fra_fil("eliteserien_2026.txt")

    runde1 = sesong.runde(1)
    runde1.legg_til("HamKam", "Viking")
    runde1.legg_til("Molde", "Rosenborg")
    runde1.legg_til("Kristiansund", "Brann")
    runde1.legg_til("KFUM Oslo", "Start")
    runde1.legg_til("Sarpsborg 08", "Bodø/Glimt")
    runde1.legg_til("Vålerenga", "Sandefjord")
    runde1.legg_til("Aalesund", "Lillestrøm")
    runde1.legg_til("Tromsø", "Fredrikstad")

    runde2 = sesong.runde(2)
    runde2.legg_til("Start", "Aalesund")
    runde2.legg_til("Viking", "Molde")
    runde2.legg_til("Rosenborg", "Vålerenga")
    runde2.legg_til("Brann", "Tromsø")
    runde2.legg_til("Fredrikstad", "KFUM Oslo")
    runde2.legg_til("Lillestrøm", "Kristiansund")
    runde2.legg_til("Sandefjord", "Sarpsborg 08")
    runde2.legg_til("Bodø/Glimt", "HamKam")

    runde3 = sesong.runde(3)
    runde3.legg_til("Vålerenga", "Viking")
    runde3.legg_til("HamKam", "Brann")
    runde3.legg_til("Kristiansund", "Bodø/Glimt")
    runde3.legg_til("Molde", "Lillestrøm")
    runde3.legg_til("Sarpsborg 08", "Start")
    runde3.legg_til("Tromsø", "Rosenborg")
    runde3.legg_til("Aalesund", "Fredrikstad")
    runde3.legg_til("KFUM Oslo", "Sandefjord")

    runde4 = sesong.runde(4)
    runde4.legg_til("Lillestrøm", "Start")
    runde4.legg_til("Tromsø", "Kristiansund")
    runde4.legg_til("Viking", "Bodø/Glimt")
    runde4.legg_til("Rosenborg", "Sarpsborg 08")
    runde4.legg_til("Fredrikstad", "Vålerenga")
    runde4.legg_til("Molde", "HamKam")
    runde4.legg_til("Aalesund", "KFUM Oslo")
    runde4.legg_til("Brann", "Sandefjord")

    for rundenummer in range(1, 5):
        print(f"--- Runde {rundenummer} ---")
        for kamp in sesong.runde(rundenummer):
            kamp.simuler()
            print(kamp)
        print()


if __name__ == "__main__":
    main()
