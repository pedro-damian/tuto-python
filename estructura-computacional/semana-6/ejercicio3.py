
productos = ["arroz","azucar","fideo"]
producto_mayor_50 =[]

for producto in productos:
    kilos= float(input("¿cuanto pesa el: " + producto + "? : "))
    if kilos > 50:
        producto_mayor_50.append(producto)
for producto in producto_mayor_50:
    productos.remove(producto)

print("los productos menos de 50kg son " + str(productos))