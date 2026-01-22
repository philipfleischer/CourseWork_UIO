#Under vises hvordan dag og måned i datoen skal skrives
dato = input("Skriv inn en dato (24 10): ")
#Under brukes kommandoen split(), for å få de to heltallene til å bli to objekter i listen dagMaaned
dagMaaned = dato.split()
print(dagMaaned)

dato2 = input("Skriv inn en til dato: ")
dagMaaned2 = dato2.split()
print(dagMaaned2)
#Under bruker jeg dagMaaned[0] for å finne dagen i den første datoen og dagMaaned[1] for å finne måneden, samme for den andre datoen
if  dagMaaned[0] <= dagMaaned2[0] and dagMaaned[1] < dagMaaned2[1]:
    print("Riktig rekkefølge!")
elif dagMaaned[0] < dagMaaned2[0] and dagMaaned[1] == dagMaaned2[1]:
    print("Riktig rekkefølge")
elif dagMaaned[0] >= dagMaaned2[0] and dagMaaned[1] < dagMaaned2[1]:
    print("Riktig rekkefølge")
elif dagMaaned[0] == dagMaaned2[0] and dagMaaned[1] == dagMaaned2[1]:
    print("Samme dato!")
else:
    print("Feil rekkefølge")
