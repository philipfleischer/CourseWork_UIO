fil_1750 = open("max_temperatures_per_month.csv", "r")
fil_2018 = open("max_daily_temperature_2018.csv", "r")

def funk1(fil_1750):
    ordbok = {}
    for linjer in fil_1750:
        linjer = linjer.strip()
        kolonner = linjer.split(",")
        maaned = kolonner[0]
        temp = float(kolonner[1])
        ordbok[maaned] = temp

    print(ordbok)
    return ordbok

def funk2(fil_2018, fil_1750):
    ordbok = funk1(fil_1750)

    hoyeste_temp = None
    naa_maaned = None
    hoyeste_temp_dag = None
    for linjer in fil_2018:
        linjer = linjer.strip()
        kolonner = linjer.split(",")
        maaned = kolonner[0]
        dag = kolonner[1]
        temp = float(kolonner[2])

        if hoyeste_temp == None:
            hoyeste_temp = temp
            hoyeste_temp_dag = dag

        if temp > hoyeste_temp:
            hoyeste_temp = temp
            hoyeste_temp_dag = dag

        if naa_maaned == None:
            naa_maaned = maaned

        if maaned != naa_maaned:
            temp_1750 = ordbok[naa_maaned]
            if hoyeste_temp > temp_1750:
                print("Ny rekord", naa_maaned, hoyeste_temp_dag, "på hele", hoyeste_temp, "grader celsius")
                ordbok[naa_maaned] = hoyeste_temp

            naa_maaned = maaned
            hoyeste_temp = None
            hoyeste_temp_dag = None

    print(ordbok)

funk2(fil_2018, fil_1750)
