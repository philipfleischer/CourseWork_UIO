# 02.21
def siste_siffer():
    a, b, c = 123, 421, 44141

    a_liste = list(map(int, str(a)))
    siste_a = a_liste[-1]

    b_liste = list(map(int, str(b)))
    siste_b = b_liste[-1]

    c_liste = list(map(int, str(c)))
    siste_c = c_liste[-1]

    if siste_a == siste_b:
        print(f"a: {a}, siste verd: {siste_a} ---- b: {b}, siste verd: {siste_b}")

    if siste_a == siste_c:
        print(f"a: {a}, siste verd: {siste_a} ---- c: {c}, siste verd: {siste_c}")

    if siste_b == siste_c:
        print(f"b: {b}, siste verd: {siste_b} ---- c: {c}, siste verd: {siste_c}")

    # FASIT:
    if a % 10 == b % 10:
        print(f"a: {a}, siste verd: {a % 10} ---- b: {b}, siste verd: {b % 10}")

    if a % 10 == c % 10:
        print(f"a: {a}, siste verd: {a % 10} ---- c: {c}, siste verd: {c % 10}")

    if c % 10 == b % 10:
        print(f"c: {c}, siste verd: {c % 10} ---- b: {b}, siste verd: {b % 10}")


def main():
    siste_siffer()

if __name__ == "__main__":
    main()
