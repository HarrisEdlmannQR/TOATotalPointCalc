from functions import get_rewards, estimate_points

def run(raid_level):
    points, purp_chance, quantities = get_rewards(estimate_points(raid_level=raid_level), raid_level=raid_level)
    print(points, purp_chance, quantities)

if __name__ == "__main__":
    raid_level = 370
    run(raid_level)