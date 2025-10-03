
# BUCLES
# Si la condición es False (igual a cero) el cuerpo no se ejecuta ni una sola vez
# si la condición es True al principio, el cuerpo podría funcionar continuamente hasta el infinito

""" mientras haya algo que hacer
  hazlo """
  
# Un bucle infinito
# denominado bucle sin fin
# Es un bucle que no puede finalizar su ejecución

""" while True:
    print("Estoy atrapado dentro de un bucle.") """
    
    
# ESTE CODIGO ENTRA EN UN BUCLE WHILE DONDE PIDE UN NUMERO MAYOR TERMINARA HASTA QUE INGRESES -1 Y MOSTRARA EL NUMERO MAYOR INGRESADO 

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number)

#----------------------------------------------------------------------------------------------------------------------------
# SI CONTADOR ES DIFERENTE A 0 ENTRARA EN UN BUCLE DESCENDENTE HASTA LLEGAR A 0 Y TERMINAR EL BUCLE AUTOMATICAMENTE
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#----------------------------------------------------------------------------------------------------------------------------
# ES EL MISMO EJERCICIO ANTERIOR PERO DE FORMA ABREVIADA 
counter = 5
# aqui no especificamos la condicion ya que se cerrara de forma automatica
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#----------------------------------------------------------------------------------------------------------------------------

# Un programa que lee una secuencia de números  y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)

#----------------------------------------------------------------------------------------------------------------------------

""" Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:
- Pedirá al usuario que ingrese un número entero.
- Utilizará un bucle while.
- Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!"  y se le solicitará que ingrese un número nuevamente. 
- Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".
 """

### SOLUCION N1
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

secret_number = 777
numero = int(input("ingrese el numero secreto para terminar el juego: "))

while numero != secret_number:
    print("¡Ja, Ja! ¡estas atrapado en mi bucle!")
    numero = int(input("ingrese el numero secreto para terminar el juego: "))

print("El numero secreto es: ", secret_number, "¡Bien hecho, muggle! Eres libre ahora!")

### SOLUCION N2
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

secret_number = 777
number = int(input("Introduce un número o escribe 0 para detener: "))
while number != 0:
    if number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        number = False
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        number = int(input("Introduce un número o escribe 0 para detener: "))


#----------------------------------------------------------------------------------------------------------------------------

# Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla
x = 1
while x < 11:
    if x%2 !=0:
        print(x)
    x+=1
    
#------------------------------------------------------------------------------------------------------------

n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)