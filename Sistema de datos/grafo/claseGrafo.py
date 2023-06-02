import numpy as np
from claseColaEnlazada import Cola
from clasePilaSec import Pila


class Grafo:
    __matriz: np.array

    def adyacentes(grafo: np.array, n1: int):
        ret = []
        for i in range(grafo.shape[0]):
            if grafo[n1][i] != 0:
                ret.append(i)

        return ret
    
    def __REA(g:np.array, s=0):
        """
        busqueda en amplitud, d es un arreglo auxiliar
        """ 
        c = Cola()
        d = np.zeros(g.shape[0])
        for i in range(g.shape[0]):
            d[i] = -1
        d[s] = 0
        c.insertar(s)               #iniciamos la cola con el vertice inicial
        while not c.vacia():
            v = c.suprimir()        
            for u in Grafo.adyacentes(g, v):        #visitamos todos los adyacentes del úlitmo vertice que sacamos de la cola
                if d[u] == -1:
                    d[u] = d[v]+1
                    c.insertar(u)                   #marcamos a los adyacentes que no hayan sido visitados y los ingresamos en la cola
        return d

    def REA(g: np.array, s=0):
        d = Grafo.__REA(g,s)
        for i in range(g.shape[0]):
            print(f'Distancia de {s} a {i} es {d[i]}')

    def conexo(g):
        d = Grafo.__REA(g, 0)
        ret = True
        for i in range(g.shape[0]):
            if d[i] < 0:
                ret = False
        return ret

    def REP(g:np.array, s=0):
        """
        busqueda en profunidad, d es un arreglo auxiliar, s vertice inicial, t es tiempos que se tarda en acceder a los vértices
        """
        d = np.zeros(g.shape[0])
        for i in range(g.shape[0]):
            d[i] = -1
        t = -1               #tiempo
        d = Grafo.REP_visita(g,s,d,t)
        for i in range(g.shape[0]):
            print(f'{i}, {d[i]}')

    def REP_visita(g, s:int, d: np.array, t:int):
        t = t+1
        d[s] = t
        for i in Grafo.adyacentes(g,s):
            if d[i] == -1:
                d = Grafo.REP_visita(g, i, d, t)
        return d
    
    def aciclico(g:np.array, s:int):        #s es el vertice inicial
        """
        Esto en grafos es díficil, aplicarlo en digrafos
        lo último que intenté es agregando un auxiliar anterior, pero tampoco anda mucho
        """
        ret = True
        visitados = []
        rec = Pila()
        visitados.append(s)
        rec.insertar(s)
        v = s
        while not rec.vacia():
            anterior = v
            v = rec.suprimir()
            for u in Grafo.adyacentes(g, int(v)):
                if u not in visitados:
                    visitados.append(u)
                    rec.insertar(u)
                elif u != anterior:
                    ret = False
        print(visitados)
        return ret
