
# ------------------------------------------------TUPLAS ( ) -----------------------------------------------
# son colecciones de elementos que se encierran entre ( )
# Los elementos de las tuplas son inmutables (no se puede alterar sus valores)
# son utilizados si quieres que sus elementos no sean modificados

numeros = (1,3,5,7,8,9,2,3,3)
strings = ("Pedro", "adrian", "carlos", "jose")

# El metodo index()
print("El elemento 7 de la tupla numeros se encuentra en el indice =>",numeros.index(7))

# El metodo count()
# sirve para contar las veces que un elemento se repite
print("El elemento 3 de la tupla numeros se repite =>",numeros.count(3))


# ---------------------------------------CONVERTIR UNA TUPLA A LISTA -------------------------------------
# FUNCION list()
# esto convierte una cadena, tupla, range en una lista
# al convertir en lista podre realizar el CRUD
cadena = "Hola mundo"
rango = range(10)

# convierte una cadena a lista
lista_cadena = list(cadena)
# convierte un rango a lista
lista_rango = list(rango)
# convierte una tupla a lista
lista_string = list(strings)

print("La cadena ahora es una lista =>",lista_cadena,"era de tipo =>",type(cadena), "ahora es de tipo =>",type(lista_cadena))
print("El rango ahora es una lista =>",lista_rango,"era de tipo =>",type(rango), "ahora es de tipo =>",type(lista_rango))
print("La Tupla ahora es una lista =>",lista_string,"era de tipo =>",type(strings), "ahora es de tipo =>",type(lista_string))

# --------------------------------CONVERTIR UNA LISTA A TUPLA-----------------------------------------
# Funcion tuple()
# convierte una cadena, lista en una tupla inmutable
tupla_cadena = tuple(cadena)
tupla_string = tuple(lista_string)


print("La cadena ahora es una Tupla =>",tupla_cadena,"era de tipo =>",type(cadena), "ahora es de tipo =>",type(tupla_cadena))
print("La Lista ahora es una Tupla =>",tupla_string,"era de tipo =>",type(lista_string), "ahora es de tipo =>",type(tupla_string))
