
# WHILE (mientras la condicion sea true..)
#  se va ejecutar hasta que sea false

# inicializamos una variable en 0
counter = 0

# mientras el contador sea menor a 10
#while counter < 10:
  # contara uno a uno
  #counter +=1
  # imprimira del uno al diez
  #print(counter)
  
  
# BREAK (detiene un ciclo de manera forzada)
#while counter < 20:
  #counter +=1
  # si contador es igual a 10
  #if counter ==10:
    # se detiene el proceso
    #break
  #print(counter)
  
  
# CONTINUE (salta procesos sin imprimir)
while counter < 20:
  counter +=1
  # si contador es mayor a 10
  if counter > 10:
    # continue al siguiente proceso sin imprimir
    continue
  # imprimira los numeros de numeros 1 a 10
  print(counter)
  
