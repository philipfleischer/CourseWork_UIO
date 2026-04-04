#02.16
def beregn_skatt(inntekt):
    if inntekt < 10000:
        return inntekt * 0.1
    else:
        return 10000 * 0.1 + (inntekt - 10000) * 0.3

def main():
    inntekt = float(input("Tast inn din inntekt:\n> "))
    skatt = beregn_skatt(inntekt)
    print(f"Skatt: {skatt}")

if __name__ == "__main__":
    main()
