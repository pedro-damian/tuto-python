
productos = int(input("Ingrese el número de productos: "))

chico = 0
mediano = 0
grande = 0
plastico = 0
carton = 0

for i in range(productos):
    tamaño = input(f"Elija el tamaño del producto N°{i+1} donde S= pequeño, M= mediano, L= grande: ")
    while tamaño not in ["S","M","L"]:
      print("Opcion Incorrecta, elija S= pequeño, M= mediano, L= grande")
      tamaño = input(f"Elija el tamaño del producto N°{i+1} donde S= pequeño, M= mediano, L= grande: ")
      
    if tamaño == "S":
      chico +=1
    elif tamaño == "M":
      mediano +=1
    elif tamaño == "L":
      grande +=1
      
  
    material = input(f"Elija el material del producto N°{i+1} P= plastico, C= carton: ")
    while material not in ["P","C"]:
      print("Opcion Incorrecta, elija P= plastico, C= carton")
      material = input(f"Elija el material del producto N°{i+1} P= plastico, C= carton: ")
      
    if material == "P":
      plastico +=1
    elif material == "C":
      carton +=1
      
  
p_cajas_chicas = format((chico/productos)*100,'.2f')
p_cajas_medianas = format((mediano/productos)*100,'.2f')
p_cajas_grandes = format((grande/productos)*100,'.2f')
  
print(f"La cantidad de cajas de plastico es {plastico}")
print(f"La cantidad de cajas de cartón es {carton}")
print(f"La cantidad de cajas chicas es {chico} ({p_cajas_chicas}%)")
print(f"La cantidad de cajas medianas es {mediano} ({p_cajas_medianas}%)")
print(f"La cantidad de cajas grandes es {grande} ({p_cajas_grandes}%)")
