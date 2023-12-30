

# MODULO PLATFORM
# El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

import platform

print(dir(platform))

#----------------------------- funcion platform() ------------------------------------
# devuelve una cadena que describe el entorno

""" Así es como se puede invocar:
platform(aliased = False, terse = False) 

"""

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

#----------------------------- funcion machine() ------------------------------------
# conocer el nombre genérico del procesador que ejecuta el sistema operativo junto con Python y el código.

from platform import machine
print(machine())

#----------------------------- funcion processor() ------------------------------------
# devuelve una cadena con el nombre real del procesador

from platform import processor
print(processor())


#----------------------------- funcion system() ------------------------------------
# devuelve el nombre genérico del sistema operativo en una cadena.

from platform import system
print(system())

#----------------------------- funcion version() ------------------------------------
# devuelve La versión del sistema operativo 

from platform import version
print(version())

#----------------------------- La funcion python_implementation()  ------------------------------------
# devuelve una cadena que denota la implementación de Python 

from platform import python_implementation
print(python_implementation())


#----------------------------- La funcion python_version_tuple()  ------------------------------------
# devuelve una tupla de tres elementos la cual contiene:
# La parte mayor de la versión de Python.
# La parte menor.
# El número del nivel de parche.

from platform import python_version_tuple
print(python_version_tuple())