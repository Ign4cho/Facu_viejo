from claseManejador import Manejador
from claseConjunto import Conjunto

if __name__ == '__main__':

    lista1 = [1,3,7,9,13,16]
    lista2 = [3,1,7,9,16,13]

    conj1 = Conjunto()
    conj2 = Conjunto()
    conj1.generaConjunto(lista1)
    conj2.generaConjunto(lista2)


    print(f'Suma: {conj1 + conj2}')

    conj3 = Conjunto()
    conj4 = Conjunto()
    conj3.generaConjunto(lista1)
    conj4.generaConjunto(lista2)


    print(f'Resta: {conj3-conj4}')

    conj5 = Conjunto()
    conj6 = Conjunto()
    conj5.generaConjunto(lista1)
    conj6.generaConjunto(lista2)

    print(conj5==conj6)

