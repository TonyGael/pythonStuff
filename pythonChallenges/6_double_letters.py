def double_letters(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            count += 1
            return True
    
    return False

print(double_letters('hello'))
print(double_letters('nono'))
