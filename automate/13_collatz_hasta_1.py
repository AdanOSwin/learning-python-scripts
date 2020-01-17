##import random

def collatz(number):
    global suma
    suma = 0
    if(number%2==0):
        number = number//2
    else:
        number = (3*number) + 1
    return number


i = int(input("Ingresa un numero: "))
while(i!=1):
    i = collatz(i)
    print(i)