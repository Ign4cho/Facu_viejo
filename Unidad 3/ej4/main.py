from claseManejadorCalefactor import ManejadorCalefactor
from claseCalefactor import Calefactor

if __name__ == '__main__':

    cant = int(input('Ingrese la cantidad de calefactores del arreglo (8): '))
    mc = ManejadorCalefactor(cant)

    mc.testCalefactores()
    costogas = int(input('Ingrese el costo por m^3: '))
    metros = int(input('Ingrese la cantidad de m^3: '))
    mc.setCostoGas(costogas)

    unGas = mc.menorCostoGas(costogas, metros)

    print(f'Menor consumo de gas\nMarca: {unGas.getMarca()}\nModelo: {unGas.getModelo()}')

    costoKilo = int(input('Ingrese el costo del kw/hora: '))
    mc.setCostoKilo(costoKilo)

    unElectrico = mc.menorCostoElectrico(metros, costoKilo)

    print(f'Menor consumo de electricidad\nMarca: {unElectrico.getMarca()}\nModelo: {unElectrico.getModelo()}')

    mc.mostrarMenor(unGas, unElectrico, metros, costoKilo, costogas)



