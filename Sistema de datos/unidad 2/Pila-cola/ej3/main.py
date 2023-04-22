from claseColaEnlazada import Cola
from random import random, randrange


if __name__ == '__main__':
    c = Cola()
    acumula = 0
    impresora = 0           #Se inicializa variable impresora en 0
    limiteTiempo = 120      #Limite de tiempo en minutos
    t = 0

    while t < limiteTiempo:
        if (random() < 0.2):                           #Si un float al azar es menor a 0.2 
            c.insertar([randrange(1,10), 0])           #se inserta un trabajo con un valor de timepo 
            print('ingreso un trabajo')                #entre 1 y 10, y tiempo de espera = 0 
        if impresora == 0:
            if not c.vacia():
                enCurso = c.suprimir()
                print(f'entra en impresora el trabajo {enCurso}')
                if enCurso[0] > 5:
                    impresora = 5                   #si el tiempo que tiene el trabajo es mayor a 5, le asignamos 5 tiempos de impresora
                else:
                    impresora = enCurso[0]
                
            else:
                print('La impresora y la cola están vacías :(')
        else:
            impresora -= 1                                  # si la impresora tiene un tiempo asignado, se decrementa
            enCurso = [enCurso[0]-1, enCurso[1]]            #también se decrementa el elemento que se está trabajando
            if impresora == 0 and enCurso[0] != 0:
                c.insertar(enCurso)                         
    

            if not c.vacia():
                c.aumentaValores()                                            # si hay elementos en la cola les aumenta el tiempo de espera


        t += 1
    
    print(f'Cantidad de trabajos sin atender {c.getCantidad()}')

    #falta el item b