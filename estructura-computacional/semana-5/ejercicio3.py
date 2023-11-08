""" Crear un programa que permita ingresar una gran cantidad de números enteros positivos y
calcule la cantidad de múltiplos de 3 y múltiplos de 7 encontrados en la relación de números
ingresados, El programa termina cuando se ingresa un número mayor a 100.
 """

# inicializa variables en cero
multiplos_de_tres = 0
multiplos_de_siete = 0
lista_numeros = []   # se crea una lista vacia

# mientras la condicion es verdadera
while True:
    # se crea un try para manejar los errores
    try:
        numero = int(input("Ingrese un número o un número mayor a 100 para salir: "))
        # si numero es menor a cero
        if numero < 0:
            # mostrara un mensaje de error 
            print("ERROR, ingrese un número mayor a 0.")
            continue # regresa el bucle al inicio ignorando el codigo siguiente
        
        # agrega el numero ingresado a la lista vacia
        lista_numeros.append(numero)
        
        # si numero es mayor a 100
        if numero > 100:
            # sale del bucle
            break
        # si numero es multiplo de 3
        if numero % 3 == 0:
            # entonces aumentara la variable en 1
            multiplos_de_tres += 1
        # si numero es multiplo de 7
        if numero % 7 == 0:
            # entonces aumentara la variable en 1
            multiplos_de_siete += 1
    # mostrara un mensaje de error si el dato ingresado no es numero
    except:
        print("ERROR de dato, ingrese un número entero positivo.")

print(f"La cantidad de múltiplos de 3 es: {multiplos_de_tres}")
print(f"La cantidad de múltiplos de 7 es: {multiplos_de_siete}")
