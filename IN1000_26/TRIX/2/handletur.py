#02.18
def handler():
    print("Hei! Velkommen til IFI-butikken.")
    broad = int(input("Hvor mange brød vil du ha?\n> "))
    melk = int(input("Hvor mange melk vil du ha?\n> "))
    ost = int(input("Hvor mange ost vil du ha?\n> "))
    yoghurt = int(input("Hvor mange yoghurt vil du ha?\n> "))

    pb = 20
    pm = 15
    po = 40
    py = 12

    print(f"Du skal betale: {pb*broad + pm*melk + po*ost + py*yoghurt} kr.")

def main():
    handler()

if __name__ == "__main__":
    main()
