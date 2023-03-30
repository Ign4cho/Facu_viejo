from claseCama import Cama
import csv

class ManejadorCama:
    __listaCamas = []

    def __init__(self):
        self.__listaCamas = []

    def testListaCama(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                idc = linea[0]
                hab = linea[1]
                est = linea[2]
                nom = linea[3]
                diag = linea[4]
                intern = linea[5]
                alta = linea[6]
                unaCama = Cama(idc,hab,est,nom,diag,intern,alta)
                self.cargaCama(unaCama)

    def cargaCama(self, unaCama):
        if type(unaCama) == Cama:
            self.__listaCamas.append(unaCama)

        else:
            print("Error de tipos en la carga.")


    def buscaPaciente(self):
        nombre = input('Ingrese el nombre del paciente que desea buscar. (Apellido, Nombre)\n ')
        bandera = True
        i = len(self.__listaCamas)-1
        retorno = 0
        while i >= 0 and bandera:
            if nombre == self.__listaCamas[i].getNom():
                retorno = self.__listaCamas[i]
                bandera = False
            else:
                i -= 1
        return retorno

    def darAlta(self):
        paciente = self.buscaPaciente()
        ret = 0
        if type(paciente) == Cama:
            paciente.cargaAlta('09/05/2022')
            paciente.muestraPaciente()
            ret = paciente.getID()
        else:
            print("No se encontró el paciente")
        return ret


    def listaPacientes(self):
        diagnostico = input('Ingrese el diagnostico que desea buscar ')
        for pac in self.__listaCamas:
            if diagnostico == pac.getDiag():
                print(f'Paciente: {pac.getNom()}')


