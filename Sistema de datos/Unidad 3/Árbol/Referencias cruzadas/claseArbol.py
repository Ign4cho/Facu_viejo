from claseNodoArbol import Nodo

class Arbol:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None

    def iniciar(self, i, linea):
        for palabra in linea:
            self.inserta(self.__raiz, Nodo(palabra, i), i)

    def inserta(self,nodo:Nodo, nuevo:Nodo, i):
        if self.__raiz == None:             #para la primera inserción en la raíz
            self.__raiz = Nodo(nuevo.getValor(), i)
        elif nuevo.getValor() < nodo.getValor():
            if nodo.getIz() == None:
                nodo.setIz(nuevo)
            else:
                self.inserta(nodo.getIz(), nuevo,i)
        elif nuevo.getValor() > nodo.getValor():
            if nodo.getDe() == None:
                nodo.setDe(nuevo)
            else:
                self.inserta(nodo.getDe(), nuevo,i)
        else: 
            nodo.setCuenta(i)

    def suprimir(self, valor):
        actual, anterior = self.__raiz, self.__raiz
        while actual.getValor() != valor:
            """ Hacemos Caminar """
            if valor < actual.getValor():
                anterior = actual
                actual = actual.getIz()
            else: 
                anterior = actual
                actual = actual.getDe()
        if actual == self.__raiz:
            """ El nodo a suprimir es la raiz"""
            
            sust = self.__sustituto(actual)
            self.suprimir(sust.getValor())
            self.__enganchar(sust, actual)
            self.__raiz = sust

        elif self.hoja(actual.getValor()):
            """ caso que el nodo sea una hoja """
            if actual.getValor() < anterior.getValor():
                anterior.setIz(None)
            else:
                anterior.setDe(None)
        
        elif actual.getDe() is not None and actual.getIz() is not None:
            """ caso que tenga dos hijos """
            sust = self.__sustituto(actual)

            if actual.getValor() < anterior.getValor():
                """ a la izq del anterior """
                anterior.setIz(sust)
            else:
                """ a la der del anterior"""
                anterior.setDe(sust)
            self.__enganchar(sust, actual)
            

        else:
            """ Caso que tenga un solo hijo """
            if actual.getValor() < anterior.getValor():
                """ estamos a la izquierda del anterior"""
                if actual.getDe() == None:
                    anterior.setIz(actual.getIz())
                else:
                    anterior.setIz(actual.getDe())
            else: 
                """ estamos a la derecha del anterior"""
                if actual.getDe() == None:
                    anterior.setDe(actual.getIz())
                else:
                    anterior.setDe(actual.getDe())  
        

          
    def __enganchar(self, nuevo:Nodo, viejo:Nodo):
        """         Método auxiliar para el suprimir            """
        """ Le da al sustituto los hijos del nodo que se suprime"""
        if viejo.getIz() != nuevo:
            nuevo.setIz(viejo.getIz())
        else:
            if not self.hoja(nuevo.getValor()):
                nuevo.setIz(nuevo.getIz())
        """ el sustituto puede ser el nodo a la izquierda del nodo a sustituir, pero nunca el hijo derecha"""
        nuevo.setDe(viejo.getDe())

    
    def hijo(self, hijo: str, padre:str): #unico problema, si ingresan dos veces la misma clave retorna true
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
    
    def padre(self, padre: str, hijo:str):
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
        re += f'{nodo.getValor()} - {nodo.getCuenta()}\n'
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
        re += f'{nodo.getValor()} - {nodo.getCuenta()}\n'
        return re
    
    def inorden(self, nodo: Nodo, re=''):
        if nodo.getIz() != None:
            re = self.inorden(nodo.getIz(), re)
        re += f'{nodo.getValor()} - {nodo.getCuenta()}\n'
        if nodo.getDe() != None:
            re = self.inorden(nodo.getDe(), re)
        return re
    
    def getRaiz(self):
        return self.__raiz
    
    def __sustituto(self, nodo: Nodo):
        """ Si buscamos sustituto, sabemos que el nodo a sustituir tiene izquierda y derecha"""
        """ el nodo sustituto o es hoja, o tiene un hijo a la izquierda solamente"""
        nodo = nodo.getIz()
        while nodo.getDe() != None:
            nodo = nodo.getDe()
        return nodo
