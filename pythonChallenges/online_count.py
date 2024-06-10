""" def online_count(dict):
    count = 0

    for key, value in dict.items():
        if value == 'online':
            count+=1
    
    return count

print(online_count({'tony' : 'online', 'gael' : 'offline', 'marylin' : 'online'}))
 """

def online_count(statuses):
    return len([status for status in statuses.values() if status == "online"])

# Ejemplo de uso
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))  # Debería imprimir 2
