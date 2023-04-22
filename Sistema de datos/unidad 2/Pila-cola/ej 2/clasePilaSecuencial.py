from claseElemento import Elemento

class Pila:
    __tope: int
    __lista: list

    def __init__(self):
        self.__tope = -1
        self.__lista = []

    def vacia(self):
        return (self.__tope == -1)
        
    def insertar(self, nuevo):
        self.__lista.append(nuevo)
        self.__tope += 1
    
    def suprimir(self):
        x = None
        if not self.vacia():
            x = self.__lista.pop(self.__tope)
            self.__tope -= 1
            
        return x

    def recorrer(self):
        print('entro')
        for i in range(self.__tope):
            print(f'{self.__lista[-i]}')
        