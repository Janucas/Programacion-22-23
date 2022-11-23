'''
Created on 22 nov 2022

@author: Juanan
'''

def inverso(cadena):
    inverso=""
    for i in range((len(cadena))-1,-1,-1):
        inverso+=str(cadena[i])
    return inverso
def convertirBIN(numero):
    conversion=0
    posicion=(len(numero))-2
    exponente=0
    try:
        if numero[-1]=="B":
            while posicion > -1:
                conversion+=int(numero[posicion])*(2**exponente)
                posicion-=1
                exponente+=1
            for i in range(len(numero)-1):
                if int(numero[i])!=0 and int(numero[i])!=1:
                    conversion="Los numeros binarios solo contienen 0 o 1"
        elif numero=="0D":
            conversion=0        
        elif numero[-1]=="D":
            entero=0
            entero=int(numero[0:len(numero)-1])
            binario=""
            while (entero!=0):
                binario+=str(entero%2)
                entero=entero//2
            conversion=inverso(binario)
        else:
            conversion="Introduce valores correctos (ej: 111B para binario-decimal o 256D para decimal-binario)"
    except:
        conversion="Introduce valores correctos (ej: 111B para binario-decimal o 256D para decimal-binario)"

    return conversion

print(convertirBIN(""))

