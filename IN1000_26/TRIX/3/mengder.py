# 03.06
# Hva skrives ut når følgende kodesnitter blir kjørt?

# a)
frukt = {"banan", "eple", "banan", "appelsin", "Banan", "banan"}
print(frukt)

# OUTPUT:
# {"eple", "appelsin", "Banan", "banan"}

# b)
navn = set(["Anna", "Ola", "Inger"])
if "anna" in navn:
    print("Anna er i mengde")
else:
    print("Anna er ikke i mengde")

# OUTPUT:
# Anna er ikke i mengde

# c)
mengde_a = set([1, 2, 3, 2, 3])
mengde_b = {1, 2, 3}
print(mengde_a == mengde_b)

# OUTPUT:
# True

# d)
dyr = {"Dromedar", "Dromedar", "Sjiraff", "Kakadue"}

dyr.remove("Dromedar")
dyr.add("Katt")
print(dyr)

# OUTPUT:
# {"Dromedar", "Sjiraff", "Kakadue", "Katt"}

# e)
bokstav = set("abcdefg")
print(bokstav)

# OUTPUT:
# {a, b, c, d, e, f, g}
