from claseGrafo import Grafo
import numpy as np

if __name__ == '__main__':
    g= np.array([[0,1,0,0,1,0],[1,0,1,1,0,0],[0,1,0,0,0,1], [0,1,0,0,0,1],[1,0,0,0,0,0],[0,0,1,1,0,0]])
    g2 = np.array([[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]])

    print(Grafo.aciclico(g, 0))
    print(Grafo.aciclico(g2, 0))

    
