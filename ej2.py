'''
Created on 9 nov 2022

@author: Juanan
'''

def imprimirLista():
    lista=[]
    contador=0
    while contador<10:
        num=int(input("Introduce un numero"))
        contador+=1
        lista.append(num)
        
    print(lista)
    
    lista=[1,3,5,7]
    
    a_borrar, a_escribir=0, lista[0]
    
    for i in range(len(lista)):
        a_borrar=lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=a_escribir
        a_escribir=a_borrar