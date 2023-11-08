""" Se ingresan los resultados de la evaluación del curso de Química; por cada alumno se informa: su condición (1 = ingresante, 2 = traslado) y su calificación obtenida que va de 0 a 20. Para estar aprobado debe tener una nota mínima de 14, A partir de esta información se debe mostrar:
• La cantidad de alumnos ingresantes y la cantidad de traslado.
• La nota promedio de los aprobados y la nota promedio de los desaprobados, EI programa termina cuando no se desea registrar más alumnos. """


# inicializa y declara variables
ingresantes = 0
traslados = 0
suma_notas_aprobados = 0  # luego se divide con cantidad de aprobados para el promedio
cantidad_aprobados = 0
suma_notas_desaprobados = 0  # luego se divide con cantidad de desaprobados para el promedio
cantidad_desaprobados = 0

while True:
    continuar = input("¿Desea registrar a un alumno? (s) o cualquier tecla para salir: ")
    # si continuar es diferente a "s" terminara el bucle
    if continuar.lower() != 's':
        break

    
    calificacion = float(input("Ingrese la calificación del alumno (0 a 20): "))
    # si calificacion es mayor o igual a 14 y menor o igual a 20
    if 14 <= calificacion <= 20:
        # entonces se iran sumando las notas aprobadas
        suma_notas_aprobados += calificacion
        # aumnetara los aprobados en 1
        cantidad_aprobados += 1
        # aumentara los ingresantes en 1
        ingresantes += 1
    # tambien si calificacion es mayor o igual a cero y menor a 14
    elif 0 <= calificacion < 14:
        # entonces se iran sumando las notas desaprobadas
        suma_notas_desaprobados += calificacion
        # aumnetara los desaprobados en 1
        cantidad_desaprobados += 1
        # aumentara los traslados en 1
        traslados += 1
    else:
        print("Ingreso una nota entre 0-20")
        continue

# bloque de control de errores
try:
    # calcular el promedio de los aprobados
    promedio_aprobados = suma_notas_aprobados / cantidad_aprobados
except:
    # en caso no exista un aprobado
    # el promedio se establece en 0
    promedio_aprobados=0

try:
    # calcular el promedio de los desaprobados
    promedio_desaprobados = suma_notas_desaprobados / cantidad_desaprobados
except:
    # en caso no exista un desaprobado
    # el promedio se establece en 0
    promedio_desaprobados=0


print(f"Cantidad de alumnos ingresantes: {ingresantes}")
print(f"Cantidad de alumnos de traslado: {traslados}")
print(f"Nota promedio de los aprobados: {promedio_aprobados}")
print(f"Nota promedio de los desaprobados: {promedio_desaprobados}")
