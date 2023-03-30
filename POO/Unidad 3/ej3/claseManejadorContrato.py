from claseJugador import Jugador
from claseEquipo import Equipo
from claseContrato import Contrato
from claseManejadorEquipo import ManejadorEquipo
import numpy as np
import datetime
import csv

class ManejadorContrato:
    __arreglo = []
    __cantidad: int
    __dimension: int

    def __init__(self):
        self.__dimension = 1
        self.__cantidad = 0
        self.__arreglo = np.empty(self.__dimension, dtype = Contrato)

    def agregaContrato(self, unContrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += 1
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = unContrato
        self.__cantidad += 1

    def crearContrato(self, me, unJugador):
        eq = input('Ingrese el nombre del equipo')
        unEquipo = me.buscarEquipo(eq)
        while unEquipo == 0:
            eq = input('El nombre de equipo es incorrecto, intente nuevamente. ')
            unEquipo = me.buscarEquipo(eq)
        inicio = self.crearFecha('inicio')
        fin = self.crearFecha('fin')
        pago = float(input('Ingrese el pago mensual del jugador: '))
        unContrato = Contrato(unEquipo, unJugador, inicio, fin, pago)
        self.agregaContrato(unContrato)
        print('Contrato creado')


    def crearFecha(self, txt):
        print(f'    Fecha de {txt}')
        anio = int(input('Año: '))
        mes = int(input('Mes: '))
        dia = int(input('Dia: '))
        fecha = datetime.date(anio, mes, dia)
        return fecha

    def buscaDni(self, dni):
        i=0
        ret = 0
        while i < self.__cantidad and ret == 0:
            if self.__arreglo[i].getDni() == dni:
                ret = self.__arreglo[i]
            else:
                i+=1
        return ret

    def muestraContrato(self, unContrato: Contrato):
        eq = unContrato.getNomEquipo()
        fecha = unContrato.getFechaFin()
        print(f'El jugador juega para {eq} y su contrato finaliza {fecha}')

    def listaJugadores(self, unEquipo: Equipo):
        bandera = False
        print(f'Jugadores de {unEquipo.getNom()} cuyo contrato vence en menos de 6 meses')
        for i in range(self.__cantidad):
            if self.__arreglo[i].getNomEquipo() == unEquipo.getNom() and self.__arreglo[i].vencimiento():
                bandera = True
                unJugador = self.__arreglo[i].getJugador()
                print(f'Jugador: {unJugador.getNombre()}    DNI: {unJugador.getDni() }')
                print(f'Ciudad: {unJugador.getCiudad()} País: {unJugador.getPais()}   Nacimiento {unJugador.getFecha()}')

        if bandera == False:
            print('Ningun jugador cumple los requerimientos')

    def sumaContratos(self, unEquipo: Equipo):
        suma = 0
        for i in range(self.__cantidad):
            if self.__arreglo[i].getNomEquipo() == unEquipo.getNom():
                suma += self.__arreglo[i].getPago()

        return suma

    def guardarContratos(self):
        archivo = open('contratos.csv', 'w', newline='')
        writer = csv.writer(archivo)

        for i in range(self.__cantidad):
            writer.writerow([self.__arreglo[i].getFechaInicio(), self.__arreglo[i].getFechaFin(), self.__arreglo[i].getPago(), self.__arreglo[i].getNomEquipo(), self.__arreglo[i].getDni()])

        archivo.close()
