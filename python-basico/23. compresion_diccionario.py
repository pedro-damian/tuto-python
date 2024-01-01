
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