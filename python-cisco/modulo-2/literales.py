
# TIPO DE DATOS
# ENTEROS: OCTAL Y HEXADECIMAL

octal = 0o123 # número entero esta precedido por un código 0o... , en el rango del [0..7] únicamente
hexadecimal = 0x123 # números deben ser precedidos por el prefijo 0x..
print(octal) # numero octal
print(f"Es de tipo {type(octal)}")
print(hexadecimal)
print(f"Es de tipo {type(hexadecimal)}")


# FLOTANTES
decimal = 4.3
print(decimal)
print(f"Es de tipo {type(decimal)}")

# velocidad de la luz
luz_velocidad = 3E8   # hay dos opciones "e" o "E" (significa por diez a la n potencia = 3*10 elevado a 8)
print(luz_velocidad)
print(f"Es de tipo {type(luz_velocidad)}")

# La Constante de Planck
planck = 6.62607E-34 # aqui imprimira el mismo numero ya que es un numero inmenso y el programa siempre elijira la opcion mas corta
print(planck)
print(f"Es de tipo {type(planck)}")

print(0.0000000000000000000001) # impprimira 1e-22 la opcion mas corta


# CADENAS
# Imprimir comillas dobles
print("Me gusta \"Monty Python\"")
print('Me gusta "Monty Python"')
# Imprimir comillas simples
print('I\'m Monty Python.')
print("I'm Monty Python.")


# BOOLEANOS
print(True > False) # true = 1 y  false = 0
print(True < False) # true = 1 y  false = 0