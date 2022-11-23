'''
Created on 22 nov 2022

@author: Juanan
'''

cadenas=["Uni","Doni","Treni","Catuni","Doni","Treni","Catuni","Quini","Quineta","El","Rey"]

def buscarLarga(cadena):
    caracteres2=0
    cadenalarga=""
    comparador=[]
    repetidos=0
    repetidos2=0
    for i in cadena:
        caracteres=len(i)
        if caracteres > caracteres2:
            caracteres2=caracteres
            cadenalarga=i
    for i in cadena:
        if len(cadenalarga) == len(i):
            comparador.append(i)
    for i in comparador:
        repetidos=0
        for x in range(len(i)):
            for z in range(1,len(i)):
                if i[x]==i[z]:
                    repetidos+=1
        if repetidos > repetidos2:
            repetidos2=repetidos
            palabra=i
    return palabra

print(buscarLarga(cadenas))