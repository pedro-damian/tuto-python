# ============================================================
# EJERCICIO 5: 🏪 Mini Sistema de Inventario
# ============================================================
# Temas: TODO lo aprendido - variables, tipos de datos,
#        strings/métodos, operadores (aritméticos, comparación,
#        lógicos), condicionales, listas, tuplas, diccionarios,
#        sets, for, while, ciclos anidados, comprensión de
#        listas/diccionarios, funciones (return, múltiples
#        returns, scope), lambdas
# ============================================================
#
# Crea un sistema de inventario para una tienda.
#
# Estructura de datos:
# Cada producto es un DICCIONARIO dentro de una LISTA:
# inventario = [
#     {"nombre": "Laptop", "precio": 15000.00, "cantidad": 5, "categoria": "tecnología"},
#     {"nombre": "Mouse", "precio": 350.50, "cantidad": 20, "categoria": "tecnología"},
#     {"nombre": "Cuaderno", "precio": 45.00, "cantidad": 100, "categoria": "papelería"},
# ]
#
# Instrucciones:
#
# 1. FUNCIONES DE CONSULTA:
#
#    a) "buscar_producto(inventario, nombre)" que:
#       - Busque un producto por nombre (ignorando mayúsculas)
#       - Retorne el diccionario del producto o None si no existe
#
#    b) "productos_por_categoria(inventario, categoria)" que:
#       - Use COMPRENSIÓN DE LISTAS para filtrar por categoría
#       - Retorne la lista filtrada
#
#    c) "obtener_categorias(inventario)" que:
#       - Use un SET para obtener las categorías únicas
#       - Retorne el set
#
# 2. FUNCIONES DE OPERACIÓN:
#
#    a) "agregar_producto(inventario)" que:
#       - Pida nombre, precio (float), cantidad (int) y categoría
#       - Valide que el precio > 0 y la cantidad >= 0
#       - Verifique que no exista ya (usa buscar_producto)
#       - Agregue el producto al inventario
#
#    b) "actualizar_stock(inventario)" que:
#       - Pida el nombre del producto
#       - Pida la nueva cantidad
#       - Actualice si el producto existe
#
# 3. FUNCIONES DE REPORTES:
#
#    a) "valor_total_inventario(inventario)" que:
#       - Use sum() con una lambda para calcular:
#         sum(lambda: precio * cantidad de cada producto)
#       - Retorne el valor total
#
#    b) "reporte_resumen(inventario)" que:
#       - Muestre total de productos (len)
#       - Muestre las categorías disponibles (usa obtener_categorias)
#       - Muestre el valor total del inventario
#       - Use COMPRENSIÓN DE DICCIONARIOS para crear un resumen
#         por categoría: {"tecnología": 3, "papelería": 1}
#       - Use un for para mostrar cada categoría y su cantidad
#       - Muestre el producto más caro usando max() con lambda:
#         max(inventario, key=lambda p: p["precio"])
#
#    c) "productos_bajo_stock(inventario, minimo=10)" que:
#       - Use comprensión de listas para encontrar productos
#         con cantidad menor al mínimo
#       - Retorne la lista
#
# 4. MENÚ PRINCIPAL:
#    Usa while True con las opciones:
#    1. Ver inventario completo
#    2. Buscar producto
#    3. Agregar producto
#    4. Actualizar stock
#    5. Ver productos por categoría
#    6. Reporte resumen
#    7. Productos con bajo stock
#    8. Salir
#
# 💡 Pistas:
#    - sum() con lambda: sum(map(lambda p: p["precio"] * p["cantidad"], inventario))
#      O también: sum(p["precio"] * p["cantidad"] for p in inventario)
#    - max() con lambda: max(inventario, key=lambda p: p["precio"])
#    - Comprensión de diccionarios:
#      {cat: len([p for p in inventario if p["categoria"] == cat]) for cat in categorias}
# ============================================================

# Escribe tu código aquí:


