from claseCalefactor import Calefactor

class Electrico(Calefactor):
    __potencia: int
    #de clase
    costo = 0

    def __init__(self, marca, modelo, pot):
        super().__init__(marca, modelo)
        self.__potencia = float(pot)

    @classmethod
    def setCosto(cls, nuevo):
        cls.costo = nuevo

    def calcularCosto(self, costokw, cant):
        costo = self.__potencia/1000 * cant * costokw
        return costo

    def getPotencia(self):
        return self.__potencia


