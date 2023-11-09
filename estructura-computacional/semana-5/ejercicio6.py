
""" Un agricultor que siembra diferentes tipos de frutas necesita obtener la siguiente información:
La manzana que tuvo el mayor peso.
El promedio de pesos de las papayas.
El porcentaje de las sandías producidas que pesaron menos de 2.5 kilogramos comparado con el total de sandías producidas.
El proceso termina cuando se ingresa un peso con el valor de cero. """

peso_max_manzana = 0
suma_papayas = 0
papayas = 0
sandias = 0
sandias_menor_2_5 = 0

while True:
    # Entrada de datos
    fruta = input("Ingrese el tipo de fruta (manzana, papaya, sandia): ").lower()
        
        # Si la fruta no es una de las aceptadas, volver a pedir
    while fruta not in ["manzana", "papaya", "sandia"]:
      print("Fruta no reconocida")
      fruta = input("Ingrese el tipo de fruta (manzana, papaya, sandia): ").lower()
    
    peso = float(input(f"Ingrese el peso de la {fruta}: "))
    
    # Si el peso es cero, terminar el proceso
    if peso == 0:
        break

    # Procesar información de acuerdo al tipo de fruta
    if fruta == "manzana":
        if peso > peso_max_manzana:
            peso_max_manzana = peso
    elif fruta == "papaya":
        suma_papayas += peso
        papayas += 1
    elif fruta == "sandia":
        sandias += 1
        if peso < 2.5:
            sandias_menor_2_5 += 1


# Calcular promedio de pesos de las papayas
try:
    promedio_papayas = suma_papayas / papayas
except:
    promedio_papayas = 0

# Calcular porcentaje de sandías que pesaron menos de 2.5 kg
try:
    porcentaje_sandias = (sandias_menor_2_5 / sandias) * 100
except:
    porcentaje_sandias = 0


# Imprimir resultados
print("La manzana que tuvo el mayor peso: ", peso_max_manzana)
print("El promedio de pesos de las papayas: ", promedio_papayas)
print("El porcentaje de las sandías que pesaron menos de 2.5 kilogramos: ", porcentaje_sandias,"%")
