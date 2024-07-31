import random
import math

chars = ['Adobe', 'Dalista', 'Mutinous Greg']
# chars_2 = ['Piereo', 'Preston', 'Chelydra']
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
        init_list.append((monster + ' ' + str(i + 1) if quantity >
                         1 else monster, initiative, max_hp))
    return init_list


def generate_encounter_init(encounter: list):
    init_list = []
    for monster in encounter:
        for i in range(0, monster["quantity"]):
            initiative = math.ceil(
                20*random.random() + monster["init modifier"])
            init_list.append((monster["name"] + ' ' + str(i + 1) if monster["quantity"]
                             > 1 else monster["name"], initiative, monster["max hp"]))
    return init_list


bandit_encounter = [{"name": "Bandit Captain", "quantity": 1, "init modifier": 2, "max hp": 60},
                    {"name": "Bandit Heavy", "quantity": 4, "init modifier": 2, "max hp": 23}]


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


def turn_order_print_to_txt(array, file):
    # prints the entire list of entities ordered by initiative to a given text file
    with open(file, "w") as output_file:
        for i in array:
            if len(i) == 2:
                output_file.write(i[0] + ': ' + str(i[1]) + "\n")
            elif len(i) == 3:
                output_file.write(i[0] + ': ' + str(i[1]) +
                                  str(f" {i[2]}/{i[2]}") + "\n")
        output_file.close()


def print_encounter_init(file, party, encounter):
    turn_order_print_to_txt(turn_order(
        get_party_initiative(party), generate_encounter_init(encounter)), file)

# TEST DATA
# # # print(get_party_initiative(chars))
# zombies = generate_monster_initiative('zombie', 4, -2, 28)
# skele_inf = generate_monster_initiative('Skeleton Infantry', 4, 0, 15)
# wight_heavy = generate_monster_initiative('Heavy Wight', 2, 1, 50)
# zombies_2 = generate_monster_initiative('zombie', 6, -2, 28)
# skeles = generate_monster_initiative('Skeletons', 2, 2, 13)
# wight_arch = generate_monster_initiative('wight (archer)', 2, 3, 40)
# ghouls = generate_monster_initiative('ghoul', 4, 4, 22)
# ghasts = generate_monster_initiative('ghast', 1, 4, 36)


# One-Shot
# spider_bait = ['Amy', 'Chuck', 'Flim', 'Octavian', 'LF', 'LC']
# noobs = get_party_initiative(spider_bait)
# spiders = generate_monster_initiative('Giant Spider', 2, 3, 26)
# spider_queen = generate_monster_initiative('Spider Broodmother', 1, 3, 84)
# spider_swarm = generate_monster_initiative('Swarmling', 4, 2, 22)
# # turn_order_print(turn_order(spiders))
# # guards = generate_monster_initiative('Caravan Guard', 2, 1, 16)
# # captain = generate_monster_initiative('Guard Captain', 1, 2, 39)
# turn_order_print_to_txt(turn_order(
#     noobs, spiders, spider_queen, spider_swarm), "DNDscripts/Order_of_battle.txt")

# # Delian Tomb
# ratcatchers = ["gram", "Fernando", "shep", "marelle", "azrael"]
# party_init = get_party_initiative(ratcatchers)
# goblins = generate_monster_initiative('Goblin', 4, 2, 7)
# bugbear = generate_monster_initiative('Bugbear', 1, 2, 27)
# shaman = generate_monster_initiative('Shaman', 1, 2, 7)

# turn_order_print_to_txt(turn_order(party_init, goblins, bugbear, shaman),
#                         "DNDscripts/Order_of_battle.txt")

# Cat chase
# cat_chasers = ['squish', 'bob', 'Oun']
# party_init = get_party_initiative(cat_chasers)
# thugs = generate_monster_initiative('Thug', 4, 0, 32)
# thug_leader = generate_monster_initiative('Thug Leader', 1, 2, 42)

# turn_order_print_to_txt(turn_order(party_init, thugs, thug_leader),
#                         "DNDscripts/Order_of_battle.txt")
# West Marches
# active_chars = ["Paws", "Lodri", "Stuart", "Steven"]
# active_chars = ["Lod", "Stephen", "Flea"]
# party_init = get_party_initiative(active_chars)
# bandits = generate_monster_initiative('Bandit', 3, 1, 11)
# heavies = generate_monster_initiative('Bandit Heavy', 4, 1, 23)
# archers = generate_monster_initiative('Bandit Archer', 2, 2, 17)
# lieutenant = generate_monster_initiative('Bandit Lieutenant', 1, 2, 42)
# archer_lieutenant = generate_monster_initiative(
#     'Bandit Archer Lieutenant', 1, 2, 42)
# mage = generate_monster_initiative('Bandit Mage', 1, 2, 18)
# soldiers = generate_monster_initiative('Soldier', 6, 2, 28)
# castellan = generate_monster_initiative('Castellan', 1, 0, 67)
# turn_order_print_to_txt(turn_order(party_init, generate_encounter_init(
#     bandit_encounter)), "DNDscripts/Order_of_battle.txt")

# print(skeles)
# print(zombies)
# # print(ghasts)
# full_init_order_west = turn_order(
#     get_party_initiative(chars), zombies, skele_inf, wight_heavy)
# turn_order_print(turn_order(ghouls))
# turn_order_print_to_txt(full_init_order_west, "DNDscripts/Order_of_battle.txt")
# full_init_order_east = turn_order(
#     get_party_initiative(chars_2), zombies_2, skeles, wight_arch
# )
# turn_order_print_to_txt(full_init_order_east,
#                         "DNDscripts/Order_of_battle_2.txt")


# TODO
# add HP parameter for monsters to be displayed after init, rather than writing manually in txt file ||| DONE
# add option to print ordered inits in separate txt file ||| DONE
# potentially add functionality to insert new units to text file if generated mid encounter
# Maybe add gui functionality via Django or Flask, may require a SQL DB
# Add option to use object in monster statblock over typing manually

# print_encounter_init("DNDscripts/Order_of_battle.txt", chars, bandit_encounter)
