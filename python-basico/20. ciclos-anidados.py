
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