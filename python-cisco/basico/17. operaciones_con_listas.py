
# OPERACIONES EN LISTAS

# Las listas y muchas otras entidades complejas de Python (tuplas,diccionarios,etc..) almacenan de diferentes maneras que las variables ordinarias (escalares).
# El nombre de una variable ordinaria es el nombre de su contenido.
# El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.

# ¿Por que el resultado de list_2 es 2?

list_1 = [1] 
list_2 = list_1  # aqui no estas creando una copia de la list_1, esta creando una referencia que apunta a list_1, ambos estan apuntan al mismo objeto en la memoria
list_1[0] = 2 # es por eso que aqui cuando se modifica el unico valor, se esta modificando al objeto
print(list_2) # aqui se mostrara el resultado 2, ya que tanto list_1 y list_2 apuntan al objeto

#--------------------------------------------------------------------------------------------------------------------------------------------------

# CREAR COPIA DE LISTAS
# Python que permite hacer una copia nueva de una lista, o partes de una lista.
# copia el contenido de la lista, no el nombre de la lista.

list_1 = [1]
list_2 = list_1[:] # aqui esta creando una copia de list_1 y asignando a list_2 de [inicio:fin]
list_1[0] = 2 # aqui no afecta a list_2 porque es una copia independiente de list_1
print(list_2) # y es por eso que list_2 aun tiene la lista original

# OBTENER UNA REBANADA DE UNA LISTA
# En Python, cuando se utiliza la notación de rebanada [start:end] para obtener una sublista, 
# el índice start es inclusivo y el índice end es exclusivo. 
# Esto significa que se incluirán los elementos desde el índice start hasta el índice end, 
# pero no se incluirá el elemento en el índice end.

""" 
[start:end]
start: es el índice del primer elemento incluido en la rebanada.
end: es el índice del primer elemento no incluido en la rebanada. 
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # aqui estas obteniendo una rebanada de la lista [start:end], donde start es inclusivo y end es exclusivo
print(new_list) # y es por eso que solo se muestra el 8 y 6 mas no el 4 ya que es exclusivo

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1] # aqui esta obteniendo una rebanada del indice 1 al ultimo indice que es -1
print(new_list)

""" 
[:end]
Si omites el start en tu rebanada, se supone que deseas obtener un segmento que comienza en el elemento con índice 0. 
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

""" 
[start:]
si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice len(my_list) 
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# ELIMINAR REBANADAS DE UNA LISTA

""" 
La instruccion del:
puede eliminar más de un elemento de la lista a la vez, también puede eliminar rebanadas. 
"""

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)


""" 
La instruccion del:
También es posible eliminar todos los elementos a la vez: 
"""

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# OPERADORES IN | NOT IN
# son operadores de pertenencia que se utiliza para verificar si un elemento esta o no en una lista

""" 
in:
devuelve True si el valor se encuentra en la secuencia 

not in:
devuelve True si el valor no se encuentra en la secuencia

"""

my_list = [0, 3, 12, 8, 2]

print(5 in my_list) # false
print(12 in my_list) # true
print(5 not in my_list) # true
print(12 not in my_list) # false

#--------------------------------------------------------------------------------------------------------------------------------------------------

# ITERAR EN LAS LISTAS

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0] # aqui establecemos como numero mayor al primer elemento del indice [0]

# por cada elemento en mi lista
for i in my_list:
    # si elemento es mayor al primer elemento [0]
    if i > largest:
        # sera el nuevo numero mayor
        largest = i

print(largest)

# ITERAR TODOS LOS ELEMENTOS MENOS EL PRIMERO
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]: # aqui se va iterar con todos los elementos menos con el indice [0] 
    if i > largest:
        largest = i

print(largest)


#--------------------------------------------------------------------------------------------------------------------------------------------------

# Ahora encontremos la ubicación de un elemento dado dentro de una lista:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5 # numero a encontrar
found = False # esta en falso

# por cada elemento en el rango de la cantidad de lementos en mi lista
for i in range(len(my_list)):
    # encontrar = elemento en mi lista es igual a el numero a encontrar sera True
    found = my_list[i] == to_find
    # si encontrar es True
    if found:
        break # saldra del bucle

# si encontrar es True
if found:
    print("Elemento encontrado en el índice", i) # imprime el indice del elemento encontrado
else: # de los contrario
    print("ausente") # muestra numero ausente
    
#--------------------------------------------------------------------------------------------------------------------------------------------------
    
drawn = [5, 11, 9, 42, 3, 49] # numeros de la loteria
bets = [3, 7, 11, 42, 34, 49] # numeros de la apuesta
hits = 0
hits_found = [] # lista vacia donde se guardara los numeros ganadores

for number in bets:
    if number in drawn:
        hits_found.append(number)
        hits += 1
print("La cantidad de aciertos logrados son:",hits,"Los numeros son:",hits_found)


#--------------------------------------------------------------------------------------------------------------------------------------------------

""" LABORATORIO: Eliminar elementos duplicados en una lista """

# 1° OPCION : es convirtiendo a un conjunto y luego a una lista
my_list = [1, 5, 2, 4, 4,5, 1, 4, 2, 6, 2, 9]
# aqui la lista se convierte en un conjunto con set() (los conjuntos no admiten elementos duplicados) y en la misma linea se convierte a lista con list()
my_list = list(set(my_list))
print("La lista con elementos únicos:", my_list)
print("El tipo es:",type(my_list))


# 2° OPCION : es convirtiendo a un diccionario y luego a una lista
my_list = [1, 5, 2, 4, 4,5, 1, 4, 2, 6, 2, 9]
# aqui la lista se convierte en diccionario dict.fromkeys() donde cada elemento se convierte en clave y sus valores es none (los diccionarios no pueden tener claves duplicadas y mantendran el orden original) luego es convertido a lista con list()
my_list = list(dict.fromkeys(my_list))
print("La lista con elementos únicos:", my_list)
print("El tipo es:",type(my_list))


# 3° OPCION : es utilizando el bucle for
my_list = [1, 5, 2, 4, 4,5, 1, 4, 2, 6, 2, 9]
lista_no_repetida = []

# por cada elemento en mi lista
for elemento in my_list:
    # si elemento no se encuentra en lista no repetida
    if elemento not in lista_no_repetida:
        # entonces se agrega a la lista no repetida
        lista_no_repetida.append(elemento)

print("La lista con elementos únicos:",lista_no_repetida)
print("El tipo es:",type(lista_no_repetida))


