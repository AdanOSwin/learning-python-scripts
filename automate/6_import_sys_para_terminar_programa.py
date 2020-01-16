import sys

name = input("Ingresar nombre: ")
time = 0

while(name!='Clara'):
    time = time + 1
    print('Nombre incorrecto!!')
    name = input('Ingresar nombre: ')
    if(time>=5):
        print('Demasiados  errores, saliendo del sistema')
        sys.exit()
