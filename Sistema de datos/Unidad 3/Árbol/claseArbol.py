from claseNodoArbol import Nodo

class Arbol:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None

    def iniciar(self, *args):
        for num in args:
            self.inserta(self.__raiz, Nodo(num))

    def inserta(self,nodo:Nodo, nuevo:Nodo):
        if self.__raiz == None:             #para la primera inserción en la raíz
            self.__raiz = Nodo(nuevo.getValor())
        elif nuevo.getValor() < nodo.getValor():
            if nodo.getIz() == None:
                nodo.setIz(nuevo)
            else:
                self.inserta(nodo.getIz(), nuevo)
        elif nuevo.getValor() > nodo.getValor():
            if nodo.getDe() == None:
                nodo.setDe(nuevo)
            else:
                self.inserta(nodo.getDe(), nuevo)
        else: 
            nodo.setCuenta(1)
    
    def hijo(self, hijo: int, padre:int): #unico problema, si ingresan dos veces la misma clave retorna true
        npadre = self.buscar(padre)
        if hijo == padre or npadre == None or self.hoja(padre):
            return False
        elif hijo < padre:
            iz = npadre.getIz()
            if iz is not None:
                if iz.getValor() == hijo:
                    return True
                else:
                    return self.hijo(hijo, iz.getValor())
            else:
                return False
        elif hijo > padre:
            de = npadre.getDe()
            if de is not None:
                if de.getValor() == hijo:
                    return True
                else:
                    return self.hijo(hijo, de.getValor())
            else:
                return False
    
    def padre(self, padre: int, hijo:int):
        return self.hijo(hijo, padre)

    def buscar(self, valor):
        ret = None
        actual = self.__raiz
        while ret == None and actual is not None:
            if valor == actual.getValor():
                ret = actual
            elif valor < actual.getValor():
                actual = actual.getIz()
            else:
                actual = actual.getDe()
        return ret
        
    def hoja(self, valor):
        n = self.buscar(valor)
        if n == None:
            ret = None          #no existe el nodo
        else:
            if n.getIz() == None and n.getDe() == None:
                ret = True
            else:
                ret = False
        return ret  
    
    def camino(self, padre, hijo):
        if self.hijo(hijo,padre):
            if hijo < padre:
                return str(self.buscar(padre).getValor())+'-'+ self.camino(self.buscar(padre).getIz().getValor(), hijo)
            else:
                return str(self.buscar(padre).getValor())+'-'+ self.camino(self.buscar(padre).getDe().getValor(), hijo)
        else:
            return str(hijo)
        
    def nivel(self, x):
        actual = self.__raiz
        ret = 0
        if x == self.__raiz.getValor():
            pass
        elif self.hijo(x, self.getRaiz().getValor()):
            while actual.getValor() != x:
                if actual.getValor() > x:
                    actual = actual.getIz()
                else:
                    actual = actual.getDe()
                ret +=1
        else:
            ret = None
        return ret
    
    
    def preorden(self, nodo:Nodo, re=''):
        re += f'{nodo.getValor()},'
        if nodo.getIz() != None:
            re = self.preorden(nodo.getIz(), re)
        if nodo.getDe() != None:
            re = self.preorden(nodo.getDe(), re)
        return re
   
    def postorden(self, nodo:Nodo, re=''):
        if nodo.getIz() != None:
            re = self.postorden(nodo.getIz(), re)
        if nodo.getDe() != None:
            re = self.postorden(nodo.getDe(), re)
        re += f'{nodo.getValor()},'
        return re
    
    def inorden(self, nodo: Nodo, re=''):
        if nodo.getIz() != None:
            re = self.inorden(nodo.getIz(), re)
        re += f'{nodo.getValor()},'
        if nodo.getDe() != None:
            re = self.inorden(nodo.getDe(), re)
        return re
    
    def getRaiz(self):
        return self.__raiz
