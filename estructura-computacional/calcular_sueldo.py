     
cantidad_empleados = int(input("Ingrese el número de empleados: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

s_menor_700 = 0
s_700_1300 = 0
s_mayor_1300 = 0

for i in range(cantidad_empleados):
    horas = float(input(f"Ingrese las horas trabajadas por el empleado {i+1}: "))
    sueldo = horas * tarifa
    print(f"El sueldo del empleado {i+1} es S/.{sueldo}")

    if sueldo < 700:
        s_menor_700 += 1
    elif 700 <= sueldo <= 1300:
        s_700_1300 += 1
    else:
        s_mayor_1300 += 1
        
p_menor_700 = format((s_menor_700/cantidad_empleados)*100,'.2f')
p_700_1300 = format((s_700_1300/cantidad_empleados)*100,'.2f')
p_mayor_1300 = format((s_mayor_1300/cantidad_empleados)*100,'.2f')

print(f"Cantidad de empleados con sueldo menor a S/.700 es => {s_menor_700} ({p_menor_700}%)")
print(f"Cantidad de empleados con sueldo entre S/.700 y S/.1300 es => {s_700_1300} ({p_700_1300}%)")
print(f"Cantidad de empleados con sueldo mayor a S/.1300 es => {s_mayor_1300} ({p_mayor_1300}%)")

