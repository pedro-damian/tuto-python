
# VARIABLES DINAMICAS
name = "pedro"
print(type(name))
name = 32
print(type(name))
name = True
print(type(name))

#  Transformar de Int a String
age= 32
# Primer metodo 
print("Mi edad es "+ str(age) + " y el tipo de dato es:",type(str(age)))
# Segundo metodo
print(f"Mi edad es {age} y el tipo de dato es:",type(str(age)))

# TRANSFORMAR DE STRING A INT
age = input("Escribe tu edad:")
# Primer metodo
age=int(age)
print(f"Tu edad es {age} y es de tipo",type(age))
