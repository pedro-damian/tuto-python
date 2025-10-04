
# BUCLE FOR
# puede "explorar" grandes colecciones de datos elemento por elemento.

""" for i in range(100):
    # do_something()
    pass """
    
    
#----------------------------------------------------------------------------------------------------------------------------
# IMPRIMIRA DEL 0 al 9 (por la funcion range())
for i in range(10):
    print("El valor de i es actualmente", i)
print("-"*30)

#----------------------------------------------------------------------------------------------------------------------------
# IMPRIMIRA del 2 al 7 (la funcion range con 2 argumentos: (N°-inicio y N°-final))
for i in range(2, 8):
    print("El valor de i es actualmente", i)
print("-"*30)

#----------------------------------------------------------------------------------------------------------------------------
# IMPRIMIRA 2 y 5 (la funcion range con 3 argumentos, el tercer argumento son saltos)
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)
print("-"*30)

#----------------------------------------------------------------------------------------------------------------------------
# IMPRIMIRA la potencia de 2 elevado de 0 hasta el 15
power = 1
for expo in range(16):
    # aqui el orden es muy importante, ya que la potencia de 2° es 1 y el valor de power es 1
    print("2 a la potencia de", expo, "es", power)
    # aqui la variable va incrementadose el doble en cada iteracion
    power = power * 2

#----------------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
""" Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!" """

import time

    # Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle - usar: time.sleep (1)

# Escribe una función de impresión con el mensaje final.

for i in range(1,6):
    print(i,"Mississippi")
print("¡Listos o no, ahí voy!")


#----------------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
# Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla
print("Numeros Impares:")
for i in range(0,11):
    if i%2 != 0:
        print("Los numeros Impares for son:",i)

#----------------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
# Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.

for i in "pedro@gmail.com":
    if i == "@":
        break
    print(i, end=" ")

#----------------------------------------------------------------------------------------------------------------------------

print() # salto de linea
        
#------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
# Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

#----------------------------------------------------------------------------------------------------------------------------

print() # salto de linea
        
#------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print("El valor de n es:",n)

        
#------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)
    
#------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------")
for i in range(0, 6, 3):
    print(i)
    
