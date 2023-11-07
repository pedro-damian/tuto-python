

print("------------SISTEMA DE VENTAS - BODEGA TUTI---------------------")

# 
productos  = [ ["A01", "Arroz", 4.50], ["A02", "Azucar", 3.20], ["A03",
"Fideo", 3.10], ["A04", "Fideo", 2.50], ["A05","Leche", 6.50], ["A06",
"Atún", 1.20], ["A07", "Huevo", 5.50], ["A08", "Aceite", 8.0], ["A09",
"Cocoa", 2.0], ["A10", "Anís", 1.20]]
nom = ""
cp = False
cant = 0
subtotal = 0
vale = False
vales = [["V1", 0.05],["V2", 0.1],["V3",0.2],["V4", 0.3],["V5", 1]]
dsct = 0
total = 0
cv = False
print("Bienvenido:)")
opt = input("Presione \"a\" para ingresar el nombre del cliente. Presione otra tecla para finalizar:")

print("----------------------------------------------")

if opt == "a":
    nom = input("Ingrese los datos del cliente:")
    print("Presiope \"b\" para ingresar un producto. Presione otra tecla para cancelar.")
    opt = input("Opción:")
    
    while opt == "b" and cp == False:    
        cod_p = input("Ingrese el código del producto:")
        for f in productos:
            if cod_p == f[0]:
                
                producto = f[1]
                precio = f[2]
                
                print(f"Código: {f[0]}")
                print(f"Producto: {f[1]}")
                print(f"Precio: {f[2]}")
                cp = True
                break
        if cp:
            opt = input("Presiope \"c\" para ingresar una cantidad. Presione otra tecla para cancelar:")

            if opt == "c":
                cant = int(input("Ingrese cantidad a comprar:"))
                subtotal = precio * cant
                opt = input("Presiope \"d\" para obtener el subtotal\nPresione \"e\" para ingresar vale de descuento\nPresione otra tecla para cancelar:")

                if opt == "d":
                    print("\------------------------------")
                    print(f"Subtotal: {subtotal}")
                    print("\------------------------------")
                    opt = input("Presione \"e\" para ingresar vale de descuento\nPresione otra tecla para cancelar:")

                    if opt == "e":
                        vale = True
                    
                elif opt == "e":
                    vale = True
                else:
                    break

                if vale:

                    while vale == True and cv == False:                        
                        cod_vale = input("Ingrece código de vale:")

                        for f in vales:
                            if cod_vale == f[0]:
                                dsct = subtotal * f[1]
                                total = subtotal - dsct
                                print("\------------------------------")
                                print(f"Código de vale: {f[0]}")
                                print(f"Valor a descontar: {f[1]}")
                                print("\------------------------------")
                                cv = True
                                break

                        if cv:
                            boleta = input("¿Desea imprimir una boleta (Si = \"d\"/No = \"Otra tecla\")?")

                            if boleta == "d":
                                print("\n******BOLETA******\n")                                
                                print(f"Cliente: {nom}")
                                print(f"Cantidad: {cant}")
                                print(f"Subtotal: {subtotal}")
                                print(f"Descuento: {dsct}")
                                print(f"Total: {total}")
                            else:
                                break
                            
                        else:                           
                            cv = False
                            opt = input("No se encontró el vale ¿Desea ingresar otro código (Si = \"e\"/No = \"Otra tecla\")?")
                            if opt == "e":
                                vale = True
                            else:
                                vale = False
                
                    
            else:
                break
        else:
            print("--------------------------------------------------------")
            print("Error:No etá registrado el producto en la base de datos :(")
            print("--------------------------------------------------------")
            opt = input("Presiope \"b\" para ingresar un producto. Presione otra tecla para cancelar.")
        
        #end if
    
print("Gracias por utilizar nuestro sistema :)")
