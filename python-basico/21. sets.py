
# CONJUNTOS
# son mutables
# no puede tener elementos duplicados

paises = {'peru','chile','bolivia','brasil'}
print(paises)           # muestra los elementos del conjunto paises
print(type(paises))     # muestra el tipo de estructura de dato --> set

numeros = {1,2,3,4,5,6,45,67,8}
print(numeros)           # muestra los elementos del conjunto numeros
print(type(numeros))     # muestra el tipo de estructura de dato --> set

combinado = {'pedro', 45.6, 'juan', -30, 'A', True, False}
print(combinado)           # muestra los elementos del conjunto
print(type(combinado))     # muestra el tipo de estructura de dato --> set

#>>>>>>>>>>>>>>>>>>>> convertir de string (cadena) a sets (conjunto) <<<<<<<<<<<<<<<<<<<<<<

letras = set('hola mundo')
print(letras)

#>>>>>>>>>>>>>>>>>>>> convertir tuplas a sets (conjunto) <<<<<<<<<<<<<<<<<<<<<<

nombres = ("Pedro", "adrian", "carlos", "jose")
set_nombres = set(nombres)
print(set_nombres)
print(type(set_nombres))

#>>>>>>>>>>>>>>>>>>>> convertir listas a sets (conjunto) <<<<<<<<<<<<<<<<<<<<<<

lista_numeros = [1,2,3,4,5,6,7,8,45,90]
set_numeros = set(lista_numeros)
print(set_numeros)


#>>>>>>>>>>>>>>>>>>>> CRUD Sets <<<<<<<<<<<<<<<<<<<<<<

tamaño = len(paises) # calcula el N° de elementos dentro del conjunto
print(tamaño)

buscar = 'col' in paises # devuelve un booleano si el elemento se encuentra en el conjunto
print(buscar)

paises.add('colombia') # añade 1 nuevo elemento al conjunto
print(paises)

paises.update(['EEUU','Mexico','Canada']) # añade varios nuevos elementos al conjunto
print(paises)

paises.remove('EEUU') # elimina un elemento existente de un conjunto de lo contrario mostrara un ERROR
print(paises)

paises.discard('EEUU') # elimina un elemento existente de un conjunto en este caso no mostrara un ERROR si en caso el elemento no existe en el conjunto
print(paises)

paises.clear() # elimina todos los elementos de un conjunto
print(paises)

#>>>>>>>>>>>>>>>>>>>> Operaciones con sets <<<<<<<<<<<<<<<<<<<<<<

latinoamerica = {'peru', 'chile', 'brasil', 'mexico', 'argentina','colombia'}
norteamerica = {'EEUU', 'canada', 'mexico'}

union = latinoamerica.union(norteamerica) # union de 2 conjuntos con el metodo union()
union = latinoamerica | norteamerica      # tambien es la union de 2 conjuntos pero de modo diferente
print(union)

interseccion = latinoamerica.intersection(norteamerica) # interseccion de 2 conjuntos
interseccion = latinoamerica & norteamerica             # otra manera de encontrar la interseccion de 2 conjuntos
print(interseccion)

diferencia = latinoamerica.difference(norteamerica) # la diferencia de 2 conjuntos
diferencia = latinoamerica - norteamerica           # otra manera de encontrar la diferencia de 2 conjuntos
print(diferencia)

diferencia_simetrica = latinoamerica.symmetric_difference(norteamerica)
diferencia_simetrica = latinoamerica 


# Elimina elementos duplicados usando conjuntos

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries | northAm | centralAm | southAm

print(new_set)