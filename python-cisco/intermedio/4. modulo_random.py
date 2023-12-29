
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


#----------------------------- funcion randrange() y randint() ------------------------------------


""" valores enteros
randrange(fin)
randrange(inico, fin)
randrange(inicio, fin, incremento) 
randint(izquierda, derecha)

"""

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1)) # aqui sera entre 1 o 0
