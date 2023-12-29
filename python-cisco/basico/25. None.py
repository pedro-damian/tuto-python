
# Valor NONE
# Sus datos no representan valor razonable alguno; 
# en realidad, no es un valor en lo absoluto; por lo tanto, no debe participar en ninguna expresión.
# Nota: None es una palabra clave reservada.

# Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:
# Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
# Cuando se compara con una variable para diagnosticar su estado interno.

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2)) # True
print(strange_function(1)) # none