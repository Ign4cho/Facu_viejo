import os
class Nodo:
    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig
    
    def getValor(self):
        return self.__valor

class Lista: #Lista Enlazada, por posicion
    __comienzo: Nodo
    __tamaño:int
    def __init__(self):
        self.__comienzo = None
        self.__tamaño = 1

    def estaVacia(self):
        return self.__comienzo == None

    def siguiente(self,valor):
        if self.estaVacia():
            print('Lista Vacia')
        else:
            siguiente = None
            nodo = self.__comienzo
            pos = 1
            while nodo != None:
                if pos == valor:
                    siguiente = nodo.getSiguiente()
                nodo = nodo.getSiguiente()
                pos+=1
        return siguiente

    def anterior(self,posicion)->Nodo:
        anterior, aux = None, None
        nodo = self.__comienzo

        if self.estaVacia():
            print('Esta Vacia')
            
        else:
            pos = 1
            while nodo != None:
                pos+=1
                if pos == posicion:
                    anterior = nodo
                aux = nodo
                nodo = nodo.getSiguiente()
            if nodo == None:
                anterior = aux
            return anterior

    def insertar(self,valor,posicion):
        if posicion > self.__tamaño:
            raise 'Fuero de Rango'
        nodo = Nodo(valor)
        if posicion == 1:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            
        else:
            previo = self.anterior(posicion)
            nodo.setSiguiente(previo.getSiguiente())
            previo.setSiguiente(nodo)

        self.__tamaño +=1

    def recuperar(self, i):
        pos = 1
        nodo = self.__comienzo
        bandera = False
        aux = None
        if i > self.__tamaño:
            aux = 0
        else:
            while nodo != None and bandera == False:
                if pos == i:
                    aux = nodo.getValor()
                    bandera = True
                pos +=1
                nodo = nodo.getSiguiente()
            return aux

    def suprimir(self,valor):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            if self.__comienzo.getValor()== valor:
                self.__comienzo = self.__comienzo.getSiguiente
            else:
                previo = self.anterior(valor)
                sig = self.siguiente(valor)
                previo.setSiguiente(sig)

    def buscar(self,valor):
        bandera = False
        pos = 0
        nodo = self.__comienzo
        while nodo != None and bandera != True:
            if nodo.getValor() == valor:
                print('Encontre el elemento')
                bandera = True
            pos+=1
            nodo = nodo.getSiguiente()
        if bandera ==  False:
            pos = -1
        else:
            pos = pos -1
        return pos
    
    def recorrer(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            while nodo.getSiguiente() != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()
        print(nodo.getValor())

    def getTamaño(self):
        return self.__tamaño