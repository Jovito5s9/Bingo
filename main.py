import random

numero_maximo=75
numeros_por_letra=numero_maximo/5
numeros_sorteados=[]

def sortear_numero(max):
    numero=0
    while numero in numeros_sorteados or not numero:
        numero=random.randint(1,numero_maximo)
    numeros_sorteados.append(numero)
    return numero

def descobrir_letra(numero):
    letras="BINGO"
    letra= int(numero / numeros_por_letra)
    return letras[letra]

x=sortear_numero(numero_maximo)
print(x)
letra=descobrir_letra(x)
print(letra)
