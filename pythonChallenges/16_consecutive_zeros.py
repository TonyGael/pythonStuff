# Consecutive zeros

# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

# "1001101000110"
# The biggest number of consecutive zeros is 3.

# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above

# probando la función con una cadena para practicar calculando el máximo de letras a consecutivas:

# def consecutive_a(string: str) -> int:
#     max_count = 0
#     current_count = 0
    
#     for character in string:
#         if character == 'a':
#             current_count += 1
#         else:
#             if current_count > max_count:
#                 max_count = current_count
#             current_count = 0
    
#     if current_count > max_count:
#         max_count = current_count
        
#     return max_count

# print(consecutive_a('eaaaiaaaaoaaaaa'))

# def consecutive_zeros(binary: str) -> int:
#     max_count = 0
#     current_count = 0
    
#     for binary_digit in binary:
#         if binary_digit == '0':
#             current_count += 1
#         else:
#             if current_count > max_count:
#                 max_count = current_count
#             current_count = 0
    
#     if current_count > max_count:
#         max_count = current_count
    
#     return max_count

# optimizando la lógica:
def consecutive_zeros(binary: str) -> int:
    max_count = 0
    current_count = 0
    
    for binary_digit in binary:
        if binary_digit == '0':
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 0
        
    return max(max_count, current_count)
    
print(consecutive_zeros('1001101000110'))
