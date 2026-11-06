import random

encounters = {
    1: "The players encounter a group of more experienced adventurers heading in the other direction. If the players are polite, they are given some healing potions.",
    2: "A naked gnome runs across the path, gasps at the party, then runs back. Cannot be pursued.",
    3: "Omen: A roll of thunder.",
    4: "Omen: A black dog runs across the path.",
    5: "Omen: A lone yellow flower is growing in the middle of the path.",
    6: "Omen: A shadow drifts over the party.",
    7: "Omen: A pool of blood.",
    8: "Omen: The earth shakes briefly.",
    9: "Omen: The sun bursts through an overclouded sky.",
    10: "Omen: A beautiful white horse dashes past the party and disappears.",
    11: "The players find an encampment of well armed, friendly humans. They may stay the night here and avoid a random encounter for the night.",
    12: "A dwarf falls out of the sky and splatters in front of the party. No logical source of the dwarf can be seen.",
    13: "A player (whoever does the roll) trips over, takes 1D4 bludgeoning damage.",
    14: "A stranger asks to be escorted to a town, but gives the party nothing for doing it.",
    15: "The party finds the tracks of wolves going across the path (DC10 Nature/Survival).",
    16: "A local ranger gives the party directions to their next destination, but he’s an ******* that sends them the wrong way. Increase the journey length.",
    17: "An arrow strikes a nearby tree, with a note attached to it. The note reads 'You are a fool for looking!' No source of the arrow can be found.",
    18: "A dung beetle pushes a ball across the road. If disturbed, it bursts into a smog, doing 1D4 poison damage and leaves the party member poisoned.",
    19: "A mystery key is found laying in the road. If used on a locked door, roll a D20. A 20 will unlock the door, after which the key is lost.",
    20: "A thick fog prevents travel for the rest of the day.",
    21: "You were travelling in the wrong direction. Add a day of travel to your journey.",
    22: "Bard: A song of rest. Lose any debuffs.",
    23: "Bard: A song of good health. Gain 1D8 temporary hitpoints.",
    24: "Bard: A song of heroics. 1D6 party members gain inspiration.",
    25: "Bard: A song of misery. All party members with inspiration lose it.",
    26: "Bard: A song of battle. The next combat encounter grants double xp reward.",
    27: "Bard: A song of healing. Regain up to half your max HP.",
    28: "Bard: A song of pain. Lose 1D8 HP (after the bard has long since passed).",
    29: "Bard: A song of storms. A storm starts and forces the party to stop for the rest of the day.",
    30: "Bard: A song. Nothing special happens.",
    31: "Merchant: Only useful item for sale is a potion of vitality, 25gp.",
    32: "Merchant: Studded leather armour and basic weapons.",
    33: "Merchant: Five healing potions, 30gp each.",
    34: "Merchant: Basic adventuring equipment.",
    35: "Merchant: Wood.",
    36: "Merchant: Hunters bounty. Fresh meat, some herbs.",
    37: "Merchant: Herbalist (can give directions).",
    38: "Merchant: Fisherman.",
    39: "Merchant: Gem & Jewelry merchant (500gp worth of loot).",
    40: "Merchant: Bug catcher. A DC15 Nature check reveals a cartomoth, that will show them a shortcut if released. 10gp.",
    41: "The party catches up with and overtakes a slow travelling farmer, bickering with his wife. They know nothing useful.",
    42: "There is an unusually vocal chorus of birdsong. Druids, Hunters, Clerics gain inspiration.",
    43: "A stranger asks for directions from the party to the last town they left. If they help him, he gives them 1D6x10 gold when they next appear in town, if ever.",
    44: "A line of Goblin heads on spikes line the road. A sign written in Goblin next to them says 'Traitors of Yeemik'.",
    45: "A man is trapped under a log. If the party helps him, he disappears - it was an illusion.",
    46: "The party finds a sword in a stone. A DC15 Strength check pulls it out. It is a +1 (Longsword)",
    47: "A flower girl skips down the path towards the party, but disappears before she reaches them.",
    48: "Religion: The party meets an old priest and a young priest, who offer them a blessing. The party has advantage on attacks against undead till they next take a long rest.",
    49: "Religion: A temple is found on a roll. Use a D6 to determine which God, of the six below, it is dedicated to.",
    50: "Religion: Shrine to Tymora - If the party makes an offering, they all gain inspiration.",
    51: "Religion: Shrine to Chauntea - If the party makes an offering, the rest of the day has no violent encounters.",
    52: "Religion: Shrine to Mask - If the party makes an offering, they get a surprise round in their next encounter.",
    53: "Religion: Shrine to Mystra - If the party makes an offering, all spellslots are recovered.",
    54: "Religion: Shrine to Oghma - If the party makes an offering, they find a shortcut that reduces their journey by 1D4 encounters.",
    55: "Religion: Shrine to Waukeen - If the party makes an offering, they later find the amount they offered in each of their pockets.",
    56: "Religion: Abandoned, unidentifiable Shrine - If the party doesn't make an offering, they trigger a combat encounter.",
    57: "Religion: Shrine to nature spirits - If the party doesn't make an offering, a great storm prevents them from travelling any further that day.",
    58: "Religion: Demon Shrine, covered in blood - If the party makes an offering, they trigger a combat encounter.",
    59: "Religion: Shrine to Bhaal, destroyed - Nothing happens.",
    61: "Trap: DC10 Dex check or 1D6 bludgeoning damage, pit fall.",
    62: "Trap: DC15 Dex check or 1D8 bludgeoning damage, pit fall.",
    63: "Trap: DC20 Dex check or 1D12 bludgeoning damage, pit fall.",
    64: "Trap: DC10 Per check or snared, 1D6 bludgeoning damage if cut loose without landing being factored in.",
    65: "Trap: DC15 Per check or snared, 1D6 bludgeoning damage if cut loose without landing being factored in.",
    66: "Trap: DC20 Per check or snared, 1D6 bludgeoning damage if cut loose without landing being factored in.",
    67: "Trap: DC15 Per check or whole party snared by net, roll combat encounter.",
    68: "Trap: A cupcake lays in the middle of the road. If the party approaches, they trigger a pitfall into spikes. 3D6 piercing damage.",
    69: "Trap: Magic rune (DC15 Per to detect) triggers, paralyzing party. Roll for a combat encounter.",
    70: "Trap: Door in the middle of the path. If opened, a Hobgoblin is on the other side and gets a surprise attack. If walked around, the Hobgoblin flees.",
    71: "Trap: I have a tail, but no body. I have a head, but no brain. What am I? (coins, 50gp reward)",
    72: "Trap: What is running around Waterdeep, yet never truly moving? (The wall, Healing potion reward per player)",
    73: "Trap: My rivers are dry, my forests have no trees, my towns are flat and empty, and my roads cannot be walked on. What am I? (A map. The party's journey is shortened)",
    74: "Trap: Two bodies have I, though both joined in one. The more still I stand, the quicker I run. What am I? (An hourglass. Time slows down if they get it, and immediately skips to night if they don't)",
    75: "Trap: What kind of ear cannot hear? (An ear of corn. Potion of Cure Silence, everyone deafened if they don't get it)",
    76: "Trap: What has four wheels and flies? (A garbage wagon. Potion of flight if correct, attacked by Stirges if they don't get it)",
    77: "A DC10 Perception check spots a small chest hidden in a tree. It contains a gold ring worth 20gp.",
    78: "A DC15 Perception check spots a small chest hidden in a tree. It contains 44gp.",
    79: "A DC20 Perception check spots a chest hidden in a tree. It contains a +1 Short Sword.",
    80: "A DC10 Perception check spots a small chest hidden in a tree. It contains a dead mouse.",
    81: "A strong storm picks up.",
    82: "The party finds a random cow. No amount of investigation reveals anything of significance about the cow or where it came from.",
    83: "A stranger asks to be escorted to the nearest town. If the party agrees, the stranger gives them 100gp upon delivery.",
    84: "A group of excited gnomes bounce past the party. If the party is polite to them, one gives them a useless gizmo that makes a chirping noise when wound up.",
    85: "A man is trapped under a log. If the party helps him, do a DC15 check. A failure drops the log and crushes the man. He has nothing of value on him, but the saviour gets inspiration if they succeed.",
    86: "A man is buried in the road up to his neck, with the ground around him undisturbed. If the party helps him, the head pops out the ground and crawls off on spider legs, cackling. The party takes a DC14 Wisdom saving throw, taking 1D10 psychic damage on a failure.",
    87: "An enormous dragon flies overhead.",
    88: "A DC10 Perception check spots caltrops over the floor which do 1D4 piercing damage to the party if they don’t spot them.",
    89: "A drunken dwarf challenges the strongest looking party member to a wrestling match. A DC15 Strength check beats her, and she gives the party member 5gp. The party member gains a level of exhaustion on a failure.",
    90: "A road sign points back to wherever the party came from, but is otherwise useless.",
    91: "A vagrant asks for food. Nothing happens if they give him some.",
    92: "A vagrant asks for money. Nothing happens if they give him some.",
    93: "A vagrant asks for money. They get triple what they give back if they give him some.",
    94: "The party finds the tracks of an Owlbear going across the road (DC10 Nature/Survival).",
    95: "A local ranger gives the party directions to their next destination, shortening their journey.",
    96: "A mirror image of the party walks towards them, but disappears before reaching them.",
    97: "The party notices that they are being followed by a bush, which runs into the forest when they attempt to investigate. If they pursue, they find a goblin, that throws a gold coin at them to make them go away.",
    98: "A stranger on the road tells each PC to repent of their sins. He knows details.",
    99: "A door stands in the middle of the road. If opened, the frame bursts with confetti, then disappears.",
    100: "The party finds 100gp in a chest in the middle of the road."
}

