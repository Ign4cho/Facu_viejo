from claseManejaFacultades import ManejaFacultades

if __name__ == '__main__':
    mf = ManejaFacultades()
    mf.lecturaArchivo()
    opcion = 0
    while opcion != 3:
        print('1 - Buscar Facultad\n2 - Buscar Carrera\n3 - Salir')
        opcion = int(input('Opción: '))
        if opcion == 1:
            fac = input('Ingrese la facultad que desea buscar: ')
            unaFacultad = mf.buscaFacultad(fac)
            if unaFacultad == 0:
                print('No se ha cargado una facultad con ese nombre')
            else:
                mf.muestraFac(unaFacultad)
        elif opcion == 2:
            car = input('Ingrese la carrera que quiere buscar: ')
            unaCarrera = mf.buscaCarrera(car)
            if unaCarrera == 0:
                print('No se ha cargado una facultad con ese nombre')
            else:
                mf.muestraCarrera(unaCarrera)
        elif opcion == 3:
            print('Goodbye!')
        else:
            print('Opción incorrecta, intente nuevamente\n\n')
