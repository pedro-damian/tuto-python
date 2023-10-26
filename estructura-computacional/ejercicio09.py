
aulas = {}
n = int(input("Ingrese la cantidad de aulas: "))
for i in range(1, n + 1):
    aula = input(f"Ingrese el nombre del aula {i}: ")
    m = int(input(f"Ingrese la cantidad de estudiantes en el aula {aula}: "))
    estudiantes = []
    for j in range(1, m + 1):
        apellido = input(f"Ingrese el apellido del estudiante {j} del aula {aula}: ")
        nota_final = float(input(f"Ingrese la nota final del estudiante {j} del aula {aula}: "))
        estudiantes.append((apellido, nota_final))
    aulas[aula] = estudiantes

for aula, estudiantes in aulas.items():
    sum_notas = 0
    max_nota = float('-inf')
    max_apellido = ""
    for estudiante in estudiantes:
        sum_notas += estudiante[1]
        if estudiante[1] > max_nota:
            max_nota = estudiante[1]
            max_apellido = estudiante[0]
    promedio = sum_notas / len(estudiantes)
    print(f"En el aula {aula}, el mejor estudiante es: {max_apellido} y el promedio general es: {promedio:.2f}")
