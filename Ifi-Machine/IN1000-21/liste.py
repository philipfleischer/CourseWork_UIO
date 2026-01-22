kast = input("Kast fem terninger: \n >")
liste = []
liste.append(kast.split(","))
print(liste)

print(liste.count(4)*4)

if len(liste) == 1:
    print("yatzy")
else:
    print("feil")
mengde = set(liste)

#Hus eller fire like
firere_eller_hus = len(mengde) == 2
print(firere_eller_hus)
liste.count(forste_terning) in [2,3]
