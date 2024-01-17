
#---------------- capitalize() ----------------------------
# crea una nueva cadena modificada y lo devuelve como resultado si lo quieres seguir utilizando asignale una variable o pasala a una funcion de lo contrario desaparecera.
# la cadena original no se modifica ya que es inmutable 
# Si el primer carácter dentro de la cadena es una letra se convertirá a mayúsculas, Todas las letras restantes de la cadena se convertirán a minúsculas.

print('aBcD'.capitalize())  # Abcd
print("Alpha".capitalize()) # Alpha
print('ALPHA'.capitalize()) # Alpha
print(' Alpha'.capitalize()) #  alpha
print('123'.capitalize())   # 123
print("αβγδ".capitalize()) # Αβγδ
 
#---------------- center() ----------------------------
# genera una copia de la cadena original, tratando de centrarla dentro de un campo de un ancho especificado.
# El centrado se realiza al agregar algunos espacios antes y después de la cadena.

print('[' + 'alpha'.center(10) + ']') # [  alpha   ]
print('[' + 'Beta'.center(2) + ']') # [Beta]
print('[' + 'Beta'.center(4) + ']') # [Beta]
print('[' + 'Beta'.center(6) + ']') # [ Beta ]

# La variante de dos parámetros de center() hace uso del carácter del segundo argumento, en lugar de un espacio.
print('[' + 'gamma'.center(20, '*') + ']') # [*******gamma********]