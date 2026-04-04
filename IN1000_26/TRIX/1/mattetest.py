# 01.15
def matterTestser():
    while True:
        s1 = int(input("Hva er svaret på 1+2 = "))
        if s1 != 3:
            print("Beklager, det var feil! Spillet er over")
            break
        s2 = int(input("Hva er svaret på 1/1 = "))
        if s2 != 1:
            print("Beklager, det var feil! Spillet er over")
            break
        s3 = int(input("Hva er svaret på 1*3 = "))
        if s3 != 3:
            print("Beklager, det var feil! Spillet er over")
            break
        print("Gratulerer, du vant!")
        break


def main():
    matterTestser()

if __name__ == "__main__":
    main()
