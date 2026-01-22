#Lager en klasse som jeg kaller Dato
class Dato:
    #lager en konstruktør med 3 instansvariabler
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyAar = nyttAar

    def get_aar(self):
        return self._nyAar
#I denne prosedyren blir dagen, måneden og året returnert
    def pr_dato(self):
        dag = self._nyDag
        maaned = self._nyMaaned
        aar = self._nyAar
        return (f"{dag}.{maaned}.{aar}")

#Hva er dette???
    def dag_maaned(self):
        if self._nyDag > 31 or self._nyMaaned > 12:
            return False
        elif self._nyDag < 1 or self._nyMaaned < 1:
            return False
        else:
            return True
