
# FUNCIONES VS METODOS
# Una función no pertenece a ningún dato: obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.
# Un método hace todas estas cosas, pero también puede cambiar el estado de una entidad seleccionada.
# Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.

lista = [1,2,3,4,5]


# FUNCION
# result = function(arg)

#------------------------------------------------------------------------------------------------------------
# METODOS
# result = data.method(arg)

# metodo append() : agrega un nuevo elemento al final de una lista
lista.append(10)
print("El metodo append agrego el numero 10:", lista)

# metodo insert() : agrega un nuevo elemento en cualquier parte de la lista, moviendo al elemento anterior al siguiente indice
lista.insert(2, 20)
print("El metodo insert agrego el numero 20 en el indice 2:", lista)

#------------------------------------------------------------------------------------------------------------
# AGREGANDO Numeros del 1 al 5 por medio del BUCLE FOR

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)