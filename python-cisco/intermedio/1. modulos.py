
#------------------------------------------------ LOS MODULOS -----------------------------------------------------
# El código de computadora tiene una tendencia a crecer. el código que no crece probablemente sea completamente inutilizable o esté abandonado.
# El código creciente es, de hecho, un problema creciente. Un código más grande siempre significa un mantenimiento más difícil. La búsqueda de errores siempre es más fácil cuando el código es más pequeño.
# entonces, habrá la necesidad de dividirlo en muchas partes, varias docenas o incluso varios cientos de desarrolladores.
# Para contribuir o mantener el codigo, no se puede hacer usando todo el codigo fuente al mismo tiempo por todos los programadores, lo que se debe hacer es dividir el codigo en partes y despues unirlos
# Por ejemplo se puede dividir en 2 partes: La interfaz de usuario y la logica y cada una de estas partes se puede dividir en partes mas pequeñas a este proceso se le denomina "DESCOMPOSICIÓN"

# ¿Qué es un Módulo?
# un archivo que contiene definiciones y sentencias de Python, que se pueden importar más tarde y utilizar cuando sea necesario.

# ¿Cómo hacer uso de un módulo?
# se pueden utilizar de 2 maneras: de un modulo existente creado por otro programador en algun otro proyecto o crear un nuevo modulo.
# USUARIO (emplea un modulo ya existente) PROVEEDOR (crea un modulo nuevo)
# Todos estos módulos, forman la Biblioteca Estándar de Python - donde los módulos desempeñan el papel de libros (incluso podemos decir que las carpetas desempeñan el papel de estanterías). 
# ver la lista completa de todos los "volúmenes" recopilados en esa biblioteca, se puede encontrar aquí: https://docs.python.org/3/library/index.html.
# Cada módulo consta de entidades (como un libro consta de capítulos). Estas entidades pueden ser funciones, variables, constantes, clases y objetos.
# Si se sabe como acceder a un módulo en particular, se puede utilizar cualquiera de las entidades que almacena.
# Uno de lo mas conocidos es el modulo math (contiene una coleccion de  entidades que permiten realizar calculos matematicos)

# ---------------------------------------IMPORTANDO UN MODULO --------------------------------------
# Para que un módulo sea utilizable, hay que importarlo (piensa en ello como sacar un libro del estante).
# se realiza mediante una instrucción llamada import. debe colocarse antes del primer uso de cualquiera de las entidades del módulo.

import mod1

# Si se desea (o se tiene que) importar más de un módulo, se puede hacer repitiendo la cláusula import. (RECOMENDADA)
import mod1
import mod2
import mod3

# listando los módulos por comas despues de la palabra reservada import (NO RECOMENDADA)
import mod1, mod2, mod3


# ACCEDER A LAS ENTIDADES DE UN MODULO
import mod1
# utilizamos las entidades mi_funcion y mi_dato
result = mod1.mi_funcion(mod1.mi_dato)


#---------------------------- IMPORTAR MODULO con solo algunas de sus ENTIDADES  ------------------------------------------

from mod1 import mi_funcion, mi_dato

result = mi_funcion(mi_dato)

#------------------------------IMPORTAR MODULO con todas sus entidades ---------------------------------

from mod1 import *

result = mi_funcion(mi_dato)

#-----------------------------CAMBIAR NOMBRE de las ENTIDADES de un MODULO  -----------------------------

from mod1 import mi_funcion as funcion, mi_dato as dato

result = funcion(dato)