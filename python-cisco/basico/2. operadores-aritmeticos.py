
# POTENCIA (**)
# El argumento a la izquierda es la base, el de la derecha, el exponente. (2**3)
# Cuando ambos ** argumentos son enteros, el resultado es entero también.
# Cuando al menos un ** argumento es flotante, el resultado sera flotante.

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# MULTIPLICACION (*)
# Cuando ambos ** argumentos son enteros, el resultado sera entero.
# Cuando al menos un ** argumento es flotante, el resultado sera flotante.

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)


# DIVISION (/)
# El resultado producido por el operador de división siempre es flotante

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# DIVISION ENTERA (//)
# una división de entero entre entero da un resultado entero.
# si algunos de los argumentos es decimal el resultado sera decimal

print(20 // 5)
print(20 // 5.)
print(20. // 5)
print(20. // 5.)


# Division Inexacta
# si ambos numeros son enteros el resultado se redondea hacia abajo y dara un numero entero
# si uno es decimal el resultado se redondea hacia abajo y dara un numero decimal
print(6 // 4)
print(6. // 4)

# Division Numeros Negativos
# si uno de los numeros es negativo y son enteros el resultado se redondea hacia el valor valor inferior entero y sera negativo entero
# si uno de los numeros es negativo o decimal el resultado se redondea hacia el valor valor inferior entero y sera negativo decimal 
print(-6 // 4)
print(6. // -4)


# OPERADOR MODULO (%)
# El resultado de la operación es el residuo que queda de la división entera.
# si los dos numeros es entero el resultado sera entero
# si uno de los numeros es decimal el residuo sera decimal

print(14 % 4)  # el residuo es 2
print(12 % 4.5) # el residuo es 3.0

# SUMA (+)
# si los dos numeros son numeros enteros el resultado sera un numero entero
# si uno de los numeros es decimal el resultado sera un numero decimal


print(-4 + 4)
print(-4. + 8)

# RESTA (-)
# si los dos numeros es enteros el resultado sera entero
# si uno de los numeros es decimal el resultado sera decimal

print(-4 - 4)
print(4. - 8)


# OPERADOR UNARIO
# es un operador con un solo operando
print(-1.1)
print(+2)
# 1 dividido por 4 = 0.25 porque elevar un numero a un exponente negativo es igual a 1 dividido por ese numero elevado al exponente positivo
# osea 4 ** -1 = 1 / 4
print(4 ** -1) 

# JERARQUIA DE PRIORIDAD DE LOS OPERADORES
# 0 => () parentesis
# 1 => + | - => UNARIO
# 2 => ** => POTENCIA => de derecha a izquierda
# 3 => * | / | // | %  => de izquieda a derecha
# 4 => + | - => BINARIO => de izquieda a derecha

# DIRECCION DE OPERACIONES
# de izquierda a derecha
print(9 % 6 % 2)

# de derecha a izquierda
print(2 ** 2 ** 3)

# EJERCICIO
# ¿Cuál es la salida del siguiente programa?

print((2 ** 4), (2 * 4.), (2 * 4)) # 16 8.0 8

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # -0.5 0.5 0 -1

print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # -2 2 512



