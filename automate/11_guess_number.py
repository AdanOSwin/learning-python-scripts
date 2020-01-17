import random
secreto = random.randint(1,20)
print("Estoy pensando en un numero entre 1 y 20")

##se pide que adivine 6 veces

for guesses in range(0,6):
    guess = int(input("Adivina el numero: "))

    if guess < secreto:
        print("El numero es menor al numero que tengo")
    elif guess > secreto:
        print("EL numero es mayor al numero que tengo")
    else:
        break ##Esta condicion es el numero correcto

if guess == secreto:
    print("Buen trabajo adivinaste el numero correcto!!: " + str(secreto))
else:
    print("No pudiste adivinar el numero correcto!!")
    print("El numero era: " + str(secreto))