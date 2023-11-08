
if __name__ == "__main__":
    alumnos = {}
    continuar = True

    while continuar:
        apellido = input("Ingrese el apellido del alumno: ")
        while True:
            try:
                nota = float(input("Ingrese la nota del alumno: "))
                if nota < 0 or nota > 10:
                    print("Por favor ingrese una nota entre 0 y 10.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

        alumnos[apellido] = nota

        respuesta = input("¿Desea continuar registrando al siguiente alumno? (si/no): ")
        if respuesta.lower() != "si":
            continuar = False

    if alumnos:
        alumno_nota_maxima = max(alumnos, key=alumnos.get)
        alumno_nota_minima = min(alumnos, key=alumnos.get)
        print(f"El alumno con la nota más alta es: {alumno_nota_maxima} con una nota de {alumnos[alumno_nota_maxima]}.")
        print(f"El alumno con la nota más baja es: {alumno_nota_minima} con una nota de {alumnos[alumno_nota_minima]}.")
    else:
        print("No se registraron alumnos.")
