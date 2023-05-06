class Nodo:
    __valor: str
    __iz: None
    __de: None
    __cuenta: str

    def __init__(self, palabra:str, linea:int):
        self.__valor = palabra
        self.__iz, self.__de = None, None
        self.__cuenta = str(linea)

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
    
    def setValor(self, valor):
        self.__valor = valor
    
    def setCuenta(self, i: int):
        self.__cuenta += f',{i}'

    def getCuenta(self):
        return self.__cuenta