
# MASA CORPORAL (IMC)
# para calcular la masa corporal de una persona se divide el peso (kg) entre la altura (m) elevada al cuadrado

def masa_corporal(peso,altura):
  return peso/altura ** 2

print(round(masa_corporal(65,1.63),2))

#------------------------------------------------------------------------------------------------------------------------------------------

# Calcular el IMC con medidas del sistema ingles (Pies,pulgadas y libras)

def lb_a_kg(lb):
  return lb * 0.45359237
#print(round(lb_a_kg(150),2))

def pie_y_pulgadas_a_m(pie,pulgadas): # aqui se declaro el pie + pulgada en caso la altura sea 5,7 (5 pies y 7 pulgadas de altura)
  return pie * 0.3048 + pulgadas * 0.0254
#print(round(pie_a_m(5.4),2))

def masa_corporal(peso,altura):
  if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 200:
    return None
  return peso/altura ** 2

print(round(masa_corporal(peso=lb_a_kg(176),altura=pie_y_pulgadas_a_m(5,7)),2))
