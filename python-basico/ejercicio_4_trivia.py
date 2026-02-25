# ============================================================
# EJERCICIO 4: 🎯 Juego de Trivia
# ============================================================
# Temas: diccionarios, listas, tuplas, for, condicionales,
#        funciones (múltiples returns), scope, strings,
#        operadores de comparación y lógicos, sets
# ============================================================
#
# Crea un juego de trivia con preguntas de opción múltiple.
#
# Instrucciones:
#
# 1. Crea las preguntas como una LISTA DE DICCIONARIOS:
#    preguntas = [
#        {
#            "pregunta": "¿Cuál es la capital de Francia?",
#            "opciones": ["a) Madrid", "b) París", "c) Roma"],
#            "respuesta": "b"
#        },
#        ... (crea al menos 5 preguntas)
#    ]
#
# 2. Crea una función "hacer_pregunta(pregunta_dict)" que:
#    - Reciba un diccionario de pregunta
#    - Muestre la pregunta y las opciones con un for
#    - Pida la respuesta al usuario
#    - Convierta la respuesta a minúscula con .lower().strip()
#    - Compare con la respuesta correcta
#    - Retorne True si es correcta, False si no
#
# 3. Crea una función "jugar(preguntas)" que:
#    - Inicialice un puntaje en 0
#    - Cree un SET vacío para guardar las preguntas acertadas
#    - Recorra las preguntas con enumerate() para numerarlas
#    - Llame a hacer_pregunta() para cada una
#    - Si es correcta, sume 1 al puntaje y agregue al set
#    - Al final retorne una TUPLA: (puntaje, total, set_acertadas)
#
# 4. Crea una función "mostrar_resultado(puntaje, total, acertadas)" que:
#    - Desempaque la tupla
#    - Calcule el porcentaje: (puntaje / total) * 100
#    - Muestre el resultado con f-string y 1 decimal
#    - Si porcentaje >= 80: "🏆 ¡Excelente!"
#    - Si porcentaje >= 60: "👍 ¡Bien hecho!"
#    - Si no: "📚 ¡Sigue practicando!"
#
# 5. En el programa principal, llama a jugar() y mostrar_resultado()
# ============================================================

# Escribe tu código aquí:


