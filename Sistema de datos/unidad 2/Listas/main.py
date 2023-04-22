from claseListaSecuencialporContenido import ListaSecuencialporContenido as Lista

if __name__ == '__main__':
    a = Lista()
    for i in range(15):
        a.insertar(i*3)
    
    print(a)