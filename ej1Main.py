'''
Created on 4 nov 2022

@author: Juanan
'''
from programacionModular.ej1 import obtenerMayor, obtenerMenor, obtenerSuma,\
    obtenerMedia, sustituirValor, lista
    
    #Creo el menu con una constante y lo imprimo
print("MENU PRINCIPAL")
MENU=   '''\t1. Conocer el mayor
        2. Conocer el menor
        3. Obtener la suma de todos los numeros
        4. Obtener la media
        5. Sustituir el valor de un elemento por otro numero introducido por teclado
        6. Salir'''
print(MENU)
opc=int(input("Introduzca la opcion que desee"))


#Creo la estructura de bucles y condicionales necesaria para interactuar con el menu
while opc!=0:
    if opc==1:
        print(obtenerMayor(lista))
    elif opc==2:
        print(obtenerMenor(lista))
    elif opc==3:
        print(obtenerSuma(lista))
    elif opc==4:
        print(obtenerMedia(lista))
    elif opc==5:
        print(sustituirValor(lista))
    elif opc==6:
        print()
        
    print(MENU)
    opc=int(input("Introduzca de nuevo la opcion que desee"))
    