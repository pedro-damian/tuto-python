
# Ahora verificaremos si un triangulo los 3 lados pueden formar un triangulo

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Version mas compactada
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# version ultracompactada
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
  
print(is_a_triangle(1, 1, 1)) # true
print(is_a_triangle(1, 1, 3)) # false


# TEOREMA DE PITAGORAS
# c2 = a2 + b2
print()
print("************ TEOREMA DE PITAGORAS *****************")
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

""" a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: ')) """

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))