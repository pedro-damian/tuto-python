
# Solicitar al usuario un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Verificar si el número es negativo
if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")




