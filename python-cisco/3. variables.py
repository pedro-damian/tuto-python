
# VARIABLES
# es un espacio en la memoria donde se guardara un tipo de dato 
# esta compuesto de un nombre y valor
# el nombre de la variable puede contener mayusculas, minusculas, numeros y guion bajo
# El nombre de la variable debe comenzar con una letra o on guion bajo.
# el nombre de la variable NO debe comenzar con un numero o tener espacios
# el nombre de la variables se distingue entre mayusculas y minusculas: dia - Dia - DIA son diferentes variables

# PALABRAS RESERVADAS
# son reservadas porque no se deben utilizar como nombres: ni para variables, ni para funciones, ni para cualquier otra cosa.
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# CREAR Y ASIGNAR UNA VARIABLE
variable = 100
print(variable)

# MODIFICAR EL VALOR DE LA VARIABLE
variable = variable + 100
print(variable)


# TEOREMA DE PITAGORAS
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("La hipotenusa del triangulo rectangulo es:", c)


""" Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

Tu tarea es:

Crear las variables: juan, maria, y adan.
Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía.
Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
Después se debe crear una nueva variable llamada total_manzanas y se debe igualar a la suma de las tres variables anteriores.
Imprime el valor almacenado en total_manzanas en la consola.
Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número Total de Manzanas:" y total_manzanas. """

juan = 3
maria = 5
adan=6
total_manzanas = juan + maria + adan
print(juan,maria,adan, sep=",")
print("El numero total de manzanas es:",total_manzanas)


# OPERADORES ABREVIADOS (+=)(-=)(*=)(/=)(%=)(**=)

var = 8
var = var / 2 
var /= 2

rem = 100
rem = rem % 10  
rem %= 10

x = 2
x = x ** 2 
x **= 2


""" Millas y kilómetros son unidades de longitud o distancia.
Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:
Millas a kilómetros.
Kilómetros a millas.
 """

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


""" Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión: 3x3 - 2x2 + 3x - 1
El resultado debe ser asignado a y. """

x = input("ingrese numero: ")
x = float(x)
# escribe tu código aquí
y = 3*x**3 -2*x**2+3*x-1
print("El resultado de y es =", y)


""" calcula los segundos en cierto número de horas determinadas  """
a = 2 # número de horas
seconds = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en Horas: ", a * seconds) # se imprime el numero de segundos en determinado numero de horas

