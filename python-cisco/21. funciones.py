
# FUNCIONES

# 1 CONDICION: si un fragmento de código comienza a aparecer en más de una ocasión, considera la posibilidad de aislarlo en la forma de una función
# 2 CONDICION: si un fragmento de código se hace tan extenso que leerlo o entenderlo se hace complicado, considera dividirlo pequeños problemas por separado e implementa cada uno de ellos como una función independiente.
# 3 CONDICION: si se va a dividir el trabajo entre varios programadores, se debe descomponer el problema para permitir que el producto sea implementado como un conjunto de funciones escritas por separado empacadas juntas en diferentes módulos.

# ¿De dónde provienen las funciones?
# De Python mismo: funciones integradas: print()
# módulos preinstalados de Python
# Directamente del código: tu puedes escribir tus propias funciones.

#--------------------------------------------------------------------------------------------------------------------------------------------------

# SINTAXIS DE UNA FUNCION

"""
def nombre-funcion():
  contenido-funcion 
"""
# siempre inicia con la palabra def
# despues el nombre de la funcion (para darle nombre a las funciones se utiliza las mismas reglas que para las variables)
# despues del nombre de la funcion sigue el parentesis ()
# luego dos puntos :
# en la siguiente linea va las intrucciones de la funcion


def mensaje():
    print("Hola mundo")

# invoca la funcion
mensaje()

#--------------------------------------------------------------------------------------------------------------------------------------------------
# NOTA: 
# no se debe invocar una funcion antes que se haya definido ()
#  genera una excepción (la excepción NameError)

""" 
mensaje()

def mensaje():
    print("Hola mundo") 
    
"""

# una funcion no puede compartir el mismo nombre que una variable

""" 
def mensaje():
    print("Hola mundo")

mensaje = 1 
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

# INVOCAR UNA FUNCION CON UN PARAMETRO

def hola(nombre):    # definiendo una función
    print("Hola,", nombre)    # cuerpo de la función


nombre = input("Ingresa tu nombre: ")

hola(nombre)    # invocación de la función