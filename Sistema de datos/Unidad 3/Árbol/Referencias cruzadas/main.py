from claseArbol import Arbol

if __name__ == '__main__':
    a = Arbol()
    archivo = open('texto.txt', 'r')
    texto = archivo.read()
    texto = texto.lower()
    renglon = texto.split('\n')
    i=1
    for line in renglon:
        a.iniciar(i, line.split())
        i+=1

    print(a.inorden(a.getRaiz()))