def capital_indexes(str):
    # create an empty list to store the indexes
    indexes = []

    # Loop through each character in the string along with its index
    for index, char in enumerate(str):
        if char.isupper():
            indexes.append(index)
    
    return indexes

print(capital_indexes('MaMeLuCo'))
