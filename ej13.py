'''
Created on 22 nov 2022

@author: Juanan
'''

nombres=["Juan","Pepe","Juan","Antonio","Manuel","Jose","Lucia","Ana","Paula","Paloma", "Carla"]
def devolverNombres(lista,letra):
    try:
        listaDef=[]
        restricciones="1234567890!·$%&/()=?¿Çç*+^`¨´´';,.-_}{][|@#\ºª¬ "
        if letra in restricciones:
            listaDef="El segundo atributo debe ser una letra"
        else:
            for i in lista:
                if i[0].upper()==letra.upper():
                    listaDef.append(i)
        for i in lista:
            for x in range(len(i)):
                if i[x] in restricciones:
                    listaDef="Los nombres no pueden contener numeros"
    except:
        listaDef="Los nombres solo pueden contener caracteres alfabeticos A-Z"
    return listaDef

print(devolverNombres(nombres,"M"))

