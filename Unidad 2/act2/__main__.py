


from claseMenu import Menu
from claseManejadorViajero import Manejador




if __name__ == '__main__':

    mv = Manejador()
    mv.testViajeros()


    num = int(input("ingrese un numero de viajero: "))

    unViajero = mv.encuentraViajero(num)
    if unViajero == -1:
        print("El viajero no se encuentra en el archivo")
    else:
        print("Seleccione una de las siguientes opciones")
        print("1-Consultar Cantidad de Millas.\n2-Acumular Millas. \n3- Canjear millas \n4- Salir")
        op = str(input("opcion: "))

        menu = Menu()
        menu.opcion(op, unViajero)



