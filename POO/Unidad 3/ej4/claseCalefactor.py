import csv
import abc
from abc import ABC

class Calefactor:
    __marca: str
    __modelo: str
    
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @abc.abstractmethod
    def calcularCosto(self):
        pass

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
