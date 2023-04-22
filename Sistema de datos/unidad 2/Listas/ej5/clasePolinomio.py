from ListaEPorPosicion import Lista

class Polinomio:
    __grado: int
    __coeficientes: Lista

    def __init__(self, *args) -> None:
        self.__grado = -1
        self.__coeficientes = Lista()
        for numero in args:
            self.__coeficientes.insertar(numero, self.__coeficientes.getTamaño())
            self.__grado+=1
            

    def __str__(self) -> str:
        ret = ''
        for i in range(self.__grado+1):
            ret = f'{self.__coeficientes.recuperar(i)}X^{i} '+ ret
        return ret

    def getGrado(self):
        return self.__grado

    def cargar(self, *args):
        for numero in args:
            self.__coeficientes.insertar(numero, self.__coeficientes.getTamaño())
            self.__grado+=1

    def getCoeficiente(self, i):
        ret = 0
        if i <= self.getGrado():
            ret = self.__coeficientes.recuperar(i)
        return ret
    
    def __add__(self, other):
        nuevo = Polinomio()
        for i in range(max(self.getGrado(), other.getGrado())+1):
            coef = self.getCoeficiente(i) + other.getCoeficiente(i)
            nuevo.cargar(coef)

        return nuevo


    def recorrer(self):
        self.__coeficientes.recorrer()