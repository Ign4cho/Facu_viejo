import csv

from claseCalefactor import Calefactor
from claseElectrico import Electrico
from claseGasNatural import GasNatural
import numpy as np

class ManejadorCalefactor:
    __areglo = []
    __cantidad: int
    __dimension: int

    def __init__(self, cant):
        self.__cantidad = 0
        self.__dimension = cant
        self.__areglo = np.empty(self.__dimension, dtype=Calefactor)

    def agregarCalefactor(self, unCalefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += 1
            self.__areglo.resize(self.__dimension)
            print('hmm')
        self.__areglo[self.__cantidad] = unCalefactor
        self.__cantidad += 1


    def testCalefactores(self):
        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo)
        for linea in reader:
            marca = linea[0]
            mod = linea[1]
            matr = linea[2]
            cal = linea[3]
            unCalefactor = GasNatural(marca, mod, matr, cal)
            self.agregarCalefactor(unCalefactor)
        archivo.close()

        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo)
        for linea in reader:
            marca = linea[0]
            mod = linea[1]
            pot = linea[2]
            unCalefactor = Electrico(marca,mod,pot)
            self.agregarCalefactor(unCalefactor)
        archivo.close()

    def setCostoGas(self, costo):
        GasNatural.setCosto(costo)

    def setCostoKilo(self, costo):
        Electrico.setCosto(costo)

    def menorCostoGas(self, cantMetros, costoMetro):
        min = 9999999
        unCal = None
        for i in range(self.__cantidad):
            if isinstance(self.__areglo[i], GasNatural):
                if self.__areglo[i].calcularCosto(cantMetros, costoMetro) < min:
                    unCal = self.__areglo[i]
                    min = self.__areglo[i].calcularCosto(cantMetros, costoMetro)

        return unCal

    def menorCostoElectrico(self, cantMetros, costoKw):
        min = 9999999
        unCal = None
        for i in range(self.__cantidad):
            if isinstance(self.__areglo[i], Electrico):
                if self.__areglo[i].calcularCosto(cantMetros, costoKw):
                    unCal = self.__areglo[i]
                    min = self.__areglo[i].calcularCosto(cantMetros, costoKw)
        return unCal

    def mostrarMenor(self, unGas: GasNatural, unElectrico: Electrico, metros, costok, costogas):
        if unElectrico.calcularCosto(costok,metros) <= unGas.calcularCosto(metros, costogas):
            print(f'Calefactor electrico\nMarca: {unElectrico.getMarca()} Modelo: {unElectrico.getModelo()}')
            print(f'Potencia: {unElectrico.getPotencia()}')

        else:
            print(f'Calefactor a gas natural\nMarca: {unGas.getMarca()} Modelo: {unGas.getModelo()}')
            print(f'Matricula: {unGas.getMatricula()}   Calorias: {unGas.getCalorias()}')


