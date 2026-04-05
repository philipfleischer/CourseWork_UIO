#05.05
def les_song_contest(filnavn):
    aarene = []
    landene = []
    song_contest = {}
    with open(filnavn, "r") as f:
        for line in f:
            deler = line.strip().split()
            aar = deler[0]
            land = deler[1]
            aarene.append(aar)
            landene.append(land)
            song_contest[aar] = land

    return song_contest

def skriv_ting(bok):
    for aar, land in bok.items():
        print(f"År: {aar} --- Land: {land}")


def main():
    bok = les_song_contest("song_contest.txt")
    skriv_ting(bok)


if __name__ == "__main__":
    main()
