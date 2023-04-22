from claseNodoArbol import Nodo

class Arbol:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None

    def insertar(self, n):          #todavía no lo pruebo
        nuevo = Nodo(n)
        if self.__raiz == None:
            self.__raiz = nuevo
        else:
            aux = self.__raiz
            bandera = False
            while not bandera:  
                if aux.getValor() > n:                  #si el n es menor al valor del nodo, vamos por izq
                    auxiz = aux.getIz()
                    if auxiz == None:
                        aux.setIz(nuevo)
                        bandera = True
                    else:
                        aux = auxiz
                
                elif aux.getValor() < n:                #si el n es mayor al valor del nodo, vamos por der
                    auxde = aux.getDe()
                    if aux.getDe() == None:
                        aux.setDe(nuevo)
                        bandera = True

                    else:
                        aux = auxde
                else:
                    aux.setCuenta(1)                    #si es igual, incrementamos contador
                    bandera = True

    def preorden(self, nodo:Nodo, re: str):
        re += f'{nodo.getValor()}-'
        if nodo.getIz() != None:
            re = self.preorden(nodo.getIz(), re)
        if nodo.getDe() != None:
            re = self.preorden(nodo.getDe(), re)
        return re
   
    def postorden(self, nodo:Nodo, re: str):
        if nodo.getIz() != None:
            re = self.postorden(nodo.getIz(), re)
        if nodo.getDe() != None:
            re = self.postorden(nodo.getDe(), re)
        re += f'{nodo.getValor()}-'
        return re
    
    def inorden(self, nodo: Nodo, re: str):
        if nodo.getIz() != None:
            re = self.inorden(nodo.getIz(), re)
        re += f'{nodo.getValor()}-'
        if nodo.getDe() != None:
            re = self.inorden(nodo.getDe(), re)
        return re
    
    def getRaiz(self):
        return self.__raiz