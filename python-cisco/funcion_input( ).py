
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
variable = input("Inserta un número: ")
operacion = variable ** 2.0
print(variable, "al cuadrado es", operacion)


# Conversión de datos (casting)