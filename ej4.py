'''
Created on 11 nov 2022

@author: Juanan
'''
lista=[]
n=0

def obtenerMayor(lista):
    mayor=lista[0]
    
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor=lista[i]
            
    return mayor;

def obtenerPar(lista):
    listapar=[]
    for i in range (len(lista)):
        if lista[i]%2==0:
            lista+=[lista[i]]
    return listapar

while n>=0:
    n=int(input("Introduzca los numeros que desees (negativo para acabar)"))
    lista+=[n]
    print(f"El mayor de la lista es {obtenerMayor(lista)}")
    print(f"Los pares de la lista son {obtenerMayor(lista)}")


