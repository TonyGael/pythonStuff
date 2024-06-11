# Counting parameters
# Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.
# For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.

def param_count(*args):
    # *args permite que la función acepte un número indefinido de argumentos. args es una tupla que contiene todos los argumentos pasados a la función.
    return len(args)
    #  len() se utiliza para contar el número de elementos en args y devolver este valor.

print(param_count())  # Debería devolver 0
print(param_count(2, 3, 4))  # Debería devolver 3
print(param_count(1, 'a', 3.14, True))  # Debería devolver 4
