from claseJugador import Jugador
import numpy as np
from claseManejadorEquipo import ManejadorEquipo
from claseManejadorContrato import ManejadorContrato
import datetime


class ManejadorJugador:
    __lista = []
    __dimension: int
    __cantidad: int



    def crearJugador(self, mc: ManejadorContrato, me: ManejadorEquipo):
        print('-----Añadir Jugador-----')
        nom = input('Ingrese el nombre: ')
        dni = input('Dni: ')
        ciu = input('Ciudad: ')
        pais = input('Pais: ')
        fecha = input('Fecha de Nacimiento: ')
        unJugador = Jugador(nom, dni, ciu, pais, fecha)
        mc.crearContrato(me, unJugador)
        print('Jugador creado')


