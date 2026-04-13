#05.19
def dobbelt(tall):
    return tall*2

def streng_lenger_tall(streng, tall):
    return len(streng) > tall

def ant_sifre(tall):
    return len(str(tall))

def main():
    print(dobbelt(10))
    print(streng_lenger_tall("HALLA", 1))
    print(ant_sifre(1235))

if __name__ == "__main__":
    main()
