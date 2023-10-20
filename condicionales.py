
# CONDICIONALES (if) 
# son estructuras de control que permiten controlar que partes del codigo se ejecutan
# se ejecutan siempre despues de una operacion booleana

if True:
  print("el codigo se ejecuta")
if False:
  print("El codigo nunca se ejecuta")
  
pet= input("Ingrese su mascota: ")

# si 
if pet == "perro":
  print("Un gran amigo")
# sino
elif pet == "gato":
  print("muy engreidos")
# sino
elif pet == "pez":
  print("saber cuidarlos")
  # puedes dar mas opciones....

# entonces, de lo contrario
else:
  print("mascota no encontrada") 

