

# Definir listas y variables
alumnos = []
ingresantes = 0
traslados = 0
nota_aprobado_total = 0
nota_desaprobado_total = 0
contador_aprobados = 0
contador_desaprobados = 0

# Ingreso de datos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
contador = 0

while contador < cantidad_alumnos:
    condicion = int(input(f"Ingrese la condición del alumno {contador + 1} (1=ingresante, 2=traslado): "))
    nota = float(input(f"Ingrese la calificación del alumno {contador + 1} (0 a 20): "))

    if condicion == 1:
        ingresantes += 1
    elif condicion == 2:
        traslados += 1

    if nota >= 14:
        nota_aprobado_total += nota
        contador_aprobados += 1
    else:
        nota_desaprobado_total += nota
        contador_desaprobados += 1

    contador += 1

# Cálculos
if contador_aprobados > 0:
    nota_promedio_aprobados = nota_aprobado_total / contador_aprobados
else:
    nota_promedio_aprobados = 0

if contador_desaprobados > 0:
    nota_promedio_desaprobados = nota_desaprobado_total / contador_desaprobados
else:
    nota_promedio_desaprobados = 0

# Mostrar resultados
print(f"Cantidad de alumnos ingresantes: {ingresantes}")
print(f"Cantidad de alumnos de traslado: {traslados}")
print(f"Nota promedio de los aprobados: {nota_promedio_aprobados}")
print(f"Nota promedio de los desaprobados: {nota_promedio_desaprobados}")
