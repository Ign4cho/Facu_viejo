from claseAparato import Aparato

class Nodo:
    __aparato = None
    __siguiente = None

    def __init__(self, unAparato):
        self.__aparato = unAparato
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__aparato


