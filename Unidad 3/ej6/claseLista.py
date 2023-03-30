from claseAparato import Aparato
from claseNodo import Nodo
from zope.interface import Interface
from zope.interface import implementer
from interfaceLista import ILista
from claseHeladera import Heladera
from claseLavarropa import Lavarropa
from claseTelevisor import Televisor

@implementer(ILista)
class Lista:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None

    def agregarElemento(self, unAparato):
        nodo = Nodo(unAparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def insertarElemento(self, unAparato, pos):
        band = True
        contador = 0
        actual = self.__comienzo
        while contador < pos and actual is not None:
            contador+=1
            actual = actual.getSiguiente()
        if actual is None:
            band = False

        if band == False:
            print('La posición no se encuentra en el arreglo')
        else:
            if pos == 1:
                unNodo = Nodo(unAparato)
                unNodo.setSiguiente(actual)
                self.__comienzo = unNodo
                print('Carga exitosa')
            else:
                unNodo = Nodo(unAparato)
                unNodo.setSiguiente(actual.getSiguiente())
                actual.setSiguiente(unNodo)
                print('Carga exitosa')

    def mostrarElemento(self, pos):
        contador = 1
        actual = self.__comienzo
        while contador < pos and actual is not None:
            contador +=1
            actual = actual.getSiguiente()
        if actual == None:
            print('No hay ningún objeto en esa posición')
        else:
            unAparato = actual.getDato()
            print(f'En la posición {pos} se encuentra un {unAparato.getTipo()}')

    def crearAparato(self):
        print('Ingrese el tipo de aparato que quiere crear\n1- Heladera\n2- Televisor\n3- Lavarropa')
        opc = int(input('Opción: '))
        unAparato = None
        while opc not in [1,2,3]:
            opc = int(input('Opción incorrecta, ingrese una opción valida\n'))
        if opc == 1:
            unAparato = self.crearHeladera()
        elif opc == 2:
            unAparato = self.crearTelevisor()
        elif opc == 3:
            unAparato = self.crearLavarropa()
        return unAparato

    def crearHeladera(self):

        print('--------Heladera--------')
        mar = input('Marca: ')
        mod = input('Modelo: ')
        color = input('Color: ')
        pais = input('Pais: ')
        precio = input('Precio: ')
        cap = input('Capacidad (en kg): ')
        fr = input('Tiene freezer? ')
        cic = input('Es cíclica? ')
        return Heladera(mar,mod, color, pais, precio, cap, fr, cic)

    def crearTelevisor(self):

        print('--------Televisor--------')
        mar = input('Marca: ')
        mod = input('Modelo: ')
        color = input('Color: ')
        pais = input('Pais: ')
        precio = input('Precio: ')
        pan = input('Pantalla (crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch): ')
        pan = pan.lower()
        pul = input('Pulgadas: ')
        defi = input('Definición (SD, HD, FULL HD): ')
        defi = defi.upper()
        inte = input('Tiene acceso a internet? ')
        return Televisor(mar, mod, color, pais, precio, pan, pul, defi, inte)

    def crearLavarropa(self):

        print('------Lavarropa-------')
        mar = input('Marca: ')
        mod = input('Modelo: ')
        color = input('Color: ')
        pais = input('Pais: ')
        precio = input('Precio: ')
        cap = input('Capacidad en kg: ')
        vel = input('Velocidad en rpm: ')
        pr = input('Cantidad de programas: ')
        car = input('carga frontal o superior? ')
        return Lavarropa(mar,mod,color,pais,precio, cap, vel,pr,car)

    def cuentaMarca(self, marca = 'philips'):
        hel, tel, lav = 0, 0, 0
        actual = self.__comienzo
        while actual is not None:
            unAparato = actual.getDato()
            if unAparato.getMarca() == marca:
                if isinstance(unAparato, Heladera):
                    hel += 1
                elif isinstance(unAparato, Televisor):
                    tel += 1
                elif isinstance(unAparato, Lavarropa):
                    lav += 1
            actual = actual.getSiguiente()
        print(f'Apartos marca {marca}\nHeladeras: {hel}\nTelevisores: {tel}\nLavarropas: {lav}')

    def cargaSuperior(self, carga: int):
        actual = self.__comienzo
        print(f'Marca de los lavarropas con carga mayor a {carga}kg')
        while actual is not None:
            unAparato = actual.getDato()
            if isinstance(unAparato, Lavarropa):
                if unAparato.getCapacidad() > carga:
                    print(unAparato.getMarca())
            actual = actual.getSiguiente()

    def mostrarLista(self):
        actual = self.__comienzo
        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()

    def toJSON(self):
        lista = self.crearLista()
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[aparato.toJSON() for aparato in lista]
            )
        return d

    def crearLista(self):
        lista = []
        actual = self.__comienzo
        while actual is not None:
            lista.append(actual.getDato())
            actual = actual.getSiguiente()
        return lista
