
# inicializa variables en cero
multiplos_de_tres = 0
multiplos_de_siete = 0
numeros = []   # se crea una lista vacia

# mientras la condicion es
while True:
    try:
        numero = int(input("Ingrese un número o un número mayor a 100 para salir: "))
        if numero < 0:
            print("ingrese un número entero positivo.")
            continue
        numeros.append(numero)
        if numero > 100:
            break
        if numero % 3 == 0:
            multiplos_de_tres += 1
        if numero % 7 == 0:
            multiplos_de_siete += 1
    except ValueError:
        print("ingrese un número entero válido.")

print(f"La cantidad de múltiplos de 3 encontrados es: {multiplos_de_tres}")
print(f"La cantidad de múltiplos de 7 encontrados es: {multiplos_de_siete}")
