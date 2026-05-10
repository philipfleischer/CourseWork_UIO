from random import randint, choice, choices

print()
print("1) randint")
print()
print(f"Hjemmelag - Bortelag {randint(0, 9)} - {randint(0, 9)}")

print()
print()
print("2) Choice")
print()
h = choice([0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7])
b = choice([0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6])
print(f"Hjemmelag - Bortelag {h} - {b}")


print()
print()
print("3) Choices")
print()
m_hjemme = [0, 1, 2, 3, 4, 5, 6, 7, 8]
prob_hjemme = [0.1, 0.2, 0.3, 0.2, 0.1, 0.04, 0.03, 0.02, 0.01]
hjemme = choices(m_hjemme, prob_hjemme)

m_borte = [0, 1, 2, 3, 4, 5, 6, 7, 8]
prob_borte = [0.3, 0.3, 0.3, 0.2, 0.1, 0.04, 0.03, 0.02, 0.01]
borte = choices(m_borte, prob_borte)
print(f"Hjemmelag - Bortelag {hjemme} - {borte}")
print()
print()
