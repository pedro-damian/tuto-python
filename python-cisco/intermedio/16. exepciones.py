
# Cada vez que tu código intenta hacer algo erróneo, irresponsable o inaplicable, Python hace dos cosas:
# Detiene tu programa.
# Crea un tipo especial de dato, llamado excepción.

#-------------------------------- ZeroDivisionError -------------------------------

value = 1
value /= 0      # ZeroDivisionError: division by zero


#-------------------------------- IndexError ------------------------------

my_list = []
x = my_list[0]  # IndexError: list index out of range


#-------------------------------- Try | except ------------------------------
# La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
# La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal: si se genera una excepción dentro del bloque anterior try, fallará aquí.

""" 
- Los bloques except son analizados en el mismo orden en que aparecen en el código.
- No debes usar más de un bloque de excepción con el mismo nombre.
- El número de diferentes bloques except es arbitrario, la única condición es que si se emplea el try, debes poner al menos un except (nombrado o no) después de el.
- La palabra clave reservada except no debe ser empleada sin que le preceda un try.
- Si uno de los bloques except es ejecutado, ningún otro lo será.
- Si ninguno de los bloques except especificados coincide con la excepción planteada, la excepción permanece sin manejar (lo discutiremos pronto).
- Si un except sin nombre existe, tiene que especificarse como el último.

 """

first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")

# Aqui un ejemplo mas sobre como funciona el manejador de errores try | except

try:
    print("1")    # imprime 1
    x = 1 / 0     # aqui genera un error y sale del bloque try y entra al bloque except
    print("2")    # no se imprimira por el error
except:
    print("Oh cielos, algo salió mal...")   # imprime esto en caso de error

print("3")        # imprime 3


#-------------------------------- Como manejar varios errores con Try | except ------------------------------

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError: # valor que no sea 0
    print("No puedes dividir entre cero, lo siento.")
except ValueError:    # valor que no sea un caracter
    print("Debes ingresar un valor entero.")
except:   # error general
    print("Oh cielos, algo salió mal...")

print("FIN.")

# en caso el bloque ZeroDivisionError o ValueError no haya sido declarado el error pasara al ultimo except que es el general
# en caso de que el ultimo except no haya sido declarado el error se mostrara tal cual es