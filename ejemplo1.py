
base_de_datos = [
    {'dni': '12345678', 'nombre': 'Juan', 'edad': 30},
    {'dni': '23456789', 'nombre': 'Maria', 'edad': 25},
    {'dni': '34567890', 'nombre': 'Pedro', 'edad': 35},
]

# Solicitar al usuario ingresar el DNI
dni = input("Ingresa tu DNI: ")

# Buscar en la base de datos el DNI ingresado
for persona in base_de_datos:
    if persona['dni'] == dni:
        print(f"DNI: {persona['dni']}")
        print(f"Nombre: {persona['nombre']}")
        print(f"Edad: {persona['edad']}")
        break
else:
    print("DNI no encontrado")