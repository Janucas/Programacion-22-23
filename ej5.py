'''
Created on 22 nov 2022

@author: Juanan
'''

#lista=["Di","Buen","DIA","a","papa"]

def invertir(lista):
    listainvertida=[]
    for i in range(len(lista)-1,-1,-1):
        listainvertida.append(lista[i])
    return listainvertida

#print(invertir(lista))
