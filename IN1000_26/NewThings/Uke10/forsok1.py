from kommuner_fylker import kommuner, fylker

# Forsøk 1: Uten hjemmelagde objekter

kommuner_i_fylke = {}

for komnr in kommuner:
    kommunenavn = kommuner[komnr]
    fylkesnr = komnr[0:2]
    fylkesnavn = fylker[fylkesnr]

    if fylkesnavn not in kommuner_i_fylke:
        kommuner_i_fylke[fylkesnavn] = []

    kommuner_i_fylke[fylkesnavn].append(kommunenavn)

for fylkesnavn in kommuner_i_fylke:
    print(f"    {fylkesnavn}")
    for kommunenavn in kommuner_i_fylke[fylkesnavn]:
        print(f"\t{kommunenavn}")
    print()
