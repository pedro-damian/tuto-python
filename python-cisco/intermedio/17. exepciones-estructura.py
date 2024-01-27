
# Python 3 define 63 excepciones integradas, y todas ellas forman una jerarquía en forma de árbol.
# cuanto más cerca de la raíz se encuentra una excepción, más general (abstracta) es. A su vez, las excepciones ubicadas en los extremos del árbol (podemos llamarlas hojas) son concretas.

#              BaseException
#     --------------|---------------
# SystemExit    Exception   KeyboardInterrupt
#     -------------|------------------
# ValueError    LookupError   ArithmeticError
#     --------------|               |
# IndexError    KeyError    ZeroDivisionError

# Nota:

""" 
ZeroDivisionError es un caso especial de una clase de excepción más general llamada ArithmeticError.
ArithmeticError es un caso especial de una clase de excepción más general llamada solo Exception.
Exception es un caso especial de una clase más general llamada BaseException. 

"""
# Podemos describirlo de la siguiente manera: ZeroDivisionError --> ArithmeticError --> Exception --> BaseException


""" 
Recuerda:
- ¡El orden de las excepciones importa!
- No pongas excepciones más generales antes que otras más concretas.
- Esto hará que el último sea inalcanzable e inútil.
- Además, hará que el código sea desordenado e inconsistente.
- Python no generará ningún mensaje de error con respecto a este problema. 

"""

try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")    # Imprimira ¡División entre Cero!
except ArithmeticError:
    print("¡Problema Aritmético!")    # No imprimira

print("FIN.")   # Imprimira tambien Fin


try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema Aritmético!")    # Imprimira Problema Aritmetico
except ZeroDivisionError:
    print("¡División entre Cero!")    # No imprimira

print("FIN.")   # Imprimira tambien Fin

#-------------------------------- Manejador Try | except dentro de una funcion ------------------------------

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema Aritmético!")
    return None

bad_fun(0)

print("FIN.")

#-------------------------------- Manejador Try | except fuera de una funcion ------------------------------

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se generó una excepción!")

print("FIN.")

