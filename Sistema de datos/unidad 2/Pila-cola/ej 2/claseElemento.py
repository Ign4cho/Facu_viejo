
class Elemento:
    __valor: None
    __sig: None

    def __init__(self, valor):
        self.__valor = valor
        self.__sig = None

    def setSiguiente(self, siguiente):
        self.__sig = siguiente

    def getSiguiente(self):
        return self.__sig
    
    def getValor(self):
        return self.__valor