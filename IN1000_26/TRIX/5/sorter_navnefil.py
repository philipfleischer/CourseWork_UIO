#05.10
def sorter_hund_person(fil):
    personer = []
    hunder = []
    with open(fil, "r") as f:
        for line in f:
            deler = line.strip().split()
            if deler[0] == "P":
                personer.append(deler[1])
            else:
                hunder.append(deler[1])
    print(personer)
    print(hunder)

def main():
    sorter_hund_person("navn2.txt")

if __name__ == "__main__":
    main()
