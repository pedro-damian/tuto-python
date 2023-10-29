# Se han seleccionado N números de personas para realizar una encuesta, en un proceso repetitivo se ingresa el grado de instrucción y la edad de cada persona. Se desea saber:
# a) La mayor edad de todas las personas.
# b) EI número de personas con instrucción Primaria, Secundaria y Superior.
# c) Cuántas personas tienen grado Superior pero no tienen 35 años.


# solicita al usuario que ingrese un numero de personas escuestadas
personas = int(input("Ingrese el número de personas encuestadas: "))

# inicializar variables
mayor_edad =0
e_primaria = 0
e_secundaria =0
e_superior =0
e_superior_menor_35 = 0

# bucle que va iterar a traves del rango de personas encuestadas
for i in range(personas):
  
  # solicita el grado de estudio de la persona encuestada donde P S U
  grado_estudio = input(f"seleccione el grado de instruccion de la persona N°{i+1} donde P= primaria, S= secundaria, U= universitario: ").upper()
  # bucle while donde si no ingreso ninguna de las opciones 
  while grado_estudio not in ["P","S","U"]:
    # muestre el mensaje opcion incorrecta 
    print("Opcion Incorrecta!!")
    # me vuelve a pedir que elija las opciones disponibles
    grado_estudio = input(f"seleccione el grado de instruccion de la persona N°{i+1} donde P= primaria, S= secundaria, U= universitario: ").upper()

  # solicita la edad de la persona encuestada
  edad = int(input(f"Ingrese la edad de la persona N°{i+1}: "))
  
  # si el grado de estudio es igual a "P"
  if grado_estudio == "P" :
    # entonces que vaya sumando y acumulando en la variable
    e_primaria +=1

  # si el grado de estudio es igual a "S"
  elif grado_estudio == "S":
    # entonces que vaya sumando y acumulando en la variable
    e_secundaria +=1

  # si el grado de estudio es igual a "U" y la edad es menor a 35
  elif grado_estudio == "U" and edad < 35:
    # entonces que vaya sumando y acumulando en la variable
    e_superior +=1
    # entonces que vaya sumando y acumulando en la variable
    e_superior_menor_35 +=1

  # si la edad es mayor al valor de la variable mayor_edad
  elif edad > mayor_edad:
    # entonces la variable mayor_edad tendra un nuevo valor
    mayor_edad = edad
    
    
print(f"La edad mayor de todas las personas es: {mayor_edad}")
print(f"El numero de personas con instruccion primaria es: {e_primaria}")
print(f"El numero de personas con instruccion secundaria es: {e_secundaria}")
print(f"El numero de personas con instruccion Superior es: {e_superior}")
print(f"El numero de personas que tienen grado superior pero menos de 35 años es: {e_superior_menor_35}")