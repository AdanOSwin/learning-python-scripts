# coding=utf-8
passwordFile = open('Password.txt')
secretPassword = passwordFile.read()
print ('Ingresar contrasenia ')
typedPassword = input()
if typedPassword == secretPassword:
    print ('Acceso concedido')
    if(typedPassword == 'password12345'):
        print ('La contrasenia es demasiado debil')
else:
    print ('Acceso denegado')
