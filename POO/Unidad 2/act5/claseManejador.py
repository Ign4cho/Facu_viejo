import csv
from clasePlanAhorro import PlanAhorro

class Manejador:

    def __init__(self):
        self.__lista = []

    def testPlanes(self):

        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')

        for fila in reader:
            cod = int(fila[0])
            mod = fila[1]
            ver = fila[2]
            val = int(fila[3])
            cant = int(fila[4])
            lic = int(fila[5])
            unPlan = PlanAhorro(cod, mod, ver, val, cant, lic)

            self.agregarPlan(unPlan)
        archivo.close()

    def agregarPlan(self, unPlan):
        if (type(unPlan)) == PlanAhorro:
            self.__lista.append(unPlan)
        else:
            print('Error en la carga')

    def valorMenor(self):
        compara = int(input("Ingrese un valor para comparar: "))
        for plan in self.__lista:
            if compara > plan.getValor():
                print(f'Codigo del plan: {plan.getCodigo()}\nModelo: {plan.getModelo()}\nVersión: {plan.getVersion()}\n\n')


    def mostrarMontoLicitacion(self):
        for plan in self.__lista:
            print(f'Para licitar un {plan.getModelo()} {plan.getVersion()} es necesario pagar ${plan.getCuotasLic()*plan.getValorCuota():.2f}')

    def actulizaValorPlanes(self):
        for plan in self.__lista:
            plan.actualizaValor()
        print('Actualización exitosa')

    def modificaLicitacion(self):
        cod = int(input('Ingrese el código del plan que quiere modificar: '))
        bandera = True
        i=0
        while bandera and i in range(len(self.__lista)):
            if self.__lista[i].getCodigo() == cod:
                self.__lista[i].modificaCuotasLic()
                bandera = False
                print("Se ha actualizado la cantidad de cuotas con éxito")
            else:
                i+=1

        if bandera:
            print("El codigo no corresponde a ningun plan")



