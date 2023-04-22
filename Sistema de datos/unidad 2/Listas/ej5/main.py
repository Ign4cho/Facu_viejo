from clasePolinomio import Polinomio

if __name__ == '__main__':
    a = Polinomio(1,4,5,8,9,2)
    b = Polinomio(3,2,4,7,1)
    print(a)
    a.recorrer()
    c = a+b

    #c.recorrer()