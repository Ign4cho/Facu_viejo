import abc
from abc import ABC


class Aparato:
    __marca: str
    __modelo: str
    __color: str
    __pais: str
    __precioBase: float
    __precioFinal: float

    def __init__(self, marca, modelo, color, pais, precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precioBase = float(precioBase)

    def __str__(self):
        s = '----------------------\n'
        s += self.getTipo()
        s += f'\nMarca: {self.getMarca()}\n'
        s += f'Pais: {self.getPais()}\n'
        s += f'Precio de venta: {self.getPrecioFinal()}'
        return s

    @abc.abstractmethod
    def getPrecioFinal(self):
        pass

    @abc.abstractmethod
    def calcularPrecio(self):
        pass

    @abc.abstractmethod
    def getTipo(self):
        pass

    def getPrecioBase(self):
        return self.__precioBase

    def getMarca(self):
        return self.__marca

    def getPais(self):
        return self.__pais

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    @abc.abstractmethod
    def toJSON(self):
        pass
