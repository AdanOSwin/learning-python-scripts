import random

spam = []
suma=0

final = random.randint(1,20)

for i in range(0,final):
    spam.append(random.randint(1,100))



print("################################################")
print(spam)

for i in range(0,final):
    suma = suma + spam[i] 
    print(suma)


print("La suma final es: " + str(suma))