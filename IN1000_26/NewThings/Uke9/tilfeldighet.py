from random import randint, choice, choices

print()
print("1) randint")
print()
print(f"Hjemmelag - Bortelag {randint(0, 9)} - {randint(0, 9)}")
print()

print("2) Choice")
print()
h = choice([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7])
b = choice([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6])
print(f"Hjemmelag - Bortelag {h} - {b}")
print()

print("3) Choices")
print()
mål_h = [0, 1, 2, 3, 4, 5, 6, 7, 8] # Like mange elementer som listen under
sannsynligheter_h = [0.1, 0.2, 0.3, 0.2, 0.1, 0.04, 0.03, 0.02, 0.01] # Må ha sum()=1
h = choices(mål_h, sannsynligheter_h)

mål_b = [0, 1, 2, 3, 4, 5, 6, 7, 8] # Like mange elementer som listen under
sannsynligheter_b = [0.1, 0.2, 0.3, 0.2, 0.1, 0.04, 0.03, 0.02, 0.01] # Må ha sum()=1
b = choices(mål_b, sannsynligheter_b)

print(f"Hjemmelag - Bortelag {h} - {b}")
print()
