# Deloppgave 4G:
from oppgave_4b import Studieprogram
from oppgave_4e import Emne
from oppgave_4f import Institutt


def main():
    in1000 = Emne(
        "IN1000", "Introduksjon til objektorientert programmering", True, True
    )
    in1010 = Emne("IN1010", "Objektorientert programmering", False, True)
    in1150 = Emne("IN1150", "Logiske metoder", False, True)
    in1050 = Emne("IN1050", "Introduksjon til design", True, False)

    prosa = Studieprogram("Programmering og systemarkitektur")
    dbi = Studieprogram("Design, bruk, interaksjon")

    prosa.legg_til(in1000)
    prosa.legg_til(in1010)
    prosa.legg_til(in1150)

    dbi.legg_til(in1000)
    dbi.legg_til(in1010)
    dbi.legg_til(in1050)

    inst = Institutt("Institutt for informatikk")
    inst.legg_til(prosa)
    inst.legg_til(dbi)

    print(f"{inst.navn} har {len(inst)} studieprogrammer")

    for program in inst:
        print(program.navn)
        for emne in program:
            print(emne)


if __name__ == "__main__":
    main()
