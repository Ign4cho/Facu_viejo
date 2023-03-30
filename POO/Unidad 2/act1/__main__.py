import csv
from claseEmail import Email

def cargarMail(listaMails, mail):
    unEmail = Email()
    nuevoMail = unEmail.crearcuenta(mail)
    listaMails.append(nuevoMail)



if __name__ == '__main__':
    id = input("ingrese id: ")
    dom = input("ingrese dom: ")
    tipdom = input("ingrese tipdom: ")
    pasw = input("ingrese contraseña: ")
    unEmail=Email(id,dom,tipdom,pasw)

    nom = input("ingrese nombre: ")
    cuenta = input("ingrese su correo:  ")
    otroMail = unEmail.crearcuenta(cuenta)

    print(f'estimado {nom} te enviaremos tus correos a la dirección {otroMail}')

    print('--Cambio de contraseña--')
    print('Recuerde que la contraseña por defecto es: default')
    otroMail.modificaContra()


    listaMails = []
    rep = 0
    archivo = open('emails_csv.txt')
    reader = csv.reader(archivo)
    for fila in reader:
        cargarMail(listaMails, fila[0])
    idAbuscar =input("ingrese el identificador que quiere buscar     ")
    for mail in listaMails:
        if idAbuscar == mail.getID():
            rep+=1
    if rep > 1:
        print(f'El identificador se repite {rep} veces')
    else:
        print('El identificador no se repite')












