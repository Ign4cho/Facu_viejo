from claseAparato import Aparato
import abc


class Lavarropa(Aparato):
    __capacidad: int
    __velocidad: int
    __programas: int
    __carga: str
    __precioFinal: float

    def __init__(self, marca,modelo,color,pais,precioBase,capacidad,velocidad,programas,carga):
        super().__init__(marca,modelo, color, pais, precioBase)
        self.__capacidad = int(capacidad)
        self.__velocidad = int(velocidad)
        self.__programas = int(programas)
        self.__carga = carga
        self.__precioFinal = self.calcularPrecio(float(precioBase))

    def calcularPrecio(self, pb):
        precio = pb
        if self.__capacidad <= 5:
            precio *= 1.01
        else:
            precio *= 1.03
        return precio

    def getPrecioFinal(self):
        return self.__precioFinal

    @classmethod
    def getTipo(self):
        return 'Lavarropa'

    def getCapacidad(self):
        return self.__capacidad

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
                velocidad = self.__velocidad,
                programas = self.__programas,
                carga = self.__carga

            )
        )
        return d
