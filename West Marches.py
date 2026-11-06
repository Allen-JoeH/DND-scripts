from InitOrder import print_encounter_init, turn_order, turn_order_print_to_txt, generate_monster_initiative, get_party_initiative, generate_encounter_init
from Travel import travel_summary, encounter
from EncounterGenerator import generate_encounter, hobgoblin_patrol, bandit_patrol
import RandomEncounters
import EncounterRating
import Campaign_Monsters
from Campaign_Tables import *
# Set chars to be used at start of session
# all_chars = ["Flea",  "Merthyn", "Stuart", "Lodri", "Paws", "Steve"]
active_chars = ["Belinda", "Guregg", "Otho"]
# active_chars = ["Chris", "Guthin", "Ekki", "Flea", "Paws", "Grog"]

# active_chars = ["Ekki", "Flea", "Pen", "Stu", "Paws", "Selyn", "Yiwee"]
# active_chars = ["Flea", "Ekki", "Pen"]
# active_chars = ["Stu", "Paws", "Merddyn"]

campaign_season = "Autumn"

# sets library of monsters to be used
monster_library = Campaign_Monsters.monsters_library

# bandits = generate_encounter([4, 4, 4, 4], "Hard", 10,
#                              monster_library, Campaign_Monsters.bandit_patrol)
# print_encounter_init("DNDscripts/Order_of_battle.txt",
#                      active_chars, Campaign_Monsters.bandit_holy_fight)

# journey = travel_summary("normal", control_param="time",
#                          time=5, danger_modifier=3)

# # encounter(journey, "evening", modifier=2)
thugs_hvy = generate_monster_initiative('heavy thug', 1, 0, 40)
thugs = generate_monster_initiative('thug', 1, 0, 32)
esteban = generate_monster_initiative('Esteban', 1, 9, 112)
# thugs_lt = generate_monster_initiative('light thug', 2, 0, 32)
# guard_heavy = generate_monster_initiative("guard heavy", 2, 0, 20)
# guard_ranged = generate_monster_initiative("guard crossbowman", 2, 0, 17)
# master_thief = generate_monster_initiative('master thief', 1, 4, 60)
ghouls = generate_monster_initiative("ghoul", 4, 2, 22)
ghast = generate_monster_initiative("ghast", 2, 3, 36)
deathlock = generate_monster_initiative("deathlock", 1, 2, 36)

hobgoblin_infantry = generate_monster_initiative('hobgoblin infantry', 3, 1, 32)
hobgoblin_arbalest = generate_monster_initiative('hobgoblin arbalester', 2, 2, 22)
hobgoblin_captain = generate_monster_initiative("hobgoblin captain", 1, 2, 39)

goblins = generate_monster_initiative("goblin", 2, 2, 7)
goblin_spearmen = generate_monster_initiative('goblin spearman', 3, 2, 27)
goblin_sharpshooters = generate_monster_initiative('goblin sharpshooter', 3, 3, 18)
goblin_skulker = generate_monster_initiative("goblin skulker", 1, 3, 28)
goblin_boss = generate_monster_initiative("goblin boss", 1, 2, 21)
goblin_chief = generate_monster_initiative("goblin chief", 1, 3, 50)
bugbear_merc = generate_monster_initiative("bugbear mercenary", 1, 2, 45)




# hired_blades = generate_monster_initiative('hired blade', 3, 2, 58)
# banshee = generate_monster_initiative('banshee', 1, 2, 58)
# shadows = generate_monster_initiative('shadow', 2, 2, 16)
orc_scouts = generate_monster_initiative("Orc scout", 3, 3, 30)
orc_scout_captain = generate_monster_initiative("Orc Scout Captain", 1, 3, 52)
dragon = generate_monster_initiative("Adult green dragon", 1, 1, 207)
rot_troll = generate_monster_initiative("Rot troll", 1, 1, 138)
shadow_demons = generate_monster_initiative("Shadow demon", 3, 3, 66)
babaus = generate_monster_initiative("Babau", 3, 3, 82)
# bulezaus = generate_monster_initiative("Bulezau", 2, 2, 52)
# glabrezu = generate_monster_initiative("Glabrezu", 1, 2, 157)


