
#----------------------------- Compresion de Listas ------------------------------------
# es una forma de escribir listas con una sintaxis mas corta

#>>>>>>>>> Version 1 - agregar numeros del 1-10 a la lista vacia
numeros = []

for elemento in range(1,11):
  numeros.append(elemento)
  
print(f"La version 1: {numeros}")

#>>>>>>>>> Version 2 - agregar numeros del 1-10 a la lista vacia
numeros_2 =[elemento for elemento in range(1,11)]
print(f"La version 2: {numeros_2}")

#>>>>>>>>  Version 3 - agregar numeros pares a la lista vacia
numeros_3 = []
for elemento in range(1,11):
  if elemento % 2 == 0:
    numeros_3.append(elemento)
print(f"La version 3: {numeros_3}")

#>>>>>>>>  Version 4 - agregar numeros pares a la lista vacia
numeros_4 = [elemento for elemento in range(1,11) if elemento%2 ==0]
print(f"La version 4: {numeros_4}")

#>>>>>>>>  Version 5 - agregar numeros impares a la lista vacia
numeros_5 = []
for elemento in range(1,11):
  if elemento%2 != 0:
    numeros_5.append(elemento)
print(f"La version 5: {numeros_5}")

#>>>>>>>>  Version 6 - agregar numeros impares a la lista vacia
numeros_6 = [elemento for elemento in range(1,11) if elemento%2 != 0]
print(f"La version 6: {numeros_6}")

#>>>>>>>>  Version 7 - agregar numeros dobles a la lista vacia
numeros_7 = []
for elemento in range(1,11):
  numeros_7.append(elemento * 2)
print(f"La version 7: {numeros_7}")

#>>>>>>>>  Version 8 - agregar numeros dobles a la lista vacia
numeros_8 = [elemento * 2 for elemento in range(1,11)]
print(f"La version 8: {numeros_8}")

