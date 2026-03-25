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

    for kamp in runde1:
        kamp.simuler()
        print(kamp)


if __name__ == "__main__":
    main()
