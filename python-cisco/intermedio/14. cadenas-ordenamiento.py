
# ----------------- ORDENAMIENTO -------------------------

#>>>>>>>>>> sorted()
# La función toma un argumento (una lista) y retorna una nueva lista, con los elementos ordenados del argumento.
# La lista original permanece intacta.

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)      # ['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2)    # ['alpha', 'gamma', 'omega', 'pi']


#>>>>>>>>>> sort()
# afecta a la lista misma - no se crea una nueva lista.

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()     # ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)     # ['alpha', 'gamma', 'omega', 'pi']
