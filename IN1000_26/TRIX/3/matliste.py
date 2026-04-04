#03.12
def favMat():
    favorittmat = ["Tunfisk", "Kål", "Kjøttboller"]
    print(favorittmat)

    favorittmat.remove("Kål")
    favorittmat.append("Kål")
    favorittmat.pop(1)
    print(favorittmat)
    print(len(favorittmat))

    for mat in favorittmat:
        print(mat.upper())

def main():
    favMat()

if __name__ == "__main__":
    main()
