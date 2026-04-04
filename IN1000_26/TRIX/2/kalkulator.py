# 02.17
def kalkulator():
    t1 = int(input("Første tall: "))
    op = input("Operasjon: ")
    t2 = int(input("Andre tall: "))

    if op not in ["+", "-", "/", "*"]:
        return f"Error, {op} is not an accepted operation"

    if op == "+":
        return f"{t1} {op} {t2} = {t1 + t2}"
    elif op == "-":
        return f"{t1} {op} {t2} = {t1 - t2}"
    elif op == "*":
        return f"{t1} {op} {t2} = {t1 * t2}"
    else:
        return f"{t1} {op} {t2} = {t1 / t2}"


def main():
    print(kalkulator())


if __name__ == "__main__":
    main()
