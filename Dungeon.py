import random
import math
from Roll import roll_dice
from Treasure_Tables import c_under_4, c_under_10, c_under_16
class Dungeon:
    def __init__(self, environment: str = "rand", size: str = "rand", enemy_type: str = "rand", rating = "rand", enemy_frequency : str = "rand", rewards : str = "rand", *tags : str):
        # set class variables, randomising if not provided
        if environment != "rand":
            self.environment = environment
        else:
            self.environment = random.choice(["caves", "settlement_active", "settlement_abandoned", "fortified", "nature"])
        if size != "rand":
            self.size = size
        else:
            self.size = random.choice(["small", "medium", "large", "huge"])
        if enemy_type != "rand":
            self.enemy_type = enemy_type
        else:
            match self.environment:
                case "caves":
                    self.enemy_type = random.choice(["undead", "beasts_caves", "goblins", "ogres", "giants", "orcs_caves", "trogs", "draconic"])
                case "settlement_active":
                    self.enemy_type = random.choice(["orcs_settlement", "goblins", "centaurs", "kobolds", "drow", "elves", "duergar", "bandits"])
                case "settlement_abandoned":
                    self.enemy_type = random.choice(["orcs_squatters", "goblin_squatters", "kobolds", "undead", "bandit_squatters", "gnolls", "wildlife"])
                case "fortified":
                    self.enemy_type = random.choice(["orcs_warcamp", "goblin_warcamp", "Hobgoblins", "undead", "Drow", "Duergar", "bandits"])
                case "nature":
                    self.enemy_type = random.choice(["wildlife_terrain"])
        if rating != "rand":
            self.rating = rating
        else:
            self.rating = random.choice(["Trivial", "Easy", "Medium", "Hard", "Deadly"])
        if enemy_frequency != "rand":
            self.enemy_frequency = enemy_frequency
        else:
            self.enemy_frequency = random.choice(["Rare", "Infrequent", "Frequent", "Constant"])
        if rewards != "rand":
            self.rewards = rewards
        else:
            self.rewards = random.choice(["None", "Meagre", "Average", "Generous", "Rich"])
    # generate the dungeon given input parameters
    def generate(self, char_levels : list):

        # generate number of rooms, encounters, treasure
        rooms_mod = {"small" : random.uniform(0.5, 0.75), "medium" : random.uniform(0.8, 1.5), "large" : random.uniform(1.5, 2.5), "huge" : random.uniform(2.5, 5)}[self.size]
        env_rooms = {"caves" : 4, "settlement_active": 6, "settlement_abandoned" : 6, "fortified" : 5, "nature" : 3}[self.environment]
        encounter_mod = {"Rare" : random.uniform(0.2, 0.5), "Infrequent" : random.uniform(0.5, 1), "Frequent" : random.uniform(1, 1.5), "Constant" : random.uniform(1.5, 2)}[self.enemy_frequency]
        treasure_mod = {"None": 0, "Meagre": random.uniform(0.1, 0.5), "Average": random.uniform(0.5, 1.2), "Generous" : random.uniform(1.2, 1.7), "Rich": random.uniform(1.7, 2.2)}[self.rewards]
        rooms = max(math.floor(rooms_mod*env_rooms),1)
        encounters = max(1, math.floor(encounter_mod*rooms/2.2))
        group_level = sum(char_levels)/len(char_levels)
        treasure_rolls = {"None": min(roll_dice(100),roll_dice(100),roll_dice(100),roll_dice(100)), 
                          "Meagre": min(roll_dice(100),roll_dice(100)), 
                          "Average": roll_dice(100,2)/2, 
                          "Generous" : max(roll_dice(100),roll_dice(100)),
                          "Rich" : max(roll_dice(100),roll_dice(100),roll_dice(100),roll_dice(100))}[self.rewards]
        if group_level <= 4:
            money = f"{math.floor(roll_dice(6,6)*50*treasure_mod)} copper pieces, {math.floor(roll_dice(6,3)*50*treasure_mod)} silver pieces, {math.floor(roll_dice(6,2)*5*treasure_mod)} gold pieces"
            treasure = c_under_4(treasure_rolls)
        elif group_level <= 10:
            money = f"{math.floor(roll_dice(6,2)*50*treasure_mod)} copper pieces, {math.floor(roll_dice(6,2)*400*treasure_mod)} silver pieces, {math.floor(roll_dice(6,6)*30*treasure_mod)} gold pieces, {math.floor(roll_dice(6,3)*5*treasure_mod)} platinum pieces"
            treasure = c_under_10(treasure_rolls)
        elif group_level <= 16:
            money = f"{math.floor(roll_dice(6,2)*50*treasure_mod)} copper pieces, {math.floor(roll_dice(6,2)*500*treasure_mod)} silver pieces, {math.floor(roll_dice(6,4)*500*treasure_mod)} gold pieces, {math.floor(roll_dice(6,5)*50*treasure_mod)} platinum pieces"
            treasure = c_under_16(treasure_rolls)
        else:
            pass        
        

        # generate the encounters up to dungeon rating
        for encounter in range(1, encounters+1):
            print(f"ENCOUNTER {encounter}")
            if encounter != encounters:
                # generate lower diff encounters
                pass
            else:
                # generate boss encounter
                pass

        # generate the layout of the dungeon, with room types and traps
        

        # generate 
        return {"rooms" : rooms, "encounters" : encounters, "money" : money, "treasure" : treasure}
        

test_group = [5,5,5,5,5]

treasure_mod = random.uniform(0.1, 0.5)
treasure_rolls = 32


money = f"{math.floor(roll_dice(6,2)*50*treasure_mod)} copper pieces, {math.floor(roll_dice(6,2)*400*treasure_mod)} silver pieces, {math.floor(roll_dice(6,6)*30*treasure_mod)} gold pieces, {math.floor(roll_dice(6,3)*5*treasure_mod)} platinum pieces"
treasure = c_under_10(treasure_rolls)

print(money)
print(treasure)


# test = Dungeon()
test_2 = Dungeon(size = "medium", environment="fortified", rewards="Meagre", enemy_type="orcs_warcamp", enemy_frequency="Frequent")
# print(test.environment, test.size, test.enemy_type)
print(test_2.environment, test_2.size)
# print(test.__dict__)
# print(test.__repr__)
# print(test.__str__)
print(test_2.__dict__)
print(test_2.generate(test_group))

