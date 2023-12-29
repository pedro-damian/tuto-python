
# ALCANCES
# una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.

def my_function():
    print("¿Conozco a la variable?", var)

var = 1
my_function() # invoca la funcion con el valor de la variable, se puede ver que dentro de la funcion la variable no tiene un valor asignado y que el valor que muestra es de la variable que esta fuera de la funcion


# el alcance de una variable existente fuera de una función solo se puede implementar dentro de una función cuando su valor es leído. El asignar un valor hace que la función cree su propia variable.

def my_function():
    # variable local
    var = 2
    print("¿Conozco a la variable?", var)

var = 1
my_function() # el resultado sera 2 

#------------------------------------------------------------------------------------------------------------------------------------------

# palabra clave reservada global
# Es utilizar la palabra reservada global + una o mas variables separadas por comas dentro una funcion 
# esta variable y su valor podran ser utilizadas fuera de la funcion hasta que se asigne otro valor a la variable fuera de la funcion

def my_function():
    global var # puedo declarar las variables necesarias separadas por coma
    var = 2
    var2 = 4
    print(f"¿Conozco a aquella variable? {var}")


var = 1 # esta variable declarada no tiene efecto ya que la siguiente linea llama a la misma variable pero con otro valor
my_function() # resultado es 2 y 4 por la variable global dentro de la funcion
var = 5
print(var) # aqui el resultado es 5 porque el valor de la variable se modifico en la linea anterior, de lo contrario tendria el valor global de la funcion.
