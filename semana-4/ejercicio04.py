
# Inicializar listas
pesos_menores = []
pesos_mayores = []
n = int(input("Ingrese la cantidad de personas: "))
c = 0


while c < n:
    edad = int(input(f"Ingrese la edad de la persona {c + 1}: "))
    peso = float(input(f"Ingrese el peso de la persona {c + 1}: "))
    if edad < 18:
        pesos_menores.append(peso)
    else:
        pesos_mayores.append(peso)
    c += 1

# Calcular promedios
if len(pesos_menores) > 0:
    promedio_pesos_menores = sum(pesos_menores) / len(pesos_menores)
else:
    promedio_pesos_menores = 0

if len(pesos_mayores) > 0:
    promedio_pesos_mayores = sum(pesos_mayores) / len(pesos_mayores)
else:
    promedio_pesos_mayores = 0

# Mostrar resultados
print(f"El promedio de pesos de personas menores de 18 años es: {promedio_pesos_menores}")
print(f"El promedio de pesos de personas de 18 años o más es: {promedio_pesos_mayores}")