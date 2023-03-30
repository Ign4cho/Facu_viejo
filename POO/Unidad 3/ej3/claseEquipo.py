

class Equipo:
    __nombre: str
    __ciudad: str

    def __init__(self, nom, ciudad):
        self.__nombre = nom
        self.__ciudad = ciudad

    def getNom(self):
        return self.__nombre


