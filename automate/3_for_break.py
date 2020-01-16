for i in range(0,9):
    name = input('Cual es tu nombre?: ')
    if(name == 'Clara'):
        print('Bienvenidoa señorita Oswald')
        break

for j in range(0,3):
    password = input('Hola ' + name + ' ingresa la contraseña: ')
    if(password!='tardis'):
        continue
    
##este for imprime hasta 10 en intervalos de 2
for i in range(0,12, 2):
    print(i)