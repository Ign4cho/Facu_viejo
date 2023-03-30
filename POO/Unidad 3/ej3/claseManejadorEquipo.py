from claseEquipo import Equipo
import numpy as np
import csv

class ManejadorEquipo:
    __arreglo = []
    __dimension: int
    __cantidad: int

    def __init__(self):
        self.__dimension = 1
        self.__cantidad = 0
        self.__arreglo = np.empty(1, dtype = Equipo)

    def agregarEquipo(self, unEquipo):

        if self.__cantidad == self.__dimension:
            self.__dimension += 1
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = unEquipo
        self.__cantidad += 1

    def testEquipos(self):
        archivo = open('equipos.csv')
        reader = csv.reader(archivo)
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                nom = linea[0]
                ciu = linea[1]

                unEquipo = Equipo(nom, ciu)
                self.agregarEquipo(unEquipo)
        archivo.close()

    def buscarEquipo(self, nombre):
        i=0
        ret = 0
        while ret == 0 and i < self.__cantidad:
            if self.__arreglo[i].getNom() == nombre:
                ret = self.__arreglo[i]
            else:
                i += 1
        return ret

