#05.14
def omvendt_fil(inn, ut):
    innfil = open(inn, "r")
    utfil = open(ut, "w")

    linjer = []
    for line in innfil:
        linjer.append(line)

    j = 0
    for _ in range(len(linjer)):
        j -= 1
        utfil.write(linjer[j])

    innfil.close()
    utfil.close()

#FASIT
def omvent_fil_fasit(input_filnavn, output_filnavn):
    linjene = []
    input_fil = open(input_filnavn, "r")
    for linje in input_fil:
        linjene.append(linje)

    input_fil.close()

    omvendte_linjene = linjene[::-1]

    output_fil = open(output_filnavn, "w")
    for linje in omvendte_linjene:
        output_fil.write(linje)

    output_fil.close()

def main():
    omvendt_fil("omvendt.txt", "om_omvendt.txt")

if __name__ == "__main__":
    main()
