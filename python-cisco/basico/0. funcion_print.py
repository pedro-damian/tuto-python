
####### FUNCION PRINT() EN PYTHON ###########
# La función print() en Python se utiliza para mostrar información en la consola o terminal.
# Puede imprimir texto, números, variables y otros tipos de datos.

print("Hola mundo")
print("Pedro")  # Pedro
print('Pedro')  # Pedro
print(1), print(2), print(3) # imprime 1,2,3 en lineas diferentes

###########  ERRORES COMUNES
# print "Hola"  # Error de sintaxis, falta los parentesis
# print(Hola)   # Error, Hola no esta definido
# print('Hola)  # Error de sintaxis, falta la comilla simple al final
# print(Hola')  # Error de sintaxis, falta la comilla simple al inicio
# print('Hola")  # Error de sintaxis, comillas diferentes


###########  Caracteres de escape y nueva línea en Python ###########
print("La Witsi Witsi Araña\nsubió a su telaraña.\n") # \n (salto de linea)
print()  # genera una linea vacia
print("Vino\"() la lluvia\ny se la llevó.")

print("El simbolo de comillas \"\" ") # \ ayuda a imprimir unas comillas dentro de comillas
print("El simbolo de la barra invertida  \\")  # \


########### múltiples argumentos en print() ###########
# Argumentos posicionales
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.") # 3 argumentos divididos por comas (generara un espacio en blanco entre los argumentos)
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.", 2024, True) # se pueden mezclar tipos de dato

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

###################### LABORATORIO
# Resultado Final: Programming***Essentials***in...Python
print("Programming","Essentials","in")
print("Python")
# solucion
print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")

# EJERCICIO DE LAS FLECHAS
# con saltos de lineas
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
# mas grande
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")


# El duplicado de la figura anterior
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)


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



# Pregunta 1: ¿Cuál es la salida del siguiente programa?
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")

# Pregunta 2: ¿Cuál es la salida del siguiente programa?
print(sep="&", "fish", "chips") # TypeError: 'sep' debe ubicarse al final

# Pregunta 3: ¿Cuál de las siguientes print() invocaciones de función generarán un SyntaxError?
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."') # SyntaxError: comillas diferentes no coinciden
 