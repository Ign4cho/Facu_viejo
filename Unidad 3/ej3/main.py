import datetime
from datetime import timedelta
from claseManejadorEquipo import ManejadorEquipo
from claseManejadorJugador import ManejadorJugador
from claseManejadorContrato import ManejadorContrato


if __name__ == '__main__':
    me = ManejadorEquipo()
    mj = ManejadorJugador()
    mc = ManejadorContrato()

    me.testEquipos()
    car = 'si'
    while bool(car in ['si', 'Si', 'SI']):
        mj.crearJugador(mc, me)
        car = input('Continuar con la carga?')

    opc = 0
    while opc != 5:
        print('1-Consultar jugadores contratados\n2-Consultar contratos\n3-Obtener importes de contratos\n4-Guardar contratos\n5-Salir')
        opc = int(input('Opcion: '))
        if opc == 1:
            dni = input('Ingrese el dni del jugador que desea buscar: ')
            unContrato = mc.buscaDni(dni)
            if unContrato == 0:
                print('No se ha encontrado ningún jugador con ese dni')
            else:
                mc.muestraContrato(unContrato)
        elif opc == 2:
            eq = input('Equipo: ')
            unEquipo = me.buscarEquipo(eq)
            if unEquipo == 0:
                print('El equipo no se ha cargado')
            else:
                mc.listaJugadores(unEquipo)

        elif opc == 3:
            eq = input('Equipo: ')
            unEquipo = me.buscarEquipo(eq)
            if unEquipo == 0:
                print('El equipo no se ha cargado')
            else:
                suma = mc.sumaContratos(unEquipo)
                print(f'El importe total de los contratos es de {suma}')

        elif opc == 4:
            mc.guardarContratos()
        elif opc == 5:
            print('bye!')
        else:
            print('Opción incorrecta')



