# ============================================================
# EJERCICIO 3: 📇 Directorio de Contactos
# ============================================================
# Temas: diccionarios (CRUD), listas, funciones, while, for,
#        condicionales, strings y métodos, operadores lógicos
# ============================================================
#
# Crea un directorio de contactos usando un diccionario
# donde la clave sea el nombre y el valor sea otro diccionario
# con teléfono y email.
#
# Estructura:
# contactos = {
#     "Pedro": {"telefono": "555-1234", "email": "pedro@mail.com"},
#     "Ana": {"telefono": "555-5678", "email": "ana@mail.com"},
# }
#
# Instrucciones:
#
# 1. Crea una función "agregar_contacto(contactos)" que:
#    - Pida nombre, teléfono y email
#    - Convierta el nombre a título con .title()
#    - Verifique que el nombre no exista ya (usando "in")
#    - Agregue el contacto al diccionario
#
# 2. Crea una función "buscar_contacto(contactos)" que:
#    - Pida el nombre a buscar
#    - Use .lower() para comparar sin importar mayúsculas
#    - Muestre la info del contacto si existe
#
# 3. Crea una función "eliminar_contacto(contactos)" que:
#    - Pida el nombre a eliminar
#    - Use del o .pop() para eliminar
#
# 4. Crea una función "mostrar_todos(contactos)" que:
#    - Use un for para recorrer contactos.items()
#    - Muestre cada contacto formateado
#    - Si no hay contactos, muestre "No hay contactos"
#
# 5. Crea el menú principal en un while True con opciones:
#    1. Agregar  2. Buscar  3. Eliminar  4. Ver todos  5. Salir
#
# 💡 Pistas:
#    - Para recorrer un diccionario:
#      for nombre, datos in contactos.items():
#    - Para acceder a datos internos: contactos["Pedro"]["email"]
# ============================================================

# Escribe tu código aquí:


