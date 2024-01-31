
# ¿Que es una Pila?
# Una pila es una estructura desarrollada para almacenar datos de una manera muy específica.
# El nombre alternativo para una pila (pero solo en la terminología de TI) es UEPS (LIFO son sus siglas en inglés).
# Es una abreviatura para una descripción muy clara del comportamiento de la pila: Último en Entrar - Primero en Salir (Last In - First Out).
# Una pila es un objeto con dos operaciones elementales, denominadas convencionalmente push (cuando un nuevo elemento se coloca en la parte superior) y pop (cuando un elemento existente se retira de la parte superior).
# La pila normalmente realiza al menos dos operaciones, llamadas push() y pop().

stack = []  # pila

def push(val):              # funcion para introducir datos en la pila
    stack.append(val)

def pop():                  # funcion para eliminar los datos en la pila
    val = stack[-1]
    del stack[-1]
    return val

push(3)     # introduce el numero 3
push(2)     # introduce el numero 2
push(1)     # introduce el numero 1

print(pop())    # elimina el ultimo numero ingresado 1
print(pop())    # elimina el ultimo numero ingresado 2
print(pop())    # elimina el ultimo numero ingresado 3


#------------------- Constructor -----------------------
# La parte de la clase en Python responsable de crear nuevos objetos se llama constructor y se implementa como un método de nombre __init__.

class Stack:  # Definiendo la clase de la pila.
    def __init__(self):  # Definiendo la función del constructor.
        print("¡Hola!")

stack_object = Stack()  # Instanciando el objeto.

#------------------ Encapsulamiento -------------------------

# Este es un ejemplo sin encapsulamiento
class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))     # mostrara el valor de 0

# Este es un ejemplo con encapsulamiento
# Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), se vuelve privado, esto significa que solo se puede acceder desde dentro de la clase.
class Stack:
    def __init__(self):
        self.__stack_list = []


stack_object = Stack()
print(len(stack_object.__stack_list))   # mostrara un ERROR ya que no podra acceder al componente solo desde dentro de la clase

#-----------------------------------------

class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


# ------------------------------------------------
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack()         # creo primer objeto de la clase Stack
another_stack = Stack()        # creo segundo objeto de la clase Stack
funny_stack = Stack()          # creo tercer objeto de la clase Stack

little_stack.push(1)                            # el primer objeto introduce el numero 1
another_stack.push(little_stack.pop() + 1)      # el segundo objeto introduce el numero 2 ( esto se debe a la operacion dentro del parentesis)
funny_stack.push(another_stack.pop() - 2)       # el tercer objeto introduce el numero 0 ( de igual forma a la operacion dentro del parentesis)

print(funny_stack.pop())                        # elimina y imprime el numero


# ------------- CREANDO UNA SUBCLASE --------------------