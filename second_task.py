import random

def get_numbers_tickets(min,max,quantity = 1):
    if min < 1:
        return "Мінімальне значення менше ніж 1"
    elif max > 1000:
        return "Максимальне значення більше ніж 1000"
    numbers_set = set()
    for i in range(quantity):
        numbers_set.add(random.randint(min,max))
    
    return numbers_set