random.choice(["A roll of thunder.",
               "A black dog runs across the path.",
               "A lone yellow flower is growing in the middle of the path.",
               "A shadow drifts over the party.",
               "A pool of blood.",
               "The earth shakes briefly.",
               "The sun bursts through an overclouded sky."])


def random_encounter(encounters_dictionary):
    roll = random.randint(1, len(encounters_dictionary))
    return encounters_dictionary[roll]


# print(random_encounter())

encounters2 = {
    1: "The players encounter a group of more experienced adventurers heading in the other direction. If the players are polite, they are given some healing potions.",
    # create encounter type with varied adventurers averaging random.randint(1,3) levels above party
    2: "A naked gnome runs across the path, gasps at the party, then runs back. Cannot be pursued.",
    3: random.choice(["A roll of thunder.",
                      "A black dog runs across the path.",
                      "A lone yellow flower is growing in the middle of the path.",
                      "A shadow drifts over the party.",
                      "A pool of blood.",
                      "The earth shakes briefly.",
                      "The sun bursts through an overclouded sky.", "A beautiful white horse dashes past the party and disappears."]),
    # 4:
    # 5:
    # 6:
    # 7:
    # 8:
    # 9:
    # 10:
    11: "The players find an encampment of well armed, friendly humans. They may stay the night here and avoid a random encounter for the night.",
    12: "A dwarf falls out of the sky and splatters in front of the party. No logical source of the dwarf can be seen.",
    13: "A player (whoever does the roll) trips over, takes 1D4 bludgeoning damage.",
    14: "A stranger asks to be escorted to a town, but gives the party nothing for doing it.",
    # 15: random.choice([]),  # animal tracks
    16: "A local ranger gives the party directions to their next destination, but he's an ******* that sends them the wrong way. Increase the journey length.",
    17: "An arrow strikes a nearby tree, with a note attached to it. The note reads 'You are a fool for looking!' No source of the arrow can be found.",
    18: "A dung beetle pushes a ball across the road. If disturbed, it bursts into a smog, doing 1D4 poison damage and leaves the party member poisoned.",
    19: "A mystery key is found laying in the road. If used on a locked door, roll a D20. A 20 will unlock the door, after which the key is lost.",
    20: "A thick fog prevents travel for the rest of the day.",
    21: "You were travelling in the wrong direction. Add a day of travel to your journey.",
    22: random.choice(["A song of rest. Lose any debuffs.",
                       "A song of good health. Gain 1D8 temporary hitpoints.", "A song of heroics. 1D6 party members gain inspiration.", "A song of misery. All party members with inspiration lose it.", "A song of battle. The next combat encounter grants double xp reward.", "A song of healing. Regain up to half your max HP.", "A song of pain. Lose 1D8 HP (after the bard has long since passed).", "A song of storms. A storm starts and forces the party to stop for the rest of the day.", "A song. Nothing special happens.",]),
    # 23:
    # 24:
    # 25:
    # 26:
    # 27:
    # 28:
    # 29:
    # 30:
    31: "Merchant: Only useful item for sale is a potion of vitality, 25gp.",
    32: "Merchant: Studded leather armour and basic weapons.",
    33: "Merchant: Five healing potions, 30gp each.",
    34: "Merchant: Basic adventuring equipment.",
    35: "Merchant: Wood.",
    36: "Merchant: Hunters bounty. Fresh meat, some herbs.",
    37: "Merchant: Herbalist (can give directions).",
    38: "Merchant: Fisherman.",
    39: "Merchant: Gem & Jewelry merchant (500gp worth of loot).",
    40: "Merchant: Bug catcher. A DC15 Nature check reveals a cartomoth, that will show them a shortcut if released. 10gp.",
    41: "The party catches up with and overtakes a slow travelling farmer, bickering with his wife. They know nothing useful.",
    42: "There is an unusually vocal chorus of birdsong. Druids, Hunters, Clerics gain inspiration.",
    43: "A stranger asks for directions from the party to the last town they left. If they help him, he gives them 1D6x10 gold when they next appear in town, if ever.",
    44: "A line of Goblin heads on spikes line the road. A sign written in Goblin next to them says 'Traitors of Yeemik'.",
    45: "A man is trapped under a log. If the party helps him, he disappears - it was an illusion.",
    46: "The party finds a sword in a stone. A DC15 Strength check pulls it out. It is a +1 (Longsword)",
    47: "A flower girl skips down the path towards the party, but disappears before she reaches them.",
    48: "Religion: The party meets an old priest and a young priest, who offer them a blessing. The party has advantage on attacks against undead till they next take a long rest.",
    49: "Religion: A temple is found on a roll. Use a D6 to determine which God, of the six below, it is dedicated to.",
    50: "Religion: Shrine to Tymora - If the party makes an offering, they all gain inspiration.",
    51: "Religion: Shrine to Chauntea - If the party makes an offering, the rest of the day has no violent encounters.",
    52: "Religion: Shrine to Mask - If the party makes an offering, they get a surprise round in their next encounter.",
    53: "Religion: Shrine to Mystra - If the party makes an offering, all spellslots are recovered.",
    54: "Religion: Shrine to Oghma - If the party makes an offering, they find a shortcut that reduces their journey by 1D4 encounters.",
    55: "Religion: Shrine to Waukeen - If the party makes an offering, they later find the amount they offered in each of their pockets.",
    56: "Religion: Abandoned, unidentifiable Shrine - If the party doesn't make an offering, they trigger a combat encounter.",
    57: "Religion: Shrine to nature spirits - If the party doesn't make an offering, a great storm prevents them from travelling any further that day.",
    58: "Religion: Demon Shrine, covered in blood - If the party makes an offering, they trigger a combat encounter.",
    59: "Religion: Shrine to Bhaal, destroyed - Nothing happens.",
    61: "Trap: DC10 Dex check or 1D6 bludgeoning damage, pit fall.",
    62: "Trap: DC15 Dex check or 1D8 bludgeoning damage, pit fall.",
    63: "Trap: DC20 Dex check or 1D12 bludgeoning damage, pit fall.",
    64: "Trap: DC10 Per check or snared, 1D6 bludgeoning damage if cut loose without landing being factored in.",
    65: "Trap: DC15 Per check or snared, 1D6 bludgeoning damage if cut loose without landing being factored in.",
    66: "Trap: DC20 Per check or snared, 1D6 bludgeoning damage if cut loose without landing being factored in.",
    67: "Trap: DC15 Per check or whole party snared by net, roll combat encounter.",
    68: "Trap: A cupcake lays in the middle of the road. If the party approaches, they trigger a pitfall into spikes. 3D6 piercing damage.",
    69: "Trap: Magic rune (DC15 Per to detect) triggers, paralyzing party. Roll for a combat encounter.",
    70: "Trap: Door in the middle of the path. If opened, a Hobgoblin is on the other side and gets a surprise attack. If walked around, the Hobgoblin flees.",
    71: "Trap: I have a tail, but no body. I have a head, but no brain. What am I? (coins, 50gp reward)",
    72: "Trap: What is running around Waterdeep, yet never truly moving? (The wall, Healing potion reward per player)",
    73: "Trap: My rivers are dry, my forests have no trees, my towns are flat and empty, and my roads cannot be walked on. What am I? (A map. The party's journey is shortened)",
    74: "Trap: Two bodies have I, though both joined in one. The more still I stand, the quicker I run. What am I? (An hourglass. Time slows down if they get it, and immediately skips to night if they don't)",
    75: "Trap: What kind of ear cannot hear? (An ear of corn. Potion of Cure Silence, everyone deafened if they don't get it)",
    76: "Trap: What has four wheels and flies? (A garbage wagon. Potion of flight if correct, attacked by Stirges if they don't get it)",
    77: "A DC10 Perception check spots a small chest hidden in a tree. It contains a gold ring worth 20gp.",
    78: "A DC15 Perception check spots a small chest hidden in a tree. It contains 44gp.",
    79: "A DC20 Perception check spots a chest hidden in a tree. It contains a +1 Short Sword.",
    80: "A DC10 Perception check spots a small chest hidden in a tree. It contains a dead mouse.",
    81: "A strong storm picks up.",
    82: "The party finds a random cow. No amount of investigation reveals anything of significance about the cow or where it came from.",
    83: "A stranger asks to be escorted to the nearest town. If the party agrees, the stranger gives them 100gp upon delivery.",
    84: "A group of excited gnomes bounce past the party. If the party is polite to them, one gives them a useless gizmo that makes a chirping noise when wound up.",
    85: "A man is trapped under a log. If the party helps him, do a DC15 check. A failure drops the log and crushes the man. He has nothing of value on him, but the saviour gets inspiration if they succeed.",
    86: "A man is buried in the road up to his neck, with the ground around him undisturbed. If the party helps him, the head pops out the ground and crawls off on spider legs, cackling. The party takes a DC14 Wisdom saving throw, taking 1D10 psychic damage on a failure.",
    87: "An enormous dragon flies overhead.",
    88: "A DC10 Perception check spots caltrops over the floor which do 1D4 piercing damage to the party if they don't spot them.",
    89: "A drunken dwarf challenges the strongest looking party member to a wrestling match. A DC15 Strength check beats her, and she gives the party member 5gp. The party member gains a level of exhaustion on a failure.",
    90: "A road sign points back to wherever the party came from, but is otherwise useless.",
    91: "A vagrant asks for food. Nothing happens if they give him some.",
    92: "A vagrant asks for money. Nothing happens if they give him some.",
    93: "A vagrant asks for money. They get triple what they give back if they give him some.",
    94: "The party finds the tracks of an Owlbear going across the road (DC10 Nature/Survival).",
    95: "A local ranger gives the party directions to their next destination, shortening their journey.",
    96: "A mirror image of the party walks towards them, but disappears before reaching them.",
    97: "The party notices that they are being followed by a bush, which runs into the forest when they attempt to investigate. If they pursue, they find a goblin, that throws a gold coin at them to make them go away.",
    98: "A stranger on the road tells each PC to repent of their sins. He knows details.",
    99: "A door stands in the middle of the road. If opened, the frame bursts with confetti, then disappears.",
    100: "The party finds 100gp in a chest in the middle of the road."
}

