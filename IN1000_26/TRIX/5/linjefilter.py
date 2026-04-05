#05.08
def fil_na_filter(inn_fil, ut_fil):
    with open(inn_fil, "r") as innfil:
        with open(ut_fil, "w") as utfil:
            for line in innfil:
                if "NA" not in line:
                    utfil.write(line)

#FASIT:
def fil_na_filter_fasit(inn_fil, ut_fil):
    inputfil = open(inn_fil, "r")
    outputfil = open(ut_fil, "w")

    for linje in inn_fil:
        if "NA" not in linje:
            outputfil.write(linje)

    inputfil.close()
    outputfil.close()


def main():
    fil_na_filter("na_fil.csv", "no_na_fil.txt")

if __name__ == "__main__":
    main()
