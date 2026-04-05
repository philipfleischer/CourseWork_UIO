#05.01
def lesern():
    navneliste = []
    with open("navn.txt", "r") as file:
        for navn in file:
            navneliste.append(navn.strip())
        print(navneliste)

    file.close()



def main():
    lesern()


if __name__ == "__main__":
    main()
