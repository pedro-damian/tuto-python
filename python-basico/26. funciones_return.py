
#>>>>>>>>>>>>>>>>>>>>>>>>> Funcion : Return

def sumar_rango(min,max):
    
    i = 0
    for elemento in range(min,max):
        i += elemento
    return i

print(f"Invoca el resultado por medio la funcion print(): {sumar_rango(1,10)}") # invoca por medio de print()

resultado = sumar_rango(20,30) # invoca por medio de una variable para luego seguir utilizando el resultado
print(f"Invoca el resultado por medio de una variable resultado: {resultado}")


# CALCULADORA

def calculadora(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    print(f"La suma es: {suma} , La resta es: {resta} , La multiplicacion {multiplicacion}, La division es: {division}")
    
calculadora(10,2)


# CREAR UNA LISTA con NUMEROS 

print("_" * 30, "LISTA DE NUMEROS", "_" * 30)
print() # genera una linea vacia

a = int(input("Ingrese numero donde iniciar: "))
b = int(input("Ingrese numero donde terminar: "))

def lista_numeros(a,b):
    numeros = [ elemento for elemento in range(a,b)]
    return numeros

# print(lista_numeros(a,b))
conteo = lista_numeros(a,b)
print(conteo)