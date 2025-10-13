#Åpner to csv filer med informasjon om temperatur per måned og/eller dag
fil_1750 = open("max_temperatures_per_month.csv", "r")
fil_2018 = open("max_daily_temperature_2018.csv", "r")

#Henter inn den ene filen som parameter i funksjonen
def funk1(fil_1750):
    ordbok = {}
    #bruker en for løkke til å iterere gjennom linjene i filen
    for linjer in fil_1750:
        #fjerner alle mellomrom foran og bak
        linjer = linjer.strip()
        #splitter linjene der det er et ","
        kolonner = linjer.split(",")
        maaned = kolonner[0]
        temp = float(kolonner[1])
        #setter informasjonen inn i ordboken, der maaned er keys og temp er values
        ordbok[maaned] = temp

    print(ordbok)
    return ordbok
#her henter jeg inn begge filene som parameter i funksjonen
def funk2(fil_2018, fil_1750):
    #gir ordboken som blir returnert i funk1 variabelnavnet ordbok
    ordbok = funk1(fil_1750)
    #Setter høyeste temp til None siden en ikke burde anta her
    hoyeste_temp = None
    #Setter også den nåværende måneden til None, siden det ikke alltid er sikkert at Januar er først
    naa_maaned = None
    hoyeste_temp_dag = None
    for linjer in fil_2018:
        linjer = linjer.strip()
        kolonner = linjer.split(",")
        maaned = kolonner[0]
        dag = kolonner[1]
        temp = float(kolonner[2])
        #Hvis den hoyeste temperaturen == None, så er den første temp
        #verdien som blir iterert satt til høyste temp, og den dagen blir til høyeste temp dag
        if hoyeste_temp == None:
            hoyeste_temp = temp
            hoyeste_temp_dag = dag
        #Hvis temp er høyere enn den tidligere høyeste tempen så endres de, samme med dagen
        if temp > hoyeste_temp:
            hoyeste_temp = temp
            hoyeste_temp_dag = dag
        #Samme konseptet som over
        if naa_maaned == None:
            naa_maaned = maaned
        #Hvis maaned ikke er lik den nåværende måneden, så skal vi gå over til neste måned og
        #sjekke for temperaturene i den måneden
        if maaned != naa_maaned:
            temp_1750 = ordbok[naa_maaned]
            #Hvis tempen i 2018 er større enn noen gang tidligere målt blir det printet ut ny rekord
            # med dagen, tempen og måneden
            if hoyeste_temp > temp_1750:
                print("Ny rekord", naa_maaned, hoyeste_temp_dag, "på hele", hoyeste_temp, "grader celsius")
                #Ordboken blir oppdatert med den nye temp-rekorden
                ordbok[naa_maaned] = hoyeste_temp

            naa_maaned = maaned
            hoyeste_temp = None
            hoyeste_temp_dag = None

    print(ordbok)

funk2(fil_2018, fil_1750)
