# 02.20
def busstur():
    ant_plasser = 30

    stopp1 = int(input("Stasjon 1! Hvor mange venter på bussen?\n> "))
    ant_plasser = beregn_plasser(ant_plasser, stopp1)

    stopp2 = int(input("Stasjon 2! Hvor mange venter på bussen?\n> "))
    ant_plasser = beregn_plasser(ant_plasser, stopp2)

    stopp3 = int(input("Stasjon 3! Hvor mange venter på bussen?\n> "))
    ant_plasser = beregn_plasser(ant_plasser, stopp3)

    print(f"Bussen er fremme med {30-ant_plasser} personer ombord!")

def beregn_plasser(ant_plasser, stopp):
    if ant_plasser - stopp > 0:
        ant_plasser -= stopp
        print(f"{stopp} personer går ombord i bussen.")
    else:
        gaa = abs(ant_plasser - stopp)
        print(f"Bussen er full. {gaa} må gå til fots")
        ant_plasser = 0
    return ant_plasser

def main():
    busstur()

if __name__ == "__main__":
    main()
