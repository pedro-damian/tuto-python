
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
# IMPRIMIRA 2 y 5 (el tercer argumento son saltos)
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