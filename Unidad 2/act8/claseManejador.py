from claseConjunto import Conjunto

class Manejador:

    def generaConjunto(self, lista):
        unConjunto = Conjunto()
        for num in lista:
            unConjunto.agregaElemento(num)
        return unConjunto

