
# PASO DE ARGUMENTOS POSICIONALES
# asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.

""" 
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

"""

# EJEMPLOS
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#-----------------------------------------------------------------------------------------------------------------------------------------

# PASO DE ARGUMENTOS CON PALABRA CLAVE
# otra manera de pasar argumentos, donde el significado del argumento está definido por su nombre, no su posición, a esto se le denomina paso de argumentos con palabra clave.
# los valores pasados a los parámetros son precedidos por el nombre del parámetro al que se le va a pasar el valor, seguido por el signo de =.


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# no se debe de utilizar el nombre de un parámetro que no existe. TypeError: introduction() got an unexpected keyword argument 'surname'

""" 
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke") 
"""


#-------------------------------------------------------------------------------------------------------------------------------------

# ARGUMENTOS COMBINADOS: Posicionales y Palabra clave
# Es posible combinar ambos tipos si se desea, solo hay una regla inquebrantable: se deben colocar primero los argumentos posicionales y después los de palabra clave.

def agregar(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

agregar(3, c = 1, b = 2) # aqui el argumento 3 asume el parametro a
agregar(4, 3, c = 2) # aqui el argumento 4 y 3 toman el parametro a y b respectivamente

# aqui mostraria error

""" 
def subtra(a, b):
    print(a - b)

subtra(a=5, 2)    # Syntax Error 

"""