
#>>>>>>>>>>>>>>>>>>> MULTIPLES RETURN en una FUNCION

def volumen_rectangulo(longitud, ancho, altura):
  volumen = longitud * ancho * altura
  return volumen, longitud, ancho, altura
  
resultado = volumen_rectangulo(10,20,30)
print(resultado)


# >>>>>>>>>>>>>>>>> CALCULADORA

operador = ['+','-', '*', '/']
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
op = input(f"Ingrese operador {operador}: ")

def calculadora(a,b):
  total = 0
  mensaje = ""
  if op == '+':
    total = a+b
  elif op == '-':
    total = a-b
  elif op == '*':
    total = a*b
  elif op == '/':
    if b !=0:
      total = a/b
    else:
      mensaje= "introduce un numero mayor a cero"
  """ else:
    mensaje = "Operador no valido"  """
    
  return total, mensaje

total, mensaje = calculadora(a,b)
print(f"total: {total}")
print(f"mensaje: {mensaje}")
