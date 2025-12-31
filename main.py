import random

numero_maximo=75
numeros_sorteados=[]

def sortear_numero(max):
    numero=0
    while numero in numeros_sorteados or not numero:
        numero=random.randint(1,numero_maximo)
    numeros_sorteados.append(numero)
    return numero

x=sortear_numero(numero_maximo)
print(x)
