#Esta clase es una lista Secuencial ordenada por contenido
#El contenido en este caso es para tipos de dato entero
#Para otros tipos de dato, hay que cambiar la inserción

#ya anda la inserción falta hacer el suprimir
import numpy as np

class ListaSecuencialporContenido:
    __tope: int                     #tope apunta al primer espacio vació
    __lista: np.ndarray
    __cant: int


    def __init__(self, cant = 20):
        self.__lista = np.empty(20, int)
        self.__tope = 0
        self.__cant = cant
    
    def __str__(self) -> str:
        return (str(self.__lista))

    def vacia(self):
        return (self.__tope == 0)
    
    def llena(self):
        return (self.__tope == self.__cant)
    
    def insertar(self, nuevo):
        if self.vacia():
            self.__lista[0] = nuevo
            self.__tope += 1
        elif self.llena():
            print('Lista llena, no se puede insertar')
        else:
            i=0
            while i < self.__tope and nuevo > self.__lista[i]:
                i+=1
            if i == self.__tope:                                        #si i = tope entonces nuevo es el último elemento del arreglo y lo insertamos acá
                self.__lista[i] = nuevo
                self.__tope += 1
            else:
                self.__shifteoInsercion(i)
                self.__lista[i] = nuevo
                self.__tope += 1

    def __shifteoInsercion(self, indice):
        for i in range(self.__tope - indice):                                       #tope - indice da como resultado la cantidad de celdas que se van a mover
            self.__lista[self.__tope - i] = self.__lista[self.__tope - i - 1]

    def __shifteoSuprimir(self, indice):
        for i in range(self.__tope - indice):
            self.__lista[indice + i] = self.__lista[indice + i + 1]

    def primer_elemento(self):
        if not self.vacia():
            return self.__lista[0]
        else:
            print('Lista vacia, no hay primer elemento')
            return -1

    def ultimo_elemento(self):
        if not self.vacia():
            return self.__lista[self.__tope-1]                
        else:
            print('Lista vacía, no hay tope')
            return -1
    
    def recuperar(self, indice):
        x = -1
        if indice < self.__tope:
            x = self.__lista[indice]
        else:
            print('El elemento está fuera de rango')
        return x
        
    def suprimir(self, indice):
        x = -1
        if indice > self.__tope:
            print('El indice a suprimir no está en la lista')
        else:
            x = self.__lista[indice]
            self.__shifteoSuprimir(indice)
            self.__tope -= 1
        return x

    def buscar(self, valor):
        
        i=0
        while i < self.__tope and valor != self.__lista[i]:
            i+=1
        if valor == self.__lista[i]:
            return i
        else:
            return -1
        
    def recorrer(self):
        pass