class Nodo:
    __valor: None
    __iz: None
    __de: None
    __cuenta: int

    def __init__(self, valor):
        self.__valor = valor
        self.__iz, self.__de = None, None
        self.__cuenta = 1

    def setIz(self, siguiente):
        self.__iz = siguiente

    def getIz(self):
        return self.__iz
    
    def setDe(self, siguiente):
        self.__de = siguiente

    def getDe(self):
        return self.__de
    
    def getValor(self):
        return self.__valor
    
    def setCuenta(self, i: int):
        self.__cuenta += i

    def getCuenta(self):
        return self.__cuenta