import random

def collatz(number):
    if(number%2==0):
        return number//2
    else:
        return (3*number)+1


i = random.randint(1,1000)
while(i!=1):
    i = collatz(i)
    print(i)