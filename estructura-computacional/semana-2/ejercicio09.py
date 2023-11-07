# Se registran las N aulas de la sección secundaria de un centro educativo, y por cada sección se registran las notas finales de sus M alumnos. Elaborar un programa que muestre el apellido del mejor alumno de cada aula y el promedio general de la misma aula.



# solicita al usuario el numero de aulas
n_aulas = int(input("Ingrese el número de aulas: "))

# bucle que va iterar con cada numero de aula ingresado 
for a in range(n_aulas):
    # se crea la variable aula que almacenara la seccion del aula
    aula = input(f"Ingrese la seccion del aula {a+1}: ")
    # solicita al usuario el numero de estudiantes del aula
    n_estudiantes = int(input(f"Ingrese el número de estudiantes en el aula {aula}: "))
    
    # se crea 2 listas vacias que almacenaran apellidos y notas
    apellidos = []
    notas = []

    # bucle que va iterar por cada estudiante en el aula
    for e in range(n_estudiantes):
        # solicita al usuario que ingrese el apellido del alumno
        apellido = input(f"Ingrese el apellido del estudiante {e+1}: ")
        # solicita que ingrese la nota final del estudiante
        nota_final = int(input(f"Ingrese la nota final del estudiante {e+1}: "))
        
        # los datos de apellidos y notas finales se agregaran a las lista apellidos y notas respectivamente
        apellidos.append(apellido)
        notas.append(nota_final)

    # Calcula el promedio de las notas utilizando la funcion sum (sumara todas las notas) entre la funcion len (cantidad de elementos en la lista)
    promedio = sum(notas) / len(notas)
    # Encuentrar al estudiante con la nota más alta por el metodo index y la funcion max
    indice_mejor_estudiante = notas.index(max(notas))
    # Usa el índice para encontrar el apellido del estudiante con la nota más alta
    mejor_estudiante = apellidos[indice_mejor_estudiante]

    print(f"En el aula {aula}, el mejor estudiante es {mejor_estudiante} y el promedio general del aula es {promedio:.2f}")
