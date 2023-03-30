


class Medicamento:
    __idCama:int
    __idMed: int
    __nombre: str
    __monodroga: str
    __presentacion: str
    __cantidad: int
    __precio: float

    def __init__(self, idC, idM, nom, monod, pres, cant, precio):
        self.__idCama = int(idC)
        self.__idMed = int(idM)
        self.__nombre = nom
        self.__monodroga = monod
        self.__presentacion = pres
        self.__cantidad = int(cant)
        self.__precio = float(precio)

    def getIDCama(self):
        return self.__idCama

    def getNom(self):
        return self.__nombre

    def getPres(self):
        return self.__presentacion

    def getCant(self):
        return self.__cantidad

    def getPrecio(self):
        return self.__precio
