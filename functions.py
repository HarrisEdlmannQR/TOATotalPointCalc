from math import trunc

NORMAL_LOOT = [
    {"item": "Coins", "divisor": 1},
    {"item": "Death rune", "divisor": 20},
    {"item": "Soul rune", "divisor": 40},
    {"item": "Gold ore", "divisor": 90},
    {"item": "Dragon dart tip", "divisor": 100},
    {"item": "Mahogany logs", "divisor": 180},
    {"item": "Sapphire", "divisor": 200},
    {"item": "Emerald", "divisor": 250},
    {"item": "Gold bar", "divisor": 250},
    {"item": "Potato cactus", "divisor": 250},
    {"item": "Raw shark", "divisor": 250},
    {"item": "Ruby", "divisor": 300},
    {"item": "Diamond", "divisor": 400},
    {"item": "Raw manta ray", "divisor": 450},
    {"item": "Cactus spine", "divisor": 600},
    {"item": "Dragonstone", "divisor": 600},
    {"item": "Battlestaff", "divisor": 1100},
    {"item": "Coconut milk", "divisor": 1100},
    {"item": "Lily of the sands", "divisor": 1100},
    {"item": "Toadflax seed", "divisor": 1400},
    {"item": "Ranarr seed", "divisor": 1800},
    {"item": "Torstol seed", "divisor": 2200},
    {"item": "Snapdragon seed", "divisor": 2200},
    {"item": "Dragon med helm", "divisor": 4000},
    {"item": "Magic seed", "divisor": 6500},
    {"item": "Blood essence", "divisor": 7500},
    {"item": "Cache of runes", "divisor": 999999},
]

def scale_hp(base, raid_level, team_size, path_level):
	path_multiplier = 1.0
	if path_level > 0:
		path_multiplier = 1.03 + path_level * 0.05
	return trunc(base * (1 + raid_level / 250) * path_multiplier)

def estimate_points(raid_level, path_invocation = 0, walk_the_path = True, team_size = 1):
    AVERAGE_WTP_LEVEL = [0, 4 / 6, 7 / 6, 13 / 6]
    POINTS_TABLE = [
        {"name": "Akkha", "hp": scale_hp(480, raid_level, team_size, path_invocation + AVERAGE_WTP_LEVEL[3]),
         "mult": 1.0, "approx": walk_the_path},
        {"name": "Akkha's Shadow", "hp": scale_hp(70, raid_level, team_size, path_invocation + AVERAGE_WTP_LEVEL[3]),
         "mult": 1.0, "count": 4},
        {"name": "Baboons", "hp": scale_hp(300, raid_level, team_size, 0), "mult": 1.2, "approx": True},
        {"name": "Ba-Ba", "hp": scale_hp(380, raid_level, team_size, path_invocation + AVERAGE_WTP_LEVEL[0]),
         "mult": 2.0, "approx": walk_the_path},
        {"name": "Zebak", "hp": scale_hp(580, raid_level, team_size, path_invocation + AVERAGE_WTP_LEVEL[2]),
         "mult": 1.5, "approx": walk_the_path},
        {"name": "Scarab Swarms", "hp": 200, "mult": 1.0, "approx": True},
        {"name": "Scarabs", "hp": 200, "mult": 0.5, "approx": True},
        {"name": "Kephri's Shield", "hp": scale_hp(375, raid_level, team_size, path_invocation + AVERAGE_WTP_LEVEL[1]),
         "mult": 1.0, "approx": True},
        {"name": "Kephri", "hp": scale_hp(130, raid_level, team_size, path_invocation + AVERAGE_WTP_LEVEL[1]),
         "mult": 1.0, "approx": walk_the_path},
        {"name": "P1 Obelisk", "hp": scale_hp(260, raid_level, team_size, 0), "mult": 1.5},
        {"name": "P2 Warden", "hp": scale_hp(140, raid_level, team_size, 0), "mult": 2.0, "count": 2},
        {"name": "P3 Warden", "hp": scale_hp(880, raid_level, team_size, 0), "mult": 2.5},
        {"name": "Misc. damage", "hp": 80 * team_size, "mult": 1.0, "approx": True},
        {"name": "Het - seal mining", "hp": 130 + trunc(95.81 * (team_size - 1)), "mult": 2.5},
        {"name": "Scabaras - puzzles", "points": 300 * team_size, "approx": True},
        {"name": "Apmeken - traps", "points": 450 * team_size, "approx": True},
        {"name": "Crondis - palm watering", "points": 400 * team_size},
        {"name": "MVP", "points": 2700 * team_size},
    ]

    total_points = 0
    for v in POINTS_TABLE:
        if 'points' in v:
            total_points = total_points + v['points']
        else:
            total_points = total_points + trunc(v['hp'] * v['mult'] * v.get('count', 1))
    return total_points * 1.07

def get_rewards(points, raid_level, team_size = 1):
    purple_denominator = 100 * (10500 - 20 * raid_level)
    percent = trunc((raid_level - 300) / 5) + 15
    scale = 1 + percent / 100
    base_purple_rate = min(points / purple_denominator, 0.55)

    item_quantities = {}

    for v in NORMAL_LOOT:
        quantity = max(trunc(scale * trunc(points / team_size / v['divisor'])), 1)
        item_quantities[v['item']] = quantity

    return points, base_purple_rate, item_quantities