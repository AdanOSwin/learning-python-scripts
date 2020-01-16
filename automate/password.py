password = open('password.txt')
contra = password.read()
print(contra)
print("#########################################################33")
contra2 = input("Ingresar contraseña: ")
if(contra == contra2):
    print("Acceso concedido")
else:
    print("Acceso denegado")