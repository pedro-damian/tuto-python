
# FUNCIONES VS METODOS
# Una función no pertenece a ningún dato: obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.
# Un método hace todas estas cosas, pero también puede cambiar el estado de una entidad seleccionada.
# Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.

lista = [1,2,3,4,5]

#------------------------------------------------------------------------------------------------------------
# METODOS (sintaxis)
# result = data.method(arg)

# metodo append() : agrega un nuevo elemento al final de una lista
lista.append(10)
print("El metodo append agrego el numero 10:", lista)

# metodo insert() : agrega un nuevo elemento en cualquier parte de la lista, moviendo al elemento anterior al siguiente indice
lista.insert(2, 20)
print("El metodo insert agrego el numero 20 en el indice 2:", lista)

#------------------------------------------------------------------------------------------------------------
# AGREGANDO Numeros del 1 al 5 por medio del BUCLE FOR

my_list1 = []  # lista vacía.

for i in range(5):
    my_list1.append(i + 1)

print(my_list1)  # [1,2,3,4,5]

my_list2 = []  # lista vacía.

for i in range(5):
    my_list2.insert(0, i + 1)

print(my_list2)  # [5,4,3,2,1]

#------------------------------------------------------------------------------------------------------------
#SUMAR todos los numeros de una lista con el metodo range
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#SUMAR todos los numeros de una lista
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#------------------------------------------------------------------------------------------------------------

