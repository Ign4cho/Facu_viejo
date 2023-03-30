from claseManejadorFlor import ManejadorFlor
from claseManejadorRamo import ManejadorRamo

if __name__ == '__main__':
    mf = ManejadorFlor()
    mr = ManejadorRamo()

    mf.testFlores()
    opc = 0
    while opc != 4:
        print('1-Carga Ramo\n2-Flores mas vendidas\n3-Mostrar flores para tamaño de ramo\n4-Salir')
        opc = int(input('Opcion: '))
        if opc == 1:
            mr.registraRamo(mf)
        elif opc == 2:
            mr.cuentaFlores(mf)
        elif opc == 3:
            ramo = int(input('Ingresa tamaño de ramo: '))
            if ramo in [1,2,3,4]:
                mr.floresVendidas(ramo)
            else:
                print('Valor incorrecto')
        elif opc == 4:
            print('Goodbye')
        else:
            print('Opción incorrecta, intente de nuevo')
