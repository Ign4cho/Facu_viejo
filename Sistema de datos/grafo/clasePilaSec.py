import numpy as np
class Pila:
    __tope: int
    __lista: list
    

    def __init__(self):
        self.__tope = -1
        self.__lista = np.zeros(30)

    def vacia(self):
        return (self.__tope == -1)
        
    def insertar(self, nuevo):
        self.__lista[self.__tope] = nuevo
        self.__tope += 1
    
    def suprimir(self):
        x = None
        if not self.vacia():
            x = self.__lista[self.__tope-1]
            self.__tope -= 1
            
        return x

    def recorrer(self):
        for i in range(self.__tope):
            print(f'{self.__lista[-i]}')
        