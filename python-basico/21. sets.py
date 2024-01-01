
# CONJUNTOS
# son mutables
# no puede tener elementos duplicados

paises = {'peru','chile','bolivia','brasil'}
print(paises)           # muestra los elementos del conjunto paises
print(type(paises))     # muestra el tipo de estructura de dato --> set

numeros = {1,2,3,4,5,6,45,67,8}
print(numeros)           # muestra los elementos del conjunto numeros
print(type(numeros))     # muestra el tipo de estructura de dato --> set

combinado = {1, 'pedro', 45.6, 'juan', -30, 'A'}
print(combinado)           # muestra los elementos del conjunto
print(type(combinado))     # muestra el tipo de estructura de dato --> set

#>>>>>>>>>>>>>>>>>>>> convertir de string (cadena) a sets (conjunto) <<<<<<<<<<<<<<<<<<<<<<

letras = set('hola mundo')
print(letras)

#>>>>>>>>>>>>>>>>>>>> convertir de tupla a sets (conjunto) <<<<<<<<<<<<<<<<<<<<<<

nombres = ("Pedro", "adrian", "carlos", "jose")
set_nombres = set(nombres)
print(set_nombres)
print(type(set_nombres))

#>>>>>>>>>>>>>>>>>>>> convertir de lista a sets (conjunto) <<<<<<<<<<<<<<<<<<<<<<

lista_numeros = [1,2,3,4,5,6,7,8,45,90]
set_numeros = set(lista_numeros)
print(set_numeros)