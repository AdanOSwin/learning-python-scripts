import random

def pregunta(res):
    if res == 1:
        return 'Es seguro'
    elif res == 2:
        return 'Esta decidido'
    elif res == 3:
        return 'si'
    elif res == 4:
        return 'Intenta de nuevo'
    elif res == 5:
        return 'preguntame mas tarde'
    elif res == 6:
        return 'La respuesta es no'
    elif res == 7: 
        return 'Definitivamente'
    elif res == 8:
        return 'Suerte con eso'


##generas numero random
res = random.randint(1,9)

##mandas llamar la funcion y el resultado lo guardas en una variable
fortuna = pregunta(res)

##Imprimes el valor almacenado en la variable
print(fortuna)

print('###########################################333')

##otra manera mas pro de hacerlo
print(pregunta(random.randint(1,9)))