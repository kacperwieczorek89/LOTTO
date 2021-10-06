from random import randint

def lotto():

    lucky_numbers = []
    x = False
    while not x:
        num = randint(1,49)
        if num in lucky_numbers:
            continue
        elif num not in lucky_numbers:
            lucky_numbers.append(num)
        if len(lucky_numbers) == 6:
            x = True

    return lucky_numbers

print(lotto())
