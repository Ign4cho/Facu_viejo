


class Registro:
    __temperatura: float
    __humedad: int
    __presion: int

    def __init__(self, temp: float, hum: int, pres: int):

        self.__temperatura = temp
        self.__humedad = hum
        self.__presion = pres

    def __str__(self):
        s = str(self.__temperatura) + ',' + str(self.__humedad) + ',' + str(self.__presion) + '\n'
        return s

    def getTemp(self):
        return self.__temperatura

    def getHum(self):
        return self.__humedad

    def getPres(self):
        return self.__presion
