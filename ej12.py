'''
Created on 22 nov 2022

@author: Juanan
'''


def unionListas(lista1,lista2):
    lista1.extend(lista2)
    union=[]
    for i in lista1:
        if i not in union:
            union.append(i)     
    return union

