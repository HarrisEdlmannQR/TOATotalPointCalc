from src.functions import (
    minimise_residuals,
    estimate_points,
    estimate_purple_chance,
)

def run():
    average_raid_level = minimise_residuals()
    average_points = estimate_points(average_raid_level)
    average_purple_chance = estimate_purple_chance(average_raid_level)

    print(f"Based of given observations, the average raid level is {average_raid_level}, giving ~{average_points} "
          f"points and a purple chance of ~{round(average_purple_chance*100, 3)}% "
          f"(or 1/{round(100/(average_purple_chance*100), 3)}).")

if __name__ == "__main__":
    run()