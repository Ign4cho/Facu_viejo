from claseLista import Lista

class Menu:
    __opc: int

    def __init__(self):
        self.__opc = 0

    def muestraMenu(self):
        print('----Menu----')
        print('1- Insertar aparato en una posición determinada')
        print('2- Agregar aparato a la colección')
        print('3- Mostrar aparato que se encuentra en una posición')
        print('4- Cuenta aparatos de marca philips')
        print('5- Mostrar marca de lavarropas con carga superior a xKg')
        print('6- Mostrar todos los aparatos')
        print('7- Almacenar los objetos de la lista en un archivo JSON')
        print('8- Salir')

    def getOpc(self):
        opc = int(input('Opcion:'))
        while opc not in [1,2,3,4,5,6,7,8]:
            opc = int(input('Opción inconrrecta, intente nuevamente: '))
        return opc
