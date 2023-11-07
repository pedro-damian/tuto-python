
print("------------SISTEMA DE VENTAS - LIBRERIA EL LAPICITO---------------------")

productos  = [ ["L001", "Lapiz", 1.50, 50], ["L002", "Lapicero", 2.00, 20], ["L003", "Regla", 1.20, 30], ["L004", "Borrador", 0.80, 60], ["L005", "Cuaderno A4", 3.50, 40], ["L006", "Folder", 2.30, 30], ["L007", "Plumon", 2.80, 10], ["L008", "Goma", 3.80, 20], ["L009", "Tajador", 0.50, 15], ["L010", "Corrector", 1.60, 40]]


nom = ""
cp = False
cant = 0
subtotal = 0
total = 0
cv = False
print("Bienvenido:)")
opt = input("Presione \"y\" para ingresar el nombre del cliente. Presione otra tecla para finalizar:")

print("----------------------------------------------")

if opt == "y":
    nom = input("Ingrese los datos del cliente:")
    print("Presiope \"y\" para ingresar un producto. Presione otra tecla para cancelar.")
    opt = input("Opción:")
    
    while opt == "y" and cp == False:    
        cod_p = input("Ingrese el código del producto:")
        for f in productos:
            if cod_p == f[0]:
                producto = f[1]
                precio = f[2]
                stock = f[3]
                
                print(f"Código: {f[0]}")
                print(f"Producto: {f[1]}")
                print(f"Precio: {f[2]}")
                print(f"Stock: {f[3]}")
                cp = True
                break
            
        if cp:
            opt = input("Presiope \"y\" para ingresar una cantidad. Presione otra tecla para cancelar:")

            if opt == "y":
                for f in productos:
                    stock = f[3]
                    precio = f[2]
                    
                    while True:
                        cant = int(input("Ingrese cantidad a comprar:")) 
                        if cant > stock:
                            print(f"Stock NO DISPONIBLE la cantidad disponible es: {stock}")
                        else:
                            opt = input("Presione \"y\" para obtener el subtotal. Presione otra tecla para cancelar:")
                            cv = True
                            break
                 
                    if opt == "y":
                        subtotal = precio * cant
                        print("\------------------------------")
                        print(f"Subtotal: {subtotal}")
                        print("\------------------------------")
                        
                    if cv:
                        boleta = input("¿Desea imprimir una boleta (Si = \"y\"/No = \"Otra tecla\")?")
                        
                    if boleta == "y":
                        total = subtotal
                        print("\n******BOLETA******\n")                                
                        print(f"Cliente: {nom}")
                        print(f"Cantidad: {cant}")
                        print(f"Subtotal: {subtotal}")
                        print(f"Total: {total}")
                    else:
                        break
                    
            else:
                break