from claseArbol import Arbol

if __name__ == '__main__':
    a = Arbol()
    a.insertar(10)
    a.insertar(5)
    a.insertar(7)
    a.insertar(11)
    a.insertar(15)
    a.insertar(12)

    print(a.preorden(a.getRaiz(), ''))
    print(a.postorden(a.getRaiz(), ''))
    print(a.inorden(a.getRaiz(), ''))