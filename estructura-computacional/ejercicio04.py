  
# solicita al usuario el numero de empleados
empleados = int(input("Ingrese el número de empleados: "))

# inicializamos variables
hombres = 0
mujeres = 0
mujeres_menos_800 = 0
mayor_sueldo_hombre = 0
nombre_mayor_sueldo_hombre = ""

# bucle que va iterar a traves del rango de empleados ingresados
for i in range(empleados):
    # solicita el nombre del empleado
    nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
    # solicita el sexo del empleado 
    sexo = input(f"Ingrese el sexo del empleado {i+1} (M = masculino, F = femenino): ").upper()
    # solicita el salario que corresponde al empleado
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))

    # si sexo igual a "M"
    if sexo == 'M':
        # entonces que se vaya sumando y acumulando en la variable
        hombres += 1
        # si salario es mayor al valor de la variable mayor_sueldo_hombre
        if salario > mayor_sueldo_hombre:
            # entonces la variable mayor_sueldo_hombre tendra el valor del salario ingresado
            mayor_sueldo_hombre = salario
            # tambien el nombre del empleado se almacenara en la variable nombre_mayor_sueldo_hombre
            nombre_mayor_sueldo_hombre = nombre
            
    # en este caso si sexo es igual a "F"
    elif sexo == 'F':
        # entonces que se vaya sumando y acumulando en la variable
        mujeres += 1
        # si salario es menor a 800
        if salario < 800:
            # entonces que se vaya sumando y acumulando en la variable
            mujeres_menos_800 += 1
   
# Calculamos el porcentaje de las mujeres que ganan menos de 800
# se divide la cantidad de mujeres que ganan menos de 800 entre la cantidad de mujeres 
# redondea el resultado a dos decimales          
p_mujeres_menos_800 = round((mujeres_menos_800/mujeres)*100, 2)

print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")
print(f"Porcentaje de mujeres que ganan menos de 800 soles: {p_mujeres_menos_800}%")
print(f"Nombre del hombre con mayor sueldo: {nombre_mayor_sueldo_hombre}")

