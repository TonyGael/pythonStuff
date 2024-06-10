def is_anagram(str_1, str_2):
    # eliminamos espacios y pasamos a minusculas
    str_1 = str_1.replace(' ', '').lower()
    str_2 = str_2.replace(' ', '').lower()

    # ordenamos de manera ascendentes las cadenas
    str_1 = sorted(str_1)
    str_2 = sorted(str_2)
    
    # comparamos las acdenas
    return str_1 == str_2

print(is_anagram('he llo', 'o l l eh'))
