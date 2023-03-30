from ClaseViajero import Viajero

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self, op, unViajero:Viajero):
        bandera=True
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1':
            self.opcion1(unViajero)
        elif op == '2':
            self.opcion2(unViajero)
        elif op == '3':
            self.opcion3(unViajero)
        elif op == '4':
            self.salir()
            bandera=False
        return bandera

    def salir(self):
        print("Ha salido del programa")

    def opcion1(self, unViajero:Viajero):
        mi = unViajero.cantidadTotaldeMillas()
        print(f'Tiene {mi} millas acumuladas')

    def opcion2(self, unViajero:Viajero):
        ac = int(input("Ingrese la cantidad de millas que desea acumular   "))
        unViajero + ac

    def opcion3(self, unViajero:Viajero):
        can = int(input("Ingrese la cantidad de millas que desea canjear"))
        ret = unViajero - can
        if ret == -1:
            print("No tiene las millas necesarias para realizar el canje")
        else:
            print("Canje exitoso")


