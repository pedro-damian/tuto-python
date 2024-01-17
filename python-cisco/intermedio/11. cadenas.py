
# ----------------------------- CADENAS ----------------------
# son secuencias inmutables.

word = 'by'
print(len(word)) # la funcion len() devuelve el numero de caracteres en este caso es 2

empty = ''
print(len(empty)) # la funcion len() devuelve el numero de caracteres en este caso es 0

i_am = 'I\'m'
print(len(i_am)) # la funcion len() devuelve el numero de caracteres en este caso es 3, ya que la diagonal no esta incluida


# --------------CADENAS MULTILINEA -------------------------
# Las cadenas multilínea pueden ser delimitadas también por comillas triples,

multiline = '''Línea #1
Línea #2'''
print(len(multiline)) # Aqui el resultado es 17 por el salto de linea (\n)  tambien cuenta como caracter.


# ----------------- OPERACIONES CON CADENAS ----------------------------

str1 = 'a'
str2 = 'b'

# >>>>>>>> CONCATENADAS (+)
print(str1 + str2)
print(str2 + str1)

# >>>>>>>> REPLICADAS (*)
print(5 * 'a')
print('b' * 4)

# >>>>>>>> ord() 
# devuelve el valor del punto de código ASCII/UNICODE de un carácter específico.

char_1 = 'a'
char_2 = ' '  # space
char_3 = '@'  # aroba
char_4 = '#'  # michi

print(f"El valor del caracter 'a' es: {ord(char_1)}")
print(f"El valor del caracter ' ' es: {ord(char_2)}")
print(f"El valor del caracter '@' es: {ord(char_3)}")
print(f"El valor del caracter '#' es: {ord(char_4)}")

# >>>>>>>>>> chr()
# toma un punto de código y devuelve su carácter.

print(chr(64)) # @
print(chr(945)) # α

# ----------------- INDEXACIÓN y ITERAR --------------------------
# cadenas de Python son secuencias
# Las cadenas no son listas, pero pueden ser tratadas como tal en muchos casos.


the_string = 'silly walks'

for elemento in range(len(the_string)):
    print(the_string[elemento],elemento, sep=" => ") # s i l l y   w a l k s

print() # Salto de linea


the_string = 'silly walks'

for character in the_string:
    print(character, end=' ') # s i l l y   w a l k s
print() # Salto de linea

# ----------------- REBANADAS ---------------------------

cadena = "Hola mundo"

print(cadena[1:3]) # del indice 1 al 3
print(cadena[3:]) # del indice 3 hasta el final
print(cadena[:3]) # del inicio hasta el indice 3
print(cadena[3:-2]) # del indice 3 hasta el indice -2
print(cadena[-3:4]) # error
print(cadena[::2]) # devuelve el caracter del inicio hasta el final saltandose de 2 en 2
print(cadena[1::2]) # del indice 1 hasta el final saltandose 2 en 2


#---------------------- Operadores in y not in ----------------------------------

# el operador "in" "not in" comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) # true
print("F" in alphabet) # False
print("1" in alphabet) # False
print("ghi" in alphabet) # True
print("Xyz" in alphabet) # False


alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet) # False
print("F" not in alphabet) # True
print("1" not in alphabet) # True
print("ghi" not in alphabet) # False
print("Xyz" not in alphabet) # True


#--------------------------------- No puedes utilizar del() , append(), insert() ------------------------------
# puedes agregar un caracter a una cadena de esta forma:

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet  # agrega el caracter "a" al inicio de la cadena
alphabet = alphabet + "z"  # agrega el caracter "z" al final de la cadena

print(alphabet)


# -------------------------- min() --------------------------
# encuentra el elemento mínimo de la secuencia pasada como argumento

print(min("aAbByYzZ")) # A: por que en la tabla ASCII la letra A mayuscula tiene un numero menor


t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']') # espacio = 32

t = [0, 1, 2]
print(min(t)) # 0

# ------------------------- max() --------------------------------
# encuentra el elemento máximo de la secuencia.

print(max("aAbByYzZ")) # z = 122 en ASCII

t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']') # ¡ = 173

t = [0, 1, 2]
print(max(t)) # 2


# --------------------- index() ----------------------------
# devuelve el indice de un caracter dentro de la secuencia

alphabet = "bcdefghijklmnopqrstuvwxy"

print(alphabet.index("b")) # 0
print(alphabet.index("d")) # 2
print(alphabet.index("f")) # 4
print(alphabet.index("y")) # 23

print(len(alphabet)-1) # asi encuentras el ultimo indice sin saber el caracter


# ------------------ list() ------------------------------------
# toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena, uno por elemento de la lista.
# igual pasa con una tupla o diccionario los vuelve una lista

print(list(alphabet)) # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']


# ------------------- count() ---------------------------------
# cuenta cuantas veces aparece el elemento dentro de la secuencia

cadena2 = "abcabc"
print(cadena2.count("b")) # 2
print(cadena2.count("d")) # 0


# Mas informacion en la documentacion oficial de python3 https://docs.python.org/es/3/library/stdtypes.html#string-methods