# weighted_encounters_test = {"encounter 1": [1,2,3,4,5], "encounter 2" : [6,7,8,9,10], "encounter 3" :[11,12,13,14,15] }
weighted_encounters_template = {"encounter 1": range(10), 
                            "encounter 2" : range(11,21),
                            "encounter 3" : range(21,31),
                            "encounter 4" : range(31,41),
                            "encounter 5" : range(41,51),
                            "encounter 6" : range(51,61),
                            "encounter 7" : range(61,71),
                            "encounter 8" : range(71,81),
                            "encounter 9" : range(81,91),
                            "encounter 10" : range(91,100)}

weighted_locations_template = {"Location One": range(10), 
                            "Location Two" : range(11,21),
                            "Location Three" : range(21,31),
                            "Location Four" : range(31,41),
                            "Location Five" : range(41,51),
                            "Location Six" : range(51,61),
                            "Location Seven" : range(61,71),
                            "Location Eight" : range(71,81),
                            "Location Nine" : range(81,91),
                            "Location Ten" : range(91,100)}

location_enemies_template = {"Location One": ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Two" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Three" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Four" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Five" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Six" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Seven" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Eight" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Nine" : ["Enemy one", "Enemy two", "Enemy Three"],
                            "Location Ten" : ["Enemy one", "Enemy two", "Enemy Three"],
                            }


def random_weighted_encounter(weighted_encounters, max_roll=100):
    roll = random.randint(1, max_roll)
    # print(roll)
    for key, value in weighted_encounters.items():
        if roll in value:
                return key
    else:
        return "no encounter"
    
def random_location(weighted_locations, location_details, max_roll=100):
    roll = random.randint(1, max_roll)
    # print(roll)
    for key, value in weighted_locations.items():
        if roll in value:
                enemy_list = location_details[key]
                enemies = location_details[key][random.randint(0,len(enemy_list)-1)]
                return key, enemies
    else:
        return "no encounter"

# print(random_weighted_encounter(weighted_encounters_template))


# print(random_location(weighted_locations_template,location_enemies_template))