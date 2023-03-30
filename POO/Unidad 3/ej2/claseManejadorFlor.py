import csv
from claseFlor import Flor
import numpy as np

class ManejadorFlor:
    __lista = []
    __dimension: int
    __cantidad: int

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 1
        self.__lista = np.empty(1, dtype=Flor)

    def agregarFlor(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension += 1
            self.__lista.resize(self.__dimension)
        self.__lista[self.__cantidad] = unaFlor
        self.__cantidad += 1

    def testFlores(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter=';')

        for linea in reader:
            num = linea[0]
            nom = linea[1]
            color = linea[2]
            desc = linea[3]

            unaFlor = Flor(num,nom,color,desc)
            self.agregarFlor(unaFlor)
        archivo.close()

    def buscaFlor(self, num):
        i=0
        ret = 0
        while ret == 0 and i < self.__cantidad:
            if self.__lista[i].getNum() == num:
                ret = self.__lista[i]
            else:
                i += 1
        return ret

    def creaLista(self):
        lista = []
        for i in range(self.__cantidad):
            x = [self.__lista[i].getNum(), 0]
            lista.append(x)
        return lista

    def muestraFlores(self, lista):
        print('Las flores más vendidas son: ')
        for i in range(5):
            num = lista[i][0]
            unaFlor = self.buscaFlor(num)
            print(unaFlor)
