class Cama:
    __idCama: int
    __habitacion: int
    __estado: bool
    __nombre: str
    __diagnostico: str
    __fechaInternacion: str
    __fechaAlta: str

    def __init__(self, idc, hab, est, nom, diag, internacion, alta = None):
        self.__idCama = int(idc)
        self.__habitacion = int(hab)
        self.__estado = bool(est == 'True')
        self.__nombre = nom
        self.__diagnostico = diag
        self.__fechaInternacion = internacion
        self.__fechaAlta = alta

    def cargaAlta(self, fecha):
        self.__fechaAlta = str(fecha)

    def getID(self):
        return self.__idCama

    def getHab(self):
        return self.__habitacion

    def getNom(self):
        return self.__nombre

    def getDiag(self):
        return self.__diagnostico

    def getFechaInt(self):
        return self.__fechaInternacion

    def getFechaAlta(self):
        return self.__fechaAlta
    
    def muestraPaciente(self):
        print(f'Paciente: {self.getNom()}   Cama: {self.getID()}    Habitación{self.getHab()}')
        print(f'Diagnostico: {self.getDiag()}       Fecha de internación:{self.getFechaInt()}')
        print(f'Fecha de alta: {self.getFechaAlta()}')
