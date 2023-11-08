""" Se realiza un muestreo con N personas, de las cuales se registran sus edades y sus pesos. Se
pide elaborar un programa que calcule el promedio de pesos de las personas menores de 18
años y el promedio de pesos de los que tienen 18 años a mas. """


# solicita el numero de personas
num_personas = int(input("Ingrese la cantidad de personas: "))
# se crea dos listas vacias donde guardara el peso de menores de 18 y mayores de 18 años
pesos_menores_de_18 = []
pesos_mayores_de_18 = []

# recorre cada persona en el rango de la cantidad de personas ingresadas
for p in range(num_personas):
        # mientras la condicion sea verdadera
        while True:
                # solicita la edad de la persona
                edad = int(input(f"Ingrese la edad de la persona {p + 1}: "))
                # si edad es menor a cero
                if edad < 0:
                    # muestre un mensaje de error y vuelve iniciar la peticion
                    print("Por favor ingrese una edad mayor a cero.")
                    continue
                
                # solicita el peso de la persona
                peso = float(input(f"Ingrese el peso de la persona {p + 1}: "))
                # si peso es menor a cero
                if peso < 0:
                    # muestre un mensaje de error y vuelve a iniciar la peticion
                    print("Por favor ingrese un peso mayor a cero.")
                    continue
                
                # si edad es menor a 18
                if edad < 18:
                    # entonces el peso de la persona se agregara a la lista vacia peso_menores_18
                    pesos_menores_de_18.append(peso)
                # de los contrario
                else:
                    # el peso de la persona se agregara a la lista vacia peso_mayores_18
                    pesos_mayores_de_18.append(peso)
                break
            
# utilizamos bloques de manejo errores
try:
    # calculamos el promedio del peso de los menores de 18
    promedio_menores_de_18 = sum(pesos_menores_de_18) / len(pesos_menores_de_18)
except:
    # si en caso la lista pesos_menores_18 no tenga ningun valor almacenado
    # se establecera el promedio_menores_18 en cero
    promedio_menores_de_18 = 0

try:
    # calculamos el promedio del peso de los mayores de 18
    promedio_mayores_de_18 = sum(pesos_mayores_de_18) / len(pesos_mayores_de_18)
except:
    # si en caso la lista pesos_mayores_18 no tenga ningun valor almacenado
    # se establecera el promedio_mayores_18 en cero
    promedio_mayores_de_18 = 0

print(f"El promedio de pesos de personas menores de 18 años es: {promedio_menores_de_18} ")
print(f"El promedio de pesos de personas mayores de 18 años es: {promedio_mayores_de_18} ")
