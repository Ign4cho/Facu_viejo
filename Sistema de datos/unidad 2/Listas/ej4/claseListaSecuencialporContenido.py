
import numpy as np

class Elemento:
    __fila: int
    __col: int
    __valor: int

    def __init__(self, nuevo: list):
        self.__fila = nuevo[0]
        self.__col = nuevo[1]
        self.__valor = nuevo[2]

    def __str__(self):
        return f'[{self.getFila()}, {self.getColumna()}, {self.getValor()}]'

    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__col
    
    def getValor(self):
        return self.__valor
    

class ListaSecuencialporContenido:
    __tope: int                     #tope apunta al primer espacio vació
    __lista: np.ndarray
    __cant: int


    def __init__(self, cant = 20):
        self.__lista = np.empty(20, Elemento)
        self.__tope = 0
        self.__cant = cant
    
    def __str__(self) -> str:
        return (str(self.__lista))

    def vacia(self):
        return (self.__tope == 0)
    
    def llena(self):
        return (self.__tope == self.__cant)
    
    def getTope(self):
        return self.__tope
    
    def getElemento(self, indice):
        return self.__lista[indice]

    def insertar(self, nuevo):
        nuevo = Elemento(nuevo)
        if self.vacia():
            self.__lista[0] = nuevo
            self.__tope += 1
        elif self.llena():
            print('Lista llena, no se puede insertar')
        else:
            
            i=0
            while i < self.__tope and nuevo.getFila() < self.__lista[i].getFila():
                i+=1
            
            if i == self.__tope:                                        #si i = tope entonces nuevo es el último elemento del arreglo y lo insertamos acá
                self.__lista[i] = nuevo
                self.__tope += 1
            else:
                while i < self.__tope and nuevo.getFila() == self.__lista[i].getFila() and nuevo.getColumna() < self.__lista[i].getColumna():
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

        
    def recorrer(self):
        for i in range(self.__tope):
            print(self.__lista[i])

    def __add__(self, otro):
        nuevo = ListaSecuencialporContenido()
        i,j = 0,0
        while i < self.getTope() and j < otro.getTope():
            print(f'-- {self.getElemento(i)}, - {otro.getElemento(j)}')
            if self.__lista[i].getFila() == otro.getElemento(j).getFila():
                if self.__lista[i].getColumna() == otro.getElemento(j).getColumna():        #coinciden fila y columna
                    nuevo.insertar([self.__lista[i].getFila(), self.__lista[i].getColumna(), self.__lista[i].getValor() + otro.getElemento(j).getValor()])
                    i += 1
                    j += 1
                    print('Coincide fila y columna')
                elif self.__lista[i].getColumna() >= otro.getElemento(j).getColumna():
                    nuevo.insertar([self.__lista[i].getFila(), self.__lista[i].getColumna(), self.__lista[i].getValor()])
                    i+=1
                    print('Misma fila, a tiene menos columna')
                else:
                    nuevo.insertar([otro.getElemento(j).getFila(), otro.getElemento(j).getColumna(), otro.getElemento(j).getValor()])
                    print('Misma fila, a tiene más columna')
                    j+=1
            elif self.__lista[i].getFila() >= otro.getElemento(j).getFila():
                nuevo.insertar([self.__lista[i].getFila(), self.__lista[i].getColumna(), self.__lista[i].getValor()])
                i+=1
                print('a tiene menos fila')
            else:
                nuevo.insertar([otro.getElemento(j).getFila(), otro.getElemento(j).getColumna(), otro.getElemento(j).getValor()])
                j+=1
                print('b tiene menos fila')
        print(f'i={i}, j={j}    topei = {self.getTope()}, topej = {otro.getTope()}')
        while i < self.getTope():
            nuevo.insertar([self.__lista[i].getFila(), self.__lista[i].getColumna(), self.__lista[i].getValor()])
            i+=1
        
        while j < otro.getTope():
            nuevo.insertar([otro.getElemento(j).getFila(), otro.getElemento(j).getColumna(), otro.getElemento(j).getValor()])
            j+=1
        
        return nuevo