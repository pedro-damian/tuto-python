
# PALABRA CLAVE (in)
#  verifica si un valor existe en una secuencia (listas,tupla, string)

texto = "si Miras dentro del abismo el abismo Mira Dentro de Ti"

if "abismo" in texto:
  print("¡La palabra abismo se encuentra en el texto!")
else:
  print("La palabra abismo no se encuentra en el texto!")


# La Funcion len()
# verifica la cantidad total de caracteres tiene el string

letras = len(texto)
print("La cantidad total de caracteres del texto es: ",letras)

# El metodo upper()
# convierte en mayusculas el string
print("Texto en Mayusculas: ", texto.upper())

# El metodo lower()
# convierte en minusculas todo el string

print("Texto en minusculas: ", texto.lower())

# El metodo count()
# define cuantos elementos iguales dentro de la lista o string se repiten

print("La cantidad de veces que abismo se repite en el texto son =>", texto.count("abismo"))

# El metodo swapcase()
# convierte en mayuscula en minuscula y minuscula en mayuscula el string

print("Texto invertido =>", texto.swapcase())

# El metodo starswith()
# verifica que una palabra determinada empiece en un string

print("Si la primera palabra es Si en el texto entonces sera =>", texto.startswith("Si"))

# El metodo endswith()
# verifica que una palabra determinada termine en un string

# El metodo replace()
# reemplaza un elemento por otro

print("Reemplazamos abismo por oscuridad =>", texto.replace("abismo","oscuridad"))

# El metodo capitalize
# establece la primera letra en mayuscula
print("Este texto tendra la primera letra en mayuscula =>", texto.capitalize())

# El metodo title()
# las primeras letras de cada palabra dentro del string sera en mayuscula
print("Cada palabra dentro del texto sera en mayuscula", texto.title())

# El metodo isdigit()
# verifica si todos los elementos dentro de un string son numeros si es asi mostrara true de lo contrario false
print("El texto contiene numeros =>", texto.isdigit())