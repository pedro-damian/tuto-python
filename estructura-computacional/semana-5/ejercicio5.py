""" Ingresar el apellido y la nota del alumno, preguntar si se desea continuar o no registrando al siguiente alumno. Al terminar el curso de Principios de Programas se desea saber cuál ha sido el alumno con la nota más alta y cuál con la nota más baja """

# crea una lista vacia
alumnos = []

# mientras la condicion es verdadera
while True:
    
    try:
        # solicita el apellido del alumno
        apellido = input("Ingrese el apellido del alumno: ")
        # solicita la nota del alumno
        nota = float(input("Ingrese la nota del alumno 0 a 20: "))
        
        # se agrega apellido y nota a la lista vacia
        alumnos.append((apellido, nota))
        
        print(f"Alumno {apellido} registrado")
        
        # solicita si desea continuar el registro
        registrar = input("¿Desea continuar? (s) ¿Deseas salir(cualquier tecla)?: ")
        
        # si registrar es diferente a s 
        if registrar.lower() != 's':
            # entonces termina el proceso del bucle
            break  
    # muetra un mensaje de error de dato ingresado incorrecto
    except:
        print("ERROR, Dato incorrecta ingrese un numero en nota")

# declara y inicializa las variables para el alumno con la nota más alta y más baja
# donde se asume que el primer alumno de la lista tendra la nota mas alta hasta comprobar lo contrario
alumno_nota_alta = alumnos[0]
# donde se asume que el primer alumno de la lista tendra la nota mas baja hasta comprobar lo contrario
alumno_nota_baja = alumnos[0]

# recorre cada alumno en la lista de alumnos
for alumno in alumnos:
    # aqui comprobamos si la nota del primer alumno es mayor que la nota del alumno en la variable alumno_nota_alta
    if alumno[1] > alumno_nota_alta[1]:
        # entonces sera el nuevo alumno con la nota mas alta
        alumno_nota_alta = alumno
    # de igual manera si la nota del primer alumno es menor que la nota del alumno en la variable alumno_nota_baja
    if alumno[1] < alumno_nota_baja[1]:
        # entonces sera el alumno con la menor nota
        alumno_nota_baja = alumno

print(f"El alumno con la nota más alta es {alumno_nota_alta[0]} con una nota de {alumno_nota_alta[1]}")
print(f"El alumno con la nota más baja es {alumno_nota_baja[0]} con una nota de {alumno_nota_baja[1]}")

