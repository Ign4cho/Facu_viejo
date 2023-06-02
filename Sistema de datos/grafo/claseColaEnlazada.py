from claseCelda import Celda

class Cola:
    __cant: int
    __prim: Celda
    __ult: Celda

    def __init__(self):
        self.__cant = 0
        self.__prim = None
        self.__ult = None

    def vacia(self):
        return (self.__cant == 0)
    
    def insertar(self, x):
        aux = Celda(x)
        if self.__cant == 0:
            self.__prim = aux
            self.__ult = aux
        elif self.__cant == 1:
            self.__prim.setSiguiente(aux)
            self.__ult = aux
        else:
            self.__ult.setSiguiente(aux)
            self.__ult = aux
        self.__cant += 1

    def suprimir(self):
        aux = None
        if self.__cant != 0:
            
            aux = self.__prim.getValor()
            self.__prim = self.__prim.getSiguiente()
            self.__cant -= 1
            
        
        return aux

    def recorrer(self):
        aux = self.__prim
        for i in range(self.__cant):
            print(f'{aux.getValor()}')
            aux = aux.getSiguiente()

    def aumentaValores(self):
        aux = self.__prim
        for i in range(self.__cant):
            v = aux.getValor()
            aux.setValor([v[0], v[1]+1])

    def getCantidad(self):
        return self.__cant