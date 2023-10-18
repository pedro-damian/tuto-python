
# A veces para comparar numeros flotantes se vuelven muy tedioso

x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

# El resultado sera falso 
print(x==y)

# PRIMER METODO
# convertimos a string el valor de la variable y
y_str = format(y, ".2g")
# Tambien convertimos a string el valor de la variable x
# Asi comparamos los valores y nos da true
print(y_str == str(x))

# SEGUNDO METODO
print(x,y)

tolerancia = 0.00001
print(abs(x-y)<tolerancia)