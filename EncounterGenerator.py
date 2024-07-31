# Autogenerates list of monsters based on party
import EncounterRating
import random
from Campaign_Monsters import monsters_library
# encounter_template = {
#     {"name": "monster name", "challenge rating": 0, "encounter limit": 99}
# }


def dict_to_tuple_list(dict: dict):
    return [(monster_name, monster_quantity)
            for monster_name, monster_quantity in dict.items()]


def generate_encounter(character_levels: list[int], difficulty: str, monster_limit: int, monster_types: dict, *encounter_types: list):

    encounter = encounter_types[random.randint(0, len(encounter_types))-1]
    # print("encounter", encounter)
    difficulty_ratings = ["Trivial", "Easy", "Medium", "Hard", "Deadly"]
    # try:
    #     difficulty in difficulty_ratings
    # except:
    #     print("Need valid difficulty rating")
    current_rating_int = 0
    current_monsters = {}
    # print("Starting Loop")
    encounter_break = 0
    while current_rating_int < difficulty_ratings.index(difficulty):
        # print(f"Current difficulty {difficulty_ratings[current_rating_int]}")
        # print(f"Desired difficulty {difficulty}")
        # print(f"Current monsters: {current_monsters}")
        encounter_break += 1
        if encounter_break == 50:
            # print("Encounter limit reached for all monsters")
            break
        # determine if encounter limit reached
        if monster_limit == 0:
            # print(
            #     f"Monster limit of {sum([y for x,y in current_monsters.items()])} reached for encounter")
            break
        for monster in encounter:
            # print(f"Monster: {monster}")
            current_rating = EncounterRating.encounter_rating(
                character_levels, dict_to_tuple_list(current_monsters), EncounterRating.monsters_dict)
            if monster["name"] not in current_monsters or current_monsters[monster["name"]] < monster["encounter limit"]:
                # print(f"Difficulty rating if adding {monster['name']}:", EncounterRating.encounter_rating(
                #     character_levels, dict_to_tuple_list(current_monsters)+[(monster["name"], 1)], EncounterRating.monsters_dict))
                # determine if adding monster raises difficulty rating beyond desired
                if difficulty_ratings.index(EncounterRating.encounter_rating(character_levels, dict_to_tuple_list(current_monsters)+[(monster["name"], 1)], EncounterRating.monsters_dict)) < difficulty_ratings.index(difficulty) + 1:
                    if monster["name"] not in current_monsters:
                        # print(f"Adding {monster['name']} to encounter")
                        current_monsters[monster["name"]] = 1
                        monster_limit -= 1
                    elif current_monsters[monster["name"]] < monster["encounter limit"]:
                        # print(f"Adding another {monster['name']} to encounter")
                        current_monsters[monster["name"]] += 1
                        monster_limit -= 1
                # else:
                #     print("Not adding", monster["name"])
                current_rating_int = difficulty_ratings.index(current_rating)
            # else:
            #     print("Encounter limit reached for monster")
            current_rating = EncounterRating.encounter_rating(
                character_levels, dict_to_tuple_list(current_monsters), EncounterRating.monsters_dict)
    #         print("Current rating:", current_rating)
    #         print("Monsters:", current_monsters, "\n")
    # print("Loop completed.")
    # print("Final encounter:", "Monsters", current_monsters,
    #       "Current rating", current_rating)
    final_enounter = []
    for monster in current_monsters:
        final_enounter.append(
            {"name": monster, "quantity": current_monsters[monster], "init modifier": monster_types[monster]["init modifier"], "max hp": monster_types[monster]["max hp"]})
    # print(final_enounter)
    return final_enounter
# add randomisation


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

encounters = [hobgoblin_patrol, bandit_patrol]

# print(list_of_lists_number([1], [2], [3]))
# generate_encounter([4, 4, 4, 4], "Hard", 10, hobgoblin_patrol, bandit_patrol)

generate_encounter([4, 4, 4, 4], "Hard", 10, monsters_library, bandit_patrol)
