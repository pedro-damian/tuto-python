
personas = int(input("Ingrese el número de personas encuestadas: "))

mayor_edad =0
e_primaria = 0
e_secundaria =0
e_superior =0
e_superior_menor_35 = 0


for i in range(personas):
  
  grado_estudio = input(f"seleccione el grado de instruccion de la persona N°{i+1} donde P= primaria, S= secundaria, U= universitario: ").upper()
  while grado_estudio not in ["P","S","U"]:
    print("Opcion Incorrecta!!")
    grado_estudio = input(f"seleccione el grado de instruccion de la persona N°{i+1} donde P= primaria, S= secundaria, U= universitario: ").upper()

  edad = int(input(f"Ingrese la edad de la persona N°{i+1}: "))
  
  if grado_estudio == "P" :
    e_primaria +=1
  elif grado_estudio == "S":
    e_secundaria +=1
  elif grado_estudio == "U" and edad < 35:
    e_superior +=1
    e_superior_menor_35 +=1
  elif edad > mayor_edad:
    mayor_edad = edad
    
    
print(f"La edad mayor de todas las personas es: {mayor_edad}")
print(f"El numero de personas con instruccion primaria es: {e_primaria}")
print(f"El numero de personas con instruccion secundaria es: {e_secundaria}")
print(f"El numero de personas con instruccion Superior es: {e_superior}")
print(f"El numero de personas que tienen grado superior pero menos de 35 años es: {e_superior_menor_35}")