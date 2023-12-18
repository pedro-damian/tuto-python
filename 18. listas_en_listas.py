
# comprensión de listas

row = []


for i in range(8):
    # agrega la cadena 8 veces a la lista vacia row[]
    row.append("peon blanco")
print(row)

# EJEMPLO DE COMPRESION DE LISTA
row = ["torre blanca" for i in range(8)]
print(row)

#--------------------------------------------------------------------------------------------------------------------------------------------------
# MAS EJEMPLOS DE COMPRESION DE LISTAS

""" 
El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de diez números enteros que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81) 
"""
squares = [x ** 2 for x in range(10)]

#--------------------------------------------------------------------------------------------------------------------------------------------------

""" 
El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos (1, 2, 4, 8, 16, 32, 64, 128) 
"""
twos = [2 ** i for i in range(8)]

#--------------------------------------------------------------------------------------------------------------------------------------------------

""" 
Este codigo selecciona solo los numeros impares de la lista 
"""
squares=[1,2,3,4,5,6,7,8,9]
# elmento por elemento en la lista squares; si el modulo del elemento es diferente de cero: se agrega a la lista odds
odds = [x for x in squares if x % 2 != 0 ]
print(odds)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# EJEMPLO TABLERO VACIO: este ejemplo crea una lista dentro de una lista


board = []
# por cada elemento en el rango de 8
for i in range(8):
   # se crea una lista rows[] con 8 elementos dentro
    row = ["vacio" for i in range(8)]
    # aqui la lista row[] se agregara 8 veces en la lista board[]
    board.append(row)
    
print(board)


# EJEMPLO COMPRIMIDO
board = [["vacio" for i in range(8)] for j in range(8)]


#--------------------------------------------------------------------------------------------------------------------------------------------------


