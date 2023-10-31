
# WHILE (mientras la condicion sea true..)
#  se va ejecutar hasta que sea false

# inicializamos una variable en 0
counter = 0
# mientras counter es menor que 10
while counter < 20:
  # entonces que counter vaya aumentando en uno en uno
  counter +=1

  # si counter es igual a 15 
  if counter == 15:
    # entonces se detiene
    break

  print(counter, end=" ")