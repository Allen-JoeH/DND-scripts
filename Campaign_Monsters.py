monsters_library = {
    # list of all monsters being used/to be used in campaign
    "wight": 700,
    "wight (heavy)": 1100,
    "wight (archer)": 1100,
    "skeleton infantry": 50,
    "skeleton": 50,
    "zombie": 50,
    "ghoul": 200,
    "ghast": 450,
    "hobgoblin": {"xp": 100, "init modifier": 2, "max hp": 30},
    "hobgoblin captain": {"xp": 700, "init modifier": 2, "max hp": 60},
    "bandit": {"xp": 25, "init modifier": 2, "max hp": 11},
    "bandit heavy": {"xp": 50, "init modifier": 2, "max hp": 23},
    "bandit archer": {"xp": 50, "init modifier": 2, "max hp": 17},
    "bandit lieutenant": {"xp": 200, "init modifier": 2, "max hp": 42},
    "grey wolf": {"xp": 50, "init modifier": 2, "max hp": 11},
    "dire wolf": {"xp": 200, "init modifier": 2, "max hp": 37},
    "werewolf": {"xp": 700, "init modifier": 1, "max hp": 58},
    "wyvern" : {"xp": 2300, "init modifier": 0, "max hp": 110},
    "young black dragon" : {"xp": 2900, "init modifier": 2, "max hp": 127},
    "young green dragon" : {"xp": 3900, "init modifier": 1, "max hp": 136}
}


# Encounter types to generate random encounters

encounter_type = [
    {"name": "", "challenge rating": 0, "encounter limit": 10}
]

hobgoblin_patrol = [
    {"name": "hobgoblin", "CR": 1/2, "encounter limit": 99},
    {"name": "hobgoblin captain", "CR": 3, "encounter limit": 1}
]
bandit_patrol = [
    {"name": "bandit", "challenge rating": 1/8, "encounter limit": 10},
    {"name": "bandit heavy", "challenge rating": 1/4, "encounter limit": 4},
    {"name": "bandit archer", "challenge rating": 1/4, "encounter limit": 2},
    {"name": "bandit lieutenant", "challenge rating": 1, "encounter limit": 1},
]
grey_wolf_pack = [
    {"name": "wolf", "challenge rating": 1/4, "encounter limit": 10}
]




# Scripted encounters

scripted_encounter = [{"name": "Placeholder",
                       "quantity": 1, "init modifier": 0, "max hp": 20},
                      {"name": "Guard Captain", "quantity": 1, "init modifier": 2, "max hp": 60}]

guard_fight = [
    {"name": "guard Heavy", "quantity": 4,
     "init modifier": 0, "max hp": 20},
    {"name": "guard Crossbowman", "quantity": 6,
     "init modifier": 2, "max hp": 17},
    {"name": "bandit leader", "quantity": 1, "init modifier": 4, "max hp": 79},
    {"name": "bandit mage", "quantity": 1, "init modifier": 2, "max hp": 18},
    {"name": "bandit heavy", "quantity": 4, "init modifier": 2, "max hp": 23},
    {"name": "bandit archer", "quantity": 4, "init modifier": 2, "max hp": 17}
]

guard_fight_2 = [
    {"name": "guard Heavy", "quantity": 4,
     "init modifier": 0, "max hp": 20},
    {"name": "guard Captain", "quantity": 1, "init modifier": 2, "max hp": 58},
    {"name": "bandit heavy", "quantity": 2, "init modifier": 2, "max hp": 23}
]

bandit_holy_fight = [
    {"name": "bandit leader", "quantity": 1, "init modifier": 4, "max hp": 79},
    {"name": "bandit mage", "quantity": 1, "init modifier": 2, "max hp": 18},
    {"name": "bandit heavy", "quantity": 2, "init modifier": 2, "max hp": 23},
    {"name": "bandit archer", "quantity": 2, "init modifier": 2, "max hp": 17},
    {"name": "Holy warrior",
     "quantity": 2, "init modifier": 1, "max hp": 17},
    {"name": "Holy paladin",
     "quantity": 1, "init modifier": 0, "max hp": 41}
]

wyvern_encounter = [{"name": "Wyvern", "quantity": 1, "init modifier": 0, "max hp": 127}]

black_dragon_encounter = [{"name": "Young Black Dragon", "quantity": 1, "init modifier": 2, "max hp": 127}]


green_dragon_encounter = [{"name": "Young Green Dragon", "quantity": 1, "init modifier": 1, "max hp": 136}]

Orc_Scouts_Elf_Rangers = [{"name": "Orc Scout", "quantity": 4, "init modifier": 3, "max hp": 30},
                      {"name": "Orc Scout Captain", "quantity": 1, "init modifier": 2, "max hp": 52},
                      {"name": "Elf Ranger", "quantity": 4, "init modifier": 4, "max hp": 52}]

# scripted_encounter = [{"name": "Thug",
#                        "quantity": 1, "init modifier": 0, "max hp": 20},
#                       {"name": "Guard Captain", "quantity": 1, "init modifier": 2, "max hp": 60}]
