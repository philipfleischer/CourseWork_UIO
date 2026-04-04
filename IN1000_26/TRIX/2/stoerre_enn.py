tall1 = input("Skriv inn et tall: ")            # 11
tall2 = input("Skriv inn et annet tall: ")      # 7

if tall1 > tall2:
    print(tall1 + " er størst!")
else:
    print(tall2 + " er størst!")

# OUTPUT:
# 7 er størst!

"""
a)
Skriv henholdsvis 11 og 7. Er det som skrives ut overraskende?
- Det er kanskje overraskende at 7 sies å være det største tallet. På en annen
    side; siden Python sammenligner strenger leksikografisk ved bruk av
    logiske operatorer (i dette tilfellet >), er ikke svaret overraskende.

b) Utforsk hva større enn (>) betyr for ulike datatyper. Endre programmet under,
    slik at det oppfører seg korrekt i ethvert tilfelle.

- Operatoren ">" sammenligner tegn for tegn (posisjonvis fra start til slutt) ved
    sammenligning av strenger. For like lange strenger av tall, blir derfor resultatet
    av sammenligningen den samme som ved sammenligning av tall. For strenger av tall
    med ulik lengde, kan vi få feil resultat. For eksempel vil strengen "300" være
    større enn strengen "2000", fordi 3 er større enn 2.
    Merk at leksikografisk sammenligning med logiske operatorer også gjør forskjell
    på store og små bokstaver.
    For heltall og flyttall sammenlignes tallstørrelsene med logiske operatorer
    (i dette tilfellet ">"), uavhengig av lengdeforskjeller mellom tallene. Siden
    programmet skal kunne sammenligne alle tall med hverandre, bør vi konvertere
    input til tall før vi sammenligner.
"""
