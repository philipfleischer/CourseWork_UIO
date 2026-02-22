def max_month(filnavn):
    ordbok = {}
    with open(filnavn, 'r') as fil:
        for line in fil:
            deler = line.strip().split(",")
            maaned = deler[0]
            temp = deler[1]
            ordbok[maaned] = temp

    return ordbok

def max_calc_month(filnavn, tidligere_rekorder):
    ordbok = {}
    with open(filnavn, 'r') as fil:
        for line in fil:
            deler = line.strip().split(",")
            maaned = deler[0]
            dag = deler[1]
            temp = deler[2]

            if temp > tidligere_rekorder[maaned]:
                tidligere_rekorder[maaned] = temp

    return tidligere_rekorder

def write_temps_records(records):
    new_file = "Updated_temp_records.csv"

    with open(new_file, 'w') as fil:
        for maaned, temp in records.items():
            fil.write(f"{maaned},{temp}\n")


def main():
    filnavn1 = "max_temperatures_per_month.csv"
    filnavn2 = "max_daily_temperature_2018.csv"

    ordbok1 = max_month(filnavn1)
    print("max_month:\n")
    print(ordbok1)

    ordbok2 = max_month(filnavn2)
    print("2018 updated max month:\n")
    print(ordbok2)

    write_temps_records(ordbok2)


if __name__ == "__main__":
    main()
