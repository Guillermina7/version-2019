import random
def generador(minimo,maximo):
    return random.randint(minimo,maximo)

def generador_mejor(minimo,maximo,lista):
    encontrado = True
    while encontrado:
        aleatorio = random.randint(minimo,maximo)
        #O si no para hacerlo en 1 linea y no en las 3 de abajo: encontrado = aleatorio in lista
        encontrado=False
        if aleatorio in lista:
            encontrado=True
    return aleatorio