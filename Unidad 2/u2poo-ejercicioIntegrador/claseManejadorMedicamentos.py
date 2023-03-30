from claseMedicamento import Medicamento
import csv


class ManejadorMedicamento:

    __listaMed = []

    def __init__(self):
        __listaMed = []

    def testMedicamentos(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                idC = linea[0]
                idM = linea[1]
                nom = linea[2]
                monod = linea[3]
                pres = linea[4]
                cant = linea[5]
                precio = linea[6]
                unMed = Medicamento(idC, idM, nom, monod, pres, cant, precio)
                self.cargaMedicamento(unMed)
        archivo.close()

    def cargaMedicamento(self, unMedicamento):
        if type(unMedicamento) == Medicamento:
            self.__listaMed.append(unMedicamento)

        else:
            print('Error de tipos en la carga.')

    def muestraMedicamentos(self, idCama):
        print('Medicamento          Presentación           Cantidad           Precio')
        totalAdeudado = 0
        for i in range(len(self.__listaMed)):
            if self.__listaMed[i].getIDCama() == idCama:
                unMed = self.__listaMed[i]
                print(f'{unMed.getNom()}        {unMed.getPres()}                   {unMed.getCant()}             {unMed.getPrecio()}')
                totalAdeudado += unMed.getPrecio() * unMed.getCant()
        print(f'Total Adeudado: {totalAdeudado}')

        
