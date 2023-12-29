

# una secuencia (listas,tuplas y diccionarios) es un tipo de dato que puede ser escaneado por el bucle for.
# La mutabilidad es una propiedad de cualquier tipo de dato existen 2 tipos en python: MUTABLES y INMUTABLES
# Los datos mutables pueden ser actualizados libremente en cualquier momento o llamados "In situ"
# los datos inmutables no pueden ser modificados de esta manera.

# LAS TUPLAS
# Las tuplas utilizan paréntesis
# es posible crear una tupla tan solo separando los valores por comas.
# cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, o cualquier otro tipo de dato).
# Es posible crear una tupla vacía,solo se necesitan unos paréntesis.
# Si se desea crear una tupla de un solo elemento, se debe de colocar una coma al final.

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
empty_tuple = ()
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

print(type(tuple_1))
print(type(tuple_2))


# ¿Cómo utilizar una tupla?
# La función len() acepta tuplas, y regresa el número de elementos contenidos dentro.
# El operador + puede unir tuplas (ya se ha mostrado esto antes).
# El operador * puede multiplicar las tuplas, así como las listas.
# Los operadores in y not in funcionan de la misma manera que en las listas.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
