# Una fábrica de cajas registra los N productos elaborados, para esto ingresa en un proceso repetitivo: el tamaño (chico, mediano o grande) y el material (plástico o cartón). Construya un programa que permita mostrar:
# a) Cantidad de cajas de plástico y de cartón.
# b) EI porcentaje de cajas chicas, medianas y grandes elaboradas.



# solicita al usuario el numero de productos
productos = int(input("Ingrese el número de productos: "))

# inicializamos variables
chico = 0
mediano = 0
grande = 0
plastico = 0
carton = 0

# bucle que va iterar con cada numero de productos ingresado 
for i in range(productos):
    # solicita al usuario que ingrese una de las 3 opciones
    tamaño = input(f"Elija el tamaño del producto N°{i+1} donde S= pequeño, M= mediano, L= grande: ").upper()
    # bucle while donde si no ingreso ninguna de las opciones 
    while tamaño not in ["S","M","L"]:
      # muestre el mensaje opcion incorrecta 
      print("Opcion Incorrecta, elija S= pequeño, M= mediano, L= grande")
      # ingrese de nuevo una de las 3 opciones
      tamaño = input(f"Elija el tamaño del producto N°{i+1} donde S= pequeño, M= mediano, L= grande: ").upper()
      
    # si tamaño es igual "S"
    if tamaño == "S":
      # entonces que se vaya sumando y acumulando en la variable
      chico +=1
    # si tamaño es igual "M"
    elif tamaño == "M":
      # entonces que se vaya sumando y acumulando en la variable
      mediano +=1
    # si tamaño es igual "L"
    elif tamaño == "L":
      # entonces que se vaya sumando y acumulando en la variable
      grande +=1
      
    # # solicita al usuario que elija si es de material carton o plastico
    material = input(f"Elija el material del producto N°{i+1} P= plastico, C= carton: ").upper()
     # bucle while donde si no ingreso ninguna de las opciones
    while material not in ["P","C"]:
      # muestre el mensaje opcion incorrecta
      print("Opcion Incorrecta, elija P= plastico, C= carton")
      
      material = input(f"Elija el material del producto N°{i+1} P= plastico, C= carton: ").upper()
      
    # si material es igual "P"
    if material == "P":
      # entonces que se vaya sumando y acumulando en la variable
      plastico +=1
    # si material es igual "P"
    elif material == "C":
      # entonces que se vaya sumando y acumulando en la variable
      carton +=1
      
# calculamos el porcentaje de cajas chicas, medianas y grandes
# se divide la cantidad de cada tamaño de caja entre el total de productos
p_cajas_chicas = round((chico/productos)*100,2)
p_cajas_medianas = round((mediano/productos)*100,2)
p_cajas_grandes = round((grande/productos)*100,2)
  
print(f"La cantidad de cajas de plastico es {plastico}")
print(f"La cantidad de cajas de cartón es {carton}")
print(f"La cantidad de cajas chicas es {chico} ({p_cajas_chicas}%)")
print(f"La cantidad de cajas medianas es {mediano} ({p_cajas_medianas}%)")
print(f"La cantidad de cajas grandes es {grande} ({p_cajas_grandes}%)")
