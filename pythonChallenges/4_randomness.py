import random

def random_number():
    return random.randint(1, 100)

print(random_number())

print('Using _:')
for _ in range(5):
    print(random_number())

print('Using i:')
for i in range(5):
    print(f'Iteración: {i}: {random_number()}')
