
# ----------------------------------------- DICCIONARIOS { } -------------------------------------------
# es una estructura de datos
# utiliza llaves { } para encerrar la clave unica y valores
# permite almacenar y organizar elementos en pares de clave-valor
# esto quiere decir que tendra una clave unica y valor asociado 
# se puede acceder a sus valores utilizando la clave unica donde se devolvera el valor
# son mutables

""" mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
} """

mi_diccionario = {
  "nombre": "pedro",
  "apellido": "damian",
  "telefono": 987654321,
  "edad": 32
}

print(f"Los elementos de mi diccionario son {mi_diccionario} y es de tipo {type(mi_diccionario)}", )

# metodo len()
print(f"La cantidad de elementos en mi diccionario son: {len(mi_diccionario)} ")

# imprimir los valores de mi diccionario
print(f"Mi nombre es {mi_diccionario['nombre']}, mi apellido es {mi_diccionario['apellido']}, mi edad es {mi_diccionario['edad']}")

# para prevenir un error podemos utilizar el metodo get()
print(f"La clave unica direccion se encuentra en el diccionario => {mi_diccionario.get('direccion')}")

# tambien puedes verificar si el elemento se encuentra en el diccionario con boolean
print(f"El diccionario tiene la clave unica direccion => {'direccion' in mi_diccionario}")
print(f"El diccionario tiene la clave unica nombre => {'nombre' in mi_diccionario}")