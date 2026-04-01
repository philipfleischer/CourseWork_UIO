class Hus:
    """farge skal ha typen str"""
    def __init__(self, farge: str):
        self.farge = farge

    def mal(self, ny_farge: str):
        self.farge = ny_farge

a = Hus("blå")
b = Hus("rød")

c = a

a.mal("gul")

b = c

print()
print(f"Hus a har fargen {a.farge}")
print(f"Hus b har fargen {b.farge}")
print(f"Hus c har fargen {c.farge}")

print()
print(f"Hus a har minneadressen {id(a)}")
print(f"Hus b har minneadressen {id(b)}")
print(f"Hus c har minneadressen {id(c)}")

def sett_til_null(parameter):
    print(f"parameter før: {id(parameter)}")
    parameter = 0
    print(f"parameter etter: {id(parameter)}")

argument = 4
print(f"arguemtn før: {id(argument)}")
sett_til_null(argument)
print(f"argunent etter: {id(argument)}")

print()
print(f"Blir det 0? {argument}")


""" ------- OUTPUT --------

Hus a har fargen gul
Hus b har fargen gul
Hus c har fargen gul

Hus a har minneadressen 4473445344
Hus b har minneadressen 4473445344
Hus c har minneadressen 4473445344
arguemtn før: 4480689264
parameter før: 4480689264
parameter etter: 4480689136
argunent etter: 4480689264

Blir det 0? 4

"""
