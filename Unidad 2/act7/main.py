from ClaseViajero import Viajero
from claseManejadorViajero import Manejador
from claseMenu import Menu
if __name__ == '__main__':
    mv = Manejador()
    mv.testViajeros()
    print("Viajero con más millas")
    print(mv.ordena())
    num = int(input("ingrese un numero de viajero: "))

    unViajero = mv.encuentraViajero(num)
    bandera = True
    menu = Menu()
    if unViajero == -1:
        print("El viajero no se encuentra en el archivo")
    else:

        while bandera:

            print("\n\nSeleccione una de las siguientes opciones")
            print("1-Consultar Cantidad de Millas.\n2-Acumular Millas. \n3- Canjear millas \n4- Salir")
            op = str(input("opcion: "))
            bandera = menu.opcion(op, unViajero)



