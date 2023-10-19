
print("------------SISTEMA DE VENTAS - LIBRERIA EL LAPICITO---------------------")

productos  = [ ["L001", "Lapiz", 1.50, 50], ["L002", "Lapicero", 2.00, 20], ["L003", "Regla", 1.20, 30], ["L004", "Borrador", 0.80, 60], ["L005", "Cuaderno A4", 3.50, 40], ["L006", "Folder", 2.30, 30], ["L007", "Plumon", 2.80, 10], ["L008", "Goma", 3.80, 20], ["L009", "Tajador", 0.50, 15], ["L010", "Corrector", 1.60, 40]]



print("Bienvenido:)")
codigo = input("Ingresa el codigo del producto: ")

for f in productos:
    if codigo == f[0]:
                
        producto = f[1]
        precio = f[2]
        stock = f[3]
                
        print(f"Código: {f[0]}")
        print(f"Producto: {f[1]}")
        print(f"Precio: {f[2]}")
        print(f"Stock: {f[3]}")
        break