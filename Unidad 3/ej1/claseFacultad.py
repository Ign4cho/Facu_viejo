from claseCarrera import Carrera

class Facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __provincia: str
    __telefono: str
    __carrera = []

    def __init__(self, cod, nom, dire, loc, prov, tel):
        self.__codigo = int(cod)
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = loc
        self.__provincia = prov
        self.__telefono = tel
        self.__carrera = []

    def agregaCarrera(self, unaCarrera):
        if isinstance(unaCarrera, Carrera):
            self.__carrera.append(unaCarrera)
        else:
            print("Tipo de dato incorrecto para la carga")

    def getLong(self):
        return len(self.__carrera)

    def getNom(self):
        return self.__nombre

    def getCod(self):
        return str(self.__codigo)

    def getDir(self):
        return self.__direccion

    def getDuracion(self):
        print(f'{self.getNom()}')
        for i in range(len(self.__carrera)):
            print(f'Carrera: {self.__carrera[i].getNom()}  Duracion: {self.__carrera[i].getDuracion()}')

    def buscaCarrera(self, nombreCarrera):
        i = 0
        bandera = True
        ret = 0
        while i < len(self.__carrera) and bandera:
            if self.__carrera[i].getNom() == nombreCarrera:
                bandera = False
                ret = self.__carrera[i]
            else:
                i+=1
        return ret

    def muestraCarrera(self, unaCarrera):
        bandera = True
        i = 0

