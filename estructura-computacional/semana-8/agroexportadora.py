
import statistics

print("EMPRESA AGROEXPORTADORA - REPORTE DE PRODUCCIÓN")

cantidad = int(input("Ingrese cantidad de productos: "))
productos = []
producciones = []
perdida = []
semestral = []
anual = []

print("Tipos de plaga presenciadas:")
print("-----------------------------------")
print("1.- P1: PLAGA AOO1 - Pérdida: 10%")
print("2.- P2: PLAGA AOO1 - Pérdida: 15%")
print("3.- P3: PLAGA AOO1 - Pérdida: 20%")
print("4.- P4: PLAGA AOO1 - Pérdida: 30%")
print("5.- Combo 1: PLAGA AOO1 + PLAGA AOO2 - Pérdida: 25%")
print("6.- Combo 2: PLAGA AOO3 + PLAGA AOO4 - Pérdida: 50%")
print("7.- Combo 3: PLAGA AOO1 + PLAGA A004 - Pérdida: 40%")

for i in range(cantidad):
    print(f"Ingrese datos del producto {i + 1}:")
    valor1 = str(input("Ingrese producto: "))
    productos.append(valor1)
    valor2 = float(input("Ingrese producción: "))
    producciones.append(valor2)
    plaga = int(input("Ingrese tipo de plaga: "))

    if plaga == 1:
        valor3 = valor2 * 0.1
    elif plaga == 2:
        valor3 = valor2 * 0.15
    elif plaga == 3:
        valor3 = valor2 * 0.2
    elif plaga == 4:
        valor3 = valor2 * 0.3
    elif plaga == 5:
        valor3 = valor2 * 0.25
    elif plaga == 6:
        valor3 = valor2 * 0.5
    else:
        valor3 = valor2 * 0.4

    perdida.append(valor3)

for i in range(cantidad):
    valor = 6 * (producciones[i] - perdida[i])
    semestral.append(valor)
    anual.append(valor * 2)

minimo = min(anual)
maximo = max(anual)
moda = statistics.mode(anual)

print("-------------------------")
print("Reporte de producción")
print("-------------------------")
print("1.- Reporte de producción semestral")
for i in range(cantidad):
    print(f"Producto: {productos[i]} - Producción: {semestral[i]}")

print("2.- Reporte de producción anual")
for i in range(cantidad):
    print(f"Producto: {productos[i]} - Producción: {anual[i]}")

print(f"3.- Mayor producción: {maximo}")
print(f"4.- Menor producción: {minimo}")
print(f"5.- Moda de las producciones: {moda}")
print("-------------------------")
print("Reporte de perdidas")
print("-------------------------")
for i in range(cantidad):
    print(f"Producto: {productos[i]} - Pérdida anual: {12 * perdida[i]}")
