
class Flor:
    __numero: int
    __nombre: str
    __color: str
    __descripcion: str

    def __init__(self, num, nom, col, des):
        self.__numero = int(num)
        self.__nombre = nom
        self.__color = col
        self.__descripcion = des

    def __str__(self):
        return self.__nombre


    def getNum(self):
        return int(self.__numero)
