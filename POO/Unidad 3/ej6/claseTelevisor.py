from claseAparato import Aparato
import abc

class Televisor(Aparato):
    __pantalla: str
    __pulgadas: float
    __definicion: str
    __internet: bool
    __precioFinal: float

    def __init__(self, marca, modelo, color, pais, precioBase, pantalla, pulgadas, definicion, internet):
        super().__init__(marca,modelo, color, pais, precioBase)
        self.__pantalla = pantalla
        self.__pulgadas = float(pulgadas)
        self.__definicion = definicion
        self.__internet = bool(internet in ['si', 'Si', 'SI'])
        self.__precioFinal = self.calcularPrecio(float(precioBase))

    def calcularPrecio(self, pb):
        precio = pb
        if self.__definicion == 'SD':
            precio *= 1.01
        elif self.__definicion == 'HD':
            precio *= 1.02
        elif self.__definicion == 'FULL HD':
            precio *= 1.03

        if self.__internet:
            precio += pb * 0.1
        return precio

    def getPrecioFinal(self):
        return self.__precioFinal

    @classmethod
    def getTipo(self):
        return 'Televisor'

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                marca = super().getMarca(),
                modelo = super().getModelo(),
                color = super().getColor(),
                pais = super().getPais(),
                precioBase = super().getPrecioBase(),
                pantalla = self.__pantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__definicion,
                internet = self.__internet
            )
        )
        return d
