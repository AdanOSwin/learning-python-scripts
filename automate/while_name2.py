name = input("¿cual es tu nombre?: ")
times = 0

while(name!='Clara'):
    print("Tu no eres Clara!!")
    name = input("¿Cual es tu nombre?: ")
    times = times + 1
    if(times==5):
        print("Jodanse, yo me voy .|.")
        break

print("Clara!!!!, Vamos a la Tardis, los Daleks estan cerca")