from random import randint

def lotto():
    # Inputing numbers by user.
    lucky_numbers = []
    y = False
    while not y:
        try:
            given_number = int(input(
                    f"""    
    Already {len(lucky_numbers)} of 6 numbers given.
    Enter number: """))
        except ValueError:
            print("This is not a number.")
            continue
        if (given_number > 49 or given_number < 1):
            print("Enter number between 1 and 49")
            continue
        elif given_number in lucky_numbers:
            print("Number is already given.")
            continue
        elif given_number not in lucky_numbers:
            lucky_numbers.append(given_number)
        if len(lucky_numbers) == 6:
            y = True

    # Drawing numbers by program.
    drawn_numbers = []
    x = False
    while not x:
        num = randint(1,49)
        if num in drawn_numbers:
            continue
        elif num not in drawn_numbers:
            drawn_numbers.append(num)
        if len(drawn_numbers) == 6:
            x = True

    # Comparing numbers.
    number_of_hits = 0
    for number in lucky_numbers:
        if number in drawn_numbers:
            number_of_hits +=1
        else:
            continue

    return f"""
    Your lucky numbers: {sorted(lucky_numbers)}
    Drawn numbers: {drawn_numbers} 
    Number of Your lucky hits: {number_of_hits}"""

print(lotto())
