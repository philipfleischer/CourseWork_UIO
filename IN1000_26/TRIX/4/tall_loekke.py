# 04.11
def oppgave_b(tall):
    teller = 0
    total = 0
    while teller < len(tall):
        total += tall[teller]
        teller += 1
    print(f"Sum av tallene {total}")

def oppgave_c(tall):
    teller = 0
    print("Tall under 10:")
    while teller < len(tall):
        if tall[teller] < 10:
            print(tall[teller])
        teller += 1

def oppgave_d(tall):
    finnes_fem = False
    teller = 0
    while teller < len(tall):
        if tall[teller] == 5:
            finnes_fem = True
        teller += 1

    if finnes_fem:
        print("Fem finnes i listen.")
    else:
        print("Fem finnes ikke i listen.")

# Her er de samme men med "For-løkke med indekser"
def oppgave_b_for(tall):
    total = 0
    for i in range(len(tall)):
        total += tall[i]
    print("Sum av tallene i listen:", total)

def oppgave_c_for(tall):
    print("Tall under 10: ")
    for i in range(len(tall)):
        if tall[i] < 10:
            print(tall[i])

def oppgave_d_for(tall):
    fem_finnes = False
    for i in range(len(tall)):
        if tall[i] == 5:
            fem_finnes = True

    if fem_finnes:
        print("Fem finnes i listen.")
    else:
        print("Fem finnes ikke i listen.")

def main():
    tall = []
    teller = 0
    while teller < 5:
        inp_str = input("Oppgi et tall: ")
        inp_tall = int(inp_str)
        tall.append(inp_tall)
        teller += 1

    oppgave_b(tall)
    oppgave_c(tall)
    oppgave_d(tall)

if __name__ == "__main__":
    main()
