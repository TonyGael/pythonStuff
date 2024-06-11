# Challenge
# Custom zip
# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.
# If you don't get it, think of a zipper.
# For example:
# zap(
#     [0, 1, 2, 3],
#     [5, 6, 7, 8]
# )
# Should return:
# [(0, 5),
#  (1, 6),
#  (2, 7),
#  (3, 8)]

# Traducción:
# Zip personalizado
# La función incorporada zip "une" dos listas. Escribe tu propia implementación de esta función.
# Define una función llamada zap. La función toma dos parámetros, a y b. Estos son listas.
# Tu función debería devolver una lista de tuplas. Cada tupla debería contener un elemento de la lista a y uno de la lista b.
# Puedes asumir que a y b tienen la misma longitud.
# Si no lo entiendes, piensa en un cierre de cremallera.
# Por ejemplo:
# zap(
#     [0, 1, 2, 3],
#     [5, 6, 7, 8]
# )
# Debería devolver:
# [(0, 5),
#  (1, 6),
#  (2, 7),
#  (3, 8)]

def zap(list_1, list_2):
    returned_list = []
    for i in range(len(list_1)):
        returned_list.append((list_1[i], list_2[i]))
    
    return returned_list

print(zap([0,1,2,3,4], [5,6,7,8,9]))
