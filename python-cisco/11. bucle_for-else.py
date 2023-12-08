
# BUCLE FOR-ELSE

for i in range(1,6):
    print(i)
else:
    print("else:", i)


""" Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. """

for letra in "john.smith@pythoninstitute.org":
    if letra == "@":
      break
    print(letra)
    
    
""" Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla."""

cadena=""
for digit in "0165031806510":
    if digit == "0":
      cadena+="x"
      continue
    cadena+=digit
print(cadena)




