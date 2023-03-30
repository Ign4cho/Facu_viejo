from claseFlor import Flor

class Ramo:
    __tamano: int
    __flores = []

    def __init__(self, cant):
        self.__tamano = cant
        self.__flores = []

    def cargaFlor(self, unaFlor):
        if isinstance(unaFlor, Flor):
            self.__flores.append(unaFlor)

    def cuentaFlores(self, lista):
        for flor in self.__flores:
            num = flor.getNum()
            lista[num-1][1] += 1
        return lista
    
    def getTamano(self):
        return self.__tamano

    def muestraFlores(self):
        for flor in self.__flores:
            print(flor)

