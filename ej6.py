'''
Created on 22 nov 2022

@author: Juanan
'''

def esta_ordenada(lista):
    ordenada = True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            print(f"Comparación número {i+1}")
            ordenada = False
        
    return ordenada

def esta_ordenada_while(lista):
    ordenada = True
    i = 0
    while i < len(lista)-1 and ordenada:
        if lista[i] > lista[i+1]:
            print(f"Comparación número {i+1}")
            ordenada = False        
        i+=1
        
    return ordenada

from random import randint
lista_numeros = []
for i in range(2000000):
    lista_numeros.append(randint(0, 10))

assert(not esta_ordenada_while(lista_numeros))
print(lista_numeros[0:200])
assert(esta_ordenada([1, 3, 5, 9]))
assert(not esta_ordenada([1, 13, 5, 9]))
assert(esta_ordenada([1]))
assert(esta_ordenada([]))
print("Todo correcto")

