import datetime
from datetime import date, timedelta
from claseJugador import Jugador
from claseEquipo import Equipo


class Contrato:
    __fechaInicio: date
    __fechaFin: date
    __pagoMensual: float
    __equipo: None
    __jugador: None

    def __init__(self, unEq, unJu, inicio, fin, pago):
        self.__equipo = unEq
        self.__jugador = unJu
        self.__fechaInicio = inicio
        self.__fechaFin = fin
        self.__pagoMensual = float(pago)

    def getDni(self):
        dni = self.__jugador.getDni()
        return dni

    def getNomEquipo(self):
        return self.__equipo.getNom()

    def getFechaFin(self):
        return self.__fechaFin

    def getFechaInicio(self):
        return self.__fechaInicio

    def vencimiento(self):
        dif = self.__fechaFin -  date.today()
        ret = False
        if dif < timedelta(180):
            ret = True
        return ret

    def getJugador(self):
        return self.__jugador

    def getPago(self):
        return self.__pagoMensual
