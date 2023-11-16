
frutas = ["fresa","naranja","piña","platano","manzana"]
frutas_menores_20 = []
frutas_menores_cantidad=[]
frutas_mayores_20 = []
frutas_mayores_cantidad=[]
frutas_total = []
precio_total = []

for fruta in frutas:
    cantidad= int(input("¿ingrese la cantidad de " + fruta + " : "))
    precio= float(input("¿ingrese el precio de " + fruta + " : "))
    total = cantidad*precio
    if cantidad <= 20:
        frutas_menores_20.append(fruta)
        frutas_menores_cantidad.append(cantidad)
        frutas_total.append(fruta)
        precio_total.append(total)
    else:
        frutas_mayores_20.append(fruta)
        frutas_mayores_cantidad.append(cantidad)
        frutas_total.append(fruta)
        precio_total.append(total)

print(f"las frutas menores de 20 son: {frutas_menores_20} y la cantidad es {frutas_menores_cantidad}")
print(f"las frutas mayores de 20 son: {frutas_mayores_20} y la cantidad es {frutas_mayores_cantidad}")
print(f"el total de frutas son: {frutas_total} y el precio total es {precio_total}")