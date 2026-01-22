full_navn = input("Skriv inn ditt fulle navn\n< ").lower()
def lagBrukernavn(full_navn):
    full_navn = full_navn.split(" ")
    fornavn = full_navn[0]
    etternavn = full_navn[1]
    etternavnMer = etternavn[0:1]
    brukernavn = fornavn + etternavnMer
    print(brukernavn)
    return brukernavn
lagBrukernavn(full_navn)


brukernavn = input("Skriv inn et brukernavn: ")
suffix = input("Skriv inn din suffix: ")
def lagEpost(brukernavn, suffix):
    epost = brukernavn + "@" + suffix
    print(epost)
lagEpost(brukernavn, suffix)

ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}
def skrivUtEposter(ordbok):
    teller = 0
    while teller < len(ordbok):
        brukernavn = list(ordbok.keys())
        suffix = list(ordbok.values())
        lagEpost(brukernavn[teller], suffix[teller])
        teller+=1

skrivUtEposter(ordbok)


def skrivUt():
    print("Hallo")
    nyOrdbok = {}
    avgjoerelse = input("Skriv enten inn: i/p/s: ").lower()
    while avgjoerelse != "s":
        if avgjoerelse == "i":
            brukernavn = input("Skriv inn navn: ")
            suffix = input("Skriv inn epost suffix: ")
            nyttBrukernavn = lagBrukernavn(brukernavn)
            nyOrdbok[nyttBrukernavn] = suffix
            avgjoerelse = input("Skriv enten inn: i/p/s: ").lower()
        elif avgjoerelse == "p":
            skrivUtEposter(nyOrdbok)
            avgjoerelse = input("Skriv enten inn: i/p/s: ").lower()

skrivUt()
