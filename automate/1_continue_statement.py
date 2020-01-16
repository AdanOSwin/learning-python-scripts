while True:
    name = input('Enter username: ')
    if name != 'Clara':
        continue
    print('Hi Clara, ¿what is the password? (its a fish) : ')
    password = input()
    if password == 'swordfish':
        print('Acceso concedido')
        break

print('Ten un buen día :)')