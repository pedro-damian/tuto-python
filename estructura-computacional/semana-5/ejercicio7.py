
""" En una prueba para obtener un puesto de trabajo como ingeniero de planta se establecen rangos de: 0 a 49, de 50 a 79 y de 80 a 100 puntos. Mostrar en un informe los siguientes datos:
a) La cantidad de postulantes que se ubicaron en cada uno de los rangos.
b) El total de postulantes que rindieron la prueba.
EI programa termina cuando no desea registrar más postulantes. """

rango1 = 0
rango2 = 0
rango3 = 0
total_postulantes = 0

while True:
    continuar = input("¿Desea registrar postulantes? (s)(n): ").lower()
    # si continuar es diferente a "s" terminara el bucle
    if continuar.lower() != 's':
        break
      
    # mientras la condicion sea verdadera
    while True:
        puntaje = int(input("Ingrese el puntaje del postulante (0 - 100): "))
        # si puntaje esta entre 0 y 100 sale de este bucle
        if 0 <= puntaje <= 100:
            break
        # de lo contrario continuara mostrando este mensaje y volviendo a pedir el puntaje
        else:
            print("Puntaje incorrecto. Introduce un puntaje de 0-100.")

    total_postulantes += 1

    if 0 <= puntaje <= 49:
        rango1 += 1
    elif 50 <= puntaje <= 79:
        rango2 += 1
    elif 80 <= puntaje <= 100:
        rango3 += 1

print("-"*30)
print("Informe de postulantes:")
print("-"*30)
print(f"Rango 0-49: {rango1} postulantes")
print(f"Rango 50-79: {rango2} postulantes")
print(f"Rango 80-100: {rango3} postulantes")
print(f"Total de postulantes: {total_postulantes}")
print("-"*30)

