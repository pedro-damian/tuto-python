
# CRUD (create read update delete)

# ----------------------------- CREATE ------------------------------------
lista = [4, "Hola", False, 4.16]
lista2 = [4,7,8,20,50,28,3,1,13,70]
lista3 = ["julio","adrian","raul","eduardo","pedro","beto"]

#------------------------------ READ -------------------------------------
print("Los elementos de la lista son =>", lista)
print("El elemento del primer indice es =>", lista[0])
print("El elemento del ultimo indice es =>", lista[-1])

#------------------------------- UPDATE --------------------------------
lista[-1]= "Miguel"
print("Actualizando el ultimo elemento a =>", lista[-1])

# metodo .append()
# agrega un nuevo elemento en la parte final de la lista
lista.append(700)
print("Se agrego un nuevo elemento a la lista =>",lista)

# metodo .insert()
# agrega un nuevo elemento en la posicion o indice que desees dentro de la lista
lista.insert(0, "Pedro")
print("Se inserto en el indice [0] el elemento =>",lista)

# UNIR LISTAS
listas_unidas = lista + lista2
print("Union de listas =>", listas_unidas)

# El metodo .index()
# encuentra el indice de un elemento de una lista
print("El indice del elemento 50 en la lista_unida es =>",listas_unidas.index(50) )


#------------------------------- DELETE ------------------------------------
# El metodo remove()
# elimina un elemento de la lista
listas_unidas.remove('Hola')
print("Elemento 'Hola' a sido eliminado de la lista-unida =>", listas_unidas)

# El metodo pop()
# elimina el ultimo elemento por defecto pero tambien se puede eliminar un elemento por su indice en el argumento del metodo
ultimo_elemento = listas_unidas.pop()
print("Ultimo elemeto eliminado =>", ultimo_elemento)
print(listas_unidas)

primer_elemento = listas_unidas.pop(0)
print("El primer elemento eliminado =>", primer_elemento)


# El metodo reverse()
# invierte el roden de la lista
listas_unidas.reverse()
print("Lista invertida =>",listas_unidas)

# El metodo sort()
# ordena los elementos en forma ascendente
lista2.sort()
print("Lista de numeros ordenado =>",lista2)
lista3.sort()
print("Lista de strings ordenados =>", lista3)