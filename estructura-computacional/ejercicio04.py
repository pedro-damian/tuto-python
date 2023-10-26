  
    
empleados = int(input("Ingrese el número de empleados: "))

hombres = 0
mujeres = 0
mujeres_menos_800 = 0
mayor_sueldo_hombre = 0
nombre_mayor_sueldo_hombre = ""

for i in range(empleados):
    nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
    sexo = input(f"Ingrese el sexo del empleado {i+1} (M para masculino, F para femenino): ").upper()
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))

    if sexo == 'M':
        hombres += 1
        if salario > mayor_sueldo_hombre:
            mayor_sueldo_hombre = salario
            nombre_mayor_sueldo_hombre = nombre
    elif sexo == 'F':
        mujeres += 1
        if salario < 800:
            mujeres_menos_800 += 1
            
p_mujeres_menos_800 = format((mujeres_menos_800/mujeres)*100, '.2f')

print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")
print(f"Porcentaje de mujeres que ganan menos de 800 soles: {p_mujeres_menos_800}%")
print(f"Nombre del hombre con mayor sueldo: {nombre_mayor_sueldo_hombre}")

