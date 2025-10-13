def minFunksjon():
    for x in range(2):
        c=2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b=0
    print(b)
    b=a
    a = minFunksjon()
    print (b)
    print (a)
hovedprogram()

"""
Først defineres funksjonen minFunksjon, som ikke tar imot noen parametere. Så defineres funksjonen
hovedprogram, som heller ikke har noen parametere. Deretter kalles hovedprogram.
I hovedprogram starter det med at a blir gitt verdien 42, b blir gitt verdien 0, så blir b printet.
Etter dette blir b gitt verdien til a, som altså er 42. Deretter blir a satt lik funksjonen
minFunksjon. Her starter det med en for-løkke som skal gjelde for x i rekkevidden 0-2.
Her blir c gitt verdien 2 og etter det blir c printet ut. Deretter blir verdien til c økt med 1,
altså får c verdien 3. Følgende blir b gitt verdien 10. Etter dette blir b gitt verdien til a,
men a er ikke definert i minFunksjon og dermed krasjer programmet.

Det blir altså skrevet ut 0 og 2. 0 er verdien til b i hovedprogram() og 2 er verdien til c
i minFunksjon. Til slutt blir det skrevet ut en feilmelding om at variabel a ikke er definert.

"""
