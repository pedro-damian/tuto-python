
# VARIABLES
# es un espacio en la memoria donde se guardara un tipo de dato 
# esta compuesto de un nombre y valor

# REGLAS PARA NOMBRAR VARIABLES
# el nombre de la variable puede contener mayusculas, minusculas, numeros y guion bajo
# El nombre de la variable debe comenzar con una letra o on guion bajo.
# el nombre de la variable NO debe comenzar con un numero o tener espacios
# el nombre de la variables se distingue entre mayusculas y minusculas: dia - Dia - DIA son diferentes variables

# PALABRAS RESERVADAS
# son reservadas porque no se deben utilizar como nombres: ni para variables, ni para funciones, ni para cualquier otra cosa.
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# SENSIBILIDAD A MAYUSCULAS Y MINUSCULAS
#import = "import es una palabra reservada" # Error, import es una palabra reservada
Import = "Es diferente a import" # Correcto, Import es diferente a import
IMPORT = "Es diferente a import e Import" # Correcto, IMPORT es diferente a import

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
print("La hipotenusa del triangulo rectangulo es:", c) # imprime 5.0 porque 3^2 + 4^2 = 9 + 16 = 25 y la raiz cuadrada de 25 es 5 Porque raiz es igual a elevar a la 0.5 


""" 
Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. 
Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

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
x = 10

x = x + 3 # forma larga
x += 3    # forma corta

x = x * 2 # forma larga
x *= 2    # forma corta

x = x - 4 # forma larga
x -= 4    # forma corta

x = x / 2 # forma larga
x /= 2    # forma corta

x = x ** 2 # forma larga
x **= 2    # forma corta

x = x % 2 # forma larga
x %= 2    # forma corta




""" Millas y kilómetros son unidades de longitud o distancia.
Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:
Millas a kilómetros.
Kilómetros a millas.
 """

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61  # porque 1 milla = 1.61 kilometros significa que para convertir millas a kilometros se multiplica por 1.61
kilometers_to_miles = kilometers / 1.61 # porque 1 milla = 1.61 kilometros significa que para convertir kilometros a millas se divide entre 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros") # round( , 2) redondea el numero a 2 decimales
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas") # round( , 2) redondea el numero a 2 decimales

# Convertidor de monedas
venta = 3.5
compra = 3.473

cantidad = 100

dolar_to_soles = cantidad * compra # para convertir dolares a soles se multiplica por el precio de compra
soles_to_dolar = cantidad / venta  # para convertir soles a dolares se divide entre el precio de venta

print(cantidad, "dolares son", round(dolar_to_soles,2), "soles")
print(cantidad, "soles son", round(soles_to_dolar,2), "dolares")

# convertidor de temperaturas
celsius = 37.5
fahrenheit = 99.5
celsius_to_fahrenheit = (celsius * 9/5) + 32  # formula para convertir celsius a fahrenheit
fahrenheit_to_celsius = (fahrenheit - 32) * 5/9  # formula para convertir fahrenheit a celsius
print(celsius, "grados celsius son", round(celsius_to_fahrenheit,2), "grados fahrenheit")
print(fahrenheit, "grados fahrenheit son", round(fahrenheit_to_celsius,2), "grados celsius")


""" Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, 
e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión: 
3x3 - 2x2 + 3x - 1 , El resultado debe ser asignado a y. """

x = input("ingrese numero: ")
x = float(x)
# 3x3 - 2x2 + 3x - 1 es igual a:
y = 3 * x**3 - 2 * x**2 + 3*x - 1
print("El resultado de y es =", y)


""" calcula los segundos en cierto número de horas determinadas  """
a = 2 # número de horas
seconds = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en Horas: ", a * seconds) # se imprime el numero de segundos en determinado numero de horas

