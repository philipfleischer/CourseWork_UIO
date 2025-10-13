#Spør om fornavn og etternavn, legger dem inn som et parameter i funksjonen
full_navn = input("Skriv inn fornavn og etternavn\n< ").lower()
def lagBrukernavn(full_navn):
    #splitter for for- og etternavn
    full_navn = full_navn.split(" ")
    fornavn = full_navn[0]
    etternavn = full_navn[1]
    #Her finner jeg den første bokstaven i etternavnet som skal brukes i brukernavnet
    etternavnMer = etternavn[0:1]
    #Legger sammen for- og etternavn sin første bokstav
    brukernavn = fornavn + etternavnMer
    print(brukernavn)
    return brukernavn
lagBrukernavn(full_navn)

#Under ber jeg om to parametere som skal implementeres i funksjonen lagEpost()
brukernavn = input("Skriv inn et brukernavn (som over): ")
suffix = input("Skriv inn din suffix: ")
def lagEpost(brukernavn, suffix):
    #Setter sammen brukernavnet og suffix-en med en @
    epost = brukernavn + "@" + suffix
    print(epost)
lagEpost(brukernavn, suffix)

ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}
def skrivUtEposter(ordbok):
    teller = 0
    #bruker en while løkke for p iterere gjennom hele ordboken
    while teller < len(ordbok):
        #gjør om brukernavn og suffix til liste objekter og definerer dem
        brukernavn = list(ordbok.keys())
        suffix = list(ordbok.values())
        #kaller lagEpost for hver gang teller er mindre enn lengden til ordboken
        lagEpost(brukernavn[teller], suffix[teller])
        teller+=1

skrivUtEposter(ordbok)


def skrivUt():
    nyOrdbok = {}
    avgjoerelse = input("Skriv enten inn: i/p/s (s = stopp): ").lower()
    #While-løkken fortsetter så lenge brukeren ikke skriver inn s
    while avgjoerelse != "s":
        if avgjoerelse == "i":
            brukernavn = input("Skriv inn fornavn og etternavn: ")
            suffix = input("Skriv inn epost suffix: ")
            #Lager et nytt brukernavn med informasjonen bruker akkurat har gitt og kaller funksjonen
            nyttBrukernavn = lagBrukernavn(brukernavn)
            #legger inn den nye eposten i ordboken
            nyOrdbok[nyttBrukernavn] = suffix
            avgjoerelse = input("Skriv enten inn: i/p/s: ").lower()
        elif avgjoerelse == "p":
            #når avgjoerelse == "p", blir det som er skrevet inn rett før printet ut
            skrivUtEposter(nyOrdbok)
            #Man kan skrive i nå og hvis en etter den prosedyren skriver "p",
            #vil alle epostene som er skrevet i prosedyren bli printet
            avgjoerelse = input("Skriv enten inn: i/p/s: ").lower()

skrivUt()
