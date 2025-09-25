
##### la sentencia if

#if sheep_counter >= 120: # #evalúa una expresión condicional
    #sleep_and_dream() #se ejecuta si la expresión condicional es True
    
    
##### condicional: la sentencia if-else
""" if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false """
    
#La ejecución de if-else es la siguiente:

# Si la condición se evalúa como True (su valor no es igual a cero), la instrucción perform_if_condition_true se ejecuta, y la sentencia condicional llega a su fin.
# Si la condición se evalúa como False (es igual a cero), la instrucción perform_if_condition_false se ejecuta, y la sentencia condicional llega a su fin.


##### Sentencias if-else anidadas
""" if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping() """
        
# Si hay buen clima, saldremos a caminar. Si encontramos un buen restaurante, almorzaremos allí. De lo contrario, vamos a comer un sandwich. Si hay mal clima, iremos al cine. Si no hay boletos, iremos de compras al centro comercial más cercano.


##### La sentencia elif
# elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera sentencia verdadera.

""" if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home() """
    
# si hay buen clima, saldremos a caminar, de lo contrario, si obtenemos entradas, iremos al cine, de lo contrario, si hay mesas libres en el restaurante, vamos a almorzar; si todo falla, regresaremos a casa y jugaremos ajedrez.



# ¿Cómo identificar el mayor de los dos números?
#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)


# encontremos el mayor de los tres números.
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)

