
# ¿Se puede enviar una lista a una función como un argumento?
# ¡Por supuesto que se puede! Cualquier entidad reconocible por Python puede desempeñar el papel de un argumento de función.

def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5, 4, 3]))

print(list_sum(5)) # mal invocado, error TypeError: 'int' object is not iterable


# ¿Puede una lista ser el resultado de una función?
# ¡Si, por supuesto! Cualquier entidad reconocible por Python puede ser un resultado de función.

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.append(i)
    
    return strange_list

print(strange_list_fun(5)) # muestra [0,1,2,3,4]

#----------------------------------------------------------------------

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i) # cada vez que inserta un elemento lo hace en el indice [0] y los otros elementos los arrima
    
    return strange_list

print(strange_list_fun(5)) # muestra [4,3,2,1,0]

