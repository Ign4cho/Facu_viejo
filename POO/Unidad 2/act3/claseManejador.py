import csv
from claseRegistro import Registro

class Manejador:

    def __init__(self):
        self.__lista = [[Registro for j in range(24)] for i in range(30)]

    def __str__(self):
        retorna = ""
        for Registro in self.__lista:
            retorna += str(Registro) + '\n'

        return retorna

    def testLista(self):
        archivo = open('mes.csv')
        reader = csv.reader(archivo)
        cont = 0
        bandera = True
        for linea in reader:
            if bandera:
                bandera = not bandera
            else:
                dia = int(linea[0])
                hora = int(linea[1])
                temp = float(linea[2])
                humedad = int(linea[3])
                presion = int(linea[4])
                unRegistro = Registro(temp, humedad, presion)
                self.cargaLista(unRegistro, dia-1, hora-1)
        archivo.close()

    def cargaLista(self, unReg: Registro, dia: int, hora: int):

        self.__lista[dia][hora] = unReg

    def muestraLista(self, dia:int):
        print(f"Dia {dia}")
        print(f'HORA    TEMPERATURA     HUMEDAD     PRESION')
        for i in range(24):

            print(f'{i+1}        {(self.__lista[dia-1][i].getTemp())}              {self.__lista[dia-1][i].getHum()}       {self.__lista[dia-1][i].getPres()}')

    def tempPromedio(self):
        acum = 0.0
        for hora in range(24):
            for dia in range(30):
                acum += self.__lista[dia][hora].getTemp()
            print(f'La temperatura promedio del mes para la hora {hora+1} es de {acum/30:.2f} grados')
            acum = 0.0
        print('fin')

    def valoresExtremos(self):
        minHum, minPres = [9999, -1, -1], [9999, -1, -1]
        maxHum, maxPres = [0, -1, -1], [0, -1, -1]
        minTemp, maxTemp = [100.0, -1, -1], [-100.0, -1, -1]

        for dia in range(30):
            for hora in range(24):
                if minHum[0] > self.__lista[dia][hora].getHum():
                    minHum = [self.__lista[dia][hora].getHum(), dia, hora]

                if maxHum[0] < self.__lista[dia][hora].getHum():
                    maxHum = [self.__lista[dia][hora].getHum(), dia, hora]

                if minPres[0] > self.__lista[dia][hora].getPres():
                    minPres = [self.__lista[dia][hora].getPres(), dia, hora]

                if maxPres[0] < self.__lista[dia][hora].getPres():
                    maxPres = [self.__lista[dia][hora].getPres(), dia, hora]

                if minTemp[0] > self.__lista[dia][hora].getTemp():
                    minTemp = [self.__lista[dia][hora].getTemp(), dia, hora]

                if maxTemp[0] < self.__lista[dia][hora].getTemp():
                    maxTemp = [self.__lista[dia][hora].getTemp(), dia, hora]
        print(f'El valor mínimo de humedad fue {minHum[0]} y se registró el día {minHum[1]+1} a la hora {minHum[2]+1}')
        print(f'El valor máximo de humedad fue {maxHum[0]} y se registró el día {maxHum[1]+1} a la hora {maxHum[2]+1}')
        print(f'El valor mínimo de presión fue {minPres[0]} y se registró el día {minPres[1]+1} a la hora {minPres[2]+1}')
        print(f'El valor máximo de presión fue {maxPres[0]} y se registró el día {maxPres[1]+1} a la hora {maxPres[2]+1}')
        print(f'La temperatura mínima registrada fue {minTemp[0]} y se registró el día {minTemp[1]+1} a la hora {minTemp[2]+1}')
        print(f'La temperatura máxima registrada fue {maxTemp[0]} y se registró el día {maxTemp[1]+1} a la hora {maxTemp[2]+1}')

    def opciones(self):
        i = 0
        while i != 4:
            print("\n\n\nSeleccione una opción:\n1-- Mostrar extremos de las variables\n2-- Indicar temperatura promeido mensual por hora\n3-- Mostrar variables según día\n4-- Salir ")
            i = int(input("Opción: "))
            if i == 1:
                self.valoresExtremos()
            elif i == 2:
                self.tempPromedio()
            elif i == 3:
                dia = int(input("Ignrese el día que quiere analizar: "))
                self.muestraLista(dia)
            elif i == 4:
                print("Ha salido del programa")
            else:
                print("Valor incorrecto intente nuevamente")
