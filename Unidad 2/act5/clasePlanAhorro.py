

class PlanAhorro:
    __codigo: int
    __modelo: str
    __version: str
    __valor: int
    __CantidadCuotas: int              #este tiene que ser de clase
    __cuotasLicitar: int
    __valorCuota: float

    def __init__(self, cod, model, vers, val, cuotasTotal, cuotasLic):
        self.__codigo = cod
        self.__modelo = model
        self.__version = vers
        self.__valor = val
        self.__CantidadCuotas = cuotasTotal
        self.__cuotasLicitar = cuotasLic
        self.__valorCuota = (val/cuotasTotal) + val * 0.1

    def getCodigo(self):
        return self.__codigo

    def getModelo(self):
        return self.__modelo

    def getVersion(self):
        return self.__version

    def getValor(self):
        return self.__valor

    def getCuotasLic(self):
        return self.__cuotasLicitar

    def getValorCuota(self):
        return self.__valorCuota

    def modificaValor(self, nuevo):
        self.__valor = nuevo


    def actualizaValor(self):
        print(f'Codigo del plan: {self.getCodigo()}\nModelo: {self.getModelo()}\nVersión: {self.getVersion()}')
        nuevo = int(input("Ingrese el valor actual del vehículo:  "))
        self.modificaValor(nuevo)

    def modificaCuotasLic(self):
        nuevo = int(input('Ingrese la cantidad de cutotas necesarias para licitar: '))
        self.__cuotasLicitar = nuevo







