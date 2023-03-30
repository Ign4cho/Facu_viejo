class Viajero:
    __num_viajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millas_acum: int

    def __init__ (self, id, dni, nom, ap, millas=0):
        self.__num_viajero = int(id)
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas_acum = int(millas)

    def __str__(self):
        return "%s %s %s %s %s" %(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def __gt__(self, other):
        retorno = False
        if self.cantidadTotaldeMillas() > other.cantidadTotaldeMillas():
            retorno = True
        return retorno

    def __add__(self, other: int):
        self.__millas_acum += other
        return  self.__millas_acum

    def __sub__(self, other:int):
        self.__millas_acum -= other
        return self.__millas_acum


    def cantidadTotaldeMillas (self):
        return self.__millas_acum

    def acumularMillas (self, nuevas):
        self.__millas_acum += nuevas
        print(f'Millas acumuladas acturaliado: {self.__millas_acum}')
        return self.__millas_acum


    def canjearMillas (self, canje):
        valorRetorno=-1
        if canje <= self.__millas_acum:
            self.__millas_acum -= canje
            valorRetorno = self.__millas_acum

        return valorRetorno







