'''
Created on 22 nov 2022

@author: Juanan
'''

lista1=[1,2,3,4,5,5,6,6,9,6,9,10,10]
lista2=[4,5,5,6,6,7,8,6,9,9,10,10]
def intersect(lista1,lista2):
    common=[]
    for i in lista1:
        if i in lista2 and i not in common:
            common.append(i)
    return common
#print(intersect(lista1,lista2))