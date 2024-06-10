def add_dots(str):
    return '.'.join(str)

def remove_dots(str):
    return str.replace('.', '')

print(add_dots('hola'))  # debería devolver h.o.l.a

print(remove_dots('h.o.l.a'))  # debería devolver hola

print(add_dots('hello'))

print(remove_dots(add_dots('hello')))
