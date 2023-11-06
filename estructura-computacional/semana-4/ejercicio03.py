
# variables
multiplos_tres = 0
multiplos_siete = 0


while True:
    numero = int(input("Ingrese un número entero positivo o Ingrese un número mayor que 100 para terminar: "))
    if numero >= 100:
        break
    if numero % 3 == 0:
        multiplos_tres += 1
    if numero % 7 == 0:
        multiplos_siete += 1

print(f"La cantidad de múltiplos de 3 es: {multiplos_tres}")
print(f"La cantidad de múltiplos de 7 es: {multiplos_siete}")