from claseLista import Lista
from claseMenu import Menu
import json
from claseObjectEncoder import ObjectEncoder
if __name__ == '__main__':
    jsonF = ObjectEncoder()
    lista = Lista()
    d = jsonF.leerJSONArchivo('aparatoselectronicos.json')
    lista = jsonF.decodificarDiccionario(d)
    print('Lista cargada')
    bandera = True
    menu = Menu()
    while bandera:
        menu.muestraMenu()
        opc = menu.getOpc()
        if opc == 1:
            unAparato = lista.crearAparato()
            pos = int(input('En que posición quiere agregar el aparato: '))
            lista.insertarElemento(unAparato, pos)
        elif opc == 2:
            unAparato = lista.crearAparato()
            lista.agregarElemento(unAparato)
        elif opc == 3:
            pos = int(input('Que posición quiere ver: '))
            lista.mostrarElemento(pos)
        elif opc == 4:
            lista.cuentaMarca()
        elif opc == 5:
            carga = int(input('Carga: '))
            lista.cargaSuperior(carga)
        elif opc == 6:
            lista.mostrarLista()
        elif opc == 7:
            d = lista.toJSON()
            jsonF.guardarJSONArchivo(d,'aparatoselectronicos.json')
        elif opc == 8:
            bandera = False
            print('goodbye')

