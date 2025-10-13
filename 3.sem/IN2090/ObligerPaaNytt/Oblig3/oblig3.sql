--Oppgave 1: Funksjonelle avhengigheter
MAnsatte(navn, født, personnr, lønn, stilling,
          fareT, hemmeligT, skummeltT, alder)

--Oppgave 1a
født -> alder

--Oppgave 1b
født, personnr -> navn, lønn, stilling, fareT, hemmeligT, skummeltT, alder

--Oppgave 1c
stilling, fareT, hemmeligT, skummeltT -> lønn

--Oppgave 1d
stilling, fareT -> skummeltT

--Oppgave 2: Tillukninger og nøkler
Utstyr(navn, kategori, pris, farlighetsgrad, gradering,
       leverandør, adresseLeverandør, beholdning)

1. navn, kategori → farlighetsgrad, gradering
2. navn, kategori, leverandør → pris, beholdning
3. adresseLeverandør → leverandør
4. farlighetsgrad, gradering, leverandør → kategori

Forenklet:
Utstyr(N, K, P, F, G, L, A, B)
1. NK→FG
2. NKL→PB
3. A → L
4. FGL→K

--Oppgave 2a
A^+ = A,L

--Oppgave 2b
NKA^+ = N,K,A,F,G,L,K,P,B

--Oppgave 2c
Regel 1: Hvis A ikke forekommer i noen høyreside, er A med i ALLE kandidatnøkler
Regel 2: Hvis A forekommer i minst en høyreside, men ingen venstresider, er A IKKE del av noen kandidatnøkler
Finn alle attributter som kun forekommer på høyre side
Hvis alle attributter er med sjekk minimalitet. Hvis ikke, utvid i tur og
orden med ett og ett nytt attributt

Attributter som kun forekommer på venstre side:
A,N
Attributter som kun forekommer på høyre side:
P,B

Kandidatnøkler:
NKA, NAFG,

--Oppgave 3: Normalformer
AgenterPåOppdrag(agentId, navn, initialer, født,
                 oppdragsNavn, varighet, lokasjon)

FD-er:
   1. agentId → navn, født
   2. navn, født → agentId
   3. navn → initaler
   4. oppdragNavn → varighet, lokasjon

Kandidatnøkler:
  • {agentId, oppdragsNavn}
  • {navn, født, oppdragsNavn}


--Oppgave 3a
Vi har flere normalformer som 1NF, 2NF, 3NF, BCNF, osv. En normalform gir oss et uttrykk
for dekomposisjonen som er gjort. En høy normalform gir oss færre oppdateringsanomalier.
Det gjør at vi minimerer duplisering av informasjonen vi har og trenger. I tillegg hjelper
det oss med å få anomalier når vi sletter visse ting. I en database med lav normalform kan
sletting av f.eks et navn gjøre at annen informasjon relatert til navnet blir slettet,
samtidig kan det gi oss uønskede “null”-verdier. Høyere normalform gir ofte flere tabeller
i databasen, dette kan føre til redusert hastighet. Grunnen til dette er at vi trenger flere
“joins” for å få tabellene til å relatere til hverandre. Årsaken til at vi ønsker å bruke høyere
normalformer er for å redusere avhengighet av informasjon samt redundansen.

--Oppgave 3b
FD 1: agentId er ikke en supernøkkel, altså er det brudd på BCNF. Går til steg nummer 2.
FD 1: navn og født er nøkkelattributter, går til neste FD.
FD 2: navn, født er ikke en supernøkkel, altså er det brudd på BCNF. Går til steg nummer 2.
FD 2: agentId er nøkkelattributter, går til neste FD.
FD 3: navn er ikke en supernøkkel, altså er det brudd på BCNF. Går til steg nummer 2.
FD 3: initialer er ikke et nøkkelattributt, går til steg nummer 3.
FD 3: navn er en del av en kandidatnøkkel, dermed er det brudd på 2NF.
Relasjonen AgenterPåOppdrag er på 1NF.

