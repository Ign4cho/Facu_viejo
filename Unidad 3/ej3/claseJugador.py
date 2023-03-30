

class Jugador:
    __nombre: str
    __dni: str
    __ciudad: str
    __pais: str
    __fecha_nac: str

    def __init__(self, nom, dni, ciu, pais, fecha):
        self.__nombre = nom
        self.__dni = dni
        self.__ciudad = ciu
        self.__pais = pais
        self.__fecha_nac = fecha

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getCiudad(self):
        return self.__ciudad

    def getPais(self):
        return self.__pais

    def getFecha(self):
        return self.__fecha_nac
