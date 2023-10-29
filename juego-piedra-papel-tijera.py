# importa un modulo random que se utiliza ´para generar numeros aleatorios
import random

# se crea una tupla con las 3 opciones
options = ("papel","tijera","piedra")

user = input("Elige piedra, papel o tijera => ").lower()
#user = user.lower()
# Aqui la variable computer tendra un valor aleatorio escogido de la tupla options
computer = random.choice(options)

print("La eleccion de user es:",user)
print("La eleccion de computer es:",computer)

if user == computer:
  print("Empate!!")
  
elif user == "piedra":
  if computer == "tijera":
    print("Piedra gana a tijera")
    print("user gana")
  else:
    print("papel gana a piedra")
    print("computer gana")

elif user == "tijera":
  if computer == "papel":
    print("tijera gana a papel")
    print("user gana")
  else:
    print("piedra gana a tijera")
    print("computer gana")
elif user == "papel":
  if computer == "piedra":
    print("papel gana a piedra")
    print("user gana")
  else:
    print("tijera gana a papel")
    print("computer gana")
    
else:
  print("Opcion incorrecta, Elige piedra, papel o tijera")