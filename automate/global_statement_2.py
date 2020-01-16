def spam():
    global eggs
    eggs = 'spam' #esta es la global

def bacon():
    eggs = 'bacon' #esta es local


def ham():
    print(eggs) #imprimee la variable global

eggs = 42 ##esta es una variable global
spam()
print(eggs)