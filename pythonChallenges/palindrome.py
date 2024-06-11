# learning how to use reverded function 
# import random

# list_1 = []

# for index in range(10):
#     # print(f'{index + 1}: {random.randint(0, 9)}')
#     list_1.append(random.randint(0, 9))

# print(list_1)

# # reversing the list

# reversed_list = []

# for index in reversed(list_1):
#     reversed_list.append(index)

# print(reversed_list)

# def palindrome(string: str) -> bool:
#     if string == ''.join(reversed(string)):
#         return True
#     else:
#         return False

def palindrome(string: str) -> bool:
    return string == ''.join(reversed(string))    
    
print(palindrome('abba'))
