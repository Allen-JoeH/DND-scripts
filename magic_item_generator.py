import random

# List of common D&D weapons
weapons = [
    "Club", "Dagger", "Greatclub", "Handaxe", "Javelin",
    "Light Hammer", "Mace", "Quarterstaff", "Sickle",
    "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling",
    "Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword",
    "Halberd", "Lance", "Longsword", "Maul", "Morningstar",
    "Pike", "Rapier", "Scimitar", "Shortsword", "Trident",
    "War Pick", "Warhammer", "Whip"
]

# List of minor magical effects
magical_effects = [
    "glows with a faint light", "emits a soft humming sound",
    "feels unusually warm to the touch", "vibrates slightly when enemies are near",
    "gives off a faint floral scent", "shimmers with a faint blue aura",
    "occasionally produces a faint ringing sound", "gives the wielder brief flashes of insight",
    "leaves a trail of sparkles when swung", "feels lighter than it should",
    "occasionally makes faint whispers", "grants the wielder a feeling of calmness",
    "glows faintly in the presence of magic", "emits a soft, soothing melody"
]

enemy_type = ["Aberration", "Beast", "Celestial", "Construct", "Dragon", "Elemental",
              "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead"]
weapon_bonuses = ["+ 1 attack", "+1 damage",
                  "+1 weapon", f"+d4 damage vs {random.choice(enemy_type)}"]

# List of common D&D armor
armor = ["Padded Armor", "Leather Armor", "Studded Leather Armor", "Hide Armor", "Chain Shirt", "Scale Mail",
         "Breastplate", "Half Plate", "Ring Mail", "Chain Mail", "Splint Armor", "Plate Armor", "Shield"]

# List of minor magical effects
magical_effects = ["glows faintly in the dark", "emits a soft warmth", "makes the wearer feel lighter", "produces a soft humming sound when struck", "gives off a faint herbal scent", "shimmers with a faint golden aura", "occasionally makes soft whispers",
                   "feels unusually comfortable to wear", "grants the wearer a feeling of security", "vibrates slightly when danger is near", "glows faintly in the presence of magic", "emits a soft, soothing melody", "gives the wearer brief flashes of insight", "makes the wearer feel braver"]

minor_magical_items = [
    "Wand of Sparkles",
    "Amulet of Whispering",
    "Ring of Minor Illusion",
    "Cloak of Comfort",
    "Boots of Quiet Steps",
    "Lantern of Everlight",
    "Gloves of Nimble Fingers",
    "Belt of Minor Strength",
    "Hat of Disguise",
    "Bracelet of Luck",
    "Goggles of Night Vision",
    "Brooch of Shielding",
    "Pendant of Water Breathing",
    "Cape of Billowing",
    "Book of Knowledge",
    "Necklace of Fire Resistance",
    "Bracers of Defense",
    "Stone of Good Luck",
    "Horn of Warning",
    "Mirror of Self Reflection"
]

armor_bonuses = []

magic_items = ["weapon", "armor", "item"]

item_choice = random.choice(magic_items)

# Randomly choose a piece of armor and a magical effect
chosen_armor = random.choice(armor)
chosen_effect = random.choice(magical_effects)


# Randomly choose a weapon and a magical effect
chosen_weapon = random.choice(weapons)
chosen_effect = random.choice(magical_effects)
chosen_weapon_bonus = random.choice(weapon_bonuses)

# Randomly chooses a magic item
chosen_item = random.choice(minor_magical_items)


if item_choice == "weapon":
    print(f"The {chosen_weapon} {chosen_effect}.")
    print(chosen_weapon_bonus)
elif item_choice == "armor":
    print(f"The {chosen_armor} {chosen_effect}.")
elif item_choice == "item":
    print(f"{chosen_item}.")

print(chosen_item)
