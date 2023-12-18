
# FUNCIONES CON PARAMETROS

# ¿Ques son los Parametros?
# Un parametro es una variable
# el único lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la función
# La asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca

""" 
def mi_funcion(parametro):
    #cuerpo de la funcion

"""

# Los parámetros solo existen dentro de las funciones
# Los argumentos existen fuera de las funciones
# es posible tener una variablecon el mismo nombre del parametro de la funcion

def message(number): # el parametro number es completamente diferente a una variable
    print("Ingresa un número:", number)

number = 1234 # variable number
message(1) # invoca la funcion y pasa un argumento al parametro
print(number) # imprime el valor de la variable number


#--------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCIONES CON 2 O MAS PARAMETROS
# esto significa que para invocar la funcion se necesita dos o mas argumentos

""" 
def mi_funcion(parametro1,parametro2):
  # intrucciones 

"""
# EJEMPLO DE UNA FUNCION CON 2 PARAMETROS
def message(name, age):
    print("Nombre:", name , "edad:", age)

message("pedro", 11)

#--------------------------------------------------------------------------------------------------------------------------------------------------
def calculadora(num1,num2):
  suma = num1 + num2
  resta = num1 - num2
  multiplicacion = num1 * num2
  division = num1 / num2
  print(f"La suma de los numeros es: {suma}\nLa resta de los numeros es: {resta}\nLa multiplicacion de los numeros es: {multiplicacion}\nLa division de los numeros es: {division}")
  
calculadora(10,3)


#--------------------------------------------------------------------------------------------------------------------------------------------------

