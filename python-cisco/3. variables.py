
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