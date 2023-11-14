
# LA FUNCION INPUT ()
# La función input() es capaz de leer datos que fueron introducidos por el usuario
# los datos introducidos deben ser asignado a una variable; esto es crucial, si no se hace los datos introducidos se perderán.
# el resultado de la función input() es una cadena.

variable = input()

# ARGUMENTO DE LA FUNCION INPUT()
# el argumento de la funcion input() es una cadena de texto

variable = input("Introduce tu nombre: ")

# OPERACIONES PROHIBIDAS
# el dato introducido no se debe utilizar como un argumento para operaciones matemáticas
# ya que el resultado es una cadena o string

# esto dara un error
#variable = input("Inserta un número: ")
#operacion = variable ** 2.0
#print(variable, "al cuadrado es", operacion)


# Conversión de datos (casting)
# La funcion int() convierte una entrada en entero 

numero = int(input("Ingrese un numero entero: "))
potencia = numero **2
print(numero , "Elevado al cuadrado es: ", potencia)
print(f"El numero es de tipo {type(numero)}")

# La funcion float() convierten una entrada en  float

numero_float = float(input("Ingrese un numero: "))
potencia = numero_float **3
print(numero_float,"elevado al cubo es:", potencia)
print(f"El numero float es de tipo {type(numero_float)}")

# la funcion str() convierte un numero a cadena
print(f"El numero float era de tipo {type(numero_float)} ahora es de tipo {type(str(numero_float))}")



# OPERADORES DE CONCATENACION (+)
# solo se puede concatenar cadenas 
# mostrara un error si intenta concatenar una cadena y un numero

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
print("Tu nombre y apellido es: " + nombre + " " + apellido)

# OPERADOR DE REPLICACION (*)
# se utiliza para relicar una cadena tantas veces indique el numero

print(nombre * 4)


""" Este sencillo programa "dibuja" un rectángulo, haciendo uso del operador (+), pero en un nuevo rol: """
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


""" evaluar la siguiente expresión: 1/(x + 1/(x + 1/x)) """

x = float(input("Ingresa el valor para x: "))
y = 1/(x + 1/(x + 1/x))
print("y =", y)


""" La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola. """

# Entrada de usuario
hora_inicio = int(input("Ingresa la hora de inicio (0-23): "))
minuto_inicio = int(input("Ingresa los minutos de inicio (0-59): "))
duracion_minutos = int(input("Ingresa la duración en minutos: "))

# Cálculos
total_minutos = (hora_inicio * 60 + minuto_inicio + duracion_minutos) % (24 * 60)
hora_final = total_minutos // 60
minuto_final = total_minutos % 60

# Mostrar resultado
print(f"El evento terminará a las {hora_final:02d}:{minuto_final:02d}")

# En este ejercicio podemos utlizar el input para terminar un programa

name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")

print("\nPresiona la tecla Enter para finalizar el programa.")
input()
print("FIN.")