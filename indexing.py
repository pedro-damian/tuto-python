
# INDEXAR
# referirse a un elemento dentro un iterable por su posicion

# INDEXAR UNA CADENA
cadena = "Hola Mundo"
print(cadena[0])  # Imprimirá "H"
print(cadena[1])  # Imprimirá "O"
print(cadena[2])  # Imprimirá "L"
print(cadena[5])  # Imprimirá "M"

print("Imprimira el ultimo caracter de la cadena de texto =>", cadena[-1])

# INDEXAR UNA LISTA
lista = ["manzana", "uva", "naranja", "guayaba", "plátano"]
print(lista[0])  # Imprimirá "manzana"
print(lista[4])  # Imprimirá "plátano"


# SLICING
print("Imprimira de la posicion 0 a 5 =>", cadena[0:5])
print("Imprimira de la posicion 5 a 9 =>", cadena[5:9])
print("Imprimira de la posicion 0 hasta el final de la cadena =>", cadena[:10])
print("Imprimira de la posicion 3 hasta el final de la cadena =>",cadena[3:])
print("Imprimira de la posicion 2 hasta el final de la cadena saltandose 2 caracteres =>",cadena[2:10:2])
print("Imprimira de la posicion 2 hasta el final de la cadena saltandose 3 caracteres =>",cadena[2:10:3])
print("Imprimira de la posicion inicial hasta el final de la cadena saltandose 4 caracteres =>",cadena[::4])

