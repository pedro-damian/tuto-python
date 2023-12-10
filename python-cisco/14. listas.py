
# LISTAS
# Los elementos dentro de una lista pueden tener diferentes tipos. Algunos de ellos pueden ser enteros, otros son flotantes y otros pueden ser listas.
# El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice
# mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.

numeros = [10, 5, 7, 2, 1]

# Imprimir cada elemento por separado
print(numeros[0]) # Accediendo al primer elemento de la lista.
print(numeros[1]) # Accediendo al primer elemento de la lista.
print(numeros[2]) # Accediendo al primer elemento de la lista.
print(numeros[3]) # Accediendo al primer elemento de la lista.
print(numeros[4]) # Accediendo al primer elemento de la lista.

# Imprimir toda la lista
print(numeros)

# Cambiar el valor de un ELEMENTO de una lista por otro
numeros[0] = 111
print(numeros)

# cambiar de valores entre los ELEMENTOS de una lista
numeros[1] = numeros[4]
print(numeros)

#------------------------------------------------------------------------------------------------------------
# La función len()
# verificar la longitud actual de la lista

print("La cantidad de elementos en la lista son: ",len(numeros))

#------------------------------------------------------------------------------------------------------------
# La instruccion del
del numeros[1]
print("La cantidad de elementos en la lista son: ",len(numeros))
print(numeros)

#------------------------------------------------------------------------------------------------------------
# Los índices negativos
# los numeros negativos aplicados al llamado de un indice mostaran del ultimo al primero
print(numeros[-1])
print(numeros[-2])
print(numeros[-3])
print(numeros[-4])

#------------------------------------------------------------------------------------------------------------

""" 
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.
Tu tarea es:
Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1).
Escribir una línea de código que elimine el último elemento de la lista (Paso 2).
Escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
 """
 
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero = int(input("ingrese un numero entero positivo: "))
hat_list[2]=numero

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(f"La longitud de la lista es: {len(hat_list)}")

print(hat_list)

#------------------------------------------------------------------------------------------------------------

# REVERTIR una LISTA
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

# REVERTIR con FOR
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)

#------------------------------------------------------------------------------------------------------------

""" Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista. """

# paso 1
Beatles=[]
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for _ in range(2): # el guion bajo _ indica que no se utilizara la variable de control de recorrido
    nombre = input("ingrese nombres: ")
    Beatles.append(nombre)
print("Paso 3:", Beatles)

# paso 4
del Beatles[3:5]

print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0,"Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
