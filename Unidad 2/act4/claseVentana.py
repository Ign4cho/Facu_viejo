
class Ventana:
    __titulo: str
    __xsi: int
    __ysi: int
    __xid: int
    __yid: int

    def __init__(self, tit: str, xsupiz = 0, ysupiz = 0, xinfde = 500, yinfde = 500 ):
        self.__titulo = tit
        self.__xsi, self.__ysi = xsupiz, ysupiz
        self.__xid, self.__yid = xinfde, yinfde

    def mostrar(self):
        print(f'Titulo: {self.__titulo}\nX Vertice superior izquierdo: {self.__xsi}')
        print(f'Y Vertice superior izquierdo: {self.__ysi}\nX Vertice inferior derecho: {self.__xid}\nY Vertice inferior derecho: {self.__yid}')

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return (self.__yid - self.__ysi)

    def ancho(self):
        return(self.__xid - self.__xsi)

    def moverDerecha(self, mov = 1):
        self.__xsi += mov
        self.__xid += mov

    def moverIzquierda(self, mov = 1):
        self.__xsi -= mov
        self.__xid -= mov

    def bajar(self, mov = 1):
        self.__ysi -= mov
        self.__yid -= mov

    def subir(self, mov = 1):
        self.__ysi += mov
        self.__yid += mov

