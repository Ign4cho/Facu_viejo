

class Conjunto:
    __list = []

    def __init__(self):
        self.__list = []

    def __str__(self):
        s = '{'
        for i in self.__list:
            s += str(i)+ ' '
        s+= '}'
        return s

    def agregaElemento(self, nue:int):
        self.__list.append(nue)

    def generaConjunto(self, lista):
        for i in range(len(lista)):
            self.agregaElemento(lista[i])

    def getList(self):
        return self.__list

    def __add__(self, other):
        primera = self.getList()
        segunda = other.getList()
        tercera = segunda
        for i in range(len(primera)):
            if primera[i] not in segunda:
                tercera.append(primera[i])
        tercera.sort()
        return tercera

    def __sub__(self, other):
        conjunto = []

        for i in self.getList():
            if (i not in other.getList()):
                conjunto.append(i)
        return conjunto

    def __eq__(self, other):
        bandera = True
        if len(self.getList()) != len(other.getList()):
            bandera = False
        i = len(self.getList())-1
        while bandera and i >= 0:
            if self.getList()[i] not in other.getList():
                bandera = False
            else:
                i-=1
        return bandera


