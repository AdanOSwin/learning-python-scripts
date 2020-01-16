name = input("Ingresar nombre: ")
edad = int(input("Ingresar edad: "))
if name == 'dracula' and edad >= 1000:
    print('Hola Vlad!!')
elif edad<12:
    print('Solo eres un niño')
elif edad>18 and edad<100:
    print('Ya eres grande pero no eres Vlad')
