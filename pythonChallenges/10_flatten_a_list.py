# Compirmir una lista:
# Escribe una función que tome una lista de listas
# y la aplane en una lista unidimensional.
# Nombra tu función aplanar.
# Debería tomar un único parámetro y
# devolver una lista.
# Por ejemplo, llamando:
# aplanar([[1, 2], [3, 4]])
# Debería devolver la lista:
# [1, 2, 3, 4]

# opción 1
def flatten(nested_list):
    flat_list = []
    for sub_list in nested_list:
        for item in sub_list:
            flat_list.append(item)
    return flat_list

print(flatten([[1, 2], [3,4,5]]))
