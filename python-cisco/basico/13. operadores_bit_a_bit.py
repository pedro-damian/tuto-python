
# OPERADORES BIT A BIT
# los argumentos de estos operadores deben ser enteros. No debemos usar flotantes aquí.
# los operadores lógicos no penetran en el nivel de bits de su argumento. Solo les interesa el valor entero final.
# Los operadores bit a bit son más estrictos: tratan con cada bit por separado


# &  (ampersand) - conjunción a nivel de bits.
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

# |  (barra vertical) - disyunción a nivel de bits.
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1

# ~  (tilde) - negación a nivel de bits.
# ~ 0 = 1
# ~ 1 = 0
 
# ^  (signo de intercalación) - o exclusivo a nivel de bits (xor).
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0