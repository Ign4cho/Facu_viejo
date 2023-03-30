from claseCalefactor import Calefactor

class GasNatural(Calefactor):
    __matricula: str
    __calorias: float
    #atributo de clase
    costo = 0

    def __init__(self, marca, modelo, matr, calorias):
        super().__init__(marca,modelo)
        self.__matricula = matr
        self.__calorias = float(calorias)

    @classmethod
    def setCosto(cls, nuevo):
        cls.costo = nuevo

    def calcularCosto(self, cantmetros, costometro):
        costo = self.__calorias / 1000 * cantmetros * costometro
        return costo

    def getMatricula(self):
        return self.__matricula

    def getCalorias(self):
        return self.__calorias
