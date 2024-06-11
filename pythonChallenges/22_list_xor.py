# def list_xor(n, list1, list2):
#     # Verificar si n está en list1
#     in_list1 = n in list1
#     # Verificar si n está en list2
#     in_list2 = n in list2
#     # Devuelve True solo si n estÃ¡ en una lista, pero no en ambas
#     return (in_list1 and not in_list2) or (not in_list1 and in_list2)

def list_xor(n, list1, list2):
    # Verificar si n estÃ¡ exclusivamente en una de las listas, pero no en ambas
    return (n in list1) ^ (n in list2)


print(list_xor(1, [1, 2, 3], [4, 5, 6]))  # True
print(list_xor(1, [0, 2, 3], [1, 5, 6]))  # True
print(list_xor(1, [1, 2, 3], [1, 5, 6]))  # False
print(list_xor(1, [0, 0, 0], [4, 5, 6]))  # False

