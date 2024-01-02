
#----------------------------- Compresion Diccionarios ------------------------------------

#>>>>>>>>  Version 1 - agregar valor y clave del 1 -5 al diccionario vacio
dict = {}
# paises = ['peru','chile','bolivia','brasil','colombia']

for elemento in range(1,6):
    dict[elemento] = elemento*2
print(dict)

#>>>>>>>>  Version 2 - agregar valor y clave del 1 -5 al diccionario vacio
dict_2 = {elemento: elemento*2 for elemento in range(1,6)}
print(dict_2)


#>>>>>>>>  Version 3 - agregar valor y clave en el diccionario por medio de la lista

from random import uniform
paises = ['peru','chile','bolivia','brasil','colombia'] # una lista con paises
dict_3 = {} # el diccionario vacio

for elemento in paises:
    dict_3[elemento] = round(uniform(500.000, 600.000),3)
print(dict_3)

#>>>>>>>>  Version 4 - agregar valor y clave en el diccionario por medio de la lista

dict_4 = {elemento: round(uniform(500.000,600.000),3) for elemento in paises}
print(dict_4)

#>>>>>>>>  Version 5 - agregar valor y clave en el diccionario por medio de la listas nombre y edad

nombres = ["Pedro", "adrian", "carlos", "jose"]
edades = [32,45,35,40]

dict_5 = {}

for nombre in nombres:
    for edad in edades:
        dict_5[nombre]= edades[edad]
print(dict_5)