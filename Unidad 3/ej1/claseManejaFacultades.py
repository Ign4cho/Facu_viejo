import csv
from claseCarrera import Carrera
from claseFacultad import Facultad

class ManejaFacultades:
    __listaFacultades = []

    def __init__(self):
        self.__listaFacultades = []

    def __str__(self):
        s = ''
        for fac in self.__listaFacultades:
            s += str(fac)
        return s

    def lecturaArchivo(self):
        archivo = open('facultades.csv')
        reader = csv.reader(archivo)
        numFacultad = 0
        for fila in reader:
            if int(fila[0]) == numFacultad:
                cod = fila[1]
                nom = fila[2]
                fecha = fila[3]
                dur = fila[4]
                tit = fila[5]

                unaCarrera = Carrera(cod, nom, fecha, dur, tit)
                unaFac.agregaCarrera(unaCarrera)
            else:
                numFacultad += 1
                cod = fila[0]
                nom = fila[1]
                dire = fila[2]
                loc = fila[3]
                prov = fila[4]
                tel = fila[5]

                unaFac = Facultad(cod, nom, dire, loc, prov, tel)
                self.agregaFac(unaFac)
        archivo.close()

    def agregaFac(self, unaFac):
        if isinstance(unaFac, Facultad):
            self.__listaFacultades.append(unaFac)
        else:
            print('Error de tipos')

    def agregaCarrera(self, unaFac, unaCarrera):
        bandera = True
        if not isinstance(unaFac, Facultad):
            bandera = False
        if not isinstance(unaCarrera, Carrera):
            bandera = False
        if bandera:
            unaFac.agregaCarrera(unaCarrera)

    def buscaFacultad(self, nombreFac):
        bandera = True
        i=0
        ret = 0
        while i < len(self.__listaFacultades) and bandera:
            if self.__listaFacultades[i].getNom() == nombreFac:
                bandera = False
                ret = self.__listaFacultades[i]
            else:
                i += 1
        return ret

    def muestraFac(self, unaFac):
        unaFac.getDuracion()

    def buscaCarrera(self, nombreCarrera):

        i = 0
        ret = 0
        while i < len(self.__listaFacultades) and ret == 0:
            ret = self.__listaFacultades[i].buscaCarrera(nombreCarrera)
            i+=1

        return ret

    def muestraCarrera(self, unaCarrera):

        i=0
        ret = 0
        while i < len(self.__listaFacultades) and ret == 0:
            ret = self.__listaFacultades[i].buscaCarrera(unaCarrera.getNom())
            if ret == 0:        # i se incrementa si no se encuentra, si no
                i+=1            # es el indice de la facultad donde está la carrera

        if ret != 0:
            print(f'Codigo: {self.__listaFacultades[i].getCod()}{unaCarrera.getCod()}\n'
                  f'Nombre: {unaCarrera.getNom()}\n'
                  f'Dirección: {self.__listaFacultades[i].getDir()}'
                  )



