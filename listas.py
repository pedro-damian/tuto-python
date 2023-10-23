
# LISTAS
# las listas se pueden crear con corchetes "[ ]"
# los elementos de una lista estan indexados esto quiere decir que tienen un orden donde siempre empieza de cero
nombres = ["pedro", "maria", "jose", "miguel", "raul"]
print("El indice de pedro es =>", nombres.index("pedro"))
print("El indice de maria es =>", nombres.index("maria"))
print("El indice de jose es =>", nombres.index("jose"))

# las lista pueden contener diferentes tipos de datos como cadenas, numeros y boolean
objetos =["hola", 34 ,True, 50.4,]

# las lista pueden contener elementos duplicados
numeros = [4,5,6,7,8,9,4,7]

print("La variable nombres es de tipo =>",type(nombres))

# imprime el valor del indice 
print("El valor del inidce 0 es =>", nombres[0])
print("El valor del inidce 1 es =>", nombres[1])
print("El valor del inidce 2 es =>", nombres[2])
print("El valor del inidce 3 es =>", nombres[3])

# OBJETOS MUTABLES Y INMUTABLES
# los valores de los objetos(variables) mutables puede ser modificado despues de ser creado (listas,diccionarios,sets y array)
# los valores de los objetos(variables) inmutables no pueden ser modificados despues de su creacion (int,float,complex,string,tuplas,bytes), sin embargo puedes asignarle un nuevo valor al objeto.

# MODIFICANDO LA LISTA 
nombres[1] = "jorge"
print("Modifico el elemento maria a Jorge =>", nombres[1])

print("Muestra los elementos del indice [0] al [3] =>",nombres[:3])