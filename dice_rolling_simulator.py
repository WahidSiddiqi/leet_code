import random

def roll():
    roll = (random.randint(1,6) + random.randint(1,6))
    return roll


def dice_roll():
    user_input = ''
    print("Welcome to Shahzaybs casino\nWe're gonna roll some dice, press enter to roll dice")
    user_input = input()
    if user_input == '':
        print('You rolled a: ' + str(roll()))
    else:
        print("You have to leave it input blank, "
              "and press only enter when prompted")

dice_roll()
