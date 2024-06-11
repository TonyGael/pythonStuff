# Challenge
# Writing short code
# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

# What makes this tricky is that your function body must only contain a single line of code.

from typing import List, Union

# usando comprensión de listas
# def convert(numbers):
#     return [str(number) for number in numbers]

# usando comprensión de listas mas el método map()
# def convert(numbers):
#     return list(map(str, numbers))

def convert(numbers: List[Union[int, float]]) -> List[str]:
    return list(map(str, numbers))

# Ejemplo de uso
print(convert([1, 2, 3]))  # Debería devolver ["1", "2", "3"]
