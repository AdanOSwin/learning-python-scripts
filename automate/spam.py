spam = int(input("Ingresar valor: "))

while(spam<1 or spam>3):
    spam = int(input('Ingresa un valor aceptable: '))
    continue

if(spam == 1):
    print('Hello')
elif(spam == 2):
    print('Howdy')
else:
    print('Greetings')

for i in range(2,10):
    print(i)