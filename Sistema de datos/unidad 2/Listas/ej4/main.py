"""
Las comparaciones en la suma las hago al revés porque la lista se carga al revés
"""

from claseListaSecuencialporContenido import ListaSecuencialporContenido as Lista

if __name__ == '__main__':
    a = Lista()
    b = Lista()
    
    prueba1 = [[1,1,5], [2, 3, 4], [3,2,5], [6,2,1]]
    prueba2 = [[1,2,5], [2, 1, 4], [3,4,5], [6,3,1]]
    prueba3 = [[1,3,5], [4, 3, 4], [5,2,5], [7,2,1]]
    
    for elemento in prueba3:
        a.insertar(elemento)
        b.insertar(elemento)
    for i in range(len(prueba3)):
        a.insertar(prueba1[i])
        b.insertar(prueba2[i])
    
    a.insertar([13,12,30])
    
    print('--------')
    
    c = a+b
    print('--------')
    c.recorrer()