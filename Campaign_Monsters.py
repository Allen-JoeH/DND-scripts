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
    "bandit lieutenant": {"xp": 200, "init modifier": 2, "max hp": 42}
}


# Encounter types to generate random encounters
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


# Scripted encounters
