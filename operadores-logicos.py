
# OPERADOR and
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False) 

print("10>5 and 5<10 => el valor logico es:",10>5 and 5<10)
print("10>5 and 5>10 => el valor logico es:",10>5 and 5>10)

stock = int(input("Ingrese un numero de entre 100 y 200: "))
print("Si el valor ingresado esta entre 100 y 200 mostrara True de lo contrario False => ",stock>=100 and stock<=200)

# OPERADOR or
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False) 

role = input("Escribe el cargo de admin o supervisor para ingresar: ")
print("Si el cargo es admin o supervisor dara True de lo contrario false => ", role=="admin" or role=="supervisor")

# OPERADOR not
print("La negacion de True and True =>", not(True and True))
print("La negacion de True and False =>", not(True and False))
print("La negacion de False and True =>", not(False and True))
print("La negacion de False and False =>", not(False and False)) 

print("La negacion de True or True =>", not(True or True))
print("La negacion de True or False =>", not(True or False))
print("La negacion de False or True =>", not(False or True))
print("La negacion de False or False =>", not(False or False)) 