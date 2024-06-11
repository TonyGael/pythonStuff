# Challenge
# All equal
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

# For example, calling all_equal([1, 1, 1]) should return True.

from typing import List, Any

# def all_equal(list: Union[int, str, float]) -> bool:
    # if list:
    #     return True
    # else:
    #     return False
    
    # operador ternario en Python:
    # valor_si_verdadero if condición else valor_si_falso
    # return True if list else False
    
    # usando el metodo bool()
    # return bool(list)

# print(all_equal([1, 3.14, 'a']))
# print(all_equal(['c', 'b', 'a']))
# print(all_equal([1, 1, 1]))

# def all_equal(list: List[Any]) -> bool:
#     ## uso del método all():
#     # La función all() devuelve True si todos los elementos del iterable dado son True. En este caso, estamos comprobando si cada elemento x en la lista lst es igual al primer elemento lst[0]
#     ## uso de list comprehension ( comprensión de listas):
#     # x == lst[0] for x in lst genera un generador que compara cada elemento x en lst con el primer elemento lst[0]
    
#     return all(element == list[0] for element in list) if list else True

def all_equal(list: List[Any]) -> bool:
    if not list:
        return True # ya que en una lista vacía se considerra que todos los elemntos son iguales en Python
    
    first_element = list[0]
    
    for element in list:
        if element != first_element:
            return False
    
    return True

# Ejemplos de uso
print(all_equal([1, 1, 1]))  # Salida: True
print(all_equal([1, 2, 1]))  # Salida: False
print(all_equal([])) 
