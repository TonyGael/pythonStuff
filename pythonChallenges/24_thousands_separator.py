# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.

# Your function should convert the number to a string and add commas as a thousands separator.

# For example, calling format_number(1000000) should return "1,000,000".

def format_number(number):
    # Convertir el número a una cadena
    num_str = str(number)
    
    # Inicializar una lista para construir la nueva cadena con comas
    formatted_str = []
    
    # Contador para los dígitos
    count = 0
    
    # Iterar sobre la cadena de números al revés
    for digit in reversed(num_str):
        # Añadir el dígito actual a la lista
        formatted_str.append(digit)
        count += 1
        
        # Insertar una coma cada tres dígitos, excepto si estamos al final de la cadena
        if count % 3 == 0 and count != len(num_str):
            formatted_str.append(',')
    
    # Unir la lista y revertir para obtener el formato correcto
    return ''.join(reversed(formatted_str))


# def format_number(number):
#     return f'{number:,}'

print(format_number(1000000))
print(format_number(1500000))
print(format_number(1000))
print(format_number(0))
