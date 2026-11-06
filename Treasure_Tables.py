from Roll import roll_dice
from Magic_Item_Tables import *


def c_under_4(dice_roll):
    def format_items(items):
        return ", ".join(items)

    if dice_roll <= 6:
        return "No additional loot"
    elif dice_roll <= 16:
        gems_num = roll_dice(6, 2)
        return f"{gems_num} gems 10gp each"
    elif dice_roll <= 26:
        art_num = roll_dice(4, 2)
        return f"{art_num} art objects 25gp each"
    elif dice_roll <= 36:
        gems_num = roll_dice(6, 2)
        return f"{gems_num} gems 50gp each"
    elif dice_roll <= 44:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{gems_num} gems 10gp each and {format_items(items)}"
    elif dice_roll <= 52:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 60:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 65:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 10gp each and {format_items(items)}"
    elif dice_roll <= 70:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 75:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 78:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 10gp each and {format_items(items)}"
    elif dice_roll <= 80:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 85:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 92:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 97:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 99:
        art_num = roll_dice(4, 2)
        item = get_loot(roll_dice(100), magic_item_table_G)
        return f"{art_num} art objects 25gp each and {item}"
    elif dice_roll == 100:
        gems_num = roll_dice(6, 2)
        item = get_loot(roll_dice(100), magic_item_table_G)
        return f"{gems_num} gems 50gp each and {item}"
 
def c_under_10(dice_roll):
    def format_items(items):
        return ", ".join(items)

    if dice_roll <= 4:
        return "No additional loot"
    elif dice_roll <= 10:
        art_num = roll_dice(4, 2)
        return f"{art_num} art objects 25gp each"
    elif dice_roll <= 16:
        gems_num = roll_dice(6, 3)
        return f"{gems_num} gems 50gp each"
    elif dice_roll <= 22:
        gems_num = roll_dice(6, 3)
        return f"{gems_num} gems 100gp each"
    elif dice_roll <= 28:
        art_num = roll_dice(4, 2)
        return f"{art_num} art objects 25gp each"
    elif dice_roll <= 32:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 36:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 40:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 44:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 49:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 54:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 59:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 63:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 66:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 69:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 72:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 74:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 76:
        art_num = roll_dice(4, 2)
        item = get_loot(roll_dice(100), magic_item_table_D)
        return f"{art_num} art objects 25gp each and {item}"
    elif dice_roll <= 78:
        gems_num = roll_dice(6, 3)
        item = get_loot(roll_dice(100), magic_item_table_D)
        return f"{gems_num} gems 50gp each and {item}"
    elif dice_roll == 79:
        gems_num = roll_dice(6, 3)
        item = get_loot(roll_dice(100), magic_item_table_D)
        return f"{gems_num} gems 100gp each and {item}"
    elif dice_roll == 80:
        art_num = roll_dice(4, 2)
        item = get_loot(roll_dice(100), magic_item_table_D)
        return f"{art_num} art objects 250gp each and {item}"
    elif dice_roll <= 84:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 25gp each and {format_items(items)}"
    elif dice_roll <= 88:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 50gp each and {format_items(items)}"
    elif dice_roll <= 91:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 94:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 96:
        gems_num = roll_dice(6, 3)
        items = [get_loot(roll_dice(100), magic_item_table_G) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 98:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_G) for _ in range(roll_dice(6))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll == 99:
        gems_num = roll_dice(6, 3)
        item = get_loot(roll_dice(100), magic_item_table_H)
        return f"{gems_num} gems 100gp each and {item}"
    elif dice_roll == 100:
        art_num = roll_dice(4, 2)
        item = get_loot(roll_dice(100), magic_item_table_H)
        return f"{art_num} art objects 250gp each and {item}"
    
def c_under_16(dice_roll):
    def format_items(items):
        return ", ".join(items)

    if dice_roll <= 3:
        return "No additional loot"
    elif dice_roll <= 6:
        gems_num = roll_dice(6, 2)
        return f"{gems_num} gems 100gp each"
    elif dice_roll <= 9:
        art_num = roll_dice(4, 2)
        return f"{art_num} art objects 250gp each"
    elif dice_roll <= 12:
        gems_num = roll_dice(6, 2)
        return f"{gems_num} gems 500gp each"
    elif dice_roll <= 18:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 24:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 30:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_A) for _ in range(roll_dice(6))]
        return f"{gems_num} gems 500gp each and {format_items(items)}"
    elif dice_roll <= 36:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 42:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 48:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_B) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 500gp each and {format_items(items)}"
    elif dice_roll <= 54:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 100gp each and {format_items(items)}"
    elif dice_roll <= 60:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 66:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_C) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 500gp each and {format_items(items)}"
    elif dice_roll <= 72:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_D) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 78:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_D) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 500gp each and {format_items(items)}"
    elif dice_roll <= 84:
        art_num = roll_dice(4, 2)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{art_num} art objects 250gp each and {format_items(items)}"
    elif dice_roll <= 90:
        gems_num = roll_dice(6, 2)
        items = [get_loot(roll_dice(100), magic_item_table_F) for _ in range(roll_dice(4))]
        return f"{gems_num} gems 500gp each and {format_items(items)}"
    elif dice_roll <= 96:
        art_num = roll_dice(4, 2)
        item = get_loot(roll_dice(100), magic_item_table_G)
        return f"{art_num} art objects 250gp each and {item}"
    elif dice_roll <= 100:
        gems_num = roll_dice(6, 2)
        item = get_loot(roll_dice(100), magic_item_table_G)
        return f"{gems_num} gems 500gp each and {item}"



def get_loot(roll, loot_table):
    """
    Given a dice roll (1–100) and a loot_table dictionary
    with ranges and integers as keys, return the matching item.
    """
    for key, item in loot_table.items():
        if isinstance(key, range) and roll in key:
            return item
        elif isinstance(key, int) and roll == key:
            return item
        
def rand_magic_items(loot_table : dict, items : int = 1, weighting : int = 0):
    for item in range(items):
        roll = int(roll_dice(100, 1 + weighting)/(weighting + 1))
        print(get_loot(roll, loot_table))



# print(c_under_4(roll_dice(100)))
# print(c_under_10(roll_dice(100)))