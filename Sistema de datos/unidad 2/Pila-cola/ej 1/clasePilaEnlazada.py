from claseElemento import Elemento

class Pila:
    __cabeza: Elemento
    __tope: int
    
    def __init__(self):
        self.__tope = 0
        self.__cabeza = None

    def vacia(self):
        return (self.__tope == 0)

    def insertar(self, nuevo):
        if self.vacia():
            self.__cabeza = Elemento(nuevo)
            self.__tope+=1
            print(f'insterta {nuevo} en vacio')
        else:
            aux = self.__cabeza
            self.__cabeza = Elemento(nuevo)
            self.__cabeza.setSiguiente(aux)
            self.__tope +=1
            print(f'insterta {nuevo}')
    
    def suprimir(self):
        x = self.__cabeza.getValor()
        self.__cabeza = self.__cabeza.getSiguiente()
        self.__tope-=1
        return x
    
    def recorrer(self):
        actual = self.__cabeza
        while actual != None:
            print(f'muestra {actual.getValor()}')
            actual = actual.getSiguiente()


