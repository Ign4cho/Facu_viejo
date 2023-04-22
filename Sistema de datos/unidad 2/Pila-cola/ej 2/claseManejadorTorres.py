from clasePilaEnlazada import Pila

class ManejadorTorres:
    __ATorre: Pila
    __BTorre: Pila
    __CTorre: Pila

    def __init__(self, n:int):
        self.__ATorre = Pila()
        self.__BTorre = Pila()
        self.__CTorre = Pila()

        while n > 0:
            self.__ATorre.insertar(n)
            n-=1
        
    def cambio(self, salida: str, llegada: str):
        ret = True
        pilaSalida = self.strtotorre(salida)
        pilaLlegada = self.strtotorre(llegada) 
        if (pilaSalida == None) or (pilaLlegada == None) or (pilaLlegada == pilaSalida):
            print('La entrada no es valida')
            ret = False
        elif (pilaSalida.vacia()):
            print('\n\nLa pila de salida está vacía\n\n')
            ret = False
        elif (pilaLlegada.vacia()):
            d = pilaSalida.suprimir()
            pilaLlegada.insertar(d)
            ret = True                                                                          #La pila de llegada estaba vacía
            print('\n\nLa pila de llegada estaba vacía\n\n')
        else:
            disco = pilaSalida.suprimir()
            recibe = pilaLlegada.suprimir()
            if recibe > disco:
                pilaLlegada.insertar(recibe)
                pilaLlegada.insertar(disco)
                ret = True                                                                      #La pila de llegada tenía un disco mayor al del cambio
                print('\n\nLa pila de llegada tenía un disco mayor al del cambio\n\n')
            elif recibe < disco:
                pilaSalida.insertar(disco)
                pilaLlegada.insertar(recibe)                                                    #ambos discos vuelven a su pila original, el cambio no es válido
                ret = False
                print('\n\nCambio no valido\n\n')


        return ret

    def strtotorre(self, s:str):
        ret = None
        if (s.upper()=='A'):
            ret = self.__ATorre
        elif (s.upper()=='B'):
            ret = self.__BTorre
        elif (s.upper()=='C'):
            ret = self.__CTorre
        else:
            print('La torre ingresada no es valida')
        return ret
        

    def mostrarTorres(self):
        print('Torre A')
        self.__ATorre.recorrer()
        print('Torre B')
        self.__BTorre.recorrer()
        print('Torre C')
        self.__CTorre.recorrer()
    