
# importa un modulo random que se utiliza ´para generar numeros aleatorios
import random

# se crea una tupla con las 3 opciones
options = ("papel","tijera","piedra")

user_wins=0
computer_wins=0
round=1

while True:
  
  print("*" * 10)
  print("Round", round)
  print("*" * 10)
  print("La computadora",computer_wins)
  print("El usuario",user_wins)
  
  user = input("Elige piedra, papel o tijera => ").lower()

  round +=1

  if not user in options:
    print("Esa opcion no es valida")
    continue

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
      user_wins+=1
    else:
      print("papel gana a piedra")
      print("computer gana")
      computer_wins +=1

  elif user == "tijera":
    if computer == "papel":
      print("tijera gana a papel")
      print("user gana")
      user_wins+=1
    else:
      print("piedra gana a tijera")
      print("computer gana")
      computer_wins+=1
  elif user == "papel":
    if computer == "piedra":
      print("papel gana a piedra")
      print("user gana")
      user_wins+=1
    else:
      print("tijera gana a papel")
      print("computer gana")
      computer_wins+=1
      
  if computer_wins == 3:
    print("El ganador es la computadora")
    break
  
  if user_wins == 3:
    print("El ganador es el usuario")
    break
    