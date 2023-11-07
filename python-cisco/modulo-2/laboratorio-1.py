
print("Hola mundo")
print("Pedro")
print('Pedro')
print(1), print(2), print(3)


print("La Witsi Witsi Araña\nsubió a su telaraña.\n") # \n (salto de linea)
print()  # genera una linea vacia
print("Vino\"() la lluvia\ny se la llevó.")

print("El simbolo de comillas \"\" ") # \ ayuda a imprimir unas comillas dentro de comillas
print("El simbolo de la barra invertida  \\")

print("La Witsi Witsi Araña" , "subió" , "a su telaraña.") # 3 argumentos divididos por comas (generara un espacio en blanco entre los argumentos)


# ARGUMENTO (end=" ")
print("Mi nombre es", "Python.", end=" ") # end=" " cancela el salto de linea
print("Monty Python.")

print("Mi nombre es", "Python.", end="<-> ") # end="<->" cancela el salto de linea y agrega el simbolo dentro
print("Monty Python.")

# ARGUMENTO (sep="-")
print("Mi", "nombre", "es", "Monty", "Python.", sep="-") # se utliza como separador entre todos los argumentos

# combinacion de los 2 argumentos
print("Mi", "nombre", "es", sep="_", end=" * ")
print("Monty", "Python", sep="-", end="*\n")

# EJERCICO 2 
print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")

# EJERCICIO DE LAS FLECHAS

print("""
     *           *
    ***         ***
   ** **       ** **
  **   **     **   **
 **     **   **     **
****   **** ****   ****
  **   **     **   **
  **   **     **   **
  *******     *******""")

