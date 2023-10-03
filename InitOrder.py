import random
import math

chars = ['Adobe', 'Dalista', 'Mutinous Greg']
# the list of player characters in the session


# returns a list of tuples for each PC + their initiative
def get_party_initiative(characters):
    init_list = []
    for character in characters:
        initiative = input(character + " initiative: ")
        init_list.append((character, int(initiative)))
    return init_list


def generate_monster_initiative(monster, quantity, modifier, max_hp, start_count=0):
    # generates a list of numbered monsters and rolls their initiative, returns list of tuples
    # modifier is the initiave modifier for monster type
    # start count is the numbered suffix for each monster, can be used when adding additional monsters to an encounter
    init_list = []
    for i in range(start_count, quantity+start_count):
        initiative = math.ceil(20*random.random() + modifier)
        init_list.append((monster + ' ' + str(i + 1), initiative, max_hp))
    return init_list


def turn_order(*initiatives):
    # takes a number of lists containing tuples of form (entity, iniative) and orders them by initiative
    all_inits = []
    for item in initiatives:
        all_inits += item
    return (sorted(all_inits, key=lambda x: x[1], reverse=True))


def turn_order_print(array):
    # prints the entire list of entities ordered by initiative to the console
    # can then be copied to txt file to track combat
    for i in array:
        if len(i) == 2:
            print(i[0] + ': ' + str(i[1]))
        elif len(i) == 3:
            print(i[0] + ': ' + str(i[1]) + str(f" {i[2]}/{i[2]}"))


# print(get_party_initiative(chars))
# print(generate_monster_initiative('zombie',5,-2))
skeles = generate_monster_initiative('Skeleton archer', 2, 2, 8)
# print(skeles)
# print(zombies)
# turn_order_print(turn_order(get_party_initiative(chars),zombies))
turn_order_print(skeles)

# TODO
# add HP parameter for monsters to be displayed after init, rather than writing manually in txt file
# add option to print ordered inits in separate txt file
# potentially add functionality to insert new units to text file if generated mid encounter
