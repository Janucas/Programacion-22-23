'''
Created on 18 nov 2022

@author: Juanan
'''
from pickle import FALSE
from _ast import Or

ficha_1="[6,0]"
ficha_2="[2,3]"

print(ficha_1[1] in "0123456")
#print (MINIMO<= int(ficha_1[3]) <=MAXIMO)

def es_valida(ficha):
    resultado= False
    if len(ficha)==5 and ficha[1] in "0123456" and ficha[3] in "0123456":
        resultado= True
    return resultado;

ficha_1= "[1,2]"
ficha_2= "[2,3]"

def fichas_encajan(ficha_1, ficha_2):
    if ficha_1[1]==ficha_2[1] or ficha_1[1]==ficha_2[1] or ficha_1[3]==ficha_2[1] or ficha_1[3]==ficha_2[3]:
        print(True)
        
