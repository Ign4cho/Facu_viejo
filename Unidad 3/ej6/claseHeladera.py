from claseAparato import Aparato
import abc

class Heladera(Aparato):
    __capacidad: int
    __freezer: bool
    __ciclica: bool
    __precioFinal: float

    def __init__(self, marca,modelo,color,pais,precioBase,capacidad, freezer, ciclica):
        super().__init__(marca,modelo, color, pais, precioBase)
        self.__capacidad = int(capacidad)
        self.__freezer = bool(freezer in ['si', 'Si', 'SI'])
        self.__ciclica = bool(ciclica in ['si', 'Si', 'SI'])
        self.__precioFinal = self.calcularPrecio(float(precioBase))

    def calcularPrecio(self, pb):
        precio = pb
        if self.__freezer:
            precio *= 1.05
        else:
            precio *= 1.01

        if self.__ciclica:
            precio += pb * 0.1
        return precio

    def getPrecioFinal(self):
        return self.__precioFinal

    @classmethod
    def getTipo(self):
        return 'Heladera'

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                marca = super().getMarca(),
                modelo = super().getModelo(),
                color = super().getColor(),
                pais = super().getPais(),
                precioBase = super().getPrecioBase(),
                capacidad = self.__capacidad,
                freezer = self.__freezer,
                ciclica = self.__ciclica
            )
        )
        return d


