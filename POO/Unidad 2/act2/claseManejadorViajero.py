from ClaseViajero import Viajero

import csv

class Manejador:

    def __init__(self):
        self.__listaViajeros=[]

    def __str__ (self):
        retorno = ""
        for Viajero in self.__listaViajeros:
            retorno += str(Viajero) + "\n"
        return retorno

    def testViajeros(self):
        archivo = open('datosViajeros.csv')
        reader = csv.reader(archivo)

        bandera = True
        for linea in reader:
            if bandera:
                bandera = not bandera
            else:
                num = int(linea[0])
                dni = linea[1]
                nombre = linea[2]
                apellido = linea[3]
                mill = int(linea[4])
                unViajero = Viajero(num, dni, nombre, apellido, mill)
                self.agregarViajero(unViajero)
        archivo.close()

    def agregarViajero (self, unViajero):
        self.__listaViajeros.append(unViajero)

    def encuentraViajero(self, id):
        valorRetorno = -1
        archivo = open('datosViajeros.csv')
        reader = csv.reader(archivo)
        bandera = True

        for linea in reader:
            if bandera:
                bandera = not bandera
            else:
                if int(linea[0]) == id:
                    valorRetorno = Viajero(int(linea[0]), linea[1], linea[2], linea[3], int(linea[4]))
        archivo.close()
        return valorRetorno


