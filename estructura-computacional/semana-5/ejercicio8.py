
""" La oficina de climatología de nuestro país desea saber las siguientes características climatológicas en un mes determinado. Tome en cuenta que el mes tiene 30 días.
La temperatura mínima y máxima del mes.
Cuántos días la temperatura supero los 28 °C.
EI promedio de las temperaturas del mes. """


# se inicializa a float('inf') porque queremos encontrar el valor mínimo de una serie de números.
temp_min = float('inf')
# porque queremos encontrar el valor máximo de una serie de números.
temp_max = float('-inf')
dias_temp_superior_28 = 0
suma_temperaturas = 0

for i in range(30):
    
    continuar = input("¿Desea continuar? (s)(n): ").lower()
    if continuar.lower() != 's':
        break
      
    temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
    
    suma_temperaturas += temp
    if temp < temp_min:
        temp_min = temp
    if temp > temp_max:
        temp_max = temp
    if temp > 28:
        dias_temp_superior_28 += 1

promedio_temperaturas = round(suma_temperaturas / 30,2)

print("-"*30)
print("Informe climatológico:")
print("-"*30)
print(f"Temperatura mínima del mes: {temp_min}°C")
print(f"Temperatura máxima del mes: {temp_max}°C")
print(f"Días con temperatura superior a 28°C: {dias_temp_superior_28}")
print(f"Promedio de las temperaturas del mes: {promedio_temperaturas}°C")
print("-"*30)
