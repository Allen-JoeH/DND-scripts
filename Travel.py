import math
import statistics
import random

def travel_time(miles, pace, party_speed_modifier=1):
    match pace:
        case "fast":
            per_mile = 4
        case "normal":
            per_mile = 3
        case "slow":
            per_mile = 2
    # return f'{(miles/per_mile)/party_speed_modifier} hours'
    return (miles/per_mile)/party_speed_modifier


# print(travel_time(30,"fast"))

def travel_distance(time, pace, party_speed_modifier=1):
    match pace:
        case "fast":
            per_hour = 4
        case "normal":
            per_hour = 3
        case "slow":
            per_hour = 2
    # return f'{(time*per_hour)*party_speed_modifier} miles'
    return (time*per_hour)*party_speed_modifier

# print(travel_distance(8,"fast"))

def roll_dice(die_size):
    return math.ceil(random.random() * die_size)

def check(DC):
    roll=roll_dice(20)
    # return f'Succeeds ({str(roll)})' if roll>+DC else f'Fails ({str(roll)})'
    return True if roll >= DC else False

terrain_type = {

}

def exhaustion(hours_over_8):
    checks = [10 + i for i in range(hours_over_8-8)] if hours_over_8 > 8 else None
    return checks



def travel_summary(pace,control_param,distance=None,time=None,difficult_terrain=1,danger_modifier=0):
    # Objective of travel day: provide travel time or distance dpending on input, generate a variable DC check for chance of encounter
    # Difficult_terrain should be set to 1 for regular terrain or 2 for difficult terrain. Can be higher for dangerous terrain or lower for more forgiving terrain
    if control_param == "time":
        distance_travelled = travel_distance(time,pace,party_speed_modifier=1) / difficult_terrain
        hours_travelling = time
    else:
        distance_travelled = distance
        hours_travelling = travel_time(distance,pace,party_speed_modifier=1)* difficult_terrain
    
    exhaustion_checks = exhaustion(hours_travelling)
    match pace:
        case "fast":
            hour_mod = 1.3
        case "slow":
            hour_mod = 0.5
    encounter_chance = math.floor(hours_travelling*hour_mod - danger_modifier)
    return {
        "pace" : pace,
        "miles travelled" : distance_travelled,
        "hours travelling" : hours_travelling,
        "terrain difficulty" : "regular" if difficult_terrain <= 1 else "difficult",
        "exhaustion checks needed" : exhaustion_checks,
        "encounter chance" : encounter_chance,
            }

def combine_travel(*args):
    pace = arg[0]["pace"]
    terrain_difficulty = arg[0]["terrain difficulty"]
    for arg in args:
        distance_travelled_total += arg["miles travelled"]
        hours_travelling_total += arg["hours travelling"]
        if arg["terrain difficulty"] != terrain_difficulty:
            terrain_difficulty = "varied"
            break
        if arg["pace"] != pace:
            pace = "varied"
    
    exhaustion_checks = exhaustion(hours_travelling_total)
    averaged_encounter_chance = math.ceil(statistics.mean([arg["encounter chance"] for arg in args]))
    return {
        "pace" : pace,
        "miles travelled" : distance_travelled_total,
        "hours travelling" : hours_travelling_total,
        "terrain difficulty" : terrain_difficulty,
        "exhaustion checks needed" : exhaustion_checks,
        "encounter chance" : averaged_encounter_chance,
    }

def encounter(travel_obj):
    if check(travel_obj["encounter chance"]):
        return "Random Encounter!"
    else:
        return "No "

days_travel = travel_summary("fast","distance",6)

# print(days_travel)

print(travel_time(8, "fast", party_speed_modifier=2))