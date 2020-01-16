def spam():
    eggs = 'spam local'
    print(eggs) ##imprime spam local

def bacon():
    eggs = 'bacon local'
    print(eggs) ##imprime bacon local
    spam()
    print(eggs) ##imprime bacon local


eggs = 'global'
bacon()
print(eggs) ##imprime global