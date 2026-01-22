from dato import Dato

def main():
    dato1 = Dato(1, 10, 21)
    print(dato1.get_aar())
    print(dato1.pr_dato())
    #dato1.pr_dato().split(".")
    liste = list(dato1.pr_dato())
    print(liste)
    if liste[0] == 15:
        print("Lønningsdag!")
    elif liste[0] == 1:
        print("Ny dag nye muligheter!")
    else:
        print("MAAAn")

#Oppgave 3d og e, hvordan burde jeg gjøre dette?
    dato_string = dato1.pr_dato()
    print("Her er datoen:", dato_string)




main()
