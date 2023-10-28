
# solicita al usuario el numero de empleados
cantidad_empleados = int(input("Ingrese el número de empleados: "))
# Solicita la tarifa unica para todos los empleados
tarifa = float(input("Ingrese la tarifa por hora: "))

# inicializar variables
s_menor_700 = 0
s_700_1300 = 0
s_mayor_1300 = 0

# bucle que va iterar a traves del range de empleados ingresados
for i in range(cantidad_empleados):
    # solicita las horas trabajadas del empleado
    horas = int(input(f"Ingrese las horas trabajadas por el empleado {i+1}: "))
    sueldo = horas * tarifa
    # imprimiendo la cantidad total del sueldo
    print(f"El sueldo del empleado {i+1} es S/.{sueldo}")

    # si el sueldo es menor a 700
    if sueldo < 700:
        # entonces que se vaya sumando y acumulando en la variable
        s_menor_700 += 1
    # si el sueldo es mayor o igual a 700 y menor o igual a 1300
    elif 700 <= sueldo <= 1300:
        # entonces que se vaya sumando y acumulando en la variable
        s_700_1300 += 1
    # de lo contrario no es ninguno de casos anteriones
    else:
        # entonces que se vaya sumando y acumulando en la variable
        s_mayor_1300 += 1
        
# Calculamos el porcentaje para cada caso 
# para eso dividimos la cantidad total del sueldo de cada caso entre el numero de empleados multiplicado por 100
# aqui redondea al resultado a dos decimales
p_menor_700 = round((s_menor_700/cantidad_empleados)*100, 2)
p_700_1300 = round((s_700_1300/cantidad_empleados)*100, 2)
p_mayor_1300 = round((s_mayor_1300/cantidad_empleados)*100, 2)

print(f"Cantidad de empleados con sueldo menor a S/.700 es => {s_menor_700} ({p_menor_700}%)")
print(f"Cantidad de empleados con sueldo entre S/.700 y S/.1300 es => {s_700_1300} ({p_700_1300}%)")
print(f"Cantidad de empleados con sueldo mayor a S/.1300 es => {s_mayor_1300} ({p_mayor_1300}%)")