# gnolls = generate_monster_initiative("Gnoll", 5, 1, 22)
# gnoll_hunters = generate_monster_initiative("Gnoll hunters", 3, 2, 22)
# gnoll_flesh_gnawers = generate_monster_initiative("Gnoll Flesh Gnawer", 4, 2, 22)
# gnoll_fang = generate_monster_initiative("Gnoll Fang of Yeenoghu", 1, 2, 65)

spiders = generate_monster_initiative("Giant Spider", 4, 3, 26)

orcs = generate_monster_initiative("Orc", 2, 1, 15)
orc_berserkers = generate_monster_initiative("Orc Berserker", 1, 2, 85)
orc_blade = generate_monster_initiative("Orc Blade of Ilneval", 1, 0, 60)
orc_eye = generate_monster_initiative("Orc eye of Gruumsh", 1, 1, 45)
wyvern = generate_monster_initiative("Wyvern", 1, 0, 110)

# turn_order_print_to_txt(turn_order(
#     get_party_initiative(active_chars), orc_scouts, orc_scout_captain, orcs), "Order_of_battle.txt")

turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), orcs, orc_berserkers, orc_blade), "Order_of_battle.txt")

encounter_bandit = [{'name': 'bandit', 'quantity': 5, 'init modifier': 2, 'max hp': 11}, 
 {'name': 'bandit heavy', 'quantity': 4, 'init modifier': 2, 'max hp': 23}, 
 {'name': 'bandit archer', 'quantity': 2, 'init modifier': 2, 'max hp': 17}, 
 {'name': 'bandit lieutenant', 'quantity': 1, 'init modifier': 2, 'max hp': 42}]
 
Orc_Scouts= [{"name": "Orc Scout", "quantity": 3, "init modifier": 3, "max hp": 30},
                      {"name": "Orc", "quantity": 3, "init modifier": 1, "max hp": 15}]

encounter_spiders = [{'name': 'Giant spider', 'quantity': 4, 'init modifier': 3, 'max hp': 26}, 
 {'name': 'ettercap', 'quantity': 1, 'init modifier': 2, 'max hp': 44}]


# encounter_trolls = [{'name': 'troll', 'quantity': 2, 'init modifier': 1, 'max hp': 84}]
# encounter_trolls = generate_monster_initiative('troll', 2, 1, 84)

# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), generate_encounter_init(encounter_spiders)), "Order_of_battle.txt")

# OOB GEN TEMPLATES
# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), enemies1inits, enemies2inits), "Order_of_battle.txt")
# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), generate_monster_initiative((monster, quantity, modifier, max_hp, start_count=0))), "Order_of_battle.txt")
# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), generate_encounter_init(encounter)), "Order_of_battle.txt")
# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), ghouls, ghast), "Order_of_battle.txt")

# test = generate_encounter([4, 4, 4, 4], "Hard", 10, monster_library, hobgoblin_patrol, bandit_patrol)

# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), generate_encounter_init(
#     test)), "Order_of_battle.txt")




# bandit_list = generate_encounter_init(encounter_bandit)
# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), orcs, orc_scouts, orc_scout_captain, orc_berserkers), "Order_of_battle.txt")

# random_encounter = generate_encounter([4, 4, 4, 4], "Hard", 10, monster_library, hobgoblin_patrol, bandit_patrol)
# print(random_encounter)

# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), random_encounter), "Order_of_battle.txt")


# print(RandomEncounters.random_weighted_encounter(cormanthyr_weighted_encounters, max_roll=100))
# print(RandomEncounters.random_location(cormanthyr_weighted_locations, cormanthyr_location_foes))


# print(RandomEncounters.random_weighted_encounter(Campaign_Tables.cormanthyr_weighted_locations))


# active_chars = ["Paws", "Lodri", "Stuart", "Steven"]
# bandit_encounter = [{"name": "Bandit Captain", "quantity": 1, "init modifier": 2, "max hp": 60},
#                     {"name": "Bandit Heavy", "quantity": 4, "init modifier": 2, "max hp": 23}]
# turn_order_print_to_txt(turn_order(get_party_initiative(active_chars), generate_encounter_init(
#     bandit_encounter)), "Order_of_battle.txt")

