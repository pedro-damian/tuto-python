
user = input("Elige piedra, papel o tijera => ")
user = user.lower()
computer = "papel"

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