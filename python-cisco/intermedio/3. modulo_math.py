
# MODULO math
# algunas funciones del modulo math 

""" trigonometría:

sin(x) → el seno de x.
cos(x) → el coseno de x.
tan(x) → la tangente de x.

asin(x) → el arcoseno de x.
acos(x) → el arcocoseno de x.
atan(x) → el arcotangente de x.

pi → una constante con un valor que es una aproximación de π.
radians(x) → una función que convierte x de grados a radianes.
degrees(x) → una función que convierte x de radianes a grados.

sinh(x) → el seno hiperbólico.
cosh(x) → el coseno hiperbólico.
tanh(x) → la tangente hiperbólico.
asinh(x) → el arcoseno hiperbólico.
acosh(x) → el arcocoseno hiperbólico.
atanh(x) → el arcotangente hiperbólico.

"""

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


 
""" exponenciación:
e → una constante con un valor que es una aproximación del número de Euler (e).
exp(x) → encontrar el valor de ex.
log(x) → el logaritmo natural de x.
log(x, b) → el logaritmo de x con base b.
log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).

Esta es una función incorporada y no se tiene que importar.
pow(x, y) → encuentra el valor de xy (toma en cuenta los dominios)

"""

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


""" Proposito General:
ceil(x) → devuelve el entero más pequeño mayor o igual que x.
floor(x) → el entero más grande menor o igual que x.
trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso). 

"""

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))


