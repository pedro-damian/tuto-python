
# Este archivo importara el modulo creado
# Cuando un archivo se importa como un módulo, su variable __name__ se establece al nombre del archivo

from modulo import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

