import random

def collatz(number):
    if(number%2==0):
        return number//2
    else:
        return (3*number) + 1
    

number = random.randint(1,100)
print("numero creado: ", number)
print(collatz(number))
