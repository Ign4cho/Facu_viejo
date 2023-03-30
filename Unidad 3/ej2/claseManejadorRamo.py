from claseRamo import Ramo
from claseManejadorFlor import ManejadorFlor

class ManejadorRamo:
    __lista=[]

    def __init__(self):
        self.__lista = []

    def agregaRamo(self, unRamo):
        if isinstance(unRamo, Ramo):
            self.__lista.append(unRamo)

    def registraRamo(self, mf: ManejadorFlor):

        cant = int(input('Ingrese la cantidad de flores del ramo (de 1 a 4): '))
        while cant != 0:
            unRamo = Ramo(cant)
            if cant in [1,2,3,4]:
                for i in range(cant):
                    num = int(input('Ingrese el número de la flor que va a agregar: '))
                    unaFlor = mf.buscaFlor(num)
                    if unaFlor == 0:
                        print('El numero de flor es incorrecto.')
                        i -= 1
                    else:
                        unRamo.cargaFlor(unaFlor)
                self.__lista.append(unRamo)
            else:
                print('Valor incorrecto')

            cant = int(input('Ingrese la cantidad de flores del ramo (de 1 a 4): '))

    def cuentaFlores(self, mf: ManejadorFlor):
        lista = mf.creaLista()
        for ramo in self.__lista:
            lista = ramo.cuentaFlores(lista)
        orden = sorted(lista, key=lambda l:l[1], reverse=True)

        mf.muestraFlores(orden)

    def floresVendidas(self, cant):
        print(f'En los ramos con {cant} flores, se vendieron:')
        for ramo in self.__lista:
            if ramo.getTamano() == cant:
                ramo.muestraFlores()





