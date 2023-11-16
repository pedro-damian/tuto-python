
nombre = input("Dime tu nombre: ")
print("con espacios seria:")

for i in range(0,len(nombre)):
    print(nombre[i], end="")
    print (" ", end="")
print()
print("y las letras 2 a 4 son:")
print(nombre[1:4])