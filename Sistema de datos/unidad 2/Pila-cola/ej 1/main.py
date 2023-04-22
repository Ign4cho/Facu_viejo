from clasePilaSecuencial import Pila

def factorial(n: int, p: Pila):
    print(n)
    while n != 0:
        p.insertar(n)
        
        n-=1
    ret = 1
    while (not(p.vacia())):
        aux = p.suprimir()
        print(f'{aux}*{ret}={aux*ret}')
        ret *= aux
    return ret

if __name__ == '__main__':
    p = Pila()
    n = int(input('Ingrese n: '))
    print(factorial(n,p))
    p.recorrer()

