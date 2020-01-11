import sys

while True:
    print("Ingresar exit para salir")
    respuesta = input()
    if respuesta == 'exit':
        sys.exit()
    print("Ingresaste la palabra: " + respuesta)

print("El programa ha terminado")