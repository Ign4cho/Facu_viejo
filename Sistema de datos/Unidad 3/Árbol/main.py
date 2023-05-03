from claseArbol import Arbol

if __name__ == '__main__':
    a = Arbol()
    a.iniciar(12,7,16,3,9,14,19,18,23)
    print('Prueba muestra preorden, postorden e inorden:')
    print(a.preorden(a.getRaiz()))
    print(a.postorden(a.getRaiz()))
    print(a.inorden(a.getRaiz()))

    print('\n\nPrueba hijo y camino:')
    for i in range(25):
        for j in range(25):
            if a.padre(i, j):
                print(f'{i} es padre de {j}')
                print(a.camino(i,j))

    print('\n\nPrueba Hoja')
    for i in range(25):
        if a.hoja(i):
            print(f'{i} es hoja')

    print('prueba nivel')
    for i in range(25):
        if a.buscar(i) is not None:
            print(f'el nivel de {i} es {a.nivel(i)}')
