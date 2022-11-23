'''
Created on 15 nov 2022

@author: Juanan
'''
lista=[]

def recibirNumero(lista,cont=0):
    while cont <10:        
        num=int(input("Introduzca un numero"))
        cont+=1
        lista.append(num)
    return lista

def obtenerMenorQueK(lista):
    for i in range(lista):
        if         