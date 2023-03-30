from claseManejador import Manejador

class Menu:
    __opc:int

    def __init__(self):
        self.__opc = 0

    def opcion(self):
        mc = Manejador()
        mc.testPlanes()
        while self.__opc != 5:
            print('     --Menu de opciones--')
            print('Opción 1-- Actualiza valor del vehículo de cada plan')
            print('Opción 2-- Dado un valor, se muestra los planes con valores menores al dado')
            print('Opción 3-- Muestra el costo de licitar cada plan')
            print('Opción 4-- Dado un código, se modifica la cantidad de cuotas necesarias para licitar\nOpción 5-- Salir')
            cod = int(input('Opción: '))
            self.__opc = cod

            if self.__opc == 1:
                mc.actulizaValorPlanes()
            elif self.__opc == 2:
                mc.valorMenor()
            elif self.__opc == 3:
                mc.mostrarMontoLicitacion()
            elif self.__opc == 4:
                mc.modificaLicitacion()
            elif self.__opc == 5:
                print("Goodbye!")
            else:
                print("La opción ingresada no es valida, intente nuevamente")








