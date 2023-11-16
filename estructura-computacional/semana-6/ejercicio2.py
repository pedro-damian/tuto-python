
materias = ["matematicas","fisica","quimica","historia","lengua"]
passed=[]
for materia in materias:
    score= float(input("¿que nota has sacado en: " + materia + "? : "))
    if score >= 5:
        passed.append(materia)
for materia in passed:
    materias.remove(materia)
print("tienes que repetir " + str(materias))