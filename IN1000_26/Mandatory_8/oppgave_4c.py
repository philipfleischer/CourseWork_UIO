# Deloppgave 4C:
from oppgave_4a import Emne
from oppgave_4b import Studieprogram

def main():
    in1000 = Emne(
        "IN1000", "Introduksjon til objektorientert programmering", True, True
    )
    in1010 = Emne("IN1010", "Objektorientert programmering", False, True)
    in1150 = Emne("IN1150", "Logiske metoder", False, True)
    in1050 = Emne("IN1050", "Introduksjon til design", True, False)

    prosa = Studieprogram("Programmering og systemarkitektur")
    desa = Studieprogram("Design, bruk, interaksjon")

    prosa.legg_til(in1000)
    prosa.legg_til(in1010)
    prosa.legg_til(in1150)
    desa.legg_til(in1000)
    desa.legg_til(in1010)
    desa.legg_til(in1050)

    print(f"{prosa.navn} ({len(prosa)} emner)")
    for emne in prosa:
        print(emne)

    print()
    print(f"{desa.navn} ({len(desa)} emner)")
    for emne in desa:
        print(emne)


if __name__ == "__main__":
    main()
