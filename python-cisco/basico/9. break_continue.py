
# BREAK 
# sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle
# se implementa para salir/terminar un bucle.
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# CONTINUE
# se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# EJERCICIOS DE LABORATORIO

""" La instrucción break se implementa para salir/terminar un bucle.
Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el bucle con éxito". Debe imprimirse en la pantalla y el bucle debe terminar. """

palabra= input("Ingrese la palabra secreta para salir del bucle: ")
while True:
    if palabra == "chupacabra":
        break
    else:
        palabra= input("Ingrese la palabra secreta para salir del bucle: ")
    
print("¡Has dejado el bucle con éxito")



""" Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:
Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La sentencia continue.
Tu programa debe:
Pedir al usuario que ingrese una palabra.
Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes. Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada. """

# Indicar al usuario que ingrese una palabra
user_word = input("ingrese una palabra: ")
# y asignarlo a la variable user_word.
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
      continue         
    elif letter == "E":
      continue
    elif letter == "I":
      continue
    elif letter == "O":
      continue
    elif letter == "U":
      continue
        
    print(letter, end=" ")


""" Escribe un programa que use:
Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La instrucción continue.
Tu programa debe:
Pedir al usuario que ingrese una palabra.
Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels. """


word_without_vowels = []

# Indicar al usuario que ingrese una palabra
user_word = input("ingrese una palabra: ")
# y asignarla a la variable user_word.
user_word = user_word.upper()


for letter in user_word:
   # Completa el cuerpo del bucle.
    if letter == "A":
        word_without_vowels.append(letter)
        continue
    elif letter == "E":
        word_without_vowels.append(letter)
        continue
    elif letter == "I":
        word_without_vowels.append(letter)
        continue
    elif letter == "O":
        word_without_vowels.append(letter)
        continue
    elif letter == "U":
        word_without_vowels.append(letter)
        continue

    print(letter, end=" ")
# Imprimir la palabra asignada a word_without_vowels.
print("\n",word_without_vowels)

