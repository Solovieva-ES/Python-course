import random

def get_unique_list_numbers():
    list = []
    value = 0
    i = 0
    while i < 15:
        value = random.randint(-10, 10)
        if value not in list:
            list.append(value)
            i = i + 1
    return list

list = get_unique_list_numbers()

print(list)
print(len(list) == len(set(list)))
