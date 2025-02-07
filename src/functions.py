from math import floor
import yaml

NORMAL_LOOT = {
    "Coins": 1,
    "Death rune": 20,
    "Soul rune": 40,
    "Gold ore": 90,
    "Dragon dart tip": 100,
    "Mahogany logs": 180,
    "Sapphire": 200,
    "Emerald": 250,
    "Gold bar": 250,
    "Potato cactus": 250,
    "Raw shark": 250,
    "Ruby": 300,
    "Diamond": 400,
    "Raw manta ray": 450,
    "Cactus spine": 600,
    "Dragonstone": 600,
    "Battlestaff": 1100,
    "Coconut milk": 1100,
    "Lily of the sands": 1100,
    "Toadflax seed": 1400,
    "Ranarr seed": 1800,
    "Torstol seed": 2200,
    "Snapdragon seed": 2200,
    "Dragon med helm": 4000,
    "Magic seed": 6500,
    "Blood essence": 7500,
    "Cache of runes": 999999
}

PURPLES = {
    "Tumeken's shadow (uncharged)": {"weight": 1, "level": 150},
    "Masori mask": {"weight": 2, "level": 150},
    "Masori body": {"weight": 2, "level": 150},
    "Masori chaps": {"weight": 2, "level": 150},
    "Elidinis' ward": {"weight": 3, "level": 150},
    "Osmumten's fang": {"weight": 7, "level": 50},
    "Lightbearer": {"weight": 7, "level": 50}
}

def get_config_file():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

config = get_config_file()

walk_the_path_invo = True if config['WTP_INVO'] else False
initial_path_invo = config['INITIAL_PATH_INVO']
observations = config['OBSERVATIONS']
KC = (config['KC'] * 3) - (observations['Purple Count'] * 3) - observations['Total Partisan Gems and Thread']

def estimate_points(raid_level: float) -> float:

    def scale_hp(base: int, raid_level: float, path_level: int) -> float:
        path_multiplier = 1.0
        if path_level > 0:
            path_multiplier = 1.03 + path_level * 0.05
        return floor(base * (1 + raid_level / 250) * path_multiplier) # team scale size is ignored as assumed solo

    average_wtp_level = [0, 4 / 6, 7 / 6, 13 / 6] if walk_the_path_invo else [0, 0, 0, 0] # assuming baba -> kephri -> ahkka -> zebak

    points_table = [
        {"name": "Akkha", "hp": scale_hp(480, raid_level, initial_path_invo + average_wtp_level[2]), "mult": 1.0, "approx": walk_the_path_invo},
        {"name": "Akkha's Shadow", "hp": scale_hp(70, raid_level, initial_path_invo + average_wtp_level[2]), "mult": 1.0, "count": 4},
        {"name": "Baboons", "hp": scale_hp(300, raid_level, 0), "mult": 1.2, "approx": walk_the_path_invo},
        {"name": "Ba-Ba", "hp": scale_hp(380, raid_level, initial_path_invo + average_wtp_level[0]),"mult": 2.0, "approx": walk_the_path_invo},
        {"name": "Zebak", "hp": scale_hp(580, raid_level, initial_path_invo + average_wtp_level[3]), "mult": 1.5, "approx": walk_the_path_invo},
        {"name": "Scarab Swarms", "hp": 200, "mult": 1.0, "approx": True},
        {"name": "Scarabs", "hp": 200, "mult": 0.5, "approx": True},
        {"name": "Kephri's Shield", "hp": scale_hp(375, raid_level, average_wtp_level[1]), "mult": 1.0, "approx": True},
        {"name": "Kephri", "hp": scale_hp(130, raid_level, walk_the_path_invo + average_wtp_level[1]),"mult": 1.0, "approx": walk_the_path_invo},
        {"name": "P1 Obelisk", "hp": scale_hp(260, raid_level, 0), "mult": 1.5},
        {"name": "P2 Warden", "hp": scale_hp(140, raid_level, 0), "mult": 2.0, "count": 2},
        {"name": "P3 Warden", "hp": scale_hp(880, raid_level, 0), "mult": 2.5},
        {"name": "Misc. damage", "hp": 80, "mult": 1.0, "approx": True},
        {"name": "Het - seal mining", "hp": 130, "mult": 2.5},
        {"name": "Scabaras - puzzles", "points": 300, "approx": True},
        {"name": "Apmeken - traps", "points": 450, "approx": True},
        {"name": "Crondis - palm watering", "points": 400},
        {"name": "MVP", "points": 2700},
    ]

    total_points = 0
    for v in points_table:
        if 'points' in v:
            total_points = total_points + v['points']
        else:
            total_points = total_points + floor(v['hp'] * v['mult'] * v.get('count', 1))

    # tweak this number if your observations indicate slightly different quantities
    # I have 1.07 since I typically complete "3-downs" on p2 wardens and "Skull Skip" on p3 wardens resulting in ~7% more points
    mult_factor = 1.07
    total_points *= mult_factor

    return total_points

def estimate_purple_chance(raid_level: float) -> float:
    adjusted_raid_level = raid_level
    if raid_level > 400:
        adjusted_raid_level = 400 + floor((raid_level - 400) / 3)

    purple_denominator = max(100 * (10500 - 20 * adjusted_raid_level), 150000)
    base_purple_rate = min(estimate_points(raid_level) / purple_denominator, 0.55)

    return base_purple_rate

def estimate_item_quantity(raid_level: float, item: str) -> float:
    if raid_level < 150:
        scale = 0.75
    elif raid_level >= 300:
        percent = (floor((raid_level - 300) / 5) + 15)
        scale = 1 + percent / 100
    else:
        scale = 1

    quantity = floor(estimate_points(raid_level) / NORMAL_LOOT.get(item))
    quantity = max(floor(quantity * scale), 1)

    return quantity

"""def alter_observations(observations: dict) -> dict:
    dummy_obs = {}
    for item in observations:
        if item == "Purple Count":
            dummy_obs['Purple Count'] = observations[item] + 10000 * estimate_purple_chance(450)
        elif item == "Total Partisan Gems and Thread":
            dummy_obs['Total Partisan Gems and Thread'] = observations[item] + (10000 * 1/58 * 3)
        else:
            dummy_obs[item] = observations[item] + 10000 / 27 * 3 * estimate_item_quantity(450, item)

    return dummy_obs

observations = alter_observations(observations)
KC = ((config['KC']+10000) * 3) - (observations['Purple Count'] * 3) - observations['Total Partisan Gems and Thread']"""

def minimise_residuals() -> float:

    def calculate_least_squares(raid_level: float) -> float:
        r = 0
        for item in NORMAL_LOOT:
            q_i = estimate_item_quantity(raid_level, item)
            r += (((q_i * KC / 27) - observations[item]) / q_i) ** 2
        return r

    min_residual = calculate_least_squares(1)
    estimated_raid_level = 1

    raid_levels = range(2, 600 + 1)
    for raid_level in raid_levels:
        r = calculate_least_squares(raid_level)
        if r < min_residual:
            min_residual = r
            estimated_raid_level = raid_level

    return estimated_raid_level