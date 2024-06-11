# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.

# Your function should convert the number to a string and add commas as a thousands separator.

# For example, calling format_number(1000000) should return "1,000,000".

def format_number(number):
    return f'{number:,}'

print(format_number(1000000))
print(format_number(1500000))
print(format_number(1000))
print(format_number(0))
