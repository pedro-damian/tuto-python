
productos = int(input("Ingrese el número de productos: "))

ganancia_comida = 0
ganancia_vestido = 0
mayor_precio_nacional = 0
menor_precio_importado = float('inf')

for i in range(productos):
  
  tipo_producto = input(f"Elija el tipo del producto N°{i+1} donde C= comida, V= vestido: ").upper()
  
  while tipo_producto not in ["C","V"]:
    print("Opcion incorrecta!!")
    tipo_producto = input(f"Elija el tipo del producto N°{i+1} donde C= comida, V= vestido: ").upper()
    
  procedencia = input(f"Elija la procedencia del producto N°{i+1} donde N= nacional, I=importado: ").upper()
  
  while procedencia not in ["N","I"]:
    print("Opcion incorrecta!!")
    procedencia = input(f"Elija la procedencia del producto N°{i+1} donde N= nacional, I=importado: ").upper()
    
  precio = int(input(f"Ingrese el precio del producto N°{i+1}: "))
  
  if tipo_producto == "C":
    ganancia_comida +=precio
  if tipo_producto == "V":
    ganancia_vestido += precio
   
  if procedencia == "N" and precio>mayor_precio_nacional:
    mayor_precio_nacional = precio
  if procedencia == "I" and precio < menor_precio_importado:
    menor_precio_importado = precio
  
print(f'El mayor precio pagado por un producto Nacional es: {mayor_precio_nacional}')
print(f'El menor precio pagado por un producto Importado es: {menor_precio_importado}')
print(f'La ganancia total de dinero en comida es: {ganancia_comida}')
print(f'La ganancia total de dinero en vestido es: {ganancia_vestido}')