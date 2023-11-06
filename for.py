
# por cada elemento dentro del rango del numero 20
for elemento in range(20):
    # imprimira cada numero del cero empezando del 0 a 19
    print(elemento)

# por cada elemento dentro del rango del numero 20
for elemento in range(1,20):
    # imprimira cada numero del 0 a 19
    print(elemento)


mi_tupla = ("pedro","luis","miguel")

# por cada elemento en mi tupla
for elemento in mi_tupla:
    # se imprimira cada elemento de mi tupla
    print("En mi tupla existen el elemento:",elemento)


mi_diccionario = {
    "nombre": "pedro",
    "edad": 32,
    "apellido": "damian"
}

# PRIMER METODO PARA RECORRER UN DICCONARIO
# por cada elemento en mi diccionario
for elemento in mi_diccionario:
    print(f"Para cada elemento en mi diccionario existen la llave {elemento} y su valor es {mi_diccionario[elemento]}")

# SEGUNDO METODO PARA RECORRER UN DICCIONARIO
# por cada elemento y valor en mi diccionario
for elemento, values in mi_diccionario.items():
    print(elemento, "=>" ,values)

# RECORRER UNA LISTA con DICCIONARIOS
aula = [
    {
        "aula": 101,
        "alumnos": 23,
        "seccion": "A"
    },
    {
        "aula": 102,
        "alumnos": 25,
        "seccion": "B"
    },
    {
        "aula": 103,
        "alumnos": 29,
        "seccion": "C"
    }
]

# por cada diccionario en la lista aula
for diccionario in aula:
    # por cada elemento y valor en el diccionario
    for elemento, valor in diccionario.items():
        # muestre el elemento y valor dentro del diccionario en la lista aula
        print(f"La llave de cada elemento es: {elemento} => {valor}")
    print("---------------------------")