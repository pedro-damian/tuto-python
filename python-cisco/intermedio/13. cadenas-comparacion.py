
# -------------------- Comparando cadenas ---------------------------------
# pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.
# == , != , >, >=, <, <=

# Dos cadenas son iguales cuando consisten de los mismos caracteres en el mismo orden. Del mismo modo, dos cadenas no son iguales cuando no consisten de los mismos caracteres en el mismo orden.

print('alpha' == 'alpha')   # True

# Cuando se comparan dos cadenas de diferentes longitudes y la más corta es idéntica a la más larga, la cadena más larga se considera mayor.

print('alpha' < 'alphabet') # true

# La comparación de cadenas siempre distingue entre mayúsculas y minúsculas (las letras mayúsculas se consideran menores en comparación con las minúsculas).

print('beta' > 'Beta')    # true

# Aún si una cadena contiene solo dígitos, todavía no es un número. Se interpreta como lo que es, como cualquier otra cadena regular

'10' == '010'   # False
'10' > '010'    # true
'10' > '8'      # false
'20' < '8'      # true
'20' < '80'     # true

# El comparar cadenas con los números generalmente es una mala idea. Las únicas comparaciones que puede realizar con impunidad son aquellas simbolizadas por los operadores == y !=. El primero siempre devuelve False (falso), mientras que el segundo siempre devuelve True (verdadero).

'10' == 10      # False
'10' != 10      # True
'10' == 1       # False
'10' != 1       # True
'10' > 10       # TypeError exception

