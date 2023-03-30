class Email:
    __idcuenta : str
    __dominio : str
    __tipodedominio : str
    __contrasena : str

    def __init__(self, id = None, dom= None, tipo= None, pasw='default'):
        self.__idcuenta = id
        self.__dominio = dom
        self.__tipodedominio = tipo
        self.__contrasena = pasw

    def __str__ (self):
        return f'{self.__idcuenta}@{self.__dominio}.{self.__tipodedominio}'

    def retornaEmail(self, id, dom, tipo):
        unEmail = Email(id, dom, tipo)
        return str(unEmail)

    def getDominio(self):
        return self.__dominio

    def getID(self):
        return self.__idcuenta

    def modificaContra(self):
        actual = input("Contraseña actual:   ")
        while(actual != self.__contrasena):
            print("contraseña incorrecta, vuelva a intentar")
            actual = input("Contraseña actual   ")
        else:
            self.__contrasena = input("contrseña nueva: ")
            print("Cambio de contraseña exitoso!")

    def crearcuenta(self, nueva):

        x = nueva.split('@')
        y = x[1].split('.')
        nueva = Email(x[0], y[0], y[1])
        return nueva
        
    def muestraEmail(self):
        return str(self)

