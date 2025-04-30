import random

def get_numbers_ticket(min,max,quantity = 1):
    if min < 1:
        return "Мінімальне значення менше ніж 1"
    elif max > 1000:
        return "Максимальне значення більше ніж 1000"
    elif min > max:
        return "Мінімалльне значення більше ніж максимальне значення"
    elif max - min < quantity:
        return "quantity більше ніж різниця між max і min"

    numbers_set = set()
    while quantity > len(numbers_set):
        numbers_set.add(random.randint(min,max))
        
    numbers_list = []
    for elem in numbers_set:
        numbers_list.append(elem)
        
    return numbers_list
