

# Inicializar variables
num_ingresantes = 0
num_traslado = 0
suma_aprobados = 0
num_aprobados = 0
suma_desaprobados = 0
num_desaprobados = 0

# mientras la condicion sea true
while True:
    condicion = int(input("Elija una opcion para el alumno 1 = ingresante, 2 = traslado, 0 = terminar: "))

    # si condicion es igual a 0 
    if condicion == 0:
        # se detiene el ciclo
        break


    calificacion = float(input("Ingrese la calificación obtenida: "))

    # si condicion es igual a 1
    if condicion == 1:
        # entonces el numero de ingresantes aumentara en 1
        num_ingresantes += 1

    # tambien si condicion es igual 2
    elif condicion == 2:
        # entonces el numero de traslado aumentara en 1
        num_traslado += 1

    # si calificacion es mayor o igual a 14
    if calificacion >= 14:
        # entonces la suma de la calificaciones se iran sumando y guaradando en la variables suma_aprobados
        suma_aprobados += calificacion
        # tambien el numero de aprobados aumentarian en 1
        num_aprobados += 1
    else:
        # entonces la suma de la calificaciones se iran sumando y guaradando en la variables suma_desaprobados
        suma_desaprobados += calificacion
        # tambien el numero de desaprobados aumentarian en 1
        num_desaprobados += 1

# Calcular promedio
# si numeros de aprobados es mayor a 0
if num_aprobados > 0:
    # entonces nota promedio de los aprobados es igual a la division entre suma de aprobados y numero de aprobados
    nota_promedio_aprobados = suma_aprobados / num_aprobados
# de lo contrario
else:
    # sera 0 el valor 
    nota_promedio_aprobados = 0

# si numero de desaprobados es mayor a 0
if num_desaprobados > 0:
    # entonces nota promedio de los desaprobados es igual a la division entre suma de desaprobados y numero de desaprobados
    nota_promedio_desaprobados = suma_desaprobados / num_desaprobados
# de lo contrario
else:
    # sera 0 el valor 
    nota_promedio_desaprobados = 0


print(f"Cantidad de alumnos ingresantes: {num_ingresantes}")
print(f"Cantidad de alumnos traslado: {num_traslado}")
print(f"Nota promedio de los aprobados: {nota_promedio_aprobados}")
print(f"Nota promedio de los desaprobados: {nota_promedio_desaprobados}")
