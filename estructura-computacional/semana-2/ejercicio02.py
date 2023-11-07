
# solicita al usuario el numero de personas
n_personas = int(input("Ingrese el número de personas: "))

# inicializar variables
total_10_30 = 0
total_31_50 = 0
total_51_mas = 0
sin_descuento = 0

# bucle que va iterar a traves del rango de personas ingresado 
for i in range(n_personas):
    # solicita al usuario que ingrese la edad de la persona
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    # solicita al usuario que ingreso el  
    pago = float(input(f"Ingrese el pago de la entrada de la persona {i+1}: "))

    # si la edad es mayor o igual a 10 y menor o igual a 30 años
    if 10 <= edad <= 30:
        # entonces se aplica el descuento de 2%
        total_10_30 += pago * 0.98  
     # si la edad es mayor o igual a 31 y menor o igual a 50 años
    elif 31 <= edad <= 50:
        # entonces se aplica el descuento de 3%
        total_31_50 += pago * 0.97  
    # si la edad es mayor o igual a 51 
    elif edad >= 51:
        # entonces se aplica el descuento de 5%
        total_51_mas += pago * 0.95  
    else:
        sin_descuento += pago


print(f"Total recaudado en el rango de edad 10-30 con el descuento de 2% es: {total_10_30:.2f}")
print(f"Total recaudado en el rango de edad 31-50 con el descuento de 3% es: {total_31_50:.2f}")
print(f"Total recaudado en el rango de edad 51 o más con el descuento de 5% es: {total_51_mas:.2f}")
print(f"Cantidad recaudada sin descuento: {sin_descuento:.2f}")
