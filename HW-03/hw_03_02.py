import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > max - min + 1:
       return []
    unique_numbers = set() 

    while len(unique_numbers) < quantity:
       random_num = random.randint(min, max)
       if random_num not in unique_numbers: 
          unique_numbers.add(random_num)

    lottery_numbers = list(unique_numbers)
    lottery_numbers.sort()

    return lottery_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)