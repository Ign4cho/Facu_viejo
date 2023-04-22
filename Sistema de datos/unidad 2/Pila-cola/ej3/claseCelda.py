
class Celda:
    __valor: None
    __siguiente: None

    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None
    
    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, sig):
        self.__siguiente = sig
