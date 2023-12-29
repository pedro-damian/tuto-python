
# operador de igualdad (==)
# (=) es un operador de asignación.
# (==) es una pregunta son iguales?
# el resultado de la comparación es True o False
# sera True cuando los dos operandos sean iguales
# sera False cuando los dos operandos son diferentes

a = 2
b = 2
c = 3
print(a==b)
print(a==c)

# operador no es igual a (!=)
# compara los valores de dos operandos.
# el resultado de la comparación es True o False
# sera True cuando los dos operandos sean diferentes
# sera false cuando los dos operandos sean iguales

print(a!=b)
print(a!=c)

# Operadores de comparación: mayor que (>)
# True lo confirma; False lo niega.
print(a>c)
print(c>a)

# Operadores de comparación: mayor o igual que (>=)
# mayor o igual que
# prioridad es mayor que la mostrada por == y !=


# Operadores de comparación: menor o igual que (<=)
# menor o igual que


""" Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True si n es mayor o igual que 100. """


n= int(input("Ingrese un numero: "))
menor = n<100
mayor = n >=100
print(f"El numero es menor {menor} o mayor {mayor}")

