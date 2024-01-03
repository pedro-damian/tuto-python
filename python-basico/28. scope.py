
#>>>>>>>>>>>>>>>>>>>>>>>>> Scope (alcance)
# es cuando una variable solo esta disponible desde donde fue construida y para ello existen dos ambitos, el local y el global

#>>>>>>> Scope Local
# Cuando una variable es construida dentro de una función pertenece al ámbito local de esa función y solo se puede usar dentro de esa función.

def suma():
  a = 20
  b = 30
  resultado = a+b
  
# print(a) # muestra un error ya que no esta definida afuera de la funcion

#>>>>>>> Scope Global
# el Scope Global esta creada en la parte externa de la función y esta puede ser utilizada tanto de manera global como local.

a = 100

def suma():
  a = 20
  b = 30
  resultado = a+b
  
print(a) # muestra el valor 100
