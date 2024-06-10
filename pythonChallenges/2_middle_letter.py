def middle_letter(str):
    # calcular la longitud de la cadena
    length = len(str)

    # verificamos si la longitud es impar
    if length % 2 == 1:
        # calculamos el indice de la letra del medio
        middle_index = length // 2
        # devolvemos la letra del medio
        return str[middle_index]
    else:
        # devolvemos la acdena vacía
        return ''

print(middle_letter('abCde'))
print(middle_letter('abCd'))
print(middle_letter('abcDe'))

