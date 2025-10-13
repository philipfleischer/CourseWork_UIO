from dato import Dato

def main():
    dato1 = Dato(15, 10, 21)
    print(dato1.get_aar())
    print(dato1.pr_dato())
    dag = dato1.dato()
    if dag == 15:
        print("Lønningsdag!")
    elif dag == 1:
        print("Ny måned nye muligheter!")

#Oppgave 3d og e, hvordan burde jeg gjøre dette?
    dato_string = dato1.pr_dato()
    print("Her er datoen:", dato_string)
    print(dato1.dag_maaned())




main()
