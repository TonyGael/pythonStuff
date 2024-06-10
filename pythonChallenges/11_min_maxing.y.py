# Min-maxing:
# Define a function named largest_difference that takes a list of numbers as its only parameter.

# Your function should compute and return the difference between the largest and smallest number in the list.

# For example, the call
# largest_difference([1, 2, 3]) should return 2
# because 3 - 1 is 2.
# You may assume that no numbers are smaller or larger than -100 and 100.

def largest_difference(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list[0]
        
    largest = max(numbers_list)
    smallest = min(numbers_list)
    return largest - smallest

print(largest_difference([1]))
print(largest_difference([1,2,3]))
print(largest_difference([10, 25]))
print(largest_difference([-10, 10]))

