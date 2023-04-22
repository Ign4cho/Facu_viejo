from claseManejadorTorres import ManejadorTorres

if __name__ == '__main__':
    mt = ManejadorTorres(5)
    mt.mostrarTorres()
    aux = '1'
    valido = ['a', 'A', "b", 'B', 'c', 'C', '0']
    while aux != '0':
        llegada = '1'
        while not(aux in valido):
            aux = input('De que torre quiere sacar un disco? ')
        
        if aux == 0:                                        #para que no entre en el input del disco de salida
            llegada = 'a'
        while (llegada not in valido) or (llegada == '0'):
            llegada = input('En que torre quiere poner el disco? ')
        

        if mt.cambio(aux, llegada):                         #solo muestra las torres si se realizó un cambio
            mt.mostrarTorres()
        if aux != 0:
            aux = '1'

    print('Salida')

