""" Ingresar el apellido y la nota del alumno, preguntar si se desea continuar o no registrando al siguiente alumno. Al terminar el curso de Principios de Programas se desea saber cuál ha sido el alumno con la nota más alta y cuál con la nota más baja """


alumnos = []

while True:
    apellido = input("Ingrese el apellido del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))
    
    alumnos.append((apellido, nota))
    
    continuar = input("¿Desea continuar registrando al siguiente alumno? (s/n): ")
    if continuar.lower() != 's':
        break

# Inicializamos las variables para el alumno con la nota más alta y más baja
alumno_nota_alta = alumnos[0]
alumno_nota_baja = alumnos[0]

for alumno in alumnos:
    if alumno[1] > alumno_nota_alta[1]:
        alumno_nota_alta = alumno
    if alumno[1] < alumno_nota_baja[1]:
        alumno_nota_baja = alumno

print(f"El alumno con la nota más alta es {alumno_nota_alta[0]} con una nota de {alumno_nota_alta[1]}")
print(f"El alumno con la nota más baja es {alumno_nota_baja[0]} con una nota de {alumno_nota_baja[1]}")

