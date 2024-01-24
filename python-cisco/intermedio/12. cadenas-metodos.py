
#---------------- capitalize() ----------------------------
# crea una nueva cadena modificada y lo devuelve como resultado si lo quieres seguir utilizando asignale una variable o pasala a una funcion de lo contrario desaparecera.
# la cadena original no se modifica ya que es inmutable 
# Si el primer carácter dentro de la cadena es una letra se convertirá a mayúsculas, Todas las letras restantes de la cadena se convertirán a minúsculas.

print('aBcD'.capitalize())  # Abcd
print("Alpha".capitalize()) # Alpha
print('ALPHA'.capitalize()) # Alpha
print(' Alpha'.capitalize()) #  alpha
print('123'.capitalize())   # 123
print("αβγδ".capitalize()) # Αβγδ
 
#---------------- center() ----------------------------
# genera una copia de la cadena original, tratando de centrarla dentro de un campo de un ancho especificado.
# El centrado se realiza al agregar algunos espacios antes y después de la cadena.

print('[' + 'alpha'.center(10) + ']') # [  alpha   ]
print('[' + 'Beta'.center(2) + ']') # [Beta]
print('[' + 'Beta'.center(4) + ']') # [Beta]
print('[' + 'Beta'.center(6) + ']') # [ Beta ]

# La variante de dos parámetros de center() hace uso del carácter del segundo argumento, en lugar de un espacio.
print('[' + 'gamma'.center(20, '*') + ']') # [*******gamma********]


# -------------------- endswith() --------------------------
# comprueba si la cadena dada termina con el argumento especificado
# devuelve True(verdadero) o False(falso), dependiendo del resultado.

t = "zeta"
print(t.endswith("a")) # True
print(t.endswith("A")) # False
print(t.endswith("et")) # Flase
print(t.endswith("eta")) # True


# -------------------- find() --------------------------
# busca una subcadena y devuelve el índice de la primera letra de esta subcadena
# en caso la subcadena no exista (devuelve -1)
# Funciona solo con cadenas - no aplica a secuencias (listas,tuplas. etc..)

t = 'theta'
print(t.find('eta')) # 2
print(t.find('et')) # 2
print(t.find('the')) # 0
print(t.find('ha')) # -1

# find() con 2 parametros, 1 parametro es la subcadena, 2 parametro es de que indice iniciara la busqueda

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print("La subcadena 'the' se encuentra en el indice:",fnd) # 15, 80, 198, 221, 238
    fnd = the_text.find('the', fnd + 1) # indica que comienza desde la posición siguiente a la última ocurrencia encontrada es por eso muy importante el +1 de lo contrario entra en un bucle infinito


# find() con 3 parametros, 1 subcadena, 2 indice inicio, 3 indice final donde termina la busqueda 
print('kappa'.find('a', 1, 4)) # 1
print('kappa'.find('a', 2, 4)) # -1


# -------------------- isalnum() --------------------------
# comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True(verdadero) o False(falso)

print('lambda30'.isalnum())     # True
print('lambda'.isalnum())       # True
print('30'.isalnum())           # True
print('@'.isalnum())            # False
print('lambda_30'.isalnum())    # False
print(''.isalnum())             # False

t = 'Six lambdas'
print(t.isalnum())      # False , aqui da falso por el espacio
t = 'ΑβΓδ'
print(t.isalnum())      # True
t = '20E1'
print(t.isalnum())      # True


# -------------------- isalpha() --------------------------
# busca solo letras.
print("Moooo".isalpha())    # True
print('Mu40'.isalpha())     # False



# -------------------- isdigit() --------------------------
# busca solo dígitos
print('2018'.isdigit())     # True
print("Year2019".isdigit()) # False

# -------------------- islower() --------------------------
# es una variante de isalpha() - solo acepta letras minúsculas.
print("Moooo".islower())    # False
print('moooo'.islower())    # True


# -------------------- isspace() --------------------------
# identifica espacios en blanco solamente - no tiene en cuenta ningún otro carácter (el resultado es entonces False).
print(' \n '.isspace())             # True
print(" ".isspace())                # True
print("mooo mooo mooo".isspace())   # False



# -------------------- isupper() --------------------------
# es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.
print("Moooo".isupper())    # False
print('moooo'.isupper())    # False
print('MOOOO'.isupper())    # True


# -------------------- join() --------------------------
# utiliza para concatenar elementos de una secuencia en una cadena de texto
# la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
# El argumento del join es una lista que contiene tres cadenas.

palabras = ["Hola", "mundo", "Python"]
cadena_resultante = " ".join(palabras)
print(cadena_resultante)                    # Hola mundo Python


# -------------------- ilower() --------------------------
# genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas.
# Si la cadena no contiene caracteres en mayúscula, el método devuelve la cadena original.

print("SiGmA=60".lower())       # sigma=60


# -------------------- lstrip() --------------------------
# devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.


# -------------------- isalnum() --------------------------