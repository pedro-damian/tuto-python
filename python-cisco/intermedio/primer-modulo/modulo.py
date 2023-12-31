
#!/usr/bin/env python3 
# Este archivo modulo,py sera el archivo que contendra el modulo
# Cuando se ejecuta un archivo directamente, su variable __name__ se establece a __main__
print(__name__)

if __name__ == "__main__":
    print("Estoy en el archivo del módulo")
else:
    print("EStoy siendo importado desde otro archivo")
    


""" module.py - Un ejemplo de un módulo en Python """

__counter = 0 
    
    
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

