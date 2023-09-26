import random
import math

chars = ['Adobe','Dalista','Mutinous Greg']

def get_party_initiative(characters):
    init_list = []
    for character in characters:
        initiative = input(character + " initiative: ")
        init_list.append((character,int(initiative)))
    return init_list

def generate_monster_initiative(monster,quantity,modifier,start_count=0):
    init_list = []
    for i in range(start_count,quantity+start_count):
        initiative = math.ceil(20*random.random() + modifier)
        init_list.append((monster + ' ' + str(i + 1),initiative))
    return init_list

def turn_order(*initiatives):
    all_inits = []
    for item in initiatives:
        all_inits += item
    return(sorted(all_inits, key = lambda x: x[1], reverse=True))

def turn_order_print(array):
    for i in array:
        print(i[0] + ': ' + str(i[1]))

# print(get_party_initiative(chars))
# print(generate_monster_initiative('zombie',5,-2))
skeles = generate_monster_initiative('Skeleton archer',2,2,8)
# print(skeles)
# print(zombies)
# turn_order_print(turn_order(get_party_initiative(chars),zombies))
turn_order_print(skeles)
