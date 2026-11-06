import random
def roll_dice(die_size=20, die_num=1):
    return random.randint(1*die_num, die_size*die_num)


# print(roll_dice(100))