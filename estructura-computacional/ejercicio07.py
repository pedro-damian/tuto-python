
# solicita al usuario un numero de productos
productos = int(input("Ingrese el número de productos: "))

# inicializar variables
ganancia_comida = 0
ganancia_vestido = 0
mayor_precio_nacional = 0
# esta variable tiene un valor inicial que se utiliza para buscar el valor minimo
menor_precio_importado = float('inf')

# bucle que va iterar a traves del rango de productos ingresados
for i in range(productos):
  # solicita el tipo de producto entre comida c o vestido v
  tipo_producto = input(f"Elija el tipo del producto N°{i+1} donde C= comida, V= vestido: ").upper()
   # bucle while donde si no ingreso ninguna de las opciones 
  while tipo_producto not in ["C","V"]:
    # muestre el mensaje opcion incorrecta 
    print("Opcion incorrecta!!")
    # me vuelve a pedir el tipo de producto hasta que elija la opcion correcta
    tipo_producto = input(f"Elija el tipo del producto N°{i+1} donde C= comida, V= vestido: ").upper()
    
  # solicita la procedencia del producto N nacional o I importado
  procedencia = input(f"Elija la procedencia del producto N°{i+1} donde N= nacional, I=importado: ").upper()
  # bucle while donde si no ingreso ninguna de las opciones 
  while procedencia not in ["N","I"]:
    # muestre el mensaje opcion incorrecta 
    print("Opcion incorrecta!!")
    # me vuelve la procedencia hasta que elija la opcion correcta
    procedencia = input(f"Elija la procedencia del producto N°{i+1} donde N= nacional, I=importado: ").upper()
  
  # solicita el precio del producto
  precio = int(input(f"Ingrese el precio del producto N°{i+1}: "))
  
  # si tipo de producto es igual a "C"
  if tipo_producto == "C":
    # entonces que precio se vaya sumando y acumulando en la variable
    ganancia_comida +=precio
  # si tipo de producto es igual a "V"
  if tipo_producto == "V":
    # entonces que precio se vaya sumando y acumulando en la variable
    ganancia_vestido += precio
   
  # si procedencia es igual a "N" y precio es mayor al valor de la variable mayor_precio_nacional
  if procedencia == "N" and precio>mayor_precio_nacional:
    # entonces el nuevo valor de mayor_precio_nacional sera el precio ingresado
    mayor_precio_nacional = precio
  # si procedencia es igual a "I" y precio es menor al valor de la variable menor_precio_importado 
  if procedencia == "I" and precio < menor_precio_importado:
    # entonces el nuevo valor de menor_precio_importado sera el precio ingresado
    menor_precio_importado = precio
  
print(f'El mayor precio pagado por un producto Nacional es: {mayor_precio_nacional}')
print(f'El menor precio pagado por un producto Importado es: {menor_precio_importado}')
print(f'La ganancia total de dinero en comida es: {ganancia_comida}')
print(f'La ganancia total de dinero en vestido es: {ganancia_vestido}')