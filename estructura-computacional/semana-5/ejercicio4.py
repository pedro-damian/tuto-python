""" Se realiza un muestreo con N personas, de las cuales se registran sus edades y sus pesos. Se
pide elaborar un programa que calcule el promedio de pesos de las personas menores de 18
años y el promedio de pesos de los que tienen 18 años a mas. """



if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de personas en el muestreo: "))
    pesos_menores_de_18 = []
    pesos_mayores_de_18 = []

    for i in range(n):
        while True:
            try:
                edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
                peso = float(input(f"Ingrese el peso de la persona {i + 1} en kilogramos: "))
                if edad < 0 or peso < 0:
                    print("Por favor ingrese valores positivos.")
                    continue
                if edad < 18:
                    pesos_menores_de_18.append(peso)
                else:
                    pesos_mayores_de_18.append(peso)
                break
            except ValueError:
                print("Por favor ingrese valores numéricos válidos.")

    promedio_menores_de_18 = sum(pesos_menores_de_18) / len(pesos_menores_de_18) if pesos_menores_de_18 else 0
    promedio_mayores_de_18 = sum(pesos_mayores_de_18) / len(pesos_mayores_de_18) if pesos_mayores_de_18 else 0

    print(f"El promedio de pesos de personas menores de 18 años es: {promedio_menores_de_18} kilogramos.")
    print(f"El promedio de pesos de personas de 18 años o más es: {promedio_mayores_de_18} kilogramos.")
