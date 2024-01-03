
#----------------------------- Compresion Diccionarios ------------------------------------

#>>>>>>>>  Version 1 - agregar valor y clave del 1 -5 al diccionario vacio
dict1 = {}
# paises = ['peru','chile','bolivia','brasil','colombia']

for elemento in range(1,6):
    dict1[elemento] = elemento*2
print(dict1)

#>>>>>>>>  Version 2 - agregar valor y clave del 1 -5 al diccionario vacio
dict_2 = {elemento: elemento*2 for elemento in range(1,6)}
print(dict_2)


#>>>>>>>>  Version 3 - agregar valor y clave en el diccionario vacio por medio de la lista paises

from random import uniform, randint
paises = ['peru','chile','bolivia','brasil','colombia'] # una lista con paises
dict_3 = {} # el diccionario vacio

for elemento in paises:
    dict_3[elemento] = round(uniform(500.000, 600.000),3)
print(dict_3)

#>>>>>>>>  Version 4 - agregar valor y clave en el diccionario vacio por medio de la lista paises

dict_4 = {elemento: round(uniform(500.000,600.000),3) for elemento in paises}
print(dict_4)

#>>>>>>>>  Version 5 - Unir las 2 listas en clave-valor en el diccionario vacio por medio de la listas nombre y edad

nombres = ["Pedro", "adrian", "carlos", "jose"]
edades = [32,45,35,40]

dict_5 = dict(zip(nombres, edades)) # la funcion zip une dos listas, tuplas o diccionarios, em este caso esta uniendo 2 listas luego los convierte a diccionarios
# dict_5 = tuple(zip(nombres, edades)) # aqui es lo ,mismo pero los convierte en tupla
print(dict_5)

#>>>>>>>>  Version 6 - agregar valor y clave en el diccionario por medio de la listas nombre y edad

dict_6 = {name:age for (name,age) in zip(nombres,edades)} 
print(dict_6)


#>>>>>>>>  Version 7 - Unir las 2 listas en clave-valor en el diccionario vacio por medio de la listas nombre y edad

frutas = ['fresa', 'mandarina', 'naranja', 'platano']

""" 
peso = {}
for elemento in frutas:
    peso[elemento] = randint(100,200)
print(peso) 

"""
pesos = {elemento:randint(100,1000) for elemento in frutas} # aqui encontramos el peso de cada fruta

peso_mayor_500 = {fruta:peso for (fruta,peso) in pesos.items() if peso > 500 } # aqui solo muestra las frutas que pesan mas de 500

""" 
peso_mayor_500 = {}
for fruta, peso in pesos.items():
    if peso > 500:
        peso_mayor_500[fruta] = elemento 

"""
print(peso_mayor_500)


#>>>>>>>>  Version 8 - agregar los caracteres en el diccionario vacio con la condicion que sean vocales

texto = 'hola mundo, como estas'

letras = {elemento:elemento.upper() for elemento in texto if elemento in 'aeiou'}

""" 
for elemento in texto:
    if elemento in 'aeiou':
        letras[elemento] = elemento.upper() 
"""
        
print(letras)


