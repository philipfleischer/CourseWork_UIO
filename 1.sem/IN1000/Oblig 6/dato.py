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

    def dato(self):
        return self._nyDag

#Hva er dette???
    def dag_maaned(self):
        bruker_dag = int(input("Skriv inn en dag\n< "))
        if self._nyDag == bruker_dag:
            return True
        else:
            return False
