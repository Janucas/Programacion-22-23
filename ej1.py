'''
Created on 4 nov 2022

@author: Juanan
'''


from random import randint

lista=[]

for i in range(10):
    lista.append(randint(0, 1000))
    
# print(lista)

def obtenerMayor(lista):
    mayor=lista[0]
    
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor=lista[i]
            
    return mayor;
# print("El mayor es ",obtenerMayor(lista))

def obtenerMenor(lista):
    menor=lista[0]
    
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor;
# print("El mayor es ",obtenerMenor(lista))

def obtenerSuma(lista):
    contador=0
    for i in range(len(lista)):
        contador+=lista[i]
    return contador;
#print(obtenerSuma(lista))

def obtenerMedia(lista):
    contador=0
    media=0
    for i in range(len(lista)):
        contador+=lista[i]
        media=contador/10
    return media;

def sustituirValor(lista_para_sustituir, elemento_buscar, elemento_sustituto):
    print(lista)
    for i in range(len(lista_para_sustituir)):
        if elemento_buscar==lista_para_sustituir[i]:
            lista_para_sustituir[i]=elemento_sustituto
    return lista_para_sustituir;

ns=int(input("Introduce el numero a sustituir: "))
sustituto=int(input("Introduce el sustituto"))

    
    
    
    
    
    
    