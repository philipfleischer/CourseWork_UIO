# 02.19
import math

def sirk_ber():
    r = float(input("Radius: "))
    return (2*r) ,(math.pi*(r**2)), (2*math.pi*r)

def main():
    diameter, areal, omkrets = sirk_ber()

    print(
        f"Diameter: {diameter:.2f}\nAreal: {areal:.2f}\nOmkrets: {omkrets:.2f}\n")

if __name__ == "__main__":
    main()
