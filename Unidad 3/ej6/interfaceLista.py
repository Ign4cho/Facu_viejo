from zope.interface import Interface

class ILista(Interface):
    def insertarElemento(self, unElemento: object, pos: int):
        pass

    def agregarElemento(self, unElemento):
        pass

    def mostrarElemento(self, pos):
        pass
