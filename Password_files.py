# coding=utf-8
passwordFile = open('Password.txt')
secretPassword = passwordFile.read()
secretPassword = str(secretPassword)
print (secretPassword)
typedPassword = input("Ingresar contraseña: ")
##typedPassword = str(typedPassword)
if typedPassword == secretPassword:
    print ("Acceso concedido")
else:
    print ("Acceso denegado")