--Oppgave 4: Tapsfri dekomponering
R(A, B, C, D, E, F) FDer:
1. A—>BC
2. BC—>A
3. D—>E
4. AD—>F
5. E—>F
6. Beregner nøklene til R: {A, D} og {B, C, D}
7. A —> BC, ved å bruke algoritmen for å finne normalformen får vi at det er brudd på
    BCNF, men ikke på 3NF siden BC er et nøkkelatributt.
8. Finner tillukningen til venstresiden:
    A+ =A,B,C
    S1(A, B, C). S1 har FDene 1. og 2.
    S2(A, D, E, F). S2 har FDene 3., 4. og 5.
9. Fortsetter med S2(A, D, E, F) FDer:
    D —> E
    AD —> F
    E —> F
    Kandidatnøklen er: {A, D}. D —> E, brudd på BCNF
    E er ikke et nøkkelattributit, og bryter med 3NF D er del av en kandidatnøkkel.
    D+ = D,E,F
    S21(D, E, F) og S22(A, D)
    S21 har FDene 3 og 5 og kandidatnøkkelen D, og 5 bryter derfor med BCNF.
    S22 har ingen FDer, kandidatnøkkelen AD og er på BCNF.
    Dekomponerer S21 videre:
    S211(E, F) og S212(D, E)
10. Dermed kan R(A, B, C, D, E, F) dekomponeres til S1(A, B, C), S22(D, A, F), S211(E, F) og S212(D, E).


R(A, B, C, D, E, F) FDer:
1. A—>BC
2. BC—>A
3. D—>E
4. AD—>F
5. E—>F

1. Beregner nøklene til R: {A, D} og {B, C, D}.
2. A -> BC: A er ikke en supernøkkel og bryter med BCNF, går til neste steg:
    A -> BC: BC er en kandidatnøkkel og er dermed på formen 3NF.
3. A -> BC, bryter med BCNF:
  3.1 A -> BC
  3.2 A^+ = A, B, C
  3.3 Dekomponerer til S1(A, B, C) og '(tar også med A i S2)' S2(A, D, E, F).
      S1 har FDene 1.
      S2 har FDene 3, 4 og 5.
  3.4 Fortsetter rekursivt med S1:
2. S1(A, B, C): I dette tilfellet er det kun FD 1 som gjelder og siden A er kandidatnøkkelen
                bryter den dermed ikke med BCNF.
  3.4 Fortsetter rekursivt med S2:
2. S2(A, D, E, F): I dette tilfellet er det FD 3, 4 og 5.
    Kandidatnøkler: {A, D}
    D -> E: D er ikke en supernøkkel og bryter dermed med BCNF.
    D^+ = D, E, F
    S21(D, E, F) og S22(A, D)
    S22(A, D): Har kun har ingen FDer og bryter ikke med BCNF
    S21(D, E, F): Har FD 3 og FD 5 Går videre til neste steg.
  3.4 Fortsetter rekursivt med S21(D, E, F):
2. S21(D, E, F): I dette tilfellet er det FD 3 og 5.
    E^+ = F
    S211(E, F) og S212(E, D)
Dermed kan R(A, B, C, D, E, F) dekomponeres tapsfritt til S1(A, B, C), S211(E, F) og S212(E, D).





Eksempel:
R(A,B,C)
1. AB -> C
2. C -> A

1. Nøkler til R: {A, B} og {B, C}
2. AB -> C: AB er en supernøkkel, går til neste FD.
    C -> A: C er ikke en supernøkkel og bryter med BCNF, går til neste steg:
    C -> A: A er et nøkkelattributt. Det er altså på formen 3NF.
3. R bryter med BCNF, går til neste steg:
  3.1 C -> A
  3.2 C^+ = C, A
  3.3 S1(C, A) og S2(C, B). Går rekursivt tilbake for S1 og S2:
2. S1(C -> A): C er i dette tilfellet kandidatnøkkelen og bryter dermed ikke med BCNF.
    S2(C -> B): Har ingen FDer og bryter dermed ikke med BCNF.
R(A, B, C) kan dekomponeres tapsfritt til S1(C, A) og S2(C, B)
