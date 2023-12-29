
# LA Instruccion RETURN
# logra que las funciones devuelvan un valor
# La instrucción return van dentro de la funcion

# RETURN sin una expresion
# consiste en la palabra reservada return en sí, sin nada que la siga.
# provoca la terminación inmediata de la ejecución de la función, y un retorno instantáneo al punto de invocación.

def feliz_año(deseos = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not deseos:
        return
    
    print("¡Feliz año nuevo!")

feliz_año() # sin argumento equivale a true
feliz_año(False) # con argumento false no retornara feliz año nuevo


# RETURN con una expresion
# variante de return está extendida con una expresión
# terminación inmediata de la ejecución de la función 
# evaluará el valor de la expresión y lo devolverá (de ahí el nombre una vez más) como el resultado de la función.

def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function() # aqui no retornara el valor 123
print("Esta lección es aburrida...")

print("¡Esta lección es interesante!")
retorno = boring_function() # para retornar el valor 123 se guarada en una variable 
print("El valor de retorno es:", retorno)
print("Esta lección es aburrida...")



