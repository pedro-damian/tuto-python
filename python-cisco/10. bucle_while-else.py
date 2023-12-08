
# BUCLE WHILE-ELSE
# Los bucles también pueden tener la rama else, como los if. (rara vez se usa)
# La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
    

""" Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente. """


bloques = int(input("Ingresa la cantidad de bloques: "))
# crea y inicializa la variable altura
altura = 0
# esta variable representa cuantos bloques se necesita para contruir la siguiente capa
bloques_en_capa = 1

# mientras bloques sea mayor que bloques-en-capa
while bloques >= bloques_en_capa:
    # los bloques disminuyen en 1
    bloques -= bloques_en_capa
    # la altura incrementa en 1
    altura += 1
    # aqui aumenta los bloques necesarios para construir la siguiente capa
    bloques_en_capa += 1

print("La altura de la pirámide es:", altura)