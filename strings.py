
# CONCATENACION
# Se realiza con el simbolo "+"

name ="pedro"
last_name="Damian Noriega"

full_name = name + " " + last_name 

print(full_name)

#COMILLAS SIMPLES
# se usa para imprimir comillas dobles
uso_comillas_simples= 'Ella dijo en voz alta "Pudrete"'
print(uso_comillas_simples)

# COMILLAS DOBLES
# se usa cuando quieres imprimir comillas simples
uso_comillas_dobles="I'm from Peru"
print(uso_comillas_dobles)

# Format
# Es un metodo para darle formato a cadenas con valores. 
# Existen 3 formas de darle un formato a cadenas
# 1 FORMA:
print("Forma1: Hola, mi nombre es "+ name + " y mi apellido es "+ last_name)

# 2 FORMA:
print("Forma2: Hola, mi nombre es {} y mi apellido es {}".format(name,last_name))

# 3 FORMA:
print(f"Forma3: Hola, mi nombre es {name} y mi apellido es {last_name}")