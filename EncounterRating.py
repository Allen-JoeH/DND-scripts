monsters_dict = {
    # list of all monsters being used/to be used in campaign w/ xp reward rating
    "wight": 700,
    "wight (heavy)": 1100,
    "wight (archer)": 1100,
    "skeleton infantry": 50,
    "skeleton": 50,
    "zombie": 50,
    "ghoul": 200,
    "ghast": 450
}

char_level_xp = {
    4: [125, 250, 375, 500],
    5: [250, 500, 750, 1100],
    6: [300, 600, 900, 1400],
    7: [350, 750, 1100, 1700]
}


def sum_monster_xp(*monsters_list):
    # monsters_list is list of tuples containing monster name and quantity
    xp_sum = 0
    for monster in monsters_list:
        xp_sum += monsters_dict[monster[0]]*monster[1]
    return xp_sum


def encounter_rating(character_levels, monsters_list):
    easy = sum([char_level_xp[char][0] for char in character_levels])
    medium = sum([char_level_xp[char][1] for char in character_levels])
    hard = sum([char_level_xp[char][2] for char in character_levels])
    deadly = sum([char_level_xp[char][3] for char in character_levels])
    encounter_thresholds = [easy, medium, hard, deadly]
    adjust = 1
    number_of_monsters = sum(monster[1] for monster in monsters_list)
    if number_of_monsters == 2:
        adjust = 1.5
    elif 3 <= number_of_monsters <= 6:
        adjust = 2
    elif 7 <= number_of_monsters <= 10:
        adjust = 2.5
    elif 11 <= number_of_monsters <= 14:
        adjust = 3
    elif number_of_monsters > 15 and len(character_levels) > 2:
        adjust = 4
    elif number_of_monsters > 15 and len(character_levels) <= 2:
        adjust = 5
    total_monster_xp = sum_monster_xp(*monsters_list)
    if total_monster_xp*adjust <= easy:
        return "Trivial"
    elif total_monster_xp*adjust <= medium:
        return "Easy"
    elif total_monster_xp*adjust <= hard:
        return "Medium"
    elif total_monster_xp*adjust <= deadly:
        return "Hard"
    else:
        return "Deadly"


# print(sum_monster_xp(("wight", 3), ("skeleton", 2))) tested, correct number (2200) output
encounter_monsters = [("wight", 2), ("wight (archer)", 1)]

# number_of_monsters = sum(monster[1] for monster in encounter_monsters)
# print(number_of_monsters)


char_levels = [4, 4, 4]

print(encounter_rating(char_levels, encounter_monsters))
