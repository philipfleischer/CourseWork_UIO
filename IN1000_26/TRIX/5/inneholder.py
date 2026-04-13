# 05.20
def inneholder(s1, s2):
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False
    return True


def inneholder2(s1, s2):
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False
    return True


def main():
    # Del a
    print(inneholder("hei", "hello"))
    print(inneholder("hi", "hei"))
    print(inneholder("hei", "hi"))
    print(inneholder("heihei", "hei"))

    # Del b
    print(inneholder2("hei", "hello"))
    print(inneholder2("hi", "hei"))
    print(inneholder2("hei", "hi"))
    print(inneholder2("heihei", "hei"))

if __name__ == "__main__":
    main()
