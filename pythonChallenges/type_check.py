""" def only_ints(n1, n2):
    if type(n1) == int and type(n2) == int:
        return True
    else:
        return False

print(only_ints(1, 2))
print(only_ints('a', 2)) """

""" def only_ints(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        return True
    else:
        return False

print(only_ints(1, 2))
print(only_ints('a', 2)) """

def only_ints(n1, n2):
    return all(type(x) == int for x in (n1, n2))


print(only_ints(1, 2))
print(only_ints('a', 2))
