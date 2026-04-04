# 02.03
def typerdata():
    streng, heltall, flyttall = hent_tre()
    skriv_ut_dataen(streng, heltall, flyttall)

def hent_tre():
    streng = input("Skriv inn streng: ")
    heltall = int(input("Skriv inn heltall: "))
    flyttall = float(input("Skriv inn flyttall: "))
    return streng, heltall, flyttall

def skriv_ut_dataen(streng: str, heltall: int, flyttall: float):
    print(f"Strengen: {streng} har type: {type(streng)}")
    if (type(streng) is not str):
        print("ERROR! Streng must be String")
    print(f"Heltallet: {heltall} har type: {type(heltall)}")
    if type(heltall) is not int:
        print("ERROR! Heltall must be Integer")
    print(f"Flyttallet: {flyttall} har type: {type(flyttall)}")
    if type(flyttall) is not float:
        print("ERROR! Flyttall must be Float")

def main():
    typerdata()
    skriv_ut_dataen("", 0, 3.8)
    skriv_ut_dataen(1, 2, 3)
    skriv_ut_dataen(1, -0, 3.8)
    skriv_ut_dataen(3.8, 3.8, 3.8)

if __name__ == "__main__":
    main()
