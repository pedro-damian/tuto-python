
# ----------------- ORDENAMIENTO -------------------------

#>>>>>>>>>> sorted()
# La función toma un argumento (una lista) y retorna una nueva lista, con los elementos ordenados del argumento.
# La lista original permanece intacta.

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)      # ['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2)    # ['alpha', 'gamma', 'omega', 'pi']


#>>>>>>>>>> sort()
# afecta a la lista misma - no se crea una nueva lista.

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()     # ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)     # ['alpha', 'gamma', 'omega', 'pi']


""" El Cifrado César: encriptando un mensaje: 
Solo acepta letras latinas (nota: los Romanos no usaban espacios en blanco ni dígitos).
Todas las letras del mensaje están en mayúsculas (nota: los Romanos solo conocían las mayúsculas).
La línea 02: pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
La línea 03: prepara una cadena para el mensaje cifrado (esta vacía por ahora).
La línea 04: inicia la iteración a través del mensaje.
La línea 05: si el carácter actual no es alfabético...
La línea 06: ...ignoralo.
La línea 07: convierta la letra a mayúsculas (es preferible hacerlo a ciegas, en lugar de verificar si es necesario o no).
La línea 08: obtén el código de la letra e increméntalo en uno.
La línea 09: si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
La línea 10: ... cámbialo al código de la A.
La línea 11: agrega el carácter recibido al final del mensaje cifrado.
La línea 13: imprime el cifrado.

"""

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

