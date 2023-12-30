
# MODULO random
# genera numeros aleatorios

import random

dir(random)
print(dir(random))


#----------------------------- funcion random()  ----------------------------------
# produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).

from random import random

for i in range(5):
    print(random())
    

#----------------------------- funcion seed()  ------------------------------------
# La función seed() es útil porque permite que los números generados por las funciones del módulo random sean reproducibles. Es decir, si inicializas el generador de números aleatorios con la misma semilla, obtendrás la misma secuencia de números.

# seed() - establece la semilla con la hora actual.
# seed(int_value) - establece la semilla con el valor entero int_value.

from random import random, seed

seed(0)

for i in range(5):
    print(random())


#----------------------------- funcion randint() ------------------------------------
# Permite especificar un rango de números usando los parámetros start, stop y opcionalmente step.

""" valores enteros
randrange(fin)
randrange(inico, fin)
randrange(inicio, fin, incremento) 
"""

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')



#----------------------------- funcion randint() ------------------------------------
# Permite especificar un rango de números mediante los parámetros a y b.
# es más simple y directa, generando un entero aleatorio en el rango específico sin la opción de un paso personalizado.

""" 
randint(izquierda, derecha) 

"""

print(randint(0, 5))


#----------------------------- funcion choice() ------------------------------------
# Devuelve un único elemento aleatorio

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))


#----------------------------- funcion sample() ------------------------------------
# Devuelve una lista con los elementos únicos (sin repetición)

print(sample(my_list, 5))
print(sample(my_list, 10))