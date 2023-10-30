
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

# ITEMS (cada par clave-valor) - KEYS (es la clave) - VALUES (es el valor)

mi_diccionario = {
  "nombre": "pedro",
  "apellido": "damian",
  "telefono": 987654321,
  "edad": 32,
  "idiomas": ['español','ingles','portugues']
}

print("--------------------------------------------------------------------")
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
print("--------------------------------------------------------------------")

# ------------------------------ CRUD ------------------------------------
# ----------------------------- CREATE ------------------------------------
aula = {
  "Alumnos": ['pedro','miguel','juan','jose'],
  "Profesor": "Jose martin",
  "materias": ['matematicas','lenguaje','ciencias'],
  "N_alumnos": 30,
  "grado": "primaria"
}

# ----------------------------- READ ------------------------------------

print(f"Los elementos del diccionario son => {aula}")
print(f"Los elementos par clave:valor del diccionario son {aula.items()}")
print(f"Los elementos clave del diccionario son {aula.keys()}")
print(f"Los elementos valor del diccionario son {aula.values()}")

# ----------------------------- UPDATE ------------------------------------
# modificando un valor a uno nuevo
aula['Profesor'] = 'Manuel perez'
# operando un valor
aula['N_alumnos'] -= 10
# agregando un valor nuevo
aula['materias'].append('calculo')
print("--------------------------------------------------------------------")
print(f"Llave unica actualizada se modifico el valor de profesor a {aula}")
print(f"Llave unica actualizada se realizo una operacion a N_alumnos {aula}")
print(f"Llave unica actualizada se agrego una nueva materia {aula}")
print("--------------------------------------------------------------------")
# ----------------------------- DELETE ------------------------------------
# elimina una llave unica del diccionario
del aula['grado']
# tambien elimina una llave unica del diccionario
aula.pop('N_alumnos')

print(f"Llaves unicas eliminadas grado y ")