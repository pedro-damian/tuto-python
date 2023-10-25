# Inicializa
votos_a_favor = 0
votos_en_contra = 0
abstenciones = 0

# Pide los votos de los congresistas
total_congresistas = 120
i = 0

# Bucle donde i es menor que el total_congresistas
while i < total_congresistas:

    # Imprime el numero de congresitas que va votando
    print(f"Congresista {i + 1}")
    try:
        voto = int(input("Seleccione: 1 a favor, 2 en contra, 3 para abstenerse, 0 para finalizar la votación: "))
        if voto == 0:
            break  # Sale del bucle si se ingresa 0 
        elif voto == 1:
            votos_a_favor += 1
        elif voto == 2:
            votos_en_contra += 1
        elif voto == 3:
            abstenciones += 1
        else:
            print("Seleccione: 1 a favor, 2 en contra, 3 para abstenerse, 0 para finalizar la votación: ")
            continue
        i += 1
    # En caso de que eligan un numero incorrecto mostrara este mensaje de error 
    except ValueError:
        print("Por favor, ingrese un número válido (0, 1, 2 o 3).")

# Calcula los porcentajes de cada eleccion
porcentaje_a_favor = (votos_a_favor / total_congresistas) * 100
porcentaje_en_contra = (votos_en_contra / total_congresistas) * 100
porcentaje_abstenciones = (abstenciones / total_congresistas) * 100

# imprime los resultados
print(f"A favor: {votos_a_favor} congresistas ({porcentaje_a_favor:.2f}%)")
print(f"En contra: {votos_en_contra} congresistas ({porcentaje_en_contra:.2f}%)")
print(f"Abstenciones: {abstenciones} congresistas ({porcentaje_abstenciones:.2f}%)")
